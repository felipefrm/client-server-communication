#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
import re

import libclient

sel = selectors.DefaultSelector()

def create_request(command):
    action = re.findall("[A-Za-z]*", command)[0]
    args = command.split(action, 1)[1].strip()
    action = action.upper()
    if action == "INSERT":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=args),
        )
    elif action == "SELECT":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=args),
        )
    else:
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=command),
        )


def start_connection(host, port, request):
    addr = (host, port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<host> <port> <command>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
command = sys.argv[3].strip()
request = create_request(command)
start_connection(host, port, request)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except Exception:
                print(
                    "main: error: exception for",
                    f"{message.addr}:\n{traceback.format_exc()}",
                )
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()

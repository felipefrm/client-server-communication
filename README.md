# Basic interaction Client-Server using Socket in Python

## Requirements

- [Python](https://www.python.org/) 3.6 or later.

## How To Run

1. Run the app-server:
```
python3 app-server.py <host> <port>

# <host> can be a hostname, IP address, or empty string. If an IP address is used, host should be an IPv4-formatted address string. The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, so only processes on the host will be able to connect to the server. If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

# <port> should be an integer from 1-65535 (0 is reserved). It’s the TCP port number to accept connections on from clients. Some systems may require superuser privileges if the port is < 1024.
```

2. Run the app-client as many times as you want (each execution refers to an interaction command)
```
python3 app-client.py <host> <port> <command>

# <host> can be a hostname, IP address, or empty string. If an IP address is used, host should be an IPv4-formatted address string. The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, so only processes on the host will be able to connect to the server. If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

# <port> should be an integer from 1-65535 (0 is reserved). It’s the TCP port number to accept connections on from clients. Some systems may require superuser privileges if the port is < 1024.

# <command> can be a SELECT or an INSERT. For SELECT command only the "SELECT *" (select all) statment was implemented, and for INSERT command the statment must follow the syntax "INSERT:$NAME:$GENDER:$AGE".
```

## References

- Guide: [Socket Programming in Python](https://realpython.com/python-sockets/)
- Repository: [python-socket-tutorial](https://github.com/realpython/materials/tree/master/python-sockets-tutorial)

## License

The MIT License. See the file LICENSE in this repository's base directory.

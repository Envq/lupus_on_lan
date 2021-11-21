#!/usr/bin/python3
import sys

from controller import app


def getIp():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == "__main__":
    # Get ip and port
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = sys.argv[2]
    else:
        ip = getIp()
        port = 5000
    # Run application
    app.run(debug=True, host=ip, port=port)

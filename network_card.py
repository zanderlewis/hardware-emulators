import socket

class NetworkCard:
    def __init__(self, host='127.0.0.1', port=8080, debug=False):
        self.host = host
        self.port = port
        self.debug_mode = debug
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        if self.debug_mode:
            print(f"Network card initialized on {self.host}:{self.port}")

    def send(self, data, target_host, target_port):
        """Send data to a target host and port."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_host, target_port))
            s.sendall(data)
            if self.debug_mode:
                print(f"Sent data to {target_host}:{target_port}")

    def receive(self):
        """Receive data from the network."""
        conn, addr = self.socket.accept()
        with conn:
            data = conn.recv(1024)
            if self.debug_mode:
                print(f"Received data from {addr}")
            return data

    def close(self):
        """Close the network card."""
        self.socket.close()
        if self.debug_mode:
            print("Network card closed")
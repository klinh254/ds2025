import socket

def start_server(host='0.0.0.0', port=888):
    # Create and configure server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening at {host} on port {port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established.")

    # Receive file
    with open('received_file', 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:  # EOF
                break
            file.write(data)

    print("File received and saved as 'received_file'.")
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

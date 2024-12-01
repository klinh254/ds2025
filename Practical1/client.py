import socket

def send_file(host, port, file_path):
    # Create client socket and connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((host, port))
    print(f"Connected to server {host} on port {port}.")

    # Send file
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    client_socket.close()
    print("File sent successfully!")
    print("Connection closed.")

if __name__ == "__main__":
    send_file("192.168.86.128", 888, "transfer_file.txt")
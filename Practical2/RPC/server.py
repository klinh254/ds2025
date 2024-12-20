import xmlrpc.server
import os

def send_file(filename, file_content):
    # Save the received file
    with open('received_file', 'wb') as file:
        file.write(file_content.data)
    print(f"File received and saved as 'received_file'.")
    return "File sent successfully."


def download_file(filename):
    # Check if the requested file exists
    if not os.path.exists(filename):
        return "File does not exist."

    with open(filename, 'rb') as file:
        file_content = file.read()
    print(f"Requested file sent successfully.")
    return xmlrpc.client.Binary(file_content), "File downloaded and saved as 'downloaded_file'."


if __name__ == "__main__":
    server = xmlrpc.server.SimpleXMLRPCServer(("192.168.86.128", 888))

    # Register the functions with the XML-RPC server
    server.register_function(send_file, "send_file")
    server.register_function(download_file, "download_file")

    print("Server listening on port 888...")

    # Start the server
    server.serve_forever()

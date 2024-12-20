import xmlrpc.client

def send_file(server_url, filename):
    with open(filename, 'rb') as file:
        file_content = file.read()

    proxy = xmlrpc.client.ServerProxy(server_url)   # Create an XML-RPC server proxy

    # Send the file to the server
    response = proxy.send_file(filename, xmlrpc.client.Binary(file_content))
    print(response)


def download_file(server_url, request_filename):
    proxy = xmlrpc.client.ServerProxy(server_url)

    # Request the file to download from the server
    file_content, message = proxy.download_file(request_filename)
    
    # Save the downloaded file
    if file_content.data:
        with open('downloaded_file', 'wb') as file:
            file.write(file_content.data)
    print(message)


if __name__ == "__main__":
    server_url = "http://192.168.86.128:888"

    download_file(server_url, "file_to_download.txt")
    send_file(server_url, "file_to_send.txt")

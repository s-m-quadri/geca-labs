import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen(1)
    print("Server waiting for client connection...")

    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    client_socket.sendall("Greetings!\n".encode('utf-8'))
    client_socket.sendall("Server v1.0 | GECA Assignment\n".encode('utf-8'))
    client_socket.sendall("Updated: October, 2024\n".encode('utf-8'))

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8').strip()
        print(f"Received: {message}")

        # If message is empty, break the loop (shutdown)
        if not message:
            break

        # Send back the message in uppercase
        client_socket.sendall((message.upper() + '\n').encode('utf-8'))

    client_socket.close()
    print("Client disconnected.")
    server_socket.close()
    print("Connection Closed.")

if __name__ == "__main__":
    try:
        start_server()
    except Exception as e:
        print(f"Something went wrong! {e}")
    finally:
        print("Server shutdown.")
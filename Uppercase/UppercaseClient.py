import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9090))

    # Receive the header from server 
    print(client_socket.recv(1024).decode('utf-8').strip())
    while True:
        # Send message to server
        message = input("send ➜ ")
        client_socket.sendall((message + '\n').encode('utf-8'))

        # In case of empty message, break and shutdown client
        if not message:
            break

        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8').strip()
        print(f"{response}")

    client_socket.close()
    print("Connection Closed.")

if __name__ == "__main__":
    try:
        start_client()
    except Exception as e:
        print(f"Something went wrong! {e}")
    finally:
        print("Client shutdown.")

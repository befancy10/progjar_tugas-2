import socket
import threading
import datetime

def handle_client(client_socket, address):
    print(f"New connection from {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data == "QUIT\r\n":
                break
            if data == "TIME\r\n":
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"JAM {current_time}\r\n"
                client_socket.send(response.encode('utf-8'))
            else:
                client_socket.send("Invalid request\r\n".encode('utf-8'))
        except:
            break
    client_socket.close()
    print(f"Connection closed from {address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 45000))
    server_socket.listen(5)
    print("Time server running on port 45000...")
    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    main()
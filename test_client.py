import socket
import threading
import time

# Fungsi untuk tes klien tunggal
def run_single_test():
    print("=== Single Client Test ===")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 45000))
        print("Successfully connected to server")

        # Kirim permintaan TIME
        print("Sending TIME command...")
        sock.send("TIME\r\n".encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print(f"Received from server: {data.strip()}")

        # Kirim perintah QUIT
        print("Sending QUIT command...")
        sock.send("QUIT\r\n".encode('utf-8'))
        sock.close()
        print("Connection terminated\n")
    except Exception as e:
        print(f"Test failed: {e}")

# Fungsi untuk tes klien concurrent
def run_concurrent_test(client_id):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 45000))
        print(f"Client {client_id}: Connected to server")

        # Kirim permintaan TIME
        sock.send("TIME\r\n".encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print(f"Client {client_id}: Received {data.strip()}")

        # Tunggu sebentar sebelum keluar
        time.sleep(1)
        sock.send("QUIT\r\n".encode('utf-8'))
        sock.close()
        print(f"Client {client_id}: Disconnected")
    except Exception as e:
        print(f"Client {client_id} error: {e}")

# Fungsi utama untuk menjalankan semua tes
def execute_tests():
    print("Starting Time Server Client Tests")
    print("Ensure server is running on port 45000\n")

    # Jalankan tes klien tunggal
    run_single_test()

    # Jalankan tes klien concurrent
    print("=== Concurrent Client Test ===")
    client_threads = []
    for i in range(1, 4):  # 3 klien concurrent
        t = threading.Thread(target=run_concurrent_test, args=(i,))
        client_threads.append(t)
        t.start()
        time.sleep(0.3)  # Jeda kecil antar koneksi

    # Tunggu semua thread selesai
    for t in client_threads:
        t.join()

    print("\nAll tests completed!")

if __name__ == "__main__":
    execute_tests()
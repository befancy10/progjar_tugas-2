# Tugas 2

Bernisko Fancy Aljunez P.<br>
5025211083<br>
Pemrograman Jaringan C (2024/2025)<br>

### Buatlah sebuah program time server dengan ketentuan sebagai berikut:<br>
#### a. Membuka port port 45000 dengan transport TCP<br>
#### b. Server harus dapat menerima request yang concurrent, gunakan contoh multithreading pada materi <br>
#### c. Ketiak ada request yang masuk:<br>
  - Diawali dengan string "TIME" dan diakhiri dengan karakter 13 dan karakter 10
  - Setiap request dapat diakhiri dengan string "QUIT" yang diakhiri dengan karakter 13 dan karakter 10 <br>
#### d. Server akan memberikan response dengan format <br>
  - Dalam bentuk string "[JAM=spasi=jamo]" <br>
  - Diawali dengan "JAM=spasi=jamo" <br>
  - berisi info dalam format "HH:MM:SS" dengan karakter 13 dan karakter 10<br>

### Catatan
##### Untuk mendapatkan waktu sekarang dapat menggunakan contoh berikut:
```python
from datetime import datetime
now = datetime.now()
waktu = now.strftime("%H:%M:%S")
```
##### dan dapat dilihat bahwa:
  - waktu sekarang dapat disimpan dalam variable "waktu"
  - now.strftime("%H:%M:%S") akan mengkonversi waktu saat ini ke string dengan format HH:MM:SS
#### Tuliskan dalam satu file PDF dengan nama TUGAS2.pdf
##### 1. Link menuju source code dan di github (masing-masing harus punya repository sendiri)
##### 2. Semua output dari eksekusi program
##### 3. Semua gambar hasil eksekusi program harus disertakan
##### 4. Semua poin, harus dilengkapi dengan penjelasan minimal 50 kata

#### Penjelasan Kode
##### time_server.py
This file implements a TCP-based time server that listens on port 45000. It uses multithreading to handle multiple client connections concurrently. The handle_client function processes incoming requests, responding with the current time in "JAM HH:MM:SS" format for "TIME" commands and closing the connection on "QUIT". The main function sets up the server socket and manages client threads.

##### test_client.py
This file contains a client testing script with two test functions. run_single_test performs a single client connection, sending "TIME" and "QUIT" commands. run_concurrent_test tests multiple clients simultaneously using threading. The execute_tests function orchestrates both tests, ensuring the server's concurrent handling capabilities are validated.

#### Screenshot Output

##### 3.1 Server Startup
![image](https://github.com/user-attachments/assets/d1725d01-f72c-4215-998f-decf7997d552)

Server berhasil dijalankan pada port 45000 dengan menampilkan pesan "Time server running on port 45000...". Server terikat pada alamat 0.0.0.0, memungkinkan koneksi dari berbagai antarmuka jaringan. Inisialisasi socket TCP dan pengaturan multithreading berjalan lancar, mengonfirmasi kesiapan server untuk menangani beberapa koneksi klien secara bersamaan.

##### 3.2 Single Client Test
![image](https://github.com/user-attachments/assets/f7cbf2ef-7a64-4551-bb2b-17bb1a58b268)

Keluaran dari test_client.py menunjukkan koneksi klien tunggal ke port 45000 berhasil dengan pesan "Successfully connected to server". Permintaan "TIME" menerima respons "JAM 22:22:03" (10:22 PM WIB, 29 Juni 2025), dan perintah "QUIT" menutup koneksi dengan pesan "Connection terminated", membuktikan komunikasi berjalan dengan benar.

##### 3.3 Multiple Concurrent Connections
![image](https://github.com/user-attachments/assets/532d3c6d-7a15-438f-b00e-4e63764ae307)

Tiga klien (Klien 1, 2, 3) terhubung secara bersamaan, masing-masing menerima "JAM 22:22:03", "JAM 22:22:04", dan "JAM 22:22:04" (10:22 PM WIB, 29 Juni 2025). Semua klien terputus setelah "QUIT", dengan pesan "All tests completed!" mengonfirmasi keberhasilan multithreading.

##### 3.4 Server Log Output
![image](https://github.com/user-attachments/assets/47818c7f-71a1-4874-8bfd-0927f8badeee)

Log server menunjukkan "Time server running on port 45000..." dan mencatat empat koneksi dari '127.0.0.1' dengan port dinamis (53442-53445). Setiap koneksi ditutup dengan "Connection closed from ('127.0.0.1', )" setelah "QUIT", membuktikan efektivitas multithreading dan penanganan protokol.

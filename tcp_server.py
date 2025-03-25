# TCP SERVER - Arbaaz 29052
import socket
import time

def start_server():
    # Socket creation and binding
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 12344))
    server_socket.listen(5)
    print('TCP server is listening on port 12344\n')

    # Log file
    with open('tcp_log.txt', 'a') as log_file:
        log_file.write('\nTCP Server Log:\n')
        log_file.write('____________\n')

        client_socket, addr = server_socket.accept()
        print('Connection from: ', addr)
        log_file.write(f'Connection from: {addr}\n')

        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                received_time = time.time()
                message = data.decode()
                print('Received data: ', message)
                log_file.write(f'Received data: {message}\n')

                response = f"Received: {message}"
                start_send_time = time.time()
                client_socket.send(response.encode())
                send_time = time.time() - start_send_time

                print('Sent response: ', response, f'Time to send: {send_time:.6f} seconds')
                log_file.write(f'Sent response: {response}, Time to send: {send_time:.6f} seconds\n')

        except Exception as e:
            print('Error: ', e)
            log_file.write(f'Error: {str(e)}\n')
        finally:
            client_socket.close()
            server_socket.close()
            print('Connection closed')
            log_file.write('Connection closed\n')

if __name__ == '__main__':
    start_server()
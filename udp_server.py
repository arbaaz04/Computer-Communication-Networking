# UDP SERVER - Arbaaz 29052
import socket
import random
import time

def start_server():
    # Socket creation and binding
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 12345))
    print('UDP server is listening on port 12345\n')

    # Log file in append mode
    with open('udp_log.txt', 'a') as log_file:
        log_file.write('\nUDP Server Log:\n')
        log_file.write('____________\n')

        try:
            while True:
                data, addr = server_socket.recvfrom(1024)
                message = data.decode()
                print('Received data from', addr, ':', message)
                log_file.write(f'Received data from {addr}: {message}\n')

                
                if random.random() < 0.2:  # 20% drop rate
                    print(f'Dropped packet: {message}')
                    log_file.write(f'Dropped packet: {message}\n')
                    continue

                # Respond to client
                response = f"Received: {message}"
                start_send_time = time.time()
                server_socket.sendto(response.encode(), addr)  # Send back to client’s address
                send_time = time.time() - start_send_time

                print('Sent response:', response, f'Time to send: {send_time:.6f} seconds')
                log_file.write(f'Sent response: {response}, Time to send: {send_time:.6f} seconds\n')

        except Exception as e:
            print('Error:', e)
            log_file.write(f'Error: {str(e)}\n')
        finally:
            server_socket.close()
            print('Server closed')
            log_file.write('Server closed\n')

if __name__ == '__main__':
    start_server()

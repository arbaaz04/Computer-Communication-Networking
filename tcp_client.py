# TCP CLIENT - Arbaaz 29052
import socket
import time

def run_client():
    # Socket creation and server connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveraddr = ('127.0.0.1', 12344)
    client_socket.connect(serveraddr)
    print(f"Connected to server at {serveraddr}")

    # Messages sending
    num_msgs = 100
    total_bytes = 0
    latencies = []

    # Log file
    with open('tcp_log.txt', 'a') as log_file:
        log_file.write('\nTCP Client Log:\n')
        log_file.write('____________\n')

        try:
            timestart = time.time()
            for i in range(num_msgs):
                msg = f"Message {i+1}"
                msg_bytes = msg.encode('utf-8')
                total_bytes += len(msg_bytes)
                start_time = time.time()
                client_socket.send(msg_bytes)
                data = client_socket.recv(1024).decode()
                rtt = time.time() - start_time
                latencies.append(rtt)

                log_file.write(f"Message {i+1}: Sent: {msg}, Received: {data}, RTT = {rtt:.6f} seconds\n")
                print(f"Message {i+1}: Sent: {msg}, Received: {data}, RTT: {rtt:.6f} seconds")


            total_time = time.time() - timestart
            avg_latency = sum(latencies) / len(latencies)
            throughput = total_bytes / total_time  # Bytes per second

            summary = f"""
TCP Summary:
Total time: {total_time:.2f} seconds
Average latency: {avg_latency * 1000:.2f} ms
Throughput: {throughput / 1024:.2f} KB/s
Messages sent: {num_msgs}
Bytes sent: {total_bytes}
            """
            print(summary)
            log_file.write(summary)
        except Exception as e:
            print(f"Error: {e}")
            log_file.write(f"Error: {e}\n")
        finally:
            client_socket.close()
            print("Connection closed")
            log_file.write("Connection closed\n")

if __name__ == "__main__":
    run_client()
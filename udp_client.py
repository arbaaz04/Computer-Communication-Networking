# UDP CLIENT - Arbaaz 29052
import socket
import time

def run_client():
    # Socket creation
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('127.0.0.1', 12345)
    client_socket.settimeout(1.0)  # 1-second timeout for responses
    print(f"UDP client targeting server at {server_addr}")

    # Messages and tracking
    num_msgs = 100
    total_bytes = 0
    latencies = []
    packets_sent = 0
    packets_received = 0

    # Log file in append mode
    with open('udp_log.txt', 'a') as log_file:
        log_file.write('\nUDP Client Log:\n')
        log_file.write('____________\n')

        try:
            timestart = time.time()
            for i in range(num_msgs):
                msg = f"Message {i+1}"
                msg_bytes = msg.encode('utf-8')
                total_bytes += len(msg_bytes)
                packets_sent += 1

                start_time = time.time()
                client_socket.sendto(msg_bytes, server_addr)

                try:
                    data, _ = client_socket.recvfrom(1024)
                    rtt = time.time() - start_time
                    latencies.append(rtt)
                    packets_received += 1
                    received_msg = data.decode()
                    print(f"Message {i+1}: Sent: {msg}, Received: {received_msg}, RTT: {rtt:.6f} seconds")
                    log_file.write(f"Message {i+1}: Sent: {msg}, Received: {received_msg}, RTT: {rtt:.6f} seconds\n")
                except socket.timeout:
                    print(f"Message {i+1}: Sent: {msg}, No response (dropped)")
                    log_file.write(f"Message {i+1}: Sent: {msg}, No response (dropped)\n")

            total_time = time.time() - timestart
            avg_latency = sum(latencies) / len(latencies) if latencies else 0
            packet_loss_rate = (packets_sent - packets_received) / packets_sent * 100
            throughput = total_bytes / total_time if total_time > 0 else 0

            summary = f"""
UDP Summary:
Total time: {total_time:.2f} seconds
Average latency: {avg_latency * 1000:.2f} ms (of received packets)
Packet loss rate: {packet_loss_rate:.2f}%
Throughput: {throughput / 1024:.2f} KB/s
Messages sent: {packets_sent}
Messages received: {packets_received}
Bytes sent: {total_bytes}
            """
            print(summary)
            log_file.write(summary)

        except Exception as e:
            print(f"Error: {e}")
            log_file.write(f"Error: {e}\n")
        finally:
            client_socket.close()
            print("Client closed")
            log_file.write("Client closed\n")

if __name__ == "__main__":
    run_client()

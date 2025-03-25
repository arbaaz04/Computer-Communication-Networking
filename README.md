
# Assignment #2: Socket Programming - TCP vs. UDP Comparison
By Arbaaz Murtaza (29052), IBA Karachi.

## Overview
This project implements TCP and UDP client-server applications in Python to compare latency, packet loss, and throughput. Submissions include `tcp_server.py`, `tcp_client.py`, `udp_server.py`, `udp_client.py` and logs (`tcp_log.txt`, `udp_log.txt`).

## How to Run

### TCP
1. Open two Terminal windows.
2. Server: `cd ~/CCN\ HW2 && python3 tcp_server.py` (port 12344).
3. Client: `cd ~/CCN\ HW2 && python3 tcp_client.py`.
4. Logs to `tcp_log.txt`.

### UDP
1. Open two Terminal windows.
2. Server: `cd ~/CCN\ HW2 && python3 udp_server.py` (port 12345).
3. Client: `cd ~/CCN\ HW2 && python3 udp_client.py`.
4. Logs to `udp_log.txt`.

## Expected Outputs

### TCP
- **Server**: "Connection from: ('127.0.0.1', <port>)", "Sent response: Received: Message X, Time to send: ~0.00002 seconds".
- **Client**: "Message X: Sent: Message X, Received: Received: Message X, RTT: ~0.0001 seconds", Summary: ~0.08 ms latency, ~105.33 KB/s throughput, 1092 bytes sent.

### UDP
- **Server**: "Received data from ('127.0.0.1', <port>): Message X", "Dropped packet: Message Y", "Sent response: Received: Message X, Time to send: ~0.00003 seconds".
- **Client**: "Message X: Sent: Message X, Received: Received: Message X, RTT: ~0.0002 seconds" or "No response (dropped)", Summary: ~0.26 ms latency, ~26% loss, ~0.04 KB/s throughput, 1092 bytes sent.

## Observations (TCP vs. UDP)

### Latency
- TCP: 0.08 ms avg—higher due to handshakes/ACKs.
- UDP: 0.26 ms avg (received packets)—faster per packet but timeouts inflate total time.

### Reliability & Packet Loss
- TCP: 0% loss—reliable delivery.
- UDP: 26% loss—unreliable, drops simulated at 20%.

### Throughput
- TCP: 105.33 KB/s—steady due to no loss.
- UDP: 0.04 KB/s—low due to drops/timeouts.

### Use Cases
- TCP: HTTP, file transfers (reliable).
- UDP: VoIP, streaming (real-time, loss-tolerant).

## Implementation Notes
- TCP: Uses `SOCK_STREAM`, measures server send time and client RTT.
- UDP: Uses `SOCK_DGRAM`, 20% drop rate, 1s timeout for loss detection.
- Tools: Python `socket`, `time`, `random` for simulation.

## Files
- `tcp_server.py`, `tcp_client.py`, `udp_server.py`, `udp_client.py`
- `tcp_log.txt`, `udp_log.txt`

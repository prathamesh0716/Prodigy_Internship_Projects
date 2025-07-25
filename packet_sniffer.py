from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet:")
        print(f"    From: {ip_layer.src}")
        print(f"    To:   {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")

        if TCP in packet:
            print("    TCP Packet")
        elif UDP in packet:
            print("    UDP Packet")
        else:
            print("    Other IP Protocol")

# Start sniffing (you may need to run as Administrator)
print("🔍 Starting Packet Sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=10)  # Capture 10 packets

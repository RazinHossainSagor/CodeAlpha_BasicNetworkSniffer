from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_num = packet[IP].proto
        
        protocol_name = "Other"
        payload_preview = ""

        if packet.haslayer(TCP):
            protocol_name = "TCP"
            payload_preview = bytes(packet[TCP].payload)[:50]
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
            payload_preview = bytes(packet[UDP].payload)[:50]
        elif packet.haslayer(ICMP):
            protocol_name = "ICMP"
            payload_preview = bytes(packet[ICMP].payload)[:50]
        else:
            protocol_name = f"Protocol-{protocol_num}"

        print("-" * 65)
        print(f"[+] Traffic: {src_ip}  --->  {dst_ip} | Protocol: {protocol_name}")
        if payload_preview:
            print(f"    Payload Preview (First 50 Bytes): {payload_preview}")

print("=" * 65)
print("[*] Basic Network Sniffer is running... Capturing 10 packets...")
print("=" * 65)

sniff(prn=packet_callback, count=10)
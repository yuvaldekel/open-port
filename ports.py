from scapy.all import TCP, IP, send, sr1

def main():
    ip = input("Enter an ip: ")

    for port in range(20,1025):
        syn_segment = IP(dst = ip)/TCP(dport = port, seq = 123, flags = 2)
        syn_ack_packet = sr1(syn_segment, timeout = 5)
        if syn_ack_packet != None:
            if 'R' in syn_ack_packet[TCP].flags:
                print(f'Port {port} is close.')
            else:
                print(f'Port {port} is open.')
        else:
            print(f'Port {port} is close.')

if __name__ == "__main__":
    main()
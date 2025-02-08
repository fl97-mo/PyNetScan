import socket

def scan_ports(target):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  
        result = sock.connect_ex((target, port))  
        if result == 0:
            print(f"🟢 Port {port} is open   🟢")
        else:
            print(f"🔴 Port {port} is closed 🔴")
        sock.close()

target = input("Ip- address or domain: ")
scan_ports(target)

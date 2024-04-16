import socket

def scan_vulnerabilities(ip):
    print("Scanning vulnerabilities for IP:", ip)
    open_ports = []
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
    except Exception as e:
        print("Error scanning ports:", e)

    if open_ports:
        print("Open ports found:", open_ports)
    else:
        print("No open ports found.")

def main():
    
    ip = input("Enter the IP address to scan: ")

    if ip:
        scan_vulnerabilities(ip)
    else:
        print("No IP address provided. Exiting.")

if __name__ == "__main__":
    main()

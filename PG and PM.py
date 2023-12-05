import random
import string
import socket
import subprocess

# Password Generator Functions
def generate_password(length, use_special_chars, use_japanese_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_japanese_chars:
        characters += 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("Password length: "))
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    use_japanese_chars = input("Include Japanese characters? (yes/no): ").lower() == 'yes'
    for _ in range(num_passwords):
        print(generate_password(length, use_special_chars, use_japanese_chars))

# Ports Management Functions
def open_port(port, protocol):
    command = f"netsh advfirewall firewall add rule name=\"Open Port {port}\" dir=in action=allow protocol={protocol} localport={port}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Port {port} opened successfully.")
    else:
        print(f"Failed to open port {port}. Error: {result.stderr}")

def close_port(port, protocol):
    command = f"netsh advfirewall firewall delete rule name=\"Open Port {port}\" protocol={protocol} localport={port}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Port {port} closed successfully.")
    else:
        print(f"Failed to close port {port}. Error: {result.stderr}")

def check_port_status(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_port_description(port):
    common_ports_info = {
        20: "FTP Data Transfer",
        21: "FTP Command Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "Remote Desktop (RDP)",
        5432: "PostgreSQL",
        5900: "VNC",
        8080: "HTTP Alternate"
        # Add more common ports and their descriptions here
    }
    return common_ports_info.get(port, "Unknown")

def list_all_ports(start_port, end_port):
    for port in range(start_port, end_port + 1):
        status = "Open" if check_port_status(port) else "Closed"
        description = get_port_description(port)
        print(f"Port {port}: {status} - {description}")

def explain_common_ports():
    common_ports_info = {
        20: "FTP Data Transfer",
        21: "FTP Command Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "Remote Desktop (RDP)",
        5432: "PostgreSQL",
        5900: "VNC",
        8080: "HTTP Alternate"
        # Add more common ports and their descriptions here
    }
    for port, description in common_ports_info.items():
        print(f"Port {port}: {description}")

def explain_tcp_udp():
    explanation = """
    TCP (Transmission Control Protocol) is a connection-oriented protocol. It establishes a connection before transmitting data and ensures that all data is received and in order. It's suitable for applications where reliable delivery is more important than speed, like web browsing and email.

    UDP (User Datagram Protocol) is a connectionless protocol. It sends data without establishing a connection, and there is no guarantee that all data will be received or in order. It's used in applications where speed is more important than reliability, like streaming and online gaming.
    """
    print(explanation)

def manage_ports():
    while True:
        choice = input("Choose an option: \n1. Open a port\n2. Close a port\n3. List all ports\n4. List common ports\n5. Explain TCP vs UDP\n6. Exit\n> ")
        if choice == '1':
            port = input("Enter the port number: ")
            protocol = input("Enter the protocol (TCP/UDP): ").upper()
            open_port(port, protocol)
        elif choice == '2':
            port = input("Enter the port number: ")
            protocol = input("Enter the protocol (TCP/UDP): ").upper()
            close_port(port, protocol)
        elif choice == '3':
            start_port = int(input("Enter the start port number: "))
            end_port = int(input("Enter the end port number: "))
            list_all_ports(start_port, end_port)
        elif choice == '4':
            explain_common_ports()
        elif choice == '5':
            explain_tcp_udp()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

# Main Menu
def main_menu():
    while True:
        choice = input("Choose a program to run: \n1. Password Generator\n2. Ports Management\n3. Exit\n> ")
        if choice == '1':
            password_generator()
        elif choice == '2':
            manage_ports()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()

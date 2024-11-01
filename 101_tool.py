# 101_tool.py
import platform
import socket
import requests
from datetime import datetime

# ASCII Art
ASCII_ART = """
  :::   :::::::    :::        ::::::::::: ::::::::   ::::::::  :::        
:+:+:  :+:   :+: :+:+:            :+:    :+:    :+: :+:    :+: :+:        
  +:+  +:+  :+:+   +:+            +:+    +:+    +:+ +:+    +:+ +:+        
  +#+  +#+ + +:+   +#+            +#+    +#+    +:+ +#+    +:+ +#+        
  +#+  +#+#  +#+   +#+            +#+    +#+    +#+ +#+    +#+ +#+        
  #+#  #+#   #+#   #+#            #+#    #+#    #+# #+#    #+# #+#        
####### #######  #######          ###     ########   ########  ########## 
abdula-2fal
"""


def display_menu():
    """Display the menu options."""
    print("\nWelcome to the 101 Tool!")
    print("1. Display System Information")
    print("2. Display Local IP Address")
    print("3. Display Public IP Address")
    print("4. Perform Port Scan")
    print("5. Exit")


def display_system_info():
    """Display basic system information."""
    print("\nSystem Information:")
    print(f"  OS: {platform.system()}")
    print(f"  OS Version: {platform.version()}")
    print(f"  Architecture: {platform.machine()}")
    print(f"  Processor: {platform.processor()}")


def display_local_ip():
    """Display the local IP address of the machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"\nLocal IP Address: {ip_address}")


def display_public_ip():
    """Retrieve and display the public IP address of the machine."""
    try:
        response = requests.get("https://api.ipify.org?format=json")
        public_ip = response.json().get("ip")
        print(f"\nPublic IP Address: {public_ip}")
    except requests.RequestException:
        print("\nError: Could not retrieve public IP address. Check your internet connection.")


def perform_port_scan():
    """Perform a simple port scan on a specified IP address or domain."""
    target = input("\nEnter the IP address or domain to scan: ")
    ports = [21, 22, 23, 25, 80, 110, 443]  # Common ports to scan
    print(f"\nStarting port scan on {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()
    print("Port scan completed.")


def main():
    """Main function to run the tool."""
    print(ASCII_ART)  # Display ASCII art at startup
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            display_system_info()
        elif choice == "2":
            display_local_ip()
        elif choice == "3":
            display_public_ip()
        elif choice == "4":
            perform_port_scan()
        elif choice == "5":
            print("\nExiting the 101 Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
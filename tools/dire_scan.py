#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DIRE-SCAN: Advanced Port Scanner
Developed by Mr Dire
"""

import socket
import sys
import os
import threading
from queue import Queue
from time import sleep

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))
from colors import Colors
from functions import clear_screen, print_success, print_error, print_info

class DireScan:
    def __init__(self):
        self.target = None
        self.ports = Queue()
        self.open_ports = []
        self.threads = 100
        self.timeout = 1
        
    def banner(self):
        print(f"""
{Colors.RED}{Colors.BOLD}
    ╔╦╗╦╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
     ║║║╠═╝╠╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
    ═╩╝╩╩  ╩╚═  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
{Colors.YELLOW}
              🔍 PORT SCANNER 🔍
{Colors.GREEN}              Module 2 of 20{Colors.RESET}
        """)
    
    def port_scan(self, port):
        """Scan single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                service = socket.getservbyport(port, 'tcp') if port < 1024 else "Unknown"
                self.open_ports.append((port, service))
                print_success(f"Port {port} OPEN - {service}")
            sock.close()
        except:
            pass
    
    def threader(self):
        """Thread worker"""
        while True:
            port = self.ports.get()
            self.port_scan(port)
            self.ports.task_done()
    
    def run(self):
        clear_screen()
        self.banner()
        
        # Get target
        self.target = input(f"{Colors.CYAN}[➤] Target IP/Domain: {Colors.RESET}")
        if not self.target:
            print_error("No target specified!")
            return
        
        # Resolve domain if needed
        try:
            self.target = socket.gethostbyname(self.target)
            print_info(f"Resolved to: {self.target}")
        except:
            print_error("Invalid target!")
            return
        
        # Port range
        port_range = input(f"{Colors.CYAN}[➤] Port range (default 1-1000): {Colors.RESET}") or "1-1000"
        start_port, end_port = map(int, port_range.split('-'))
        
        print_info(f"Scanning {self.target}...")
        print_info(f"Threads: {self.threads}")
        
        # Start threads
        for _ in range(self.threads):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()
        
        # Add ports to queue
        for port in range(start_port, end_port + 1):
            self.ports.put(port)
        
        self.ports.join()
        
        # Results
        print(f"\n{Colors.CYAN}[+] Scan Complete!{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Open Ports Found: {len(self.open_ports)}{Colors.RESET}")
        for port, service in self.open_ports:
            print(f"    {Colors.YELLOW}Port {port}:{Colors.RESET} {service}")

if __name__ == "__main__":
    try:
        tool = DireScan()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Scan interrupted{Colors.RESET}")

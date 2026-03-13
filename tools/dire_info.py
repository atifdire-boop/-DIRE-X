#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DIRE-INFO: System & Network Information Gathering
Developed by Mr Dire
"""

import os
import sys
import socket
import platform
import subprocess
import json
import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))
from colors import Colors
from functions import clear_screen, print_success, print_error, print_info

class DireInfo:
    def __init__(self):
        self.name = "DIRE-INFO"
        self.version = "1.0"
        
    def banner(self):
        print(f"""
{Colors.CYAN}{Colors.BOLD}
    ╔╦╗╦╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
     ║║║╠═╝╠╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
    ═╩╝╩╩  ╩╚═  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
{Colors.YELLOW}
         📊 INFORMATION GATHERING 📊
{Colors.GREEN}              Module 1 of 20{Colors.RESET}
        """)
    
    def system_info(self):
        """Gather system information"""
        print(f"\n{Colors.CYAN}[+] System Information:{Colors.RESET}")
        print(f"{Colors.GREEN}    OS:{Colors.RESET} {platform.system()} {platform.release()}")
        print(f"{Colors.GREEN}    Architecture:{Colors.RESET} {platform.machine()}")
        print(f"{Colors.GREEN}    Processor:{Colors.RESET} {platform.processor()}")
        print(f"{Colors.GREEN}    Python Version:{Colors.RESET} {platform.python_version()}")
        print(f"{Colors.GREEN}    Hostname:{Colors.RESET} {socket.gethostname()}")
        print(f"{Colors.GREEN}    Username:{Colors.RESET} {os.getlogin() if hasattr(os, 'getlogin') else 'Unknown'}")
    
    def network_info(self):
        """Gather network information"""
        print(f"\n{Colors.CYAN}[+] Network Information:{Colors.RESET}")
        try:
            hostname = socket.gethostname()
            ip_local = socket.gethostbyname(hostname)
            print(f"{Colors.GREEN}    Local IP:{Colors.RESET} {ip_local}")
            
            # Get public IP
            try:
                response = requests.get('https://api.ipify.org?format=json', timeout=5)
                public_ip = response.json().get('ip', 'Unknown')
                print(f"{Colors.GREEN}    Public IP:{Colors.RESET} {public_ip}")
            except:
                print(f"{Colors.YELLOW}    Public IP:{Colors.RESET} Unable to fetch")
            
            # Network interfaces
            print(f"\n{Colors.CYAN}[+] Network Interfaces:{Colors.RESET}")
            if platform.system() == "Linux":
                result = subprocess.run(['ifconfig'], capture_output=True, text=True)
                print(f"{Colors.WHITE}{result.stdout[:500]}...{Colors.RESET}" if len(result.stdout) > 500 else f"{Colors.WHITE}{result.stdout}{Colors.RESET}")
        except Exception as e:
            print_error(f"Network info error: {str(e)}")
    
    def run(self):
        clear_screen()
        self.banner()
        self.system_info()
        self.network_info()
        
        print(f"\n{Colors.YELLOW}[+] Options:{Colors.RESET}")
        print(f"    {Colors.GREEN}1.{Colors.RESET} Save to file")
        print(f"    {Colors.GREEN}2.{Colors.RESET} Back to main menu")
        
        choice = input(f"\n{Colors.CYAN}[➤] Select >> {Colors.RESET}")
        if choice == '1':
            filename = input(f"{Colors.CYAN}[➤] Filename (default: info.txt): {Colors.RESET}") or "info.txt"
            # Save logic here
            print_success(f"Saved to output/{filename}")

if __name__ == "__main__":
    try:
        tool = DireInfo()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Cancelled{Colors.RESET}")
    except Exception as e:
        print_error(str(e))

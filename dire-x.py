#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║     ██████╗ ██╗██████╗ ███████╗    ██╗  ██╗                    ║
║     ██╔══██╗██║██╔══██╗██╔════╝    ╚██╗██╔╝                    ║
║     ██║  ██║██║██████╔╝█████╗       ╚███╔╝                     ║
║     ██║  ██║██║██╔══██╗██╔══╝       ██╔██╗                     ║
║     ██████╔╝██║██║  ██║███████╗    ██╔╝ ██╗                    ║
║     ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝                    ║
║                                                                ║
║            ADVANCED CYBERSECURITY TOOLKIT                  ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
             Developed by Mr Dire 
"""

import os
import sys
import json
import subprocess
from time import sleep

# Add core directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from colors import Colors
from banner import show_banner, show_menu
from functions import clear_screen, print_error, print_success, print_info

class DireX:
    def __init__(self):
        self.version = "2.0"
        self.author = "Mr Dire"
        self.tools = {
            1: {"name": "DIRE-INFO", "file": "dire_info.py", "desc": "System & Network Information Gathering"},
            2: {"name": "DIRE-SCAN", "file": "dire_scan.py", "desc": "Advanced Port Scanner"},
            3: {"name": "DIRE-BRUTE", "file": "dire_brute.py", "desc": "Brute Force Attack Framework"},
            4: {"name": "DIRE-SQL", "file": "dire_sql.py", "desc": "SQL Injection Scanner & Exploiter"},
            5: {"name": "DIRE-XSS", "file": "dire_xss.py", "desc": "Cross-Site Scripting Scanner"},
            6: {"name": "DIRE-PHISH", "file": "dire_phish.py", "desc": "Phishing Page Generator"},
            7: {"name": "DIRE-DDOS", "file": "dire_ddos.py", "desc": "DDoS Attack Tool (Educational)"},
            8: {"name": "DIRE-ANON", "file": "dire_anon.py", "desc": "Anonymity & Proxy Checker"},
            9: {"name": "DIRE-WIFI", "file": "dire_wifi.py", "desc": "WiFi Security Auditor"},
            10: {"name": "DIRE-MAL", "file": "dire_mal.py", "desc": "Malware Analysis Tool"},
            11: {"name": "DIRE-CRYPTO", "file": "dire_crypto.py", "desc": "Encryption/Decryption Suite"},
            12: {"name": "DIRE-OSINT", "file": "dire_osint.py", "desc": "Open Source Intelligence"},
            13: {"name": "DIRE-EXPLOIT", "file": "dire_exploit.py", "desc": "Exploit Search & Framework"},
            14: {"name": "DIRE-WEB", "file": "dire_web.py", "desc": "Web Application Scanner"},
            15: {"name": "DIRE-SOCIAL", "file": "dire_social.py", "desc": "Social Engineering Toolkit"},
            16: {"name": "DIRE-CAM", "file": "dire_cam.py", "desc": "Camera Security Scanner"},
            17: {"name": "DIRE-REPORT", "file": "dire_report.py", "desc": "Pentest Report Generator"},
            18: {"name": "DIRE-UPDATE", "file": "dire_update.py", "desc": "System Updater"},
            19: {"name": "DIRE-BACKUP", "file": "dire_backup.py", "desc": "Data Backup & Restore"},
            20: {"name": "DIRE-HELP", "file": "dire_help.py", "desc": "Documentation & Help"},
        }
        
    def run(self):
        while True:
            clear_screen()
            show_banner()
            show_menu(self.tools)
            
            try:
                choice = input(f"\n{Colors.CYAN}[{Colors.YELLOW}➤{Colors.CYAN}] Select Option {Colors.WHITE}>> {Colors.RESET}")
                
                if choice.lower() in ['exit', 'quit', '0']:
                    self.exit_tool()
                elif choice == '99':
                    self.show_about()
                elif choice.isdigit() and int(choice) in self.tools:
                    self.launch_tool(int(choice))
                else:
                    print_error("Invalid option! Please try again.")
                    sleep(1)
                    
            except KeyboardInterrupt:
                self.exit_tool()
            except Exception as e:
                print_error(f"Error: {str(e)}")
                sleep(1)
    
    def launch_tool(self, tool_id):
        tool = self.tools[tool_id]
        tool_path = os.path.join('tools', tool['file'])
        
        if os.path.exists(tool_path):
            print_info(f"Launching {tool['name']}...")
            sleep(1)
            try:
                subprocess.run([sys.executable, tool_path])
                input(f"\n{Colors.GREEN}[+] Press Enter to return to main menu...{Colors.RESET}")
            except Exception as e:
                print_error(f"Failed to launch {tool['name']}: {str(e)}")
                sleep(2)
        else:
            print_error(f"Tool file not found: {tool_path}")
            sleep(2)
    
    def show_about(self):
        clear_screen()
        print(f"""
{Colors.CYAN}{'='*60}{Colors.RESET}
{Colors.YELLOW}{' '*15}🔥 ABOUT DIRE-X 🔥{Colors.RESET}
{Colors.CYAN}{'='*60}{Colors.RESET}

{Colors.GREEN}[+] Tool Name:{Colors.RESET} DIRE-X Advanced Cybersecurity Toolkit
{Colors.GREEN}[+] Version:{Colors.RESET} {self.version}
{Colors.GREEN}[+] Author:{Colors.RESET} {self.author}
{Colors.GREEN}[+] Platform:{Colors.RESET} Termux / Linux / macOS / Windows

{Colors.CYAN}{'='*60}{Colors.RESET}
{Colors.YELLOW}{' '*15}👨‍💻 ABOUT DEVELOPER 👨‍💻{Colors.RESET}
{Colors.CYAN}{'='*60}{Colors.RESET}

{Colors.WHITE}I'm Mr Dire, a technology learner with a deep interest in 
cybersecurity and ethical hacking. Along with that, I have 
experience in web development and app development. I enjoy 
analyzing applications, exploring security techniques, and 
learning advanced tech skills.{Colors.RESET}

{Colors.CYAN}{'='*60}{Colors.RESET}
{Colors.RED}⚠️  DISCLAIMER: Use this tool for educational purposes only!{Colors.RESET}
{Colors.CYAN}{'='*60}{Colors.RESET}
        """)
        input(f"\n{Colors.GREEN}[+] Press Enter to continue...{Colors.RESET}")
    
    def exit_tool(self):
        clear_screen()
        print(f"""
{Colors.RED}{'='*50}{Colors.RESET}
{Colors.YELLOW}{' '*10}Thanks for using DIRE-X!{Colors.RESET}
{Colors.GREEN}{' '*15}Stay Safe, Stay Ethical{Colors.RESET}
{Colors.CYAN}{' '*20}~ Mr Dire{Colors.RESET}
{Colors.RED}{'='*50}{Colors.RESET}
        """)
        sys.exit(0)

if __name__ == "__main__":
    try:
        app = DireX()
        app.run()
    except Exception as e:
        print(f"{Colors.RED}[!] Fatal Error: {str(e)}{Colors.RESET}")
        sys.exit(1)


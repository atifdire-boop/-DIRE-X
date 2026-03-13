#!/usr/bin/env python3
import os
import sys
import socket
import platform
import subprocess
from time import sleep

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear():
    os.system('clear')

def banner():
    print(f"""{CYAN}
╔════════════════════════════════════════════════════╗
║     ██████╗ ██╗██████╗ ███████╗    ██╗  ██╗      ║
║     ██╔══██╗██║██╔══██╗██╔════╝    ╚██╗██╔╝      ║
║     ██║  ██║██║██████╔╝█████╗       ╚███╔╝       ║
║     ██║  ██║██║██╔══██╗██╔══╝       ██╔██╗       ║
║     ██████╔╝██║██║  ██║███████╗    ██╔╝ ██╗      ║
║     ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝      ║
╚════════════════════════════════════════════════════╝{RESET}
{YELLOW}              Developed by Mr Dire v2.0{RESET}
{GREEN}              GitHub: atifdire-boop{RESET}
""")

def menu():
    print(f"""
{GREEN}[+] AVAILABLE TOOLS:{RESET}

{CYAN}[01]{WHITE} DIRE-INFO    {RESET}- System Information
{CYAN}[02]{WHITE} DIRE-SCAN    {RESET}- Port Scanner  
{CYAN}[03]{WHITE} DIRE-BRUTE   {RESET}- Brute Force
{CYAN}[04]{WHITE} DIRE-SQL     {RESET}- SQL Scanner
{CYAN}[05]{WHITE} DIRE-XSS     {RESET}- XSS Scanner
{CYAN}[06]{WHITE} DIRE-PHISH   {RESET}- Phishing Generator
{CYAN}[07]{WHITE} DIRE-DDOS    {RESET}- DDoS Tool
{CYAN}[08]{WHITE} DIRE-ANON    {RESET}- Anonymity Checker
{CYAN}[09]{WHITE} DIRE-WIFI    {RESET}- WiFi Auditor
{CYAN}[10]{WHITE} DIRE-MAL     {RESET}- Malware Analysis
{CYAN}[11]{WHITE} DIRE-CRYPTO  {RESET}- Encryption
{CYAN}[12]{WHITE} DIRE-OSINT   {RESET}- OSINT Tool
{CYAN}[13]{WHITE} DIRE-EXPLOIT {RESET}- Exploit Framework
{CYAN}[14]{WHITE} DIRE-WEB     {RESET}- Web Scanner
{CYAN}[15]{WHITE} DIRE-SOCIAL  {RESET}- Social Engineering
{CYAN}[16]{WHITE} DIRE-CAM     {RESET}- Camera Scanner
{CYAN}[17]{WHITE} DIRE-REPORT  {RESET}- Report Generator
{CYAN}[18]{WHITE} DIRE-UPDATE  {RESET}- System Updater
{CYAN}[19]{WHITE} DIRE-BACKUP  {RESET}- Backup Tool
{CYAN}[20]{WHITE} DIRE-HELP    {RESET}- Help & Docs

{CYAN}[99]{WHITE} About
{CYAN}[0]{WHITE} Exit
""")

def tool_info():
    clear()
    print(f"\n{GREEN}[*] DIRE-INFO - System Information{RESET}\n")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Architecture: {platform.machine()}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"IP Address: {ip}")
    except:
        print("IP: Not available")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_scan():
    clear()
    print(f"\n{GREEN}[*] DIRE-SCAN - Port Scanner{RESET}\n")
    target = input("Enter target IP: ")
    if not target:
        return
    print(f"\nScanning {target}...\n")
    ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_brute():
    clear()
    print(f"\n{GREEN}[*] DIRE-BRUTE - Brute Force{RESET}\n")
    print("This is a demo version")
    print("Passwords: admin, root, 123456")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_sql():
    clear()
    print(f"\n{GREEN}[*] DIRE-SQL - SQL Scanner{RESET}\n")
    print("SQL Injection Scanner (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_xss():
    clear()
    print(f"\n{GREEN}[*] DIRE-XSS - XSS Scanner{RESET}\n")
    print("XSS Vulnerability Scanner (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_phish():
    clear()
    print(f"\n{GREEN}[*] DIRE-PHISH - Phishing Generator{RESET}\n")
    print("Creating phishing page...")
    os.makedirs("output", exist_ok=True)
    with open("output/index.html", "w") as f:
        f.write("<html><body><h1>Login Page</h1><form><input type='text'><input type='password'></form></body></html>")
    print("Phishing page created in output/ folder")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_ddos():
    clear()
    print(f"\n{GREEN}[*] DIRE-DDOS - DDoS Tool{RESET}\n")
    print("Educational Purpose Only")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_anon():
    clear()
    print(f"\n{GREEN}[*] DIRE-ANON - Anonymity Checker{RESET}\n")
    try:
        import requests
        ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"Your IP: {ip}")
    except:
        print("Could not fetch IP")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_wifi():
    clear()
    print(f"\n{GREEN}[*] DIRE-WIFI - WiFi Auditor{RESET}\n")
    os.system('termux-wifi-scaninfo || echo "Run: termux-wifi-scaninfo"')
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_mal():
    clear()
    print(f"\n{GREEN}[*] DIRE-MAL - Malware Analysis{RESET}\n")
    print("Malware Analysis Tool (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_crypto():
    clear()
    print(f"\n{GREEN}[*] DIRE-CRYPTO - Encryption{RESET}\n")
    text = input("Enter text to encrypt: ")
    encoded = text.encode('utf-8').hex()
    print(f"Encrypted: {encoded}")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_osint():
    clear()
    print(f"\n{GREEN}[*] DIRE-OSINT - OSINT Tool{RESET}\n")
    print("Open Source Intelligence (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_exploit():
    clear()
    print(f"\n{GREEN}[*] DIRE-EXPLOIT - Exploit Framework{RESET}\n")
    print("Exploit Search Framework (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_web():
    clear()
    print(f"\n{GREEN}[*] DIRE-WEB - Web Scanner{RESET}\n")
    print("Web Application Scanner (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_social():
    clear()
    print(f"\n{GREEN}[*] DIRE-SOCIAL - Social Engineering{RESET}\n")
    print("Social Engineering Toolkit (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_cam():
    clear()
    print(f"\n{GREEN}[*] DIRE-CAM - Camera Scanner{RESET}\n")
    print("Camera Security Scanner (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_report():
    clear()
    print(f"\n{GREEN}[*] DIRE-REPORT - Report Generator{RESET}\n")
    print("Pentest Report Generator (Demo)")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_update():
    clear()
    print(f"\n{GREEN}[*] DIRE-UPDATE - System Updater{RESET}\n")
    print("Checking for updates...")
    os.system('git pull')
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_backup():
    clear()
    print(f"\n{GREEN}[*] DIRE-BACKUP - Backup Tool{RESET}\n")
    print("Creating backup...")
    os.makedirs("backup", exist_ok=True)
    print("Backup created in backup/ folder")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def tool_help():
    clear()
    print(f"\n{GREEN}[*] DIRE-HELP - Documentation{RESET}\n")
    print("For help, visit: github.com/atifdire-boop/DIRE-X")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def about():
    clear()
    print(f"""
{CYAN}╔════════════════════════════════════════╗
║         ABOUT DIRE-X                   ║
╚════════════════════════════════════════╝{RESET}

{GREEN}Version:{RESET} 2.0
{GREEN}Author:{RESET} Mr Dire
{GREEN}Tools:{RESET} 20 Security Tools
{GREEN}Platform:{RESET} Termux

{YELLOW}This tool is for educational purposes only{RESET}
""")
    input(f"\n{GREEN}[+] Press Enter to continue{RESET}")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(f"\n{CYAN}[{YELLOW}>{CYAN}] Select Option >> {RESET}")
        
        tools = {
            '1': tool_info, '01': tool_info,
            '2': tool_scan, '02': tool_scan,
            '3': tool_brute, '03': tool_brute,
            '4': tool_sql, '04': tool_sql,
            '5': tool_xss, '05': tool_xss,
            '6': tool_phish, '06': tool_phish,
            '7': tool_ddos, '07': tool_ddos,
            '8': tool_anon, '08': tool_anon,
            '9': tool_wifi, '09': tool_wifi,
            '10': tool_mal,
            '11': tool_crypto,
            '12': tool_osint,
            '13': tool_exploit,
            '14': tool_web,
            '15': tool_social,
            '16': tool_cam,
            '17': tool_report,
            '18': tool_update,
            '19': tool_backup,
            '20': tool_help,
            '99': about,
            '0': sys.exit
        }
        
        if choice in tools:
            tools[choice]()
        else:
            print(f"{RED}[!] Invalid option{RESET}")
            sleep(1)

if __name__ == "__main__":
    main()

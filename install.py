#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DIRE-X Installation Script
Developed by Mr Dire
"""

import os
import sys
import subprocess
import platform

# Colors for terminal
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
W = '\033[0m'
BOLD = '\033[1m'

def banner():
    os.system('clear' if platform.system() != 'Windows' else 'cls')
    print(f"""
{C}{BOLD}
    ╔╦╗╦╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
     ║║║╠═╝╠╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
    ═╩╝╩╩  ╩╚═  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
{Y}
         📦 DIRE-X INSTALLER 📦
{G}              By Mr Dire{W}
    """)
    print(f"{C}{'═'*50}{W}")

def check_python():
    """Check Python version"""
    print(f"\n{Y}[*] Checking Python version...{W}")
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"{G}[✓] Python {version.major}.{version.minor}.{version.micro} detected{W}")
        return True
    else:
        print(f"{R}[✗] Python 3.7+ required{W}")
        return False

def install_dependencies():
    """Install required packages"""
    print(f"\n{Y}[*] Installing dependencies...{W}")
    
    packages = [
        'requests',
        'colorama',
        'tqdm',
        'pyfiglet',
        'phonenumbers',
        'beautifulsoup4',
        'scapy',
        'python-nmap',
        'hashlib',
        'cryptography',
        'paramiko',
        'sockets',
        'threading',
        'json',
        're',
        'random',
        'string',
        'time',
        'datetime',
        'os',
        'sys',
        'subprocess',
        'platform'
    ]
    
    failed = []
    for package in packages:
        try:
            __import__(package) if package in ['json', 're', 'random', 'string', 'time', 'datetime', 'os', 'sys', 'subprocess', 'platform'] else None
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{G}[✓] {package}{W}")
        except Exception:
            print(f"{R}[✗] {package}{W}")
            failed.append(package)
    
    if failed:
        print(f"\n{Y}[!] Failed to install: {', '.join(failed)}{W}")
    return len(failed) == 0

def setup_directories():
    """Create necessary directories"""
    print(f"\n{Y}[*] Setting up directories...{W}")
    
    dirs = [
        'core',
        'tools',
        'config',
        'output',
        'logs',
        'wordlists',
        'payloads',
        'reports'
    ]
    
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{G}[✓] Created: {directory}/{W}")
        else:
            print(f"{C}[•] Exists: {directory}/{W}")

def make_executable():
    """Make main script executable"""
    print(f"\n{Y}[*] Setting permissions...{W}")
    try:
        os.chmod('dire-x.py', 0o755)
        print(f"{G}[✓] Made dire-x.py executable{W}")
    except Exception as e:
        print(f"{R}[✗] Error: {str(e)}{W}")

def create_config():
    """Create default configuration"""
    print(f"\n{Y}[*] Creating configuration...{W}")
    
    config = {
        "version": "2.0",
        "author": "Mr Dire",
        "first_run": True,
        "theme": "default",
        "auto_update": True,
        "save_logs": True,
        "default_output_dir": "output",
        "wordlist_dir": "wordlists",
        "timeout": 30,
        "threads": 100
    }
    
    import json
    with open('config/settings.json', 'w') as f:
        json.dump(config, f, indent=4)
    print(f"{G}[✓] Configuration saved{W}")

def main():
    banner()
    
    print(f"\n{C}[INFO] Starting DIRE-X installation...{W}")
    print(f"{C}[INFO] Platform: {platform.system()} {platform.release()}{W}")
    
    # Check Python
    if not check_python():
        print(f"\n{R}[!] Please install Python 3.7 or higher{W}")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print(f"\n{Y}[!] Some dependencies failed, but continuing...{W}")
    
    # Setup
    setup_directories()
    make_executable()
    create_config()
    
    # Completion
    print(f"\n{G}{'═'*50}{W}")
    print(f"{G}[✓] DIRE-X installed successfully!{W}")
    print(f"\n{Y}[+] Usage:{W}")
    print(f"    python3 dire-x.py")
    print(f"    or")
    print(f"    ./dire-x.py")
    print(f"\n{C}[⚠] Note: Use this tool for educational purposes only!{W}")
    print(f"{G}{'═'*50}{W}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Installation cancelled by user{W}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{R}[!] Error: {str(e)}{W}")
        sys.exit(1)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import platform
from colors import Colors

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}[✓] {message}{Colors.RESET}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}[✗] {message}{Colors.RESET}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.CYAN}[ℹ] {message}{Colors.RESET}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}[⚠] {message}{Colors.RESET}")

def check_root():
    """Check if running as root"""
    return os.geteuid() == 0 if hasattr(os, 'geteuid') else False

def install_package(package):
    """Install pip package"""
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except Exception:
        return False

def create_directory(path):
    """Create directory if not exists"""
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False

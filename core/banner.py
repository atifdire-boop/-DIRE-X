#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colors import Colors
import random

def show_banner():
    """Display big bold DIRE-X banner"""
    
    banners = [
        f"""
{Colors.CYAN}{Colors.BOLD}
    ██████╗ ██╗██████╗ ███████╗    ██╗  ██╗
    ██╔══██╗██║██╔══██╗██╔════╝    ╚██╗██╔╝
    ██║  ██║██║██████╔╝█████╗       ╚███╔╝ 
    ██║  ██║██║██╔══██╗██╔══╝       ██╔██╗ 
    ██████╔╝██║██║  ██║███████╗    ██╔╝ ██╗
    ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝
{Colors.YELLOW}
         ⚡ ADVANCED CYBERSECURITY TOOLKIT ⚡
{Colors.GREEN}              🔥 Developed by Mr Dire 🔥{Colors.RESET}
        """,
        
        f"""
{Colors.RED}{Colors.BOLD}
    ╔╦╗╦╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
     ║║║╠═╝╠╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
    ═╩╝╩╩  ╩╚═  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
{Colors.CYAN}
         🛡️  TERMUX SECURITY FRAMEWORK  🛡️
{Colors.GREEN}              💻 Coded by Mr Dire 💻{Colors.RESET}
        """
    ]
    
    # Random banner selection
    print(random.choice(banners))
    print(f"{Colors.CYAN}{'═'*60}{Colors.RESET}")

def show_menu(tools):
    """Display tool menu"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}[+] Available Tools:{Colors.RESET}\n")
    
    for tool_id, tool_info in tools.items():
        color = Colors.GREEN if tool_id % 2 == 0 else Colors.CYAN
        print(f"{color}[{tool_id:02d}]{Colors.RESET} {Colors.BOLD}{tool_info['name']:<15}{Colors.RESET} - {tool_info['desc']}")
    
    print(f"\n{Colors.MAGENTA}[99]{Colors.RESET} {Colors.BOLD}About DIRE-X{Colors.RESET}")
    print(f"{Colors.RED}[0] {Colors.BOLD}Exit{Colors.RESET}")

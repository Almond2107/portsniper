#!/usr/bin/env python3

import socket
import argparse
import json
import os
from colorama import Fore, Style


def show_banner():
    banner = r"""
    ____              _      _____       _             
   |  _ \ ___  _ __  (_) ___| ____|_ __ (_)_ __   __ _ 
   | |_) / _ \| '_ \ | |/ __|  _| | '_ \| | '_ \ / _` |
   |  __/ (_) | | | || | (__| |___| | | | | | | | (_| |
   |_|   \___/|_| |_|/ |\___|_____|_| |_|_|_| |_|\__, |
                    |__/                         |___/  
           PortSniper v1.0 - Fast and Flexible Port Scanner
    """
    print(banner)


def load_services():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    services_path = os.path.join(current_dir, "services.json")
    if not os.path.exists(services_path):
        print(f"{Fore.YELLOW}⚠️ services.json not found.{Style.RESET_ALL}")
        return {}
    with open(services_path) as f:
        return json.load(f)

def scan_port(target, port):
    try:
        with socket.socket() as s:
            s.settimeout(0.5)
            s.connect((target, port))
            return True
    except:
        return False

def grab_banner(ip: str, port: int) -> str:
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((ip, port))
            if port == 80:
                s.sendall(b"HEAD / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            elif port == 25:
                s.sendall(b"HELO test\r\n")
            elif port == 110:
                s.sendall(b"QUIT\r\n")
            else:
                s.sendall(b"\r\n")  # This is Generic
            banner = s.recv(1024).decode(errors="ignore")
            return banner.strip().replace('\r\n', ' | ')
    except Exception:
        return ""

def scan_and_print(target, port, open_only, show_service, version_detection, services):
    service_name = services.get(str(port), "") if show_service else ""
    service_str = f" ({service_name})" if service_name else ""

    if scan_port(target, port):
        banner = grab_banner(target, port) if version_detection else ""
        version_str = f" | {banner}" if banner else ""
        print(f"{Fore.BLUE}[+]{Style.RESET_ALL} Port {port}{service_str} is OPEN{version_str}")
    elif not open_only:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Port {port}{service_str} is CLOSED")

def main():
    parser = argparse.ArgumentParser(description="Simple and customizable port scanner.")
    parser.add_argument("-t", "--target", required=True, help="Target IP address or domain name to scan.")
    parser.add_argument("-p", "--ports", required=True, help="Port range to scan")
    parser.add_argument("-o", "--open-only", action="store_true", help="Show only open ports.")
    parser.add_argument("-s", "--service", action="store_true", help="Display service names for known ports.")
    parser.add_argument("-v", "--version", action="store_true", help="Grab banner to identify service versions.")


    args = parser.parse_args()

    # Load services infos
    services = load_services()

    # Discover ports
    if "-" in args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
    else:
        start_port = end_port = int(args.ports)

    print(f"\n{Fore.CYAN}Scanning {args.target} ports {start_port}-{end_port}...\n{Style.RESET_ALL}")

    for port in range(start_port, end_port + 1):
        scan_and_print(args.target, port, args.open_only, args.service, args.version, services)

if __name__ == "__main__":
    show_banner()
    main()


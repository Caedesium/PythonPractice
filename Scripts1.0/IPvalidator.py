#!/usr/bin/env python3

# Decided to write an ip validator for Python

import ipaddress

def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def validate_ipv4_address(ip_address):
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ValueError:
        return False

def validate_ipv6_address(ip_address):
    try:
        ipaddress.IPv6Address(ip_address)
        return True
    except ValueError:
        return False

def main():
    ip = input("Enter an IPv4 or IPv6 address: ")

    if len(ip) > 0:
        if validate_ip_address(ip):
            if validate_ipv4_address(ip):
                print(f"{ip} is a valid IPv4 address.")
            elif validate_ipv6_address(ip):
                print(f"{ip} is a valid IPv6 address.")
        else:
            print(f"{ip} is not a valid IP address.")
    else:
        print("No IP address provided.")

if __name__ == "__main__":
    main()
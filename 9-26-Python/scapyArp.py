#! /usr/bin/env python3

from collections import Counter
from scapy.all import ARP, sniff

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        return f"Request: {pkt[ARP].psrc} is asking about {pkt[ARP].pdst}"
    if pkt[ARP].op == 2: #is-at (response)
        return f"*Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}"

sniff(prn=arp_display, filter="arp", store=0, count=10)
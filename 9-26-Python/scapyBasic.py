#!/usr/bin/env python3
from scapy.all import *

def notGoogle(pkt):
    pkt = pkt.getlayer(IP)
    if hasattr(pkt, "dst") and pkt.dst != "8.8.8.8" and pkt.dst != "10.243.213.69":
        print( pkt.dst )

packet = sniff( prn=notGoogle, filter="icmp" )
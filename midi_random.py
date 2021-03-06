# Adapted from: https://github.com/mido/mido/blob/master/examples/ports/send.py
# !/usr/bin/env python
"""
Send random notes to the output port.
"""

from __future__ import print_function
import sys
import time
import random
import mido
from mido import Message

portname = None

# A pentatonic scale
notes = [36, 37, 38, 39, 40, 41]


def generateRandomNotes():
    try:
        with mido.open_output('Python App', autoreset=True, virtual=True) as port:
            print('Using {}'.format(port))
            while True:
                note = random.choice(notes)

                on = Message('note_on', note=note, channel=0)
                print('Sending {}'.format(on))
                port.send(on)
                time.sleep(0.05)

                off = Message('note_off', note=note, channel=0)
                print('Sending {}'.format(off))
                port.send(off)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def main():
    if len(sys.argv) > 1:
        portname = sys.argv[1]
    else:
        portname = None
    generateRandomNotes()


if __name__ == '__main__':
    main()

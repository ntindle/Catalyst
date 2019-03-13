# Adapted from: https://github.com/mido/mido/blob/master/examples/ports/send.py
# !/usr/bin/env python
# """
# Send random notes to the output port.
# """
#
# from __future__ import print_function
# import sys
# import time
# import random
# import mido
# from mido import Message
#
# portname = None
#
# # A pentatonic scale
# # notes = [20, 22, 24, 27, 29, 32]
# notes = [36, 37, 38, 39, 40, 41]
#
#
# def generateRandomNotes():
#     try:
#         with mido.open_output('Python App', autoreset=True, virtual=True) as port:
#             print('Using {}'.format(port))
#             while True:
#                 note = random.choice(notes)
#
#                 on = Message('note_on', note=note, channel=0)
#                 print('Sending {}'.format(on))
#                 port.send(on)
#                 time.sleep(0.05)
#
#                 off = Message('note_off', note=note, channel=0)
#                 print('Sending {}'.format(off))
#                 port.send(off)
#                 time.sleep(0.1)
#     except KeyboardInterrupt:
#         pass
#
#
# def main():
#     if len(sys.argv) > 1:
#         portname = sys.argv[1]
#     else:
#         portname = 'Python App'
#     generateRandomNotes()
#
#
# if __name__ == '__main__':
#     main()


# Adapted from: https://github.com/mido/mido/blob/master/examples/ports/send.py
# !/usr/bin/env python
"""
Translate Unity-generated strings with MIDI information into valid MIDI messages, then writing them to a port
"""

from __future__ import print_function
import sys
import time
import random
import mido
from mido import Message

dummyString = "17:45:43.836, whatever, note_on, 0, C1 127"

def noteToInt(note):
    note_value = 0
    length = len(note)
    if (note[length - 2] != "-"):
        octave = int(note[length - 1]) + 1
        note_value += 12 * octave
    if (note[0] == 'C'):
        if (note[1] == '#'):
            note_value += 1
    elif (note[0] == 'D'):
        if (note[1] == '#'):
            note_value += 3
        else:
            note_value += 2
    elif (note[0] == 'E'):
        note_value += 4
    elif (note[0] == 'F'):
        if (note[1] == '#'):
            note_value += 6
        else:
            note_value += 5
    elif (note[0] == 'G'):
        if (note[1] == '#'):
            note_value += 8
        else:
            note_value += 7
    elif (note[0] == 'A'):
        if (note[1] == '#'):
            note_value += 10
        else:
            note_value += 9
    else:  # note is B
        note_value += 11
    return note_value


def getMapping(unity_note):
    mk3_note = unity_note
    return mk3_note


def parseUnityString(in_str):
    components = in_str.split(", ")
    mk3_msg = components[2]
    chnl = int(components[3])
    note_str = components[4]
    note_velocity = note_str.split()
    unity_note = noteToInt(note_velocity[0])
    mk3_note = getMapping(unity_note)
    vel = int(note_velocity[1])
    msg = Message(mk3_msg, note=mk3_note, velocity=vel, channel=chnl)
    return msg


def maincd():
    if len(sys.argv) < 2:
        print("Missing input string")
        exit(1)
    else:
        unity_msg = dummyString
        mk3_msg = parseUnityString(unity_msg)
        with mido.open_output('Python App', autoreset=True, virtual=True) as port:
            print('Using {}'.format(port))
            port.send(mk3_msg)


if __name__ == '__main__':
    main()

# import socket
#
#
# def pushmidi(midiStr):
#     # do stuff
#
#
#
# print('Starting...')
# # TCP_IP = '10.11.17.76'
# TCP_IP = '172.20.10.10'
# TCP_PORT = 5005
# BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# while 1:
#     conn, addr = s.accept()
#     print('Connection address:' + addr[0])
#     data = conn.recv(BUFFER_SIZE)
#     if not data: break
#     print("received data: " + data.decode("utf-8"))
#     pushmidi(data.decode("utf-8"))
#
# conn.close()

# Adapted from: https://github.com/mido/mido/blob/master/examples/ports/send.py
# !/usr/bin/env python
"""
Translate Unity-generated strings with MIDI information into valid MIDI messages, then writing them to a port
"""

from __future__ import print_function
import sys
import time
import random
import socket
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


def pushMIDI(unity_str):
        unity_msg = unity_str
        mk3_msg = parseUnityString(unity_msg)
        with mido.open_output('Python App', autoreset=True, virtual=True) as port:
            print('Using {}'.format(port))
            port.send(mk3_msg)


def main():
    print('Starting...')
    TCP_IP = '10.11.17.76'
    TCP_IP = '172.20.10.10'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while 1:
        conn, addr = s.accept()
        print('Connection address:' + addr[0])
        data = conn.recv(BUFFER_SIZE)
        if not data:
            #not messages received from socket
            break
        data_str = data.decode("utf-8")
        print("received data: " + data_str)
        pushMIDI(data_str)

    conn.close()


if __name__ == '__main__':
    main()

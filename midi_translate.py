# Adapted from: https://github.com/mido/mido/blob/master/examples/ports/send.py
#!/usr/bin/env python
"""
Translate Unity-generated strings with MIDI information into valid MIDI messages, then writing them to a port
"""

from __future__ import print_function
import sys
import time
import random
import mido
from mido import Message

def noteToInt(note):
	note_value = 0
	length = len(note)
	if(note[length - 2] != "-"):
		octave = note[length - 1] + 1
		note_value += 12 * octave
	if(note[0] == 'C'):
		if(note[1] == '#'):
			note_value += 1
	elif(note[0] == 'D'):
		if(note[1] == '#'):
			note_value += 3
		else:
			note_value += 2
	elif(note[0] == 'E'):
		note_value += 4
	elif(note[0] == 'F'):
		if(note[1] == '#'):
			note_value += 6
		else:
			note_value += 5
	elif(note[0] == 'G'):
		if(note[1] == '#'):
			note_value += 8
		else:
			note_value += 7
	elif(note[0] == 'A'):
		if(note[1] == '#'):
			note_value += 10
		else:
			note_value += 9
	else: #note is B
		note_value += 11
	return note_value

def getMapping(unity_note):
	mk3_note = unity_note
	return mk3_note

def parseUnityString(in_str):
	components = in_str.split(", ")
	mk3_msg = components[2]
	chnl = components[3]
	note_str = components[4]
	note_velocity = note_str.split()
	unity_note = noteToInt(note_velocity[0])
	mk3_note = getMapping(unity_note)
	vel = int(note_velocity[1])
	msg = Message(mk3_msg, note=mk3_note, velocity=vel, channel=chnl)
	return msg

def main():
	if len(sys.argv) < 2:
    	print("Missing input string")
    	exit(1)
	else:
    	unity_msg = sys.argv[1]
    	mk3_msg = parseUnityString(unity_msg)
		with mido.open_output('Python App', autoreset=True, virtual=True) as port:
		    print('Using {}'.format(port)) 
	        port.send(mk3_msg)

if __name__ == '__main__':
	main()
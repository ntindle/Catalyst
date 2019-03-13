# Catalyst
Catalyst is a tool that makes music production easier through XR. Using the Magic Leap One, we are making music production with the Native Instruments Maschine controller more accessible to all.  

# From Motion to Music
When an inspired artist puts on the Magic Leap One headset to create music with Catalyst, they will see a portion of the Maschine interface overlaid on their surroundings.  A four by four array of virtual drum pads allow the user to trigger samples just as they would on the physical devices.  Four faders enable them to adjust the levels and parameters of several effects.

When the headset wearer gestures at one of the squares, the Maschine interface registers a MIDI command just as it would from a tap of the corresponding square in the physical drum pad.  This transduction of kinetic to musical energy is made possible through the combination of Unity, Python and Native Instruments technologies.

**Gestures to the Unity engine**

We set the scene using the Unity engine, through which we generate the Augmented Reality in which a drum pad and faders are integrated into the recording studio, a coffee shop, the beach, or anywhere else a dedicated musician can find internet.  The user's interactions with the environment are tracked by the engine and translated into a string of MIDI parameters.

**Unity to actual MIDI**

The Unity engine sends the MIDI parameters to a Python script, which continuously listens for new MIDI data on a socket connection.  The script parses each parameter string and uses the extracted values to populate a MIDI message.  This newly-formed MIDI message is organized in a format readable by the Native Instruments Maschine interface.

**MIDI to Maschine (and sound!)**

The Python script opens a virtual port, through which it can communicate with the Maschine.  Once a new MIDI message is parsed and created, the message is sent out on this port, where it triggers a MIDI action in the physical Maschine controller.  The device's interface registers the MIDI message from the Maschine and acts accordingly.

# Acknowledgements:
Thanks to Native Instruments for lending us a Maschine MK3 controller for developing testing, and impromptu jamming!
We are so grateful to the mentors at the SXSW Hackathon who helped us work out AR kinks and gave us invaluable feedback and advice.
We used a Magic Leap One headset, paired with the Unity engine, to develop the AR environment.
To manage MIDI data in Python, we used Mido.  You can find it here: https://github.com/mido/mido

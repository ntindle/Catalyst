# MIDIHandler adapted from pymidi:
# https://pypi.org/project/pymidi/#description

from pymidi import server

unity_to_mk3 = {} #we will populated this with the mapping of Unity Key IDs to MK3 keys

class MIDIHandler(server.handler)
    def on_peer_connected(self, peer):
        print('Peer connected: {}'.format(peer))

    def on_peer_disconnected(self, peer):
        print('Peer disconnected: {}'.format(peer))

    def on_midi_commands(self, command_list):
        for command in command_list:
            if command.command == 'note_on':
                key = command.params.key
                velocity = command.params.velocity
                print('Someone hit the key {} with velocity {}'.format(key, velocity)


def main():
	server = new server()
	server.add_handler(MIDIHandler)
	server.serve_forever()

if __name__ == '__main__':
	main()
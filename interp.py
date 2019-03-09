from midiutil import MIDIFile

testData = {}

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

def genMetronome(data):
    print(data['meta'])
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)

    """ for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume) """
    #bpm = data['track']['tempo']
    #length = data['track']['duration']
    #for i in range(0, length, bpm):
        #MyMIDI.addNote(track, channel, 60, time + i, duration, volume)
    """ c = 0
    while c < length:
        MyMIDI.addNote(track, channel, 60, c, duration, volume)
        c += (bpm / 60) """
    beats = data['beats']
    for b in beats:
        MyMIDI.addNote(track, channel, 60, b['start'], b['duration'], volume)

    with open("major-scale.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
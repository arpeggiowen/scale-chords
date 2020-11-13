# This program generates the chords from each degree of a selected scale.

chromatic = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']
sharps = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
flats = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

# parent scale steps
major = [2,2,1,2,2,2,1]                     # Major
mel_min = [2,1,2,2,2,2,1]                   # Melodic minor
harm_min = [2,1,2,2,1,3,1]                  # Harmonic minor
harm_maj = [2,2,1,2,1,3,1]                  # Harmonic Major
dbl_harm_maj = [1,3,1,2,1,3,1]              # Double Harmonic Major
                                            # (aka Byzantine)

# function to convert chord to integer notation
# chromatic_notes: 'sharps' or 'flats' list as preferred
def notes_to_int(chromatic_notes,chord_notes):
    int_chord = []
    
    for note in chord_notes:
        int_chord.append(chromatic_notes.index(note))

    int_chord.sort()
    
    return int_chord

# function which takes chord in integer notation and returns quality of the chord
# triad: logical input: true = triad; false = 7-chord
def id_chord(int_chord, triad):
    offset = int_chord[0]                   # chromatic offset based on root
    intervals = [n - offset for n in int_chord]

    # adjust negative intervals
    for i in intervals:
        if i < 0:
            intervals[intervals.index(i)] = i + 12

    if triad == True:
        if intervals[0:3] == [0,4,7]:
            return 'maj'
        elif intervals[0:3] == [0,3,7]:
            return 'min'
        elif intervals[0:3] == [0,4,8]:
            return 'aug'
        elif intervals[0:3] == [0,3,6]:
            return 'dim'
        elif intervals[0:3] == [0,2,7]:
            return 'sus2'
        elif intervals[0:3] == [0,5,7]:
            return 'sus4'
        elif intervals[0:3] == [0,2,6]:
            return 'sus2b5'
        elif intervals[0:3] == [0,4,6]:
            return 'majb5'
        else:
            return 0
    else:
        if intervals == [0,4,7,11]:
            return 'maj7'
        elif intervals == [0,4,7,10]:
            return '7'
        elif intervals == [0,3,7,11]:
            return 'min-maj7'
        elif intervals == [0,3,7,10]:
            return 'min7'
        elif intervals == [0,3,7,9]:
            return 'dim7#5'             # madd13 really
        elif intervals == [0,4,8,11]:
            return 'aug-maj7'
        elif intervals == [0,4,8,10]:
            return 'aug7'
        elif intervals == [0,3,6,10]:
            return 'min7b5'
        elif intervals == [0,3,6,9]:
            return 'dim7'
        elif intervals == [0,4,6,10]:
            return '7b5'
        elif intervals == [0,4,6,11]:
            return 'maj7b5'
        elif intervals == [0,2,6,9]:
            return 'dim7b3'             # Byzantine strikes again...
        else:
            return 0
    
def chord_gen(accidentals,key,scale,mode,tri):
    # set accidentals
    if accidentals.lower() == 'sharps':
        notes = sharps
    else:
        notes = flats

    # rotate chromatic notes to centre on new tonic
    degree = (notes.index(key))
    tonic = notes[degree:] + notes[:degree]

    # pick out scale notes
    mode = scale[mode:] + scale[:mode]      # rotate parent scale to mode
    mode.pop(-1)                            # remove last step

    s = 0
    mode_degrees = [0]
    for step in mode:
        s += step
        mode_degrees.append(s)

    scale_notes = []
    for d in mode_degrees:
        scale_notes.append(tonic[d])
             
    # derive chords
    scale_ext = mode_degrees + [x + 12 for x in mode_degrees] + [x + 24 for x in mode_degrees]

    chord_degs = []
    for d in range(0,7):
        chord_degs.append([scale_ext[d],scale_ext[d+2],scale_ext[d+4],scale_ext[d+6]])

    chords = []
    for c in chord_degs:
        chord = id_chord(c,tri)
        chords.append(chord)

    print(', '.join([x+''+y for x,y in zip(scale_notes,chords)]))

# pop out them chords
chord_gen('flats','C',major,0,True)
chord_gen('flats','C',mel_min,0,True)
chord_gen('flats','C',harm_min,0,True)
chord_gen('flats','C',harm_maj,0,True)
chord_gen('flats','C',dbl_harm_maj,0,True)

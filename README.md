# scale-chords
A simple tool to build chords from each interval of a specified musical scale.

Version 1.0: 2020/10/02

# How to use:

Method syntax: chord_gen(accidentals, key, parent scale, mode, triad)

'accidentals': specifies whether to use sharps or flats.
  - Expected input: (String) 'sharps', 'flats'.

'key': set key of scale
  - Expected input: (String) note name with or without accidental, e.g., 'C', 'Eb', 'F#'

'parent scale': specify parent scale to use
 - Expected inputs: (variable) major, mel_min (melodic minor), harm_min (harmonic minor), harm_maj (harmonic major), dbl_harm_maj (double harmonic major)
 
 'mode': specify which mode of parent scale to use
 - Expected input: (integer) in range 0 - 6
 
 'triad': specify whether or not to use triads
  - Expected input: (boolean) True results in triad chords; False produces 7th chords
  
  
Future versions:
- Integrate with scale tool.
- Expand to include more possible chords for each scale interval.
- Inverse functionality: derive compatible scales from given chord.

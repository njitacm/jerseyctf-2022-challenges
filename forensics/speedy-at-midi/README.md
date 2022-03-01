# speedy-at-midi

## Challenge Text
* Your partner-in-crime gets a hold of a MIDI file, `riff.mid`, which intelligence officials claim to contain confidential information.  He has tried opening it in VLC Media Player, but it sounds just like the piano riff in `riff.mp3`.  Can you find the right tool to extract the hidden data? 

## Hint
* You wouldn't have the audacity to try using a MIDI editor, would you?

## Solution
* Open up `riff.mid` in [Audacity](https://www.audacityteam.org/), a free and open-source audio editor.
* Zoom and scale the window in order to reveal the hidden MIDI track message.
    * The reason why the MIDI track cannot be heard in the `riff.mp3` is that the volume of the track with the hidden message is set to zero.
    * You can verify this by playing back using [VLC Media Player](https://www.videolan.org/).
* Flag: `jctf{kicking_it_since_1983}`

## Credit
* Developed by [Robert Argasinski](https://github.com/ra536)

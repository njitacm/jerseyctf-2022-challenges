# audio-transmission

**Challenged by FRSecure**

## Challenge Text
* We have intercepted an audio transmission from a known criminal organization. It is obviously encrypted in some way, but we've had no luck deciphering it. Can you help us out?
* https://drive.google.com/drive/folders/1U5n9f1EC7FcTiVzA3mQV7FIuPWEtNK_3?usp=sharing

## Hint
* No hints.

## Solution
* Taking a look at the spectrogram of the audio file shows several frequency bands clearly defined. The first and last frame are used as a guide to define the 8 frequencies that represent 8 bits of an ascii character. Each 200ms section represents an ascii character. Extracting the entire message from the audio file leaves you with a base64 encoded gif image.
* While this entire challenge could be done manually, it has been purposefully made into a long enough message to be very inefficient. To be completed in a short amount of time, a script should be created to analyze the audio file.
* Flag: `jctf{b1n4Ry_4sc1!_iN_sP3cTr0gr4M}`


**Example solution code:**
```
import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import base64

filename = "transmission.wav"
step = 200

def freq(data, sr, start_time, end_time):
    dataToRead = data[int(start_time * sr / 1000) : int(end_time * sr / 1000) + 1]

    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    freqs = [290, 250, 210, 170, 130, 90, 50, 10]
    f2b = []
    for f in freqs:
        f2b += [1] if np.abs(yf[f]) > 1800000 else [0]

    return f2b

sr, data = wavfile.read(filename)
alen = (len(data)/sr) * 1000
encmsg = ''

for i in range(0,int(alen),step):
    bindata = freq(data, sr, i, i+step)
    encmsg += chr(int(''.join([str(c) for c in bindata]),2))

decmsg = base64.b64decode(encmsg[2:-2])

with open("output.gif", "wb") as f:
    f.write(decmsg)
```


## Credit
* Developed by [Eric Hanson](https://github.com/vimk1ng)

# SoundVault

A library for cataloging and playing sound files (with the help of pydub).

## Usage

Define a sound configuration file like the below

```
{
    "format_version": "0.1",
    "last_updated": 1711996840968,
    "sounds_dir": "./sounds",
    "sounds": [
        {
            "id": "1",
            "name": "Sound 1",
            "file_name": "sound_01.mp3",
            "format": "mp3",
            "description": "My First Sound",
            "tags": ["generic", "sound_effect"],
            "source": "https://where-this-sound-come-from/page",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
        }
    ]
}
```

Create a SoundVault by passing in the file path to your config.

```
from sound_vault import SoundVault
from pydub.playback import play

sound_vault = SoundVault(sound_config_file_path='./sounds_config.json')

sounds = sound_vault.get_sounds()

print(sounds)

sound_1 = sounds[0]

print(sound_1.name)

# A pydub AudioSegment will be returned
audio = sound_vault.load_sound_audio(sound_1)

play(audio)

```

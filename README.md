# SoundVault

A library for cataloging and playing sound files (with the help of pydub).

## Usage

Define a sound configuration file like the below

```
{
    "format_version": "0.1",
    "last_updated": 1711996840968,
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

Create a SoundVault by passing in a valid SoundVaultConfig from the json, and the sounds directory path.

```
import os
import json
from sound_vault import SoundVault, SoundVaultConfig
from pydub.playback import play

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the sound vault config json file
sound_config_file_path = os.path.join(current_dir, 'your_sound_vault_config.json')

if not os.path.exists(sound_config_file_path):
    raise FileNotFoundError(
        f'Error: sound config file {sound_config_file_path} not found')

with open(sound_config_file_path, 'r') as f:
    config_data = json.load(f)

# Instantiate and Validate the SoundVaultConfig model
sound_vault_config = SoundVaultConfig.model_validate(config_data)

sounds_dir = os.path.join(current_dir, 'you_sounds_dir')

# Instantiate the SoundVault with the validated SoundVaultConfig and sounds directory
sound_vault = SoundVault(
    sound_vault_config=sound_vault_config, sounds_dir=sounds_dir)

# Get all sounds in the sound vault
sounds = sound_vault.get_sounds()

print(sounds)

# Get the first SoundVaultEntry model in the SoundVault model
sound_1 = sounds[0]

print(sound_1.name)

# Load the audio for sound_1
audio = sound_vault.load_sound_audio(sound_1)

play(audio)
```

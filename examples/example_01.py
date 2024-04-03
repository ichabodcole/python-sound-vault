import os
import json
from sound_vault import SoundVault, SoundVaultConfig
from pydub.playback import play

# Load the sound vault config json file
sound_config_file_path = './sounds_config.json'

if not os.path.exists(sound_config_file_path):
    raise FileNotFoundError(
        f'Error: sound config file {sound_config_file_path} not found')

with open(sound_config_file_path, 'r') as f:
    config_data = json.load(f)

# Instantiate and Validate the SoundVaultConfig model
sound_vault_config = SoundVaultConfig.model_validate(config_data)

# Instantiate the SoundVault with the validated SoundVaultConfig
sound_vault = SoundVault(sound_vault_config=sound_vault_config)

# Get all sounds in the sound vault
sounds = sound_vault.get_sounds()

print(sounds)

# Get the first SoundVaultEntry model in the SoundVault model
sound_1 = sounds[0]

print(sound_1.name)

# Load the audio for sound_1
audio = sound_vault.load_sound_audio(sound_1)

play(audio)

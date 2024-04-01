from sound_vault import SoundVault
from pydub.playback import play

sound_vault = SoundVault(sound_config_file_path='./sounds_config.json')

sounds = sound_vault.get_sounds()

print(sounds)

sound_1 = sounds[0]

print(sound_1.name)

audio = sound_vault.load_sound_audio(sound_1)

play(audio)

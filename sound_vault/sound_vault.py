import os
from .schemas.sound_vault_config import SoundVaultConfig, SoundVaultEntry
from .sound_loader import SoundLoader


class SoundVault:
    def __init__(self, sound_vault_config: SoundVaultConfig, output_sample_rate: int = 44100, output_channels: int | None = None):
        self.config = sound_vault_config
        self.sounds_dir = sound_vault_config.sounds_dir
        self.output_sample_rate = output_sample_rate
        self.output_channels = output_channels

    def get_sounds(self):
        return self.config.sounds

    def get_sounds_by_tags(self, tags: list):
        sounds = [sound for sound in self.config.sounds if any(
            tag in sound.tags for tag in tags)]
        return sounds

    def load_sound_audio(self, sound: SoundVaultEntry):
        return self.__load_sound_audio(sound.file_name, sound.format)

    def load_audio_by_sound_id(self, sound_id: str):
        sound = next(
            (sound for sound in self.config.sounds if sound.id == sound_id), None)
        if sound is None:
            raise ValueError(f'Sound {sound_id} not found in sound library')

        return self.__load_sound_audio(sound.file_name, sound.format)

    def __load_sound_audio(self, file_name: str, format: str):
        file_path = os.path.join(self.sounds_dir, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f'Error: sound file {file_path} not found in sound library')

        sound_loader = SoundLoader(
            file_path=file_path,
            format=format,
            output_sample_rate=self.output_sample_rate,
            output_channels=self.output_channels
        )

        return sound_loader.load()

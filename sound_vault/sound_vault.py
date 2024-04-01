import os
import json
from .schemas.sound_vault_config import SoundVaultConfig, SoundVaultEntry
from .sound_loader import SoundLoader


class SoundVault:
    def __init__(self, sound_config_file_path: str, output_sample_rate: int = 44100, output_channels: int | None = None):
        sound_config = self.__load_config_file(sound_config_file_path)
        self.config = sound_config
        self.sounds_dir = sound_config.sounds_dir
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

    def __load_config_file(self, sound_config_file_path: str):
        if not os.path.exists(sound_config_file_path):
            raise FileNotFoundError(
                f'Error: sound config file {sound_config_file_path} not found')

        with open(sound_config_file_path, 'r') as f:
            config_data = json.load(f)

        sound_config = SoundVaultConfig.model_validate(config_data)

        return sound_config

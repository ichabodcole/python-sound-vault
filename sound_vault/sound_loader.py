from pydub import AudioSegment


class SoundLoader:
    def __init__(self, file_path: str, format: str, output_sample_rate: int = 44100, output_channels: int | None = None):
        self.file_path = file_path
        self.format = format
        self.output_sample_rate = output_sample_rate
        self.output_channels = output_channels

    def load(self):
        try:
            sound_audio = AudioSegment.from_file(self.file_path, self.format)

            if isinstance(sound_audio, AudioSegment):
                sound_audio = sound_audio.set_frame_rate(
                    self.output_sample_rate)

                if self.output_channels is not None:
                    sound_audio = sound_audio.set_channels(
                        self.output_channels)

                return sound_audio

            else:
                raise FileNotFoundError(
                    f'Error: failed to load sound file {self.file_path}')

        except Exception as e:
            raise FileNotFoundError(
                f'Error: failed to load sound file {self.file_path} {e}')

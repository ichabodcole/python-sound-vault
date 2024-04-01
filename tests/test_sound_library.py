from sound_vault import SoundVault, SoundVaultConfig
from unittest.mock import patch, mock_open

mock_config_data = '''{
    "format_version": "1.0",
    "last_updated": 1234,
    "sounds_dir": "./sounds",
    "sounds": [
        {
            "id": "sound1",
            "name": "Sound 1",
            "description": "Sound 1 description",
            "file_name": "sound1.mp3",
            "format": "mp3",
            "tags": ["tag1", "tag2", "tag5"]
        },
        {
            "id": "sound2",
            "name": "Sound 2",
            "description": "Sound 2 description",
            "file_name": "sound2.mp3",
            "format": "mp3",
            "tags": ["tag1", "tag3", "tag4"]
        },
        {
            "id": "sound3",
            "name": "Sound 3",
            "description": "Sound 3 description",
            "file_name": "sound3.mp3",
            "format": "mp3",
            "tags": ["tag1", "tag5"]
        }
    ]
}'''


def test_load_config_file_success():

    mo = mock_open(read_data=mock_config_data)

    with patch('os.path.exists', return_value=True), patch('builtins.open', mo):
        library = SoundVault('./sound_config.json')
        assert library.sounds_dir == './sounds'
        assert isinstance(library.config, SoundVaultConfig)


def test_get_sounds():
    mo = mock_open(read_data=mock_config_data)

    with patch('os.path.exists', return_value=True), patch('builtins.open', mo):
        library = SoundVault('./sound_config.json')
        sounds = library.get_sounds()
        assert len(sounds) == 3
        assert sounds[0].id == 'sound1'
        assert sounds[1].id == 'sound2'
        assert sounds[2].id == 'sound3'


def test_get_sounds_by_tags():
    mo = mock_open(read_data=mock_config_data)

    with patch('os.path.exists', return_value=True), patch('builtins.open', mo):
        library = SoundVault('./sound_config.json')
        sounds = library.get_sounds_by_tags(['tag1'])
        assert len(sounds) == 3
        assert sounds[0].id == 'sound1'
        assert sounds[1].id == 'sound2'
        assert sounds[2].id == 'sound3'

        sounds = library.get_sounds_by_tags(['tag2'])
        assert len(sounds) == 1
        assert sounds[0].id == 'sound1'

        sounds = library.get_sounds_by_tags(['tag3'])
        assert len(sounds) == 1
        assert sounds[0].id == 'sound2'

        sounds = library.get_sounds_by_tags(['tag4'])
        assert len(sounds) == 1
        assert sounds[0].id == 'sound2'

        sounds = library.get_sounds_by_tags(['tag5'])
        assert len(sounds) == 2

        sounds = library.get_sounds_by_tags(['tag2', 'tag5'])
        assert len(sounds) == 2
        assert sounds[0].id == 'sound1'
        assert sounds[1].id == 'sound3'

        sounds = library.get_sounds_by_tags(['tag6'])
        assert len(sounds) == 0


def test_load_sound_audio():
    pass

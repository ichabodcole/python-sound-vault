import pytest
from unittest.mock import Mock, patch
from pydub import AudioSegment
from sound_vault import SoundLoader


def test_sound_loader():
    # Create a mock AudioSegment object
    mock_segment = Mock(spec=AudioSegment)
    mock_segment.set_frame_rate.return_value = mock_segment
    mock_segment.set_channels.return_value = mock_segment

    # Mock AudioSegment.from_file to return the mock AudioSegment
    with patch('pydub.AudioSegment.from_file', return_value=mock_segment):
        loader = SoundLoader("dummy/path", "wav")
        result = loader.load()

        # Assert that the result is the mock AudioSegment
        assert result == mock_segment
        # Assert that the AudioSegment.from_file was called with the correct arguments
        mock_segment.set_frame_rate.assert_called_with(44100)

        # Assert that the AudioSegment.set_channels was called with the correct arguments
        loader = SoundLoader("dummy/path", "wav", output_channels=2)
        loader.load()
        mock_segment.set_channels.assert_called_with(2)


def test_load_file_not_found():
    # Test the behavior when the file is not found
    with patch('pydub.AudioSegment.from_file', side_effect=FileNotFoundError):
        loader = SoundLoader("nonexistent/path", "wav")
        with pytest.raises(FileNotFoundError):
            loader.load()

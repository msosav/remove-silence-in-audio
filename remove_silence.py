from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
import os


def convert_m4a_to_wav(input_file, output_file):
    """
    Converts an audio file from M4A format to WAV format.
    Args:
        input_file (str): The path to the input M4A file.
        output_file (str): The path where the output WAV file will be saved.
    Returns:
        None
    Raises:
        Exception: If there is an error during the conversion process.
    """
    try:
        audio = AudioSegment.from_file(input_file, format="m4a")

        audio.export(output_file, format="wav")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")


def remove_silence(input_path, output_path):
    """
    Removes silence from an audio file and exports the processed audio to a new file.
    Args:
        input_path (str): The file path to the input audio file.
        output_path (str): The file path to save the processed audio file.
    Returns:
        None
    """
    audio = AudioSegment.from_file(input_path, format="wav")

    audio_chunks = split_on_silence(audio,
                                    min_silence_len=50,
                                    silence_thresh=-45,
                                    keep_silence=50)

    converted_audio = AudioSegment.empty()

    for chunk in audio_chunks:
        converted_audio += chunk

    converted_audio.export(output_path, format="wav")

    print(f"Silence removed: {output_path}")


def remove_aux_file():
    """
    Removes the auxiliary file 'output.wav' from the current directory.

    This function deletes the file named 'output.wav' if it exists in the
    current working directory. It is typically used to clean up temporary
    files generated during audio processing.

    Raises:
        FileNotFoundError: If the file 'output.wav' does not exist.
        PermissionError: If the file 'output.wav' cannot be deleted due to
                         insufficient permissions.
    """
    os.remove("output.wav")


if __name__ == "__main__":
    input_path = sys.argv[1]
    convert_m4a_to_wav(input_path, "output.wav")

    silence_removed_path = input_path.split(".")[0] + "_no_silence.wav"
    remove_silence("output.wav", silence_removed_path)

    remove_aux_file()

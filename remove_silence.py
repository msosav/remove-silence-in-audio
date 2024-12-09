from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
import os


def remove_silence(input_path, output_path):
    """
    Removes silence from an audio file and exports the processed audio to a new file.

    Args:
        input_path (str): The file path to the input audio file.
        output_path (str): The file path to save the processed audio file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: If there is an error during the silence removal process.
    """
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        try:
            audio = AudioSegment.from_file(input_path)
        except Exception as e:
            raise Exception(f"Invalid audio file: {input_path}. Error: {e}")

        audio_chunks = split_on_silence(audio,
                                        min_silence_len=50,
                                        silence_thresh=-45,
                                        keep_silence=50)

        if not audio_chunks:
            raise Exception(
                "No audio chunks found. The input file may be too silent.")

        converted_audio = AudioSegment.empty()

        for chunk in audio_chunks:
            converted_audio += chunk

        converted_audio.export(output_path, format="wav")

        print(f"Silence removed: {output_path}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"Error during silence removal: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_silence.py <input_audio_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    silence_removed_path = os.path.splitext(input_path)[0] + "_no_silence.wav"
    remove_silence(input_path, silence_removed_path)

from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
import os


def convert_m4a_to_wav(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file, format="m4a")

        audio.export(output_file, format="wav")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")


def remove_silence(input_path, output_path):
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
    os.remove("output.wav")


if __name__ == "__main__":
    input_path = sys.argv[1]
    convert_m4a_to_wav(input_path, "output.wav")

    silence_removed_path = input_path.split(".")[0] + "_no_silence.wav"
    remove_silence("output.wav", silence_removed_path)

    remove_aux_file()

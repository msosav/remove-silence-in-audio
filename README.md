# Remove Silence in Audio

This project uses `pydub` to remove silences from audio files.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/msosav/remove-silence-in-audio.git
   cd remove-silence-in-audio
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the script to remove silences with the path to the input audio file:

   ```sh
   python remove_silence.py "path/to/input/audiofile.m4a"
   ```

2. The processed audio files will be saved in the input audio file's directory with the suffix `_no_silence`.

## Example

```sh
python remove_silence.py "Downloads/audiofile.m4a"
```

## Dependencies

- `pydub`
- `ffmpeg` (Make sure `ffmpeg` is installed and added to your PATH)

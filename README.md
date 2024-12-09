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

### For a single audio file

1. Run the script to remove silences with the path to the input audio file:

   ```sh
   python remove_silence.py "path/to/input/audiofile.m4a"
   ```

2. The processed audio files will be saved in the input audio file's directory with the suffix `_processed`.

#### Example

```sh
python remove_silence.py "Downloads/audiofile.m4a"
```

### For multiple audio files

1. Run the script to remove silences with the path to the input audio files directory:

   ```sh
   python remove_silence_batch.py "path/to/input/audiofiles"
   ```

2. The processed audio files will be saved in the input audio files directory with the suffix `_processed`.

#### Example

```sh
python remove_silence_batch.py "Downloads/audiofiles"
```

## Dependencies

- `pydub`
- `ffmpeg` (Make sure `ffmpeg` is installed and added to your PATH)

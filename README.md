# Video to GIF Converter

This Python script allows you to convert a video from the "videos" folder into a GIF file. You can choose the video to convert and specify the start time for the GIF conversion.

## Prerequisites

- Python (3.6 or higher)
- `moviepy` library

You can install the `moviepy` library using pip:

```shell
pip install moviepy
```

## Usage

1. Place the video files you want to convert into the "videos" folder in the same directory as the script.

2. Run the `create-gif.py` script using Python:

   ```shell
   python create-gif.py
   ```

3. The script will display a list of available video files in the "videos" folder. Enter the number corresponding to the video you want to convert.

4. Optionally, specify the start time in seconds for the GIF conversion (0 by default).

5. The script will create a GIF based on your selection and specified start time.

## Example

```shell
python create-gif.py
```

In this example, the script will list the available video files in the "videos" folder and guide you through the selection and GIF conversion process.

## Supported Video Formats

The script supports the following video formats in the "videos" folder:

- `.mp4`
- `.avi`
- `.mkv`
- `.mov`

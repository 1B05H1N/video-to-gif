import os
from moviepy.editor import VideoFileClip

def create_gif(input_video_path, output_gif_path, start_time=0, end_time=None, fps=10):
    try:
        # Load the video clip from the "videos" folder
        video_clip = VideoFileClip(os.path.join("videos", input_video_path))

        # Set the end time to the video duration if not specified
        if end_time is None:
            end_time = video_clip.duration

        # Subclip the video based on start and end times
        subclip = video_clip.subclip(start_time, end_time)

        # Generate the GIF
        subclip.write_gif(output_gif_path, fps=fps)

        print(f"Created GIF: {output_gif_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # List video files in the "videos" folder
    video_files = [filename for filename in os.listdir("videos") if filename.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))]

    if not video_files:
        print("No supported video files found in the 'videos' folder.")
        exit()

    # Display available video files and prompt for selection
    print("Available video files:")
    for i, video_file in enumerate(video_files):
        print(f"{i + 1}. {video_file}")

    try:
        selected_index = int(input("Enter the number of the video to convert (1, 2, 3, etc.): ")) - 1

        if selected_index < 0 or selected_index >= len(video_files):
            print("Invalid selection.")
            exit()

        input_video_path = video_files[selected_index]
        output_gif_name = input_video_path.split('.')[0] + ".gif"
        output_gif_path = os.path.join("videos", output_gif_name)
        start_time = float(input("Enter the start time (in seconds) for the GIF conversion (0 by default): "))

        create_gif(input_video_path, output_gif_path, start_time)
    except ValueError:
        print("Invalid input.")

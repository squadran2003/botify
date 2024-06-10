from moviepy.editor import VideoFileClip
from PIL import Image


class ThumbnailCreator:
    processed_dir = None
    ext = 'jpg'
    limit = 10

    def __init__(self, path: str, filename: str, processed_dir: str):
        self.path = path
        self.filename = filename
        # split the filename and extension
        self.filename = self.filename.split('/')[1]
        self.filename, self.ext = self.filename.split('.')
        self.processed_dir = processed_dir
        self.thumbnails = []

    def create_thumbnails(self, interval=1):
        # Load the video file
        clip = VideoFileClip(self.path)

        # Get the duration of the video in seconds
        duration = int(clip.duration)

        # Loop through the video and save thumbnails
        for t in range(0, min(duration, self.limit), interval):
            # Get the frame at time t
            frame = clip.get_frame(t)

            # Convert the frame to an image
            frame_image = Image.fromarray(frame)

            frame_image = frame_image.resize((1280, 720))

            # Save the image as a thumbnail
            # done_file_path = f"{self.processed_dir}/{self.filename}_{t}.png"
            self.thumbnails.append(frame_image)
            # frame_image.save(done_file_path)

        # Close the video file
        clip.close()
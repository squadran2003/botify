import boto3
from moviepy.editor import VideoFileClip
from PIL import Image
from django.conf import settings


class ThumbnailCreator:
    tmp_filename = None
    # object in the s3 bucket
    bucket_name = None
    filename = None
    ext = None

    def __init__(self, ACCESS_KEY: str, SECRET_KEY: str, s3_url: str):
        self.s3_url = s3_url
        self.ACCESS_KEY = ACCESS_KEY
        self.SECRET_KEY = SECRET_KEY
        self.thumbnails = []

    def set_tmp_filename(self, tmp_filename: str):
        """Set the temporary filename to save the file to."""
        self.tmp_filename = tmp_filename

    def download_file(self):
        # Download file
        bucket_name = self.s3_url.split('/')[2]
        self.bucket_name = bucket_name.split('.')[0]
        key = self.s3_url.split('/')[5:][0]
        self.filename = key.split('.')[0]
        self.ext = key.split('.')[1]
        s3 = boto3.client(
            's3',
            aws_access_key_id=self.ACCESS_KEY,
            aws_secret_access_key=self.SECRET_KEY,
        )
        if not self.tmp_filename:
            raise Exception("tmp_filename not set")
        s3.download_file(
            self.bucket_name,
            key,
            "{}.{}".format(self.filename, self.ext)
        )

    def save_file(self, filename: str, bucket_name: str, key: str):
        # save file to s3
        boto3.upload_file(
            filename,
            bucket_name,
            key
        )

    def create_thumbnails(self, interval=1):
        # Load the video file
        clip = VideoFileClip(self.tmp_filename)

        # Get the duration of the video in seconds
        duration = int(clip.duration)

        # Loop through the video and save thumbnails
        for t in range(0, duration, interval):
            # Get the frame at time t
            frame = clip.get_frame(t)

            # Convert the frame to an image
            frame_image = Image.fromarray(frame)

            # Save the image as a thumbnail
            done_file_path = settings.MEDIA_ROOT + "/thumbnail_processing/done/{}.{}".format(
                self.filename, "jpg"
            )
            self.thumbnails.append(done_file_path)
            frame_image.save(done_file_path)
            print(f"Saved thumbnail: {done_file_path}")

        # Close the video file
        clip.close()
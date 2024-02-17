import cv2  # Import the OpenCV library

codecs = ['mp4v', 'XVID', 'H264', 'HEVC']

def compress_video(input_video_path, output_video_path, quality=90):
    # Open the input video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Get the video codec and frame dimensions from the input video
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec for the output video
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the frame width
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get the frame height
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))  # Get the frames per second (fps)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))  # Get the total number of frames

    # Create a VideoWriter object to write the compressed video
    video_writer = cv2.VideoWriter(output_video_path, codec, fps, (frame_width, frame_height))

    # Iterate through each frame of the input video and compress
    for _ in range(total_frames):
        ret, frame = video_capture.read()  # Read a frame from the input video
        if ret:
            # Perform JPEG compression on the frame with specified quality
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
            _, compressed_frame = cv2.imencode('.jpg', frame, encode_param)

            # Decode the compressed frame
            decompressed_frame = cv2.imdecode(compressed_frame, 1)

            # Write the decompressed frame to the output video
            video_writer.write(decompressed_frame)
        else:
            break  # Break the loop if no more frames are available

    # Release the video objects from memory
    video_capture.release()
    video_writer.release()

# The quality parameter in the provided code typically ranges from 0 to 100, where 0 corresponds to the lowest quality (highest compression) and 100 corresponds to the highest quality (lowest compression).

compress_video("Video.mp4", "output_video_compressed.mp4", quality=30)

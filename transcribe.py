import moviepy.editor as mp
import speech_recognition as sr

def extract_text_from_video(video_path, language='en-US'):
    # Load the video
    video = mp.VideoFileClip(video_path)

    # Extract audio from the video
    audio = video.audio

    # Write the audio to a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path)

    # Convert the audio to text using Google's Speech Recognition API
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_audio_path) as source:
        audio_text = recognizer.record(source)

    extracted_text = recognizer.recognize_google(audio_text, language=language)

    return extracted_text

if __name__ == "__main__":
    video_path = 'Mark-zuckerberg-video.mp4'  # Replace with your video file path
    extracted_text = extract_text_from_video(video_path)
    print(extracted_text)

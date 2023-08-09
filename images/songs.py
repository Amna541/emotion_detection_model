import cv2
import numpy as np
import pygame
import requests
import yt_dlp


# Function to check internet availability
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=3)
        return True
    except requests.ConnectionError:
        return False

# Initialize pygame for music playback
pygame.init()

# Load a basic emotion detection model (replace with your actual model)
def detect_emotion(image):
    # Replace with your emotion detection model code
    # Return the detected emotion (e.g., 'happy', 'sad', etc.)
    return "happy"

# Capture video from webcam
webcam = cv2.VideoCapture(0)

# Set camera resolution and FPS
webcam.set(3, 640)  # Set width
webcam.set(4, 480)  # Set height
webcam.set(5, 15)   # Set FPS

# Initialize the pygame mixer for music
pygame.mixer.init()

while True:
    ret, frame = webcam.read()

    # Emotion detection code
    detected_emotion = detect_emotion(frame)

    if check_internet():
        # Search for music videos on YouTube based on the detected emotion
        query = f"ytsearch:{detected_emotion} music"
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            video_urls = [entry['url'] for entry in info['entries'] if 'url' in entry]
        if video_urls:
            # Stop any currently playing music
            pygame.mixer.music.stop()
            
            # Play the audio from the first video using pygame
            pygame.mixer.music.load(video_urls[0])
            pygame.mixer.music.play()
    else:
        print("No internet connection available.")

    # Display the processed frame (you might need to modify this part)
    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Stop music and release resources before exiting
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        break

# Release the webcam and close all windows
webcam.release()
cv2.destroyAllWindows()

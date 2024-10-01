import streamlit as st
import cv2
import mediapipe as mp

st.title('AI Fitness Trainer: Squats Analysis')

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Read the video
input_video = "output_sample.mp4"  # Ensure this is the correct path
cap = cv2.VideoCapture(input_video)

# Prepare to store frames
frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame with MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    # Draw points on the frame
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Append the processed frame to the list
    frames.append(frame)

cap.release()

# Convert the frames to video
output_video = 'processed_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, 30.0, (frames[0].shape[1], frames[0].shape[0]))

for frame in frames:
    out.write(frame)

out.release()

# Display the processed video
st.video(output_video)


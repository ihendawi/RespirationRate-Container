from flask import Flask, request, jsonify, send_from_directory, render_template
import dlib
import cv2
import math
import numpy as np
from scipy import signal
from scipy.signal import find_peaks
import os

detector = dlib.get_frontal_face_detector()
app = Flask(__name__)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    points = (0,0,0,0)

    # calculate fps
    fps = cap.get(cv2.CAP_PROP_FPS)

    # calculate frame number
    mum_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        faces = detector(frame)
        for face in faces:
            x1 = face.left()
            x2 = face.right()
            y1 = face.top()
            y2 = face.bottom()
            length = y2-y1
            width = x2 - x1
            x3 = math.ceil(x1 - (0.75*width))
            x4 = math.ceil(x2 + (0.75*width))
            y3 = math.ceil(y2 + (0.3*length))
            y4 = math.ceil(y3 + length)
            w = x4 - x3
            h = y4 - y3
        points
        points = (x3, y3, w, h)

        break


    val_list = []

    x, y, w, h = points
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cropped_frame = frame[y:y + h, x:x + w]
        
        int_frame = cv2.integral(cropped_frame)
        val_list.append(int_frame[-1][-1])
        

    cap.release()

    cv2.destroyAllWindows()

    # Band-Pass-Filter
    data = val_list
    lowcut = 0.16
    highcut = 0.5
    fs = 30  # Sampling frequency
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    order = 5
    b, a = signal.butter(order, [low, high], btype='band')
    filtered = signal.filtfilt(b, a, data)

    # Find the peaks in the filtered data
    peaks, _ = find_peaks(filtered)
    peaks_count = len(peaks)
    # Time Length
    time_length = mum_frames / fps

    # RR
    rr =  math.ceil((len(peaks)/time_length)*60)
    
    respons = {'Frames per second' : fps,
               'Total number of frames': mum_frames,
               'Respiration Times': peaks_count,
               "Time Lenght": time_length,
               'RR': rr}

    return respons

@app.route('/process_video', methods=['POST'])
def process_uploaded_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    video_file = request.files['file']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if video_file:
        video_path = 'uploaded_video.mp4'
        video_file.save(video_path)
        respons = process_video(video_path)
        os.remove(video_path)  # Remove the uploaded video file after processing

        response_data = respons
        return jsonify(response_data)  # Return the JSON response containing the processed data

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

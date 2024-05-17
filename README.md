# Video Respiration Rate Detector

This project is a Flask-based web application that processes uploaded video files to detect and calculate respiration rates. The application uses OpenCV for video processing and dlib for face detection.

## Features

- Upload video files for processing
- Detect faces in the video
- Calculate respiration rates based on detected facial movements
- Display results including frames per second (FPS), total number of frames, respiration times, time length, and respiration rate (RR)

## Requirements

- Python 3.x
- Flask
- OpenCV
- dlib
- scipy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/video-respiration-rate-detector.git
    cd video-respiration-rate-detector
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download and install dlib:

    ```bash
    # On Ubuntu or Debian
    sudo apt-get install -y cmake build-essential libgl1-mesa-glx

    # Install dlib using pip
    pip install dlib
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://0.0.0.0:5000`.

3. Upload a video file and wait for the processing to complete.

4. The results will be displayed on the web page.

## Docker

You can also run this application using Docker. Follow the steps below:

1. Build the Docker image:

    ```bash
    docker build -t video-respiration-rate-detector .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 video-respiration-rate-detector
    ```

3. Open your web browser and go to `http://0.0.0.0:5000`.

## Deploying on Azure Container Instances

You can deploy this application on Azure Container Instances for a scalable and managed environment. Follow these steps:

1. Ensure you have the Azure CLI installed and are logged in:

    ```bash
    az login
    ```

2. Create a resource group if you don't have one:

    ```bash
    az group create --name myResourceGroup --location eastus
    ```

3. Create a container instance:

    ```bash
    az container create --resource-group myResourceGroup --name videoRespirationRate --image yourdockerhubusername/video-respiration-rate-detector:latest --ports 5000 --dns-name-label video-respiration-rate --environment-variables 'FLASK_ENV'='production'
    ```

4. Find the FQDN of your container instance:

    ```bash
    az container show --resource-group myResourceGroup --name videoRespirationRate --query ipAddress.fqdn
    ```

5. Open your web browser and navigate to the FQDN retrieved from the previous step.

## File Structure

- `app.py`: The main Flask application file
- `templates/index.html`: The HTML file for the web interface
- `requirements.txt`: The Python dependencies required for the project
- `Dockerfile`: The Dockerfile for containerizing the application

## Endpoints

- `GET /`: The main page with the video upload form
- `POST /process_video`: Endpoint to handle the video file upload and process the video


## Acknowledgements

- [dlib](http://dlib.net/)
- [OpenCV](https://opencv.org/)
- [Flask](https://flask.palletsprojects.com/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [ibrahimhen846@gmail.com](mailto:ibrahimhen846@gmail.com).

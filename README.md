# Face Recognition and Attendance Tracking

## Overview

This project implements a face recognition and attendance tracking system using Python, Firebase, Numpy, and OpenCV. The system automates the process of recognizing individuals and tracking attendance in real-time, providing an efficient and contactless solution for managing attendance records.

## Features

- **Real-Time Face Recognition**: Detect and recognize faces from live video feeds.
- **Automated Attendance Tracking**: Update attendance records in Firebase in real-time.
- **Efficient Processing**: Utilizes OpenCV and Numpy for fast and accurate face detection and recognition.
- **Seamless Integration**: Integrates with Firebase for real-time database management.

## Technologies Used

- **Python**: Core programming language for the application.
- **OpenCV**: For image processing and face detection.
- **Numpy**: For numerical operations and array handling.
- **Firebase**: Real-time database to manage and update attendance records.

## How It Works

1. **Face Detection**: The system captures video from the webcam and uses OpenCV to detect faces in real-time.
2. **Face Recognition**: Detected faces are compared against a database of known faces to identify individuals.
3. **Attendance Tracking**: Identified individuals are recorded, and their attendance is updated in the Firebase real-time database.

## Setup & Installation

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- OpenCV
- Numpy
- Firebase Admin SDK

Install the required libraries by running:

```bash
pip install opencv-python numpy firebase-admin

# Enhanced Human Detection Model using YOLOv8

## Overview

This project implements an enhanced human detection model using YOLOv8, a state-of-the-art object detection algorithm. The model is trained specifically for accurate and efficient detection of human beings in images and videos.

## Features

- Utilizes YOLOv8 architecture for robust object detection.
- Trained on large-scale human detection datasets for enhanced performance.
- Supports inference on both images and videos.
- Provides high detection accuracy even in complex scenes.
- Easily customizable and extensible for different use cases.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/tusharsachan15/enhanced_human_detection_model_using_Yolov8.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Training

This section details the training process for the enhanced human detection model.

**Prerequisites:**

- Downloaded pre-trained YOLOv8 weights.

**Steps:**

1. **Dataset Preparation:**
   - Download your dataset and organize it according to the YOLOv8 training data format (e.g., Heridal dataset from Robofglow).

2. **Training Script:**
   - The project includes a training script (`training.py`).
   - Modify the script to specify the paths to your downloaded pre-trained weights and your prepared dataset.
   - Additional modifications might be needed based on your desired training configuration (e.g., number of epochs, learning rate).

3. **Run Training:**
   - Execute the training script using a command like:

   ```bash
   python train.py --data path/to/your/dataset.yaml --weights path/to/yolov8.pt

 ## Result 
![Example of human detection result](https://github.com/tusharsachan15/enhanced_human_detection_model_using_Yolov8/blob/8c13dd300a77cff07e742d332007433e3f3b17fd/val4/val_batch1_pred.jpg)


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

# YOLOv8-based Indoor Door Detection

Custom YOLOv8 model for real-time door detection in indoor environments.

## Overview

This project contains a complete pipeline for training and deploying a custom YOLOv8 model to detect doors in indoor scenes. The model was trained on a professionally augmented dataset and was implemented on a CPU-only system.

## Results

### Performance Metrics

| Metric            | Value    |
|-------------------|----------|
| mAP@0.5           | 0.9617   |
| mAP@0.5:0.95      | 0.8566   |
| Precision         | 0.9670   |
| Recall            | 0.9153   |
| F1 Score          | 0.9405   |

### Performance

![Performance](https://github.com/AashishSaini16/YOLOv8-Indoor-Door-Detection/blob/main/performance_graphs.png)

### Live Detection Examples

![Live Detection 1](https://github.com/AashishSaini16/YOLOv8-Indoor-Door-Detection/blob/main/live_inference.png)

## Dataset

- **Source**: Roboflow Universe
- **Original Images**: 7,583
- **Augmented Images**: 21,263
- **Classes**: 1 (door)

## Dataset License

The dataset used in this project is licensed under **CC BY 4.0**.  
Source: [Roboflow Universe](https://universe.roboflow.com/door-2wjcn/door-ocdh8)

## Methodology

- Data preparation and augmentation using Roboflow
- Model trained using YOLOv8s on NVIDIA A100
- Training conducted for 50 epochs with early stopping
- Best model selected at epoch 43

## Installation

```bash
git clone https://github.com/AashishSaini16/YOLOv8-Indoor-Door-Detection.git
cd YOLOv8-Indoor-Door-Detection

python -m venv venv
venv\Scripts\activate

pip install ultralytics opencv-python

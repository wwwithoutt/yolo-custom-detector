<div align="center">

# 🎯 yolo-custom-detector

**Custom object detection with YOLO11: dataset collection, labeling, training, evaluation and inference.**

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white)
![YOLO11](https://img.shields.io/badge/model-YOLO11-purple)
![Ultralytics](https://img.shields.io/badge/framework-Ultralytics-00FFFF)
![Status](https://img.shields.io/badge/status-work%20in%20progress-orange)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey?logo=apple)

<!-- Replace with a real screenshot or GIF of your model's predictions -->
<!-- ![demo](assets/demo.gif) -->

</div>

---

## 📖 About

This project is an end-to-end pipeline for training a **custom object detector** based on
[Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11/).
It covers every step: downloading images, labeling them, training the model on your own
dataset, evaluating quality and running inference on images and video.

> 🚧 **Work in progress.** Training is still being tuned, and results will appear here as soon as they are ready.

**What the model detects:** _fill in your classes here, e.g. `class_1`, `class_2`, `class_3`_

## ⚡ TL;DR

```bash
git clone https://github.com/wwwithoutt/yolo-custom-detector.git
cd yolo-custom-detector
pip install ultralytics
yolo detect train data=conf.yaml model=yolo11n.pt epochs=100 imgsz=640
```

## 🧭 Pipeline

```
 Collect images  ──►  Label (labelImg)  ──►  Train (YOLO11)  ──►  Evaluate  ──►  Inference
 goruntu_indir.py      YOLO format           yolo detect train    mAP, P, R      image / video
```

## 🗂 Project structure

```
yolo-custom-detector/
├── conf.yaml               # Dataset config: paths and class names
├── goruntu_indirme/
│   └── goruntu_indir.py    # Script for downloading images
├── .gitignore              # Excludes weights, datasets and training runs
└── README.md
```

> Datasets, weights (`*.pt`) and the `runs/` folder are **not stored in the repo**
> because they are too large. See [Dataset and weights](#-dataset-and-weights).

## 🛠 Installation

Requirements: Python 3.10+ and (optionally) a GPU. On Apple Silicon Macs training uses `mps`.

```bash
# 1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install ultralytics
```

## 🏷 Data preparation

1. Collect images with `goruntu_indirme/goruntu_indir.py`.
2. Label them with [labelImg](https://github.com/HumanSignal/labelImg) in **YOLO** format
   (one `.txt` file per image with lines `class x_center y_center width height`).
3. Split the data into `train` and `val`, and point `conf.yaml` at it:

```yaml
path: datasets/my_dataset
train: images/train
val: images/val

names:
  0: class_1
  1: class_2
```

## 🚀 Training

```bash
yolo detect train data=conf.yaml model=yolo11n.pt epochs=100 imgsz=640 batch=16 device=mps
```

Or from Python:

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.train(data="conf.yaml", epochs=100, imgsz=640)
```

Training results (weights, curves, confusion matrix) are saved to `runs/detect/train/`.

## 🔍 Inference

```bash
# Image or video
yolo detect predict model=runs/detect/train/weights/best.pt source=path/to/file conf=0.25

# Webcam
yolo detect predict model=runs/detect/train/weights/best.pt source=0
```

## 📊 Results

_To be added after training finishes._

| Metric | Value |
|---|---|
| mAP@50 | – |
| mAP@50-95 | – |
| Precision | – |
| Recall | – |

## 🗺 Roadmap

- [x] Project setup and environment
- [x] Image collection script
- [ ] Dataset labeling
- [ ] Model training
- [ ] Quality evaluation (mAP, precision, recall)
- [ ] Prediction demo (GIF in this README)
- [ ] Export to ONNX / CoreML

## 📦 Dataset and weights

Files are too large for git, so they are hosted separately:

- Dataset: _link (Google Drive / Kaggle / Roboflow)_
- Trained weights: _link (GitHub Releases / Hugging Face)_

## 🙏 Acknowledgements

- [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics), the detection model and training framework
- [labelImg](https://github.com/HumanSignal/labelImg), the image annotation tool

## 👤 Author

**wwwithoutt**: [GitHub](https://github.com/wwwithoutt)

If the project was useful, give it a ⭐

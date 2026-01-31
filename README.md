# FrameExtractor-Py 🖼️

**Animated Frame Extraction Made Simple.**

A lightweight, efficient Python tool designed to batch extract individual frames from `GIF` and `APNG` animations. It automatically organizes frames into dedicated folders and ensures high-quality output with transparency support.

---

## 🚀 Key Features

* **Smart Detection**: Automatically identifies animated files and skips static images.
* **Full Transparency**: Converts every frame to `RGBA` mode to perfectly preserve transparent backgrounds.
* **Automatic Archiving**: Creates individual folders named after the source file to keep your workspace organized.
* **Broad Compatibility**: Seamlessly handles both standard `.gif` and modern `.apng` (even with `.png` extensions).

---

## 🛠️ Requirements

This script requires the **Pillow** library to handle image processing.

```bash
pip install Pillow
```


## 📖 How to Use

### 1. Interactive Mode2. Command Line Mode
Simply run the script and follow the on-screen prompts to enter your paths:
```bash
python gif_apng_extractor.py
```
### 2. Command Line Mode
Pass the input and output directories as arguments for faster processing:
```bash
python gif_apng_extractor.py [input_directory] [output_directory]
```

## 📂 Output Structure Example
After processing, your frames will be organized as follows:
```output/
├── explosion_effect/
│   ├── 1.png
│   ├── 2.png
│   └── ...
└── loading_spinner/
    ├── 1.png
    └── ...
```
## ⚖️ License
This project is licensed under the MIT License. Feel free to use, modify, and distribute!

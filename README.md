# Emotion-Based AI Music Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-aaff00)
![HuggingFace](https://img.shields.io/badge/Model-DistilBERT-orange)

Generate emotionally resonant music from textual input using state-of-the-art natural language processing and symbolic music generation models.

---

## Project Overview
This project transforms **user-provided text** into **emotionally-aligned music** using two powerful models:

1. **DistilBERT** for emotion classification
2. **EmotionBox** for symbolic music generation

The pipeline outputs both a **MIDI** and a **WAV audio** file, offering an engaging auditory experience based on the emotional context of input text.

---

## Features
- Real-time **text emotion detection** using DistilBERT
- **MIDI music generation** based on emotional output
- **WAV audio synthesis** using FluidSynth
- Streamlit-based **web interface**
- Modular & extensible codebase for experimentation
- Includes Jupyter notebook to train your own DistilBERT emotion classifier

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/anshulraj10/ai-music-generator.git
cd emotion-music-generator
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. For macOS users:
Install FluidSynth for WAV synthesis:
```bash
brew install fluid-synth
```

---

## Usage

### Run the web interface:
```bash
streamlit run app.py
```
Access it at: [http://localhost:8501](http://localhost:8501)

### Run the CLI pipeline (example):
```bash
python test.py
```
This executes:
- Emotion detection via `emotion_detector.py`
- Music generation in `music_generator.py`
- WAV rendering using `midi_to_wav.py`

Outputs saved in:
```bash
output/music_<emotion>_<timestamp>.mid
output/music_<emotion>_<timestamp>.wav
```

To play the WAV file:
```bash
open output/music_<emotion>_<timestamp>.wav  # macOS
start output/music_<emotion>_<timestamp>.wav # Windows
```

---

## Model Architecture

### DistilBERT (Emotion Detection)
- Pretrained using Hugging Face Transformers
- Lightweight and efficient
- Fine-tuned for emotion labels: joy, anger, sadness, etc.
- Option to retrain using `train_emotion_detector.ipynb`

### EmotionBox (Music Generation)
- Symbolic generation model from Georgia Tech
- Accepts emotion class and sequence length
- Outputs structured note sequences as MIDI using `music_generator.py`

### MIDI to WAV
- Converts `.mid` to `.wav` via FluidSynth using `midi_to_wav.py`
- Uses built-in or user-provided soundfont (`.sf2` file) for rendering

---

## Project Structure
```
.
├── app.py                              # Streamlit UI
├── config.py                           # Configuration for models and settings
├── emotion_detector.py                 # Text → Emotion (DistilBERT)
├── music_generator.py                  # Emotion → MIDI (EmotionBox)
├── midi_to_wav.py                      # MIDI → WAV (FluidSynth)
├── model.py                            # EmotionBox architecture
├── sequence.py                         # MIDI pattern handling for EmotionBox
├── utils.py                            # Helper functions
├── test.py                             # CLI pipeline runner
├── train_emotion_detector.ipynb        # Jupyter notebook for training emotion classifier
├── output/                             # Final outputs: .mid + .wav
├── models/                             # Model weights and configs
│   ├── distilbert_emotion/             # Emotion classifier model files
│   │   ├── config.json                 # DistilBERT configuration
│   │   ├── model.safetensors           # Trained model weights
│   │   ├── special_tokens_map.json     # Special tokens mapping
│   │   ├── tokenizer_config.json       # Tokenizer settings
│   │   └── vocab.txt                   # Vocabulary file
│   └── music_model.sess                # Serialized EmotionBox model
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
└── README.md                           # Project overview
```

---

## External Links
- [DistilBERT - Hugging Face](https://huggingface.co/distilbert-base-uncased)
- [EmotionBox - GitHub](https://github.com/KaitongZheng/EmotionBoxDEMO)
- [EmotionBox - Research Paper](https://arxiv.org/abs/2112.08561)

---

## Credits
- **NLP**: Hugging Face (DistilBERT)
- **Music Gen**: EmotionBox by GT-SALT Lab
- **Audio Tools**: PrettyMIDI, PyDub, FluidSynth
- **UI**: Streamlit for interactive web interface
- **Author**: [Anshul Raj](https://anshulraj.com)

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

> *"When words fail, music speaks – now powered by AI."*

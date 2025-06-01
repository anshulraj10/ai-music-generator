import streamlit as st
from emotion_detector import detect_emotion
from music_generator import generate_music
from midi_to_wav import convert_midi_to_wav

import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

st.title("AI Emotion-Based Music Generator")
st.write("Describe your mood and generate a music piece!")

# User Input
user_text = st.text_area("How do you feel today?")

if st.button("Generate Music"):
    if user_text:
        # Detect emotion using the NLP model
        mood = detect_emotion(user_text)

        st.success(f"Detected Mood: {mood.capitalize()}")

        # Generate MIDI music
        midi_file = generate_music(mood)

        # Convert MIDI to WAV
        wav_file = convert_midi_to_wav(midi_file)

        # Play the generated music
        st.audio(wav_file, format='audio/wav')
        st.success("Music generated and playing now!")
    else:
        st.warning("Please describe your mood.")
from emotion_detector import detect_emotion
from midi_to_wav import convert_midi_to_wav
from music_generator import generate_music


user_texts = [
    "I feel lost and alone today. Nothing seems to be going right",
    "Everything feels meaningless, and I just want to be left alone.",
    "Today is amazing! I can't stop smiling and feeling grateful.",
    "I just got some great news, and I'm so happy right now!",
    "I feel so deeply connected to someone special in my life",
    "My heart is full of love and warmth today",
    "I cant believe they treated me like that! I'm so frustrated!",
    "Everything is making me so mad right now!",
    "I'm feeling really anxious about whats going to happen next.",
    "Something just doesn't feel right, and I'm really scared.",
    "Wow, I did not see that coming! I'm completely shocked!",
    "I just got the best unexpected news of my life!",
    ]

for text in user_texts:
    mood = detect_emotion(text)
    print(f"Detected Mood: {mood.capitalize()}")

    midi_file = generate_music(mood)
    wav_file = convert_midi_to_wav(midi_file)
    
    print(f"Successfully generated {wav_file}")
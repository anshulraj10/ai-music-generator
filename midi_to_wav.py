import pretty_midi
import soundfile as sf

def convert_midi_to_wav(midi_file):
    """Convert generated MIDI to WAV for playback."""
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    
    # Synthesize to WAV
    audio_data = midi_data.fluidsynth()
    wav_file = midi_file.replace(".mid", ".wav")

    sf.write(wav_file, audio_data, 44100)

    return wav_file
import torch
import numpy as np
import os
from config import device
from model import PerformanceRNN
from sequence import Control
import utils

# Updated Mood-to-Music Controls
MOOD_CONTROLS = {
    "sadness": '2,0,1,1,0,2,0,2,1,0,1,0;3',   # Lower notes, minor scale
    "joy": '3,0,1,0,1,2,0,2,0,1,0,1;6',       # High-energy, major scale
    "love": '2,0,1,0,1,2,0,3,0,1,0,1;5',      # Soft, flowing harmonies
    "anger": '4,1,2,0,1,3,0,3,1,0,1,0;7',     # Intense, high pitch jumps
    "fear": '1,0,2,1,0,3,0,2,1,0,1,0;2',      # Slow, uncertain pitch transitions
    "surprise": '3,1,0,1,0,2,0,4,1,0,1,0;8'   # Fast, unexpected chord shifts
}

def generate_music(mood):
    """Generate MIDI music based on detected mood."""
    sess_path = "models/music_model.sess"
    assert os.path.isfile(sess_path), f"Model session '{sess_path}' not found."

    control = MOOD_CONTROLS[mood]
    pitch_histogram, note_density = control.split(';')
    pitch_histogram = np.array(list(map(float, pitch_histogram.split(','))))
    note_density = int(note_density)

    # Load PerformanceRNN model
    state = torch.load(sess_path, map_location=device)
    model = PerformanceRNN(**state['model_config']).to(device)
    model.load_state_dict(state['model_state'])
    model.eval()

    init = torch.randn(1, model.init_dim).to(device)

    with torch.no_grad():
        outputs = model.generate(init, 500, controls=None, greedy=0.8, temperature=1.0)
        
    # Convert tensor to numpy
    outputs = outputs.cpu().numpy().T

    # Ensure outputs are within the expected MIDI event range
    event_min, event_max = 0, 240  # Expected event range
    outputs = np.clip(outputs, event_min, event_max)  # Keep values within range

    # Convert to integers
    outputs = outputs.astype(int)

    # Debugging: Print fixed outputs
    # print(f"Fixed Output Data: {outputs[:10]}")

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    midi_file = f"output/{mood}.mid"
    # print(f"Generated Outputs Shape: {outputs.shape}")
    # print(f"Sample Output Data: {outputs[:10].tolist()}")
    # print(f"Min Value: {outputs.min()}, Max Value: {outputs.max()}")
    utils.event_indeces_to_midi_file(outputs.T, midi_file)

    return midi_file
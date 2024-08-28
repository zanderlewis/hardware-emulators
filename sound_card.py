import numpy as np
import pyaudio

class SoundCard:
    def __init__(self, sample_rate=44100, bit_depth=16, channels=2, buffer_size=1024, debug=False):
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.channels = channels
        self.buffer_size = buffer_size
        self.buffer = np.zeros((buffer_size, channels), dtype=np.int16)
        self.debug_mode = debug

    def load_sound(self, sound_data):
        """Load sound data into the buffer."""
        # Ensure sound_data fits into the buffer
        sound_data = np.array(sound_data, dtype=np.int16)
        if sound_data.shape[0] > self.buffer_size:
            raise ValueError("Sound data exceeds buffer size")
        self.buffer[:sound_data.shape[0], :sound_data.shape[1]] = sound_data

    def play(self):
        """Play the sound data in the buffer."""
        if self.debug_mode:
            print("Playing sound...")
        # Play sound using audio library (e.g., PyAudio)
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=self.channels,
                        rate=self.sample_rate,
                        output=True)
        stream.write(self.buffer.tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()

    def stop(self):
        """Stop sound playback."""
        if self.debug_mode:
            print("Stopping sound...")
        self.buffer.fill(0)
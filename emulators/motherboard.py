from .cpu import CPU
from .gpu import GPU
from .sound_card import SoundCard
from .hdd import HDD
from .ssd import SSD
from .network_card import NetworkCard
from .clock import Clock

class Motherboard:
    def __init__(self, cpu_bits: int = 16, ram_size: int = 512, gpu_memory: int = 1024, frame_buffer: int = 64, sound_buffer: int = 1024, debug: bool = False, hdd: bool = True, ssd: bool = True, network: bool = True):
        self.cpu = CPU(bits=cpu_bits, memory=ram_size, debug=debug)
        self.gpu = GPU(memory=gpu_memory, frame_buffer=frame_buffer, debug=debug)
        self.sound_card = SoundCard(buffer_size=sound_buffer, debug=debug)
        self.ram = self.cpu.memory  # RAM is part of the CPU
        self.hdd = HDD(debug=debug) if hdd else None
        self.ssd = SSD(debug=debug) if ssd else None
        self.network_card = NetworkCard(debug=debug) if network else None
        self.clock = Clock()
        self.gpu_memory = gpu_memory
        self.cpu_memory = ram_size

    def load_program(self, program, type="cpu"):
        """Load a program into the CPU's or GPU's memory."""
        if type == "cpu":
            self.cpu.load_program(program)
        elif type == "gpu":
            self.gpu.load_program(program)

    def run(self, type="cpu"):
        """Run the loaded program on the CPU or GPU."""
        if type == "cpu":
            self.cpu.run()
        elif type == "gpu":
            self.gpu.run()

    def render(self, *args, **kwargs):
        """Render the GPU's framebuffer."""
        self.gpu.render(*args, **kwargs)

    def play_sound(self, sound_data):
        """Play sound using the sound card."""
        self.sound_card.load_sound(sound_data)
        self.sound_card.play()
    
    def read_from_hdd(self, offset, length):
        return self.hdd.read(offset, length)

    def write_to_hdd(self, offset, data):
        self.hdd.write(offset, data)

    def format_hdd(self):
        self.hdd.format()
    
    def read_from_ssd(self, offset, length):
        return self.ssd.read(offset, length)
    
    def write_to_ssd(self, offset, data):
        self.ssd.write(offset, data)

    def format_ssd(self):
        self.ssd.format()
    
    def send_network_data(self, data, target_host, target_port):
        self.network_card.send(data, target_host, target_port)

    def receive_network_data(self):
        return self.network_card.receive()

    def close_network_card(self):
        self.network_card.close()
    
    def get_time(self):
        return self.clock.get_time()
    
    def get_timezone(self):
        self.clock.get_timezone()
    
    def set_timezone(self, timezone):
        self.clock.set_timezone(timezone)
    
    def specs(self):
        print("Virtual Hardware Specifications\n=============================\n")
        print(f"CPU:\n====\n{self.cpu.bits}-bit\nRAM: {self.cpu_memory} bytes\n")
        print(f"GPU:\n====\n{self.gpu.bits}-bit\nMemory: {self.gpu_memory} bytes\nFrame Buffer: {self.gpu.frame_buffer} bytes\nCores: {self.gpu.num_cores}\n")
        print(f"Sound Card:\n===========\nBuffer Size: {self.sound_card.buffer_size} bytes\nChannels: {self.sound_card.channels}\nBit Depth: {self.sound_card.bit_depth}\nSample Rate: {self.sound_card.sample_rate}\n")
        if self.hdd:
            print(f"HDD:\n====\nSize: {self.hdd.size} bytes\n")
        if self.ssd:
            print(f"SSD:\n====\nSize: {self.ssd.size} bytes\n")
        if self.network_card:
            print(f"Network Card:\n=============\nHost: {self.network_card.host}\nPort: {self.network_card.port}\n")
        print(f"System Specifications:\n======================\n")
        print(f"Timezone: {self.clock.timezone}\n")

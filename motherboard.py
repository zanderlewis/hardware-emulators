from cpu import CPU
from gpu import GPU

class Motherboard:
    def __init__(self, cpu_bits: int = 16, ram_size: int = 512, debug: bool = False):
        self.cpu = CPU(bits=cpu_bits, memory=ram_size, debug=debug)
        self.ram = self.cpu.memory  # RAM is part of the CPU
        self.gpu = GPU(memory=ram_size, debug=debug)  # GPU with shared memory

    def load_program(self, program, type="cpu"):
        """Load a program into the CPU's memory."""
        if type == "cpu":
            self.cpu.load_program(program)
        elif type == "gpu":
            self.gpu.load_program(program)
        else:
            raise ValueError("Invalid program type. Use 'cpu' or 'gpu'.")

    def run(self, type="cpu"):
        """Run the loaded program."""
        if type == "cpu":
            self.cpu.run()
        elif type == "gpu":
            self.gpu.run()
        else:
            raise ValueError("Invalid program type. Use 'cpu' or 'gpu'.")
    
    def debug(self):
        """Print the state of the CPU and GPU for debugging purposes."""
        self.cpu.debug()
        self.gpu.debug()
    
    def render(self):
        """Render the GPU's display."""
        self.gpu.render()
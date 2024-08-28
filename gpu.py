import numpy as np
from concurrent.futures import ThreadPoolExecutor

class GPU:
    def __init__(self, num_cores=8, memory=1024, bits=16, frame_buffer=64, debug=False):
        self.num_cores = num_cores
        self.memory = np.zeros(memory)  # Simulated memory
        self.framebuffer = np.zeros((frame_buffer, frame_buffer, 3), dtype=np.uint8)  # RGB frame buffer
        self.registers = np.zeros((num_cores, bits))  # no. of cores x no. of bits
        self.running = True
        self.debug_mode = debug
        
        # Instructions mapped to their corresponding methods
        self.instructions = {
            0x01: self.load_immediate,
            0x02: self.add,
            0x03: self.sub,
            0x04: self.mul,
            0x05: self.div,
            0x06: self.draw_pixel,
            0xFF: self.halt
        }

    def fetch(self, core_id):
        """Fetch the next instruction for a given core."""
        pc = int(self.registers[core_id][15])  # Program Counter is stored in the last register
        opcode = int(self.memory[pc])
        self.registers[core_id][15] += 1  # Increment Program Counter
        return opcode

    def decode_execute(self, core_id, opcode):
        """Decode and execute an instruction for a given core."""
        if opcode in self.instructions:
            self.instructions[opcode](core_id)
        else:
            raise Exception(f"Unknown opcode: {opcode}")

    def load_immediate(self, core_id):
        """Load an immediate value into a register."""
        pc = int(self.registers[core_id][15])
        reg = int(self.memory[pc])
        value = self.memory[pc + 1]
        self.registers[core_id][15] += 2
        if reg < 16:
            self.registers[core_id][reg] = value
        else:
            raise IndexError(f"Register index out of range: {reg}")

    def add(self, core_id):
        """Add two registers and store the result in the first register."""
        pc = int(self.registers[core_id][15])
        reg1 = int(self.memory[pc])
        reg2 = int(self.memory[pc + 1])
        self.registers[core_id][15] += 2
        self.registers[core_id][reg1] += self.registers[core_id][reg2]

    def sub(self, core_id):
        """Subtract the second register from the first register."""
        pc = int(self.registers[core_id][15])
        reg1 = int(self.memory[pc])
        reg2 = int(self.memory[pc + 1])
        self.registers[core_id][15] += 2
        self.registers[core_id][reg1] -= self.registers[core_id][reg2]

    def mul(self, core_id):
        """Multiply two registers and store the result in the first register."""
        pc = int(self.registers[core_id][15])
        reg1 = int(self.memory[pc])
        reg2 = int(self.memory[pc + 1])
        self.registers[core_id][15] += 2
        self.registers[core_id][reg1] *= self.registers[core_id][reg2]

    def div(self, core_id):
        """Divide the first register by the second register."""
        pc = int(self.registers[core_id][15])
        reg1 = int(self.memory[pc])
        reg2 = int(self.memory[pc + 1])
        self.registers[core_id][15] += 2
        if self.registers[core_id][reg2] == 0:
            raise ZeroDivisionError("Division by zero")
        self.registers[core_id][reg1] /= self.registers[core_id][reg2]

    def draw_pixel(self, core_id):
        """Draw a pixel to the framebuffer."""
        pc = int(self.registers[core_id][15])
        x = int(self.memory[pc])
        y = int(self.memory[pc + 1])
        r = int(self.memory[pc + 2])
        g = int(self.memory[pc + 3])
        b = int(self.memory[pc + 4])
        self.registers[core_id][15] += 5

        if 0 <= x < 64 and 0 <= y < 64:
            self.framebuffer[y, x] = [r, g, b]

    def halt(self, core_id):
        """Halt the GPU execution."""
        self.running = False

    def run_core(self, core_id):
        """Run instructions for a single core."""
        while self.running:
            opcode = self.fetch(core_id)
            self.decode_execute(core_id, opcode)
            self.debug(core_id)

    def run(self):
        """Run the GPU emulator across all cores in parallel."""
        with ThreadPoolExecutor(max_workers=self.num_cores) as executor:
            futures = [executor.submit(self.run_core, core_id) for core_id in range(self.num_cores)]
            for future in futures:
                future.result()  # Wait for all cores to finish

    def debug(self, core_id):
        """Print the state of the GPU for debugging purposes."""
        if self.debug_mode:
            print(f"Core {core_id} - PC: {int(self.registers[core_id][15])}, Registers: {self.registers[core_id]}")

    def load_program(self, program):
        """Load a program into GPU memory."""
        self.memory[:len(program)] = program


# Sample GPU program to draw a square outline
program = [
    # Draw top side of the square
    0x06, 10, 10, 255, 255, 255,  # Draw white pixel at (10, 10)
    0x06, 11, 10, 255, 255, 255,  # Draw white pixel at (11, 10)
    0x06, 12, 10, 255, 255, 255,  # Draw white pixel at (12, 10)
    0x06, 13, 10, 255, 255, 255,  # Draw white pixel at (13, 10)
    0x06, 14, 10, 255, 255, 255,  # Draw white pixel at (14, 10)

    # Draw bottom side of the square
    0x06, 10, 14, 255, 255, 255,  # Draw white pixel at (10, 14)
    0x06, 11, 14, 255, 255, 255,  # Draw white pixel at (11, 14)
    0x06, 12, 14, 255, 255, 255,  # Draw white pixel at (12, 14)
    0x06, 13, 14, 255, 255, 255,  # Draw white pixel at (13, 14)
    0x06, 14, 14, 255, 255, 255,  # Draw white pixel at (14, 14)

    # Draw left side of the square
    0x06, 10, 11, 255, 255, 255,  # Draw white pixel at (10, 11)
    0x06, 10, 12, 255, 255, 255,  # Draw white pixel at (10, 12)
    0x06, 10, 13, 255, 255, 255,  # Draw white pixel at (10, 13)

    # Draw right side of the square
    0x06, 14, 11, 255, 255, 255,  # Draw white pixel at (14, 11)
    0x06, 14, 12, 255, 255, 255,  # Draw white pixel at (14, 12)
    0x06, 14, 13, 255, 255, 255,  # Draw white pixel at (14, 13)

    0xFF                          # Halt
]

# Initialize GPU and load program into memory
gpu = GPU()
gpu.load_program(program)

# Run the GPU
gpu.run()

# Display the pixels
import matplotlib.pyplot as plt

# Download the image
plt.imsave("gpu_output.png", gpu.framebuffer)
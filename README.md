# Hardware Emulators
This repository contains emulators for various hardware components. It also contains a motherboard emulator that combines the CPU, GPU, and RAM emulators. This can be run with [computer.py](computer.py) as a virtual computer.

## Table of Contents
- [Hardware Emulators](#hardware-emulators)
  - [Table of Contents](#table-of-contents)
  - [CPU](#cpu)
  - [GPU](#gpu)
  - [RAM](#ram)
  - [Motherboard](#motherboard)
  - [Sound Card](#sound-card)
  - [Network Card](#network-card)
  - [HDD](#hdd)
  - [SSD](#ssd)

## CPU
[cpu.py](emulators/cpu.py)
### Example Program
```python
# Program to add two numbers
program = [
    0x01, 0x00, 0x0A,  # Load 10 into R0
    0x01, 0x01, 0x05,  # Load 5 into R1
    0x02, 0x00, 0x01,  # Add R1 to R0
    0x0D, 0x07,        # Jump to address 0x07 if R0 is zero
    0xFF               # Halt
]

cpu = CPU()
cpu.load_program(program)
cpu.run()

# Print the sum of the two numbers
print(f"Sum: {cpu.registers[0]}")
```

## GPU
[gpu.py](emulators/gpu.py)
### Example Program
```python
# Program to draw a square outline
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
```

## RAM
[ram.py](emulators/ram.py)
### Example Program
NOTE: The RAM emulator is not meant to be run as a standalone program. It is meant to be used in conjunction with the CPU emulator.

## Motherboard
[motherboard.py](emulators/motherboard.py)

### Example Program
```python
# Sample program that finds the sum of two numbers
cpu_program = [
    0x01, 0x00, 0x0A,  # Load 10 into R0
    0x01, 0x01, 0x05,  # Load 5 into R1
    0x02, 0x00, 0x01,  # Add R1 to R0
    0x0D, 0x07,        # Jump to address 0x07 if R0 is zero
    0xFF               # Halt
]

motherboard = Motherboard()
motherboard.load_program(cpu_program)
motherboard.run()

print("CPU output:", motherboard.cpu.registers[0])
```

## Sound Card
[sound_card.py](emulators/sound_card.py)

### Example Program
NOTE: The Sound Card emulator is not meant to be run as a standalone program. It is meant to be used in conjunction with the Motherboard emulator.

## Network Card
[network_card.py](emulators/network_card.py)

### Example Program
NOTE: The Network Card emulator is not meant to be run as a standalone program. It is meant to be used in conjunction with the Motherboard emulator.

## HDD
[hdd.py](emulators/hdd.py)

### Example Program
NOTE: The HDD emulator is not meant to be run as a standalone program. It is meant to be used in conjunction with the Motherboard emulator.

## SSD
[ssd.py](emulators/ssd.py)

### Example Program
NOTE: The SSD emulator is not meant to be run as a standalone program. It is meant to be used in conjunction with the Motherboard emulator.

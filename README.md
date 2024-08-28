# Hardware Emulators
This repository contains emulators for various hardware components.

## CPU
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

    0xFF                        # Halt
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
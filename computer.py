from motherboard import Motherboard

if __name__ == "__main__":
    # Sample program that finds the sum of two numbers
    cpu_program = [
        0x01, 0x00, 0x0A,  # Load 10 into R0
        0x01, 0x01, 0x05,  # Load 5 into R1
        0x02, 0x00, 0x01,  # Add R1 to R0
        0x0D, 0x07,        # Jump to address 0x07 if R0 is zero
        0xFF               # Halt
    ]

    # GPU program to draw a square outline
    gpu_program = [
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

    motherboard = Motherboard()
    motherboard.load_program(cpu_program)
    motherboard.run()

    print("CPU output:", motherboard.cpu.registers[0])

    # Render some data using the GPU
    motherboard.load_program(gpu_program, type="gpu")
    motherboard.run(type="gpu")

    motherboard.render()
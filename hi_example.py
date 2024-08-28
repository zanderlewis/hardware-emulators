from emulators.motherboard import Motherboard

# Define the pixel coordinates for the letters "H" and "I"
display_hi = [
    # Draw "H"
    0x06, 10, 10, 255, 255, 255,  # Left vertical line
    0x06, 10, 11, 255, 255, 255,
    0x06, 10, 12, 255, 255, 255,
    0x06, 10, 13, 255, 255, 255,
    0x06, 10, 14, 255, 255, 255,
    0x06, 15, 10, 255, 255, 255,  # Right vertical line
    0x06, 15, 11, 255, 255, 255,
    0x06, 15, 12, 255, 255, 255,
    0x06, 15, 13, 255, 255, 255,
    0x06, 15, 14, 255, 255, 255,
    0x06, 11, 12, 255, 255, 255,  # Middle horizontal line
    0x06, 12, 12, 255, 255, 255,
    0x06, 13, 12, 255, 255, 255,
    0x06, 14, 12, 255, 255, 255,

    # Draw "I"
    0x06, 17, 10, 255, 255, 255,  # Top horizontal line
    0x06, 18, 10, 255, 255, 255,
    0x06, 19, 10, 255, 255, 255,
    0x06, 20, 10, 255, 255, 255,
    0x06, 21, 10, 255, 255, 255,
    0x06, 19, 11, 255, 255, 255,  # Middle vertical line
    0x06, 19, 12, 255, 255, 255,
    0x06, 19, 13, 255, 255, 255,
    0x06, 19, 14, 255, 255, 255,
    0x06, 17, 14, 255, 255, 255,  # Bottom horizontal line
    0x06, 18, 14, 255, 255, 255,
    0x06, 19, 14, 255, 255, 255,
    0x06, 20, 14, 255, 255, 255,
    0x06, 21, 14, 255, 255, 255,

    0xFF  # Halt
]

def main():
    motherboard = Motherboard()
    print(motherboard.get_time())
    motherboard.load_program(display_hi, type="gpu")
    motherboard.run(type="gpu")
    motherboard.render(render_type="window")

if __name__ == "__main__":
    main()
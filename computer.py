from emulators.motherboard import Motherboard

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

    # Play a sound using the sound card
    sound_data = [
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
        [0, 22767], [22767, 0], [0, -22767], [-22767, 0],
    ]

    motherboard.play_sound(sound_data)

    # Example of writing to the HDD
    data_to_write = b"Hello, HDD!"
    motherboard.write_to_hdd(0, data_to_write)

    # Example of reading from the HDD
    read_data = motherboard.read_from_hdd(0, len(data_to_write))
    print(f"Read data: {read_data.decode()}")

    # Format the HDD
    motherboard.format_hdd()

    # Example of writing to the SSD
    ssd_data_to_write = b"Hello, SSD!"
    motherboard.write_to_ssd(0, ssd_data_to_write)

    # Example of reading from the SSD
    ssd_read_data = motherboard.read_from_ssd(0, len(ssd_data_to_write))
    print(f"Read data from SSD: {ssd_read_data.decode()}")

    # Format the SSD
    motherboard.format_ssd()

    # Example of sending data over the network
    data_to_send = b"Hello, Network!"
    motherboard.send_network_data(data_to_send, '127.0.0.1', 8081)

    # Example of receiving data from the network
    received_data = motherboard.receive_network_data()
    print(f"Received data: {received_data.decode()}")

    # Close the network card
    motherboard.close_network_card()

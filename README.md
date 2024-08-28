# cpu-emulator
 A CPU emulator written in python.

## Example Program
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

from ram import RAM

class CPU:
    def __init__(self, bits:int=16, memory:int=512, debug:bool=False):
        # 16 registers, 512 bytes of memory, and a stack
        self.registers = [0] * bits  # Registers (R0-R15 if 16-bit)
        self.pc = 0  # Program Counter
        self.memory = RAM(memory)  # Memory
        self.stack = []  # Stack for PUSH and POP
        self.running = True
        self.debug_mode = debug

        # Instructions (opcode to function mapping)
        self.instructions = {
            0x01: self.load_immediate,
            0x02: self.add,
            0x03: self.store,
            0x04: self.load,
            0x05: self.sub,
            0x06: self.mul,
            0x07: self.div,
            0x08: self.and_op,
            0x09: self.or_op,
            0x0A: self.xor_op,
            0x0B: self.not_op,
            0x0C: self.jmp,
            0x0D: self.jz,
            0x0E: self.jnz,
            0x0F: self.push,
            0x10: self.pop,
            0xFF: self.halt
        }

    def fetch(self):
        """Fetch the next instruction from memory."""
        if self.pc < len(self.memory):
            opcode = self.memory.read(self.pc)
            self.pc += 1
            return opcode
        else:
            raise Exception(f"Program counter out of bounds: {self.pc}")

    def decode_execute(self, opcode):
        """Decode and execute the instruction."""
        if opcode in self.instructions:
            self.instructions[opcode]()
        else:
            raise Exception(f"Unknown opcode: {opcode}")

    def load_immediate(self):
        """Load an immediate value into a register."""
        reg = self.memory[self.pc]
        value = self.memory[self.pc + 1]
        self.pc += 2
        if reg < len(self.registers):
            self.registers[reg] = value
        else:
            raise IndexError(f"Register index out of range: {reg}")

    def add(self):
        """Add two registers and store the result in the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] += self.registers[reg2]
        self.registers[reg1] &= 0xFF  # Ensure 8-bit wrap-around

    def sub(self):
        """Subtract the second register from the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] -= self.registers[reg2]
        self.registers[reg1] &= 0xFF  # Ensure 8-bit wrap-around

    def mul(self):
        """Multiply two registers and store the result in the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] *= self.registers[reg2]
        self.registers[reg1] &= 0xFF  # Ensure 8-bit wrap-around

    def div(self):
        """Divide the first register by the second register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        if self.registers[reg2] == 0:
            raise Exception("Division by zero")
        self.registers[reg1] //= self.registers[reg2]
        self.registers[reg1] &= 0xFF  # Ensure 8-bit wrap-around

    def and_op(self):
        """Perform bitwise AND on two registers and store the result in the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] &= self.registers[reg2]

    def or_op(self):
        """Perform bitwise OR on two registers and store the result in the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] |= self.registers[reg2]

    def xor_op(self):
        """Perform bitwise XOR on two registers and store the result in the first register."""
        reg1 = self.memory[self.pc]
        reg2 = self.memory[self.pc + 1]
        self.pc += 2
        self.registers[reg1] ^= self.registers[reg2]

    def not_op(self):
        """Perform bitwise NOT on a register."""
        reg = self.memory[self.pc]
        self.pc += 1
        self.registers[reg] = ~self.registers[reg] & 0xFF

    def jmp(self):
        """Jump to a specific memory address."""
        addr = self.memory[self.pc]
        if addr < len(self.memory):
            self.pc = addr
        else:
            raise Exception(f"Jump address out of bounds: {addr}")

    def jz(self):
        """Jump to a specific memory address if the zero flag is set."""
        addr = self.memory[self.pc]
        self.pc += 1
        if self.registers[0] == 0:
            if addr < len(self.memory):
                self.pc = addr
            else:
                raise Exception(f"Jump address out of bounds: {addr}")

    def jnz(self):
        """Jump to a specific memory address if the zero flag is not set."""
        addr = self.memory[self.pc]
        self.pc += 1
        if self.registers[0] != 0:
            if addr < len(self.memory):
                self.pc = addr
            else:
                raise Exception(f"Jump address out of bounds: {addr}")

    def push(self):
        """Push a register's value onto the stack."""
        reg = self.memory[self.pc]
        self.pc += 1
        self.stack.append(self.registers[reg])

    def pop(self):
        """Pop a value from the stack into a register."""
        reg = self.memory[self.pc]
        self.pc += 1
        if not self.stack:
            raise Exception("Stack underflow")
        self.registers[reg] = self.stack.pop()

    def store(self):
        """Store a register's value in memory."""
        reg = self.memory[self.pc]
        addr = self.memory[self.pc + 1]
        self.pc += 2
        if reg < len(self.registers):
            if addr < len(self.memory):
                self.memory[addr] = self.registers[reg]
            else:
                raise Exception(f"Store address out of bounds: {addr}")
        else:
            raise IndexError(f"Register index out of range: {reg}")

    def load(self):
        """Load a value from memory into a register."""
        reg = self.memory[self.pc]
        addr = self.memory[self.pc + 1]
        self.pc += 2
        if reg < len(self.registers):
            if addr < len(self.memory):
                self.registers[reg] = self.memory[addr]
            else:
                raise Exception(f"Load address out of bounds: {addr}")
        else:
            raise IndexError(f"Register index out of range: {reg}")

    def halt(self):
        """Halt the CPU."""
        self.running = False

    def run(self):
        """Run the CPU until halted."""
        while self.running:
            opcode = self.fetch()
            self.decode_execute(opcode)
            self.debug()

    def debug(self):
        """Print the state of the CPU for debugging."""
        if self.debug_mode:
            print(f"PC: {self.pc}, Registers: {self.registers}, Stack: {self.stack}")

    def load_program(self, program):
        """Load a program into memory."""
        self.memory.load_program(program)


if __name__ == "__main__":
    # Sample program that finds the sum of two numbers
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

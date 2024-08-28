class SSD:
    def __init__(self, file_path="ssd.bin", size=1024*1024*10, debug=False):
        self.file_path = file_path
        self.size = size
        self.debug_mode = debug
        self._initialize_disk()

    def _initialize_disk(self):
        """Initialize the virtual SSD."""
        with open(self.file_path, 'wb') as f:
            f.write(b'\x00' * self.size)
        if self.debug_mode:
            print(f"Initialized virtual SSD at {self.file_path} with size {self.size} bytes")

    def read(self, offset, length):
        """Read data from the virtual SSD."""
        with open(self.file_path, 'rb') as f:
            f.seek(offset)
            data = f.read(length)
        if self.debug_mode:
            print(f"Read {length} bytes from offset {offset}")
        return data

    def write(self, offset, data):
        """Write data to the virtual SSD."""
        with open(self.file_path, 'r+b') as f:
            f.seek(offset)
            f.write(data)
        if self.debug_mode:
            print(f"Wrote {len(data)} bytes to offset {offset}")

    def format(self):
        """Format the virtual SSD."""
        with open(self.file_path, 'wb') as f:
            f.write(b'\x00' * self.size)
        if self.debug_mode:
            print("Formatted the virtual SSD")
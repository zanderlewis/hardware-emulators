import os

class HDD:
    def __init__(self, file='hdd.bin', size=1024*1024*10, debug=False):
        self.file_path = file
        self.size = size
        self.debug_mode = debug
        self._initialize_disk()

    def _initialize_disk(self):
        """Initialize the virtual hard disk file."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'wb') as f:
                f.write(b'\x00' * self.size)
        if self.debug_mode:
            print(f"Initialized virtual hard disk at {self.file_path} with size {self.size} bytes")

    def read(self, offset, length):
        """Read data from the virtual hard disk."""
        with open(self.file_path, 'rb') as f:
            f.seek(offset)
            data = f.read(length)
        if self.debug_mode:
            print(f"Read {length} bytes from offset {offset}")
        return data

    def write(self, offset, data):
        """Write data to the virtual hard disk."""
        with open(self.file_path, 'r+b') as f:
            f.seek(offset)
            f.write(data)
        if self.debug_mode:
            print(f"Wrote {len(data)} bytes to offset {offset}")

    def format(self):
        """Format the virtual hard disk."""
        with open(self.file_path, 'wb') as f:
            f.write(b'\x00' * self.size)
        if self.debug_mode:
            print("Formatted the virtual hard disk")
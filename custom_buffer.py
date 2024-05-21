class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def add(self, item):
        if len(self.buffer) >= self.capacity:
            self.flush()
        self.buffer.append(item)

    def flush(self):
        # Process the buffer, e.g., send the data somewhere
        print("Flushing buffer:", self.buffer)
        self.buffer = []


def main():
    # Example usage
    buffer = Buffer(3)  # Capacity of 3 items
    buffer.add(1)
    buffer.add(2)
    buffer.add(3)

    # Buffer is full, will flush
    buffer.add(4)


if __name__ == "__main__":
    main()
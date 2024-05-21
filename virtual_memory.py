import random


class VirtualMemory:
    def __init__(self, physical_memory_size, page_size, virtual_memory_size):
        self.physical_memory_size = physical_memory_size
        self.page_size = page_size
        self.virtual_memory_size = virtual_memory_size
        self.physical_memory = [None] * physical_memory_size
        self.virtual_memory = [None] * virtual_memory_size
        self.page_table = {}

    def read(self, address):
        if address >= self.virtual_memory_size:
            raise ValueError("Invalid address")

        page_number, offset = divmod(address, self.page_size)

        if page_number not in self.page_table:
            self.load_page(page_number)

        physical_address = self.page_table[page_number] * self.page_size + offset
        return self.physical_memory[physical_address]

    def write(self, address, data):
        if address >= self.virtual_memory_size:
            raise ValueError("Invalid address")

        page_number, offset = divmod(address, self.page_size)

        if page_number not in self.page_table:
            self.load_page(page_number)

        physical_address = self.page_table[page_number] * self.page_size + offset
        self.physical_memory[physical_address] = data

    def load_page(self, page_number):
        if len(self.page_table) >= self.physical_memory_size / self.page_size:
            self.evict_page()

        frame_number = random.randint(0, self.physical_memory_size / self.page_size - 1)
        self.page_table[page_number] = frame_number
        for i in range(self.page_size):
            self.physical_memory[frame_number * self.page_size + i] = self.virtual_memory[
                page_number * self.page_size + i]

    def evict_page(self):
        # Simplified eviction process: just remove a random page from the page table
        page_number = random.choice(list(self.page_table.keys()))
        del self.page_table[page_number]

def main():
    # Example usage
    physical_memory_size = 16
    page_size = 4
    virtual_memory_size = 32

    vm = VirtualMemory(physical_memory_size, page_size, virtual_memory_size)

    # Write data to virtual memory
    for i in range(virtual_memory_size):
        vm.virtual_memory[i] = i

    # Read data from virtual memory
    for i in range(virtual_memory_size):
        print(vm.read(i))

    # Modify data in virtual memory
    vm.write(10, 100)

    # Read modified data
    print(vm.read(10))


if __name__ == "__main__":
    main()

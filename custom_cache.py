class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            self.evict()
        self.cache[key] = value

    def evict(self):
        # Implement your own eviction policy here, e.g., LRU, LFU, FIFO
        # For simplicity, here we just remove the first item
        if self.cache:
            del self.cache[next(iter(self.cache))]

def main():

    # Example usage
    cache = Cache(3)  # Capacity of 3 items
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)

    print(cache.get('a'))  # Output: 1
    print(cache.get('b'))  # Output: 2
    print(cache.get('c'))  # Output: 3

    # Cache is full, 'a' will be evicted
    cache.put('d', 4)
    print(cache.get('a'))  # Output: None

if __name__ == '__main__':
    main()
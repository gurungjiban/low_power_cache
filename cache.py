class Cache:
    def __init__(self, size_kb, block_size, associativity):
        self.size = size_kb * 1024
        self.block_size = block_size
        self.associativity = associativity

        self.num_blocks = self.size // self.block_size
        self.num_sets = self.num_blocks // self.associativity

        self.cache = [[] for _ in range(self.num_sets)]

        self.hits = 0
        self.misses = 0
        self.total_accesses = 0

    def access(self, address):
        self.total_accesses += 1

        block_addr = address // self.block_size
        index = block_addr % self.num_sets
        tag = block_addr // self.num_sets

        set_ = self.cache[index]

        if tag in set_:
            self.hits += 1
            set_.remove(tag)
            set_.append(tag)  # LRU
            return True
        else:
            self.misses += 1
            if len(set_) >= self.associativity:
                set_.pop(0)
            set_.append(tag)
            return False

    def get_miss_rate(self):
        return self.misses / self.total_accesses
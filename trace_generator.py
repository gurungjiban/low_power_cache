import random

def generate_trace(length=10000, max_address=2**20):
    trace = []
    for _ in range(length):
        trace.append(random.randint(0, max_address))
    return trace
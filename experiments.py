from cache import Cache
from power_model import PowerModel
from way_prediction import WayPrediction
from trace_generator import generate_trace

def run_baseline(size_kb, associativity):
    cache = Cache(size_kb, 64, associativity)
    power = PowerModel()

    trace = generate_trace()

    for addr in trace:
        hit = cache.access(addr)
        power.update(hit)

    return cache.get_miss_rate(), power.get_total_energy()

def run_way_prediction(size_kb, associativity, accuracy):
    cache = Cache(size_kb, 64, associativity)
    power = PowerModel()
    predictor = WayPrediction(prediction_accuracy=accuracy)

    trace = generate_trace()

    for addr in trace:
        hit = cache.access(addr)

        # Way prediction energy
        predictor.predict()

        power.update(hit)

    total_energy = power.get_total_energy() + predictor.get_prediction_energy()

    return cache.get_miss_rate(), total_energy
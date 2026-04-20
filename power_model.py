class PowerModel:
    def __init__(self, energy_hit=0.5, energy_miss=2.0):
        self.energy_hit = energy_hit
        self.energy_miss = energy_miss
        self.total_energy = 0

    def update(self, hit):
        if hit:
            self.total_energy += self.energy_hit
        else:
            self.total_energy += self.energy_miss

    def get_total_energy(self):
        return self.total_energy
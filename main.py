from experiments import run_baseline, run_way_prediction
from visualization import plot_energy_vs_assoc, plot_miss_rate

associativities = [1, 2, 4, 8]

baseline_energies = []
baseline_miss = []

lowpower_energies = []
lowpower_miss = []

for assoc in associativities:
    miss, energy = run_baseline(32, assoc)
    baseline_energies.append(energy)
    baseline_miss.append(miss)

    miss_lp, energy_lp = run_way_prediction(32, assoc, 0.8)
    lowpower_energies.append(energy_lp)
    lowpower_miss.append(miss_lp)

print("Baseline Energy:", baseline_energies)
print("Low Power Energy:", lowpower_energies)

plot_energy_vs_assoc(associativities, baseline_energies)
plot_energy_vs_assoc(associativities, lowpower_energies)
plot_miss_rate(associativities, baseline_miss)

for i in range(len(associativities)):
    savings = ((baseline_energies[i] - lowpower_energies[i])
               / baseline_energies[i]) * 100
    print(f"Associativity {associativities[i]} Savings: {savings:.2f}%")
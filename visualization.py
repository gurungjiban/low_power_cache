import matplotlib.pyplot as plt

def plot_energy_vs_assoc(assocs, energies):
    plt.figure()
    plt.plot(assocs, energies)
    plt.xlabel("Associativity")
    plt.ylabel("Total Energy")
    plt.title("Energy vs Associativity")
    plt.show()

def plot_miss_rate(assocs, miss_rates):
    plt.figure()
    plt.plot(assocs, miss_rates)
    plt.xlabel("Associativity")
    plt.ylabel("Miss Rate")
    plt.title("Miss Rate vs Associativity")
    plt.show()
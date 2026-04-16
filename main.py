from simulation import run_simulation
from visualize import plot_results

def main():
    print("🚦 SMART TRAFFIC SIMULATION STARTED\n")

    static, smart = run_simulation(grid_size=3, level="peak")

    print("\n📊 FINAL RESULTS")
    print("Static Traffic System:", static)
    print("Smart AI System:", smart)

    improvement = ((static - smart) / static) * 100
    print("🚀 Improvement:", round(improvement, 2), "%")

    print("\n✅ Simulation Completed\n")

    # 🔥 THIS LINE IS REQUIRED FOR GRAPH
    plot_results(static, smart)


if __name__ == "__main__":
    main()
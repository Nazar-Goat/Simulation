from simulation.simulation import Simulation
import time

def main():
    sim = Simulation(width=10, height=10)
    print("Запуск симуляции...")
    
    try:      
        while True:
            sim.next_turn()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nСимуляция остановлена пользователем")

if __name__ == "__main__":
    main()
    print("=== Программа завершена ===")
from simulator.simulate import simulate
from entities.track import Track
from entities.train import Train
def main():
    simulate(Track, Train)

if __name__ == "__main__":
    main()
import time
import montecarlopi

if __name__ == "__main__":
    start = time.time()
    pi, num_calculations = montecarlopi.mcpi(1_000_000)
    end = time.time()

    print(f"Runtime: {end - start:.2f} seconds")
    print(f"Value of PI: {pi}")
    print(f"Calculations per second: {num_calculations}")
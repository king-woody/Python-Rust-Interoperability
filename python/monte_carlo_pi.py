import math
import random
import time
from enum import Enum
import concurrent.futures
import psutil
import multiprocessing

class CalcOption(Enum):
    MULTIPROCESSING = 1
    MULTITHREADING = 2

def monte_carlo_pi(calc_option, iterations: int) -> (float, str):

    """
    Calculates PI approximation using Monte-Carlo method

    :param calc_option:
    :param iterations:
    :return:
    """

    num_cpus = psutil.cpu_count(logical=True)
    print(f"Number of CPUs available: {num_cpus}")

    now = time.time()

    if calc_option == CalcOption.MULTIPROCESSING:
        total_inside = proc_monte_carlo_pi(num_cpus, iterations)
    elif calc_option == CalcOption.MULTITHREADING:
        total_inside = thread_monte_carlo_pi(num_cpus, iterations)
    else:
        raise ValueError

    stop = time.time()
    total_iterations = num_cpus * iterations
    elapsed = stop - now
    pi = total_inside / total_iterations * 4
    calculations_string = round(total_iterations / elapsed)
    return (pi, f"{calculations_string:,}")

def monte_compute(iterations: int) -> int:

    """
    Monte-Carlo simulation

    :param iterations:
    :return:
    """

    inside = 0
    random.seed()
    for _ in range(iterations):
        a = random.random()
        b = random.random()
        c = math.pow(a, 2.0) + math.pow(b, 2.0)
        if c <= 1.0:
            inside += 1
    return inside


def proc_monte_carlo_pi(num_cpus: int, iterations: int) -> int:

    """
    Calculate the value of PI with Monte-Carlo method using multiprocessing

    :param num_cpus:
    :param iterations:
    :return:
    """

    with multiprocessing.Pool(num_cpus) as p:
        results = p.map(monte_compute, [iterations] * num_cpus)
        total_inside = sum(results)
    return total_inside


def thread_monte_carlo_pi(num_cpus: int, iterations: int) -> int:

    """
    Calculate the value of PI with Monte-Carlo method using multithreading

    :param num_cpus:
    :param iterations:
    :return:
    """

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(monte_compute, iterations) for _ in range(num_cpus)]
        total_inside = sum([f.result() for f in futures])
    return total_inside


if __name__ == "__main__":
    calc_option = CalcOption.MULTITHREADING
    start = time.time()
    pi, calcs_p_sec = monte_carlo_pi(calc_option, iterations=1_000_000)
    stop = time.time()

    print(f'Runtime: {stop - start:.2f} seconds')
    print(f"Value of PI: {pi}")
    print(f"Calculations per second: {calcs_p_sec}")

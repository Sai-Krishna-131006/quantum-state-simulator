import numpy as np

def simulate_measurements(p0, p1, shots=1000):
    """
    Simulate repeated quantum measurements.
    """
    outcomes = np.random.choice([0,1], size=shots, p=[p0,p1])

    count0 = np.sum(outcomes == 0)
    count1 = np.sum(outcomes == 1)

    return count0, count1
import numpy as np

# Parameters
start_voltage = 0.0  # Initial voltage
end_voltage = 1.17  # Final voltage
num_entries = 531  # Total number of entries
steady_state_time = 1.2  # Time to reach steady state (in seconds)
steady_state_deviation = 0.02  # Steady state fluctuation (±)

# First-order transfer function parameters
tau = 0.3  # Time constant

# Time array
time = np.linspace(0, steady_state_time, num_entries)

# First-order transfer function
voltage = (end_voltage - start_voltage) * (1 - np.exp(-time / tau)) + start_voltage

# Adding noise to steady state
steady_state = (end_voltage - start_voltage) * (1 - np.exp(-steady_state_time / tau)) + start_voltage
noise = np.random.uniform(-steady_state_deviation, steady_state_deviation, size=num_entries)
voltage += noise

# Ensure the voltage stays within the specified range
voltage = np.clip(voltage, start_voltage, end_voltage)

# Output the dataset
for t, v in zip(time, voltage):
    print(f"{t:.3f}s, {v:.3f}V")
# Test
import numpy as np
import matplotlib.pyplot as plt

# Generate sine wave data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave', color='blue')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()

# Save plot
plt.savefig('test_plot.png')
plt.close()

print("Sine wave plot saved as test_plot.png")

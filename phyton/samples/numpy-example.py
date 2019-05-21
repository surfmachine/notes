
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Element-wise calculations
# -------------------------
# Now we can perform element-wise calculations on height and weight.
# For example, you could take all 6 of the height and weight observations above, and calculate the BMI
# for each observation with a single equation.
# These operations are very fast and computationally efficient.
# They are particularly helpful when you have 1000s of observations in your data.

# Calculate bmi: weight : (height)2     // gewicht geteilt durch höhe im quadrat
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# Subsetting
# ----------

# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]


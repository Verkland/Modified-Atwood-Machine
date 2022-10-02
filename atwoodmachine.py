import math

# Calculate the acceleration of the sitting object in a modified Atwood machine
# with a hanging object of mass m1 and a sitting object of mass m2.
# the string has no mass and is inextensible.
# There is no friction in the system.

def atwoodAccel(m1, m2):
    return (9.81 * m1) / (m1 + m2)

# Get input from the user and calculate the acceleration
m1 = float(input("Enter the mass of the hanging object: "))
m2 = float(input("Enter the mass of the sitting object: "))
accel = atwoodAccel(m1, m2)

# Print the result
print("The acceleration of the sitting object is", accel, "m/s^2")
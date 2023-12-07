# Question 2:
# Write a function that returns the Nth number in the following sequence:
# [8, 15, 22, 29, 39, ...]

# Answer:

def num_in_seq(n):
    # Base case: when N is 1, return the first number in the sequence
    if n == 1:
        return 8
    # Recursive case: calculate the Nth number using the formula
    return 8 + (n - 1) * 7


# Examples
print(num_in_seq(1))  # Output: 8
print(num_in_seq(5))  # Output: 36
print(num_in_seq(10))  # Output: 71


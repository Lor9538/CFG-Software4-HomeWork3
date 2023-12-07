# Question 1 [A]:
# Write a program that takes in an input file and prints out
# a list with the final order of who's in the queue.

def process_queue(input_file):
    # Initialize an empty list to represent the queue
    queue = []

    # Open the specified input file in read mode
    with open(input_file, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into command and name
            command, name = line.strip().split()

            # Check if the command is 'JUMP'
            if command == 'JUMP':
                # If 'JUMP', insert the person at the front of the queue
                queue.insert(0, name)  # Person jumps to the front
            # Check if the command is 'JOIN'
            elif command == 'JOIN':
                # If 'JOIN', append the person at the back of the queue
                queue.append(name)  # Person joins at the back

    # Print the final order of the queue
    print("Final Queue Order:")
    for person in queue:
        print(person)


# Example usage with the provided input file 'hw3_q1.txt'
process_queue('hw3_q1.txt')


# Question 1 [B]:
# What is the time and space complexity of your solution?
# If you are making any assumptions, list them.

# Answer:

# Time Complexity:
# a) Inserting a person at the front of the list 'queue.insert(0, name)' takes O(n) time,
# where n is the number of elements in the list. This is because it requires shifting all
# existing elements to make room for the new element.
# b) Appending a person to the back of the list 'queue.append(name)' takes O(1) time on average.

# Space Complexity:
# The space complexity is O(n), where n is the number of elements in the queue. This is
# because we store each person in a list, and the space required grows linearly with the number of
# people in the queue.

# Assumptions:
# a) Solution assumes a reasonably sized input file, as the time complexity of inserting at
# the front of the list increases with the number of elements
# b) The solution assumes sequential processing of valid 'JUMP' and 'JOIN' commands in the input file
# c) Printing the final queue order is considered necessary; otherwise, they can be removed

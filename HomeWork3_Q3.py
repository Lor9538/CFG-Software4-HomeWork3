# Question 3 [A]:
# Simulate clicking around the CFG Website. Keep track of the URL changes
# and print the current URL after each move.

# Answer:

from selenium import webdriver

# Initialise the web driver
driver = webdriver.Chrome()

# Base URL
base_url = "https://codefirstgirls.com/"
current_url = base_url

# Define options and actions
options_mapping = {
    base_url: {"options": ["Courses", "Opportunities"], "actions": {}},
    base_url + "courses": {"options": ["CFGDegree", "Back"], "actions": {}},
    base_url + "opportunities": {"options": ["Ambassadors", "Back"], "actions": {}},
    base_url + "courses/cfgdegree": {"options": ["Back"], "actions": {}},
}

while True:
    print(f"You are currently on the URL {current_url}")
    print("Where are you clicking?")

    # Display available options
    current_options = options_mapping[current_url]["options"]
    print(f"Options: {', '.join(current_options)}")

    # Get user input
    choice = input().strip().lower()

    # Process user choice
    if choice == "back" and current_url != base_url:
        driver.back()  # Simulate clicking the back button
        current_url = driver.current_url
    elif choice in current_options:
        # Simulate clicking the chosen link
        driver.get(current_url + choice)
        current_url = driver.current_url
    else:
        print("Invalid choice. Please try again.")

# Question 3 [B]:
#  What is the time and space complexity of your solution? If you are making any
# assumptions, list them.

# Answer:

# Time Complexity:
# The time complexity of the solution is mainly dominated by contant time operations,
# resulting in an overall time complexity of O(1).
    # i) Getting the current URL using 'driver.current_url' and checking conditions
    # for available options in 'options_mapping' are constant time operations,
    # denoted as O(1).
    # ii) User input processing involves checking if the input is valid and simulating
    # actions based on the input. The user input processing is also constant time in
    # most practical cases, as the number of available options is typically small and
    # does not scale with the input size.

# Space Complexity:
# The space complexity is primarily determined by the size of the 'options_mapping' dictionary.
# As the dictionary has a fixed size and does not scale with the input or any iterative processes,
# the space complexity is constant, denoted at O(1).

# Assumptions:
# a) The WebDriver operations are assumed to have reasonable time complexities, and no
# specific details about WebDriver implementations are considered.
# b) The website's structure and navigation options are assumed to remain relatively static
# during the execution of the program.
# c) User input and WebDriver interactions are assumed to be the main factors affecting time complexity.
# d) No additional browser tabs or windows are opened during the simulation.

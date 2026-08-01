even_sum = 0          # Start the total at 0

for number in range(1, 51):   # Look at every number from 1 to 50
    if number % 2 == 0:       # Is it even?
        even_sum += number    # Add it to the running total

print(f"The sum of even numbers from 1 to 50 is {even_sum}.")
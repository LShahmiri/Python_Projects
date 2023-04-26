def fibonachi(num):
    # Initilize the first two numbers of the sequence
    fib_seq = [0, 1]

    # Loop through each number to n-2 (since we already have the first two numbers)
    for i in range(2, num):
        # Add the previous two numbers in the sequence to get the next number
        next_num = fib_seq[i-1]+fib_seq[i-2]

        # Add the next number to the list
        fib_seq.append(next_num)
    # Return the completed Fibonachi sequence
    return fib_seq


# Print the sequence to the console
print(fibonachi(10))

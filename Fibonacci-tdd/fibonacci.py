def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        sequence = [0,1]
        while len(sequence)<n:
            sequence.append(sequence[-1] + sequence[-2])
   
    return sequence
    
    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# fibonacci(5)
# fibonacci(4)
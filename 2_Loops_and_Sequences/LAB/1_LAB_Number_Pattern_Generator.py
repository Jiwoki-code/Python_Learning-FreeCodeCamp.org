def number_pattern(n):
    pattern = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n <= 0:
        return 'Argument must be an integer greater than 0.'
    
    numbers = [str(num+1) for num in range(n)]
    
    pattern = " ".join(numbers)
    return pattern

print(number_pattern("k"))
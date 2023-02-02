numbers = [7,-8,20,47,-7,-420,4]

def smalles_number(all_numbers):
    if len(all_numbers) == 0:
        return None
    
    min = float("inf")
    min_index = 0
    for i in range(0,len(all_numbers)):
        if all_numbers[i] < min:
            min = all_numbers[i]
            min_index = i

    return int(min_index)

print(numbers)
print(smalles_number(numbers))

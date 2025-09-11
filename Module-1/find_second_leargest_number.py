numbers = [10,8,10,20,30,50,30,48]
numbers.sort(reverse=True)

max_num = numbers[0]
second_max_number = -1

for num in numbers:
    if num != max_num:
        second_max_number = num
        break

print(f"Second Largest Number: {second_max_number}")
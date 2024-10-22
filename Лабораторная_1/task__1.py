from unicodedata import numeric

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
real_numbers =  [number for number in numbers if number is not None ]
point = sum(real_numbers) / (len(real_numbers) + 1)
numbers [4] = point
print("Измененный список:", numbers)

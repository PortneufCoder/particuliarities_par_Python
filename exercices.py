numbers = [12, 34, 36, 12452, 75]
appended = numbers.append(659)
print(appended)
ordered = sorted(numbers, reverse=True)

print(ordered)

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

test_list = ["bread", "rice", "flax", "lentils", "beans"]

length = len(test_list)
maximum = max(test_list)
minimum = min(test_list)
print(length)
print(maximum)
print(minimum)

print(test_list[0:3])  # ['bread', 'rice', 'flax']

animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3, 4, 2, 8, 2, 4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['fish'])
print(animals[3])  # Error --> must first use Key name before index position

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}}

elements['hydrogen']['is_noble_gas'] = False  # add new key/values
elements['helium']['is_noble_gas'] = True

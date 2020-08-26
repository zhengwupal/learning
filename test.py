import re
phone_numbers = []
pattern = r"\+[\d\-]+"
with open("log.txt", "r") as file:
    for line in file:
        result = re.search(pattern, line)
        phone_numbers.append(result.group(0))
print(phone_numbers)

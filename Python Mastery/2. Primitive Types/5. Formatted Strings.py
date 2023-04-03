# 5 Formatted Strings

first = "Mosh"
last = "Hamedani"

full_1 = first + " " + last  # approach 1 concatination
full_2 = f"{first} {last}"  # approach 2 formatted strings
full_3 = f"{len(first)} {last}"
full_4 = f"{len(first)} {2 + 2}"

print(full_1)
print(full_2)
print(full_3)
print(full_4)

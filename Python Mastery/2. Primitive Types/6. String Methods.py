# 6 String Methods

course = "   python Programing   " 

print(course.upper()) # Converts the message into all upercase letters
print(course.lower()) # Converts the message into all lowercase letters
print(course.title()) # Converts the first letter of any word in in the message an uppercase letter
print(course.strip())  # Removes the leftover spaces from the message
print(course.rstrip())  # Removes the leftover spaces from the right of the message
print(course.lstrip()) # Removes the leftover spaces from the left of the message
print(course.find("pro")) # Shows the index of "pro"
print(course.find("Pro")) # It's a case sensitive sequence
print(course.replace("p", "j")) # It replaces the letter with the given one
print("pro" in course) # Returns a boolean value
print("swift" not in course) # Returns a boolean value

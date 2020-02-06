# Ben Lizza
# 02/06/19
# String Manipulation Lab

# Make string with multiple words
name = 'ben, joe, anthony'

# Print the length of the string
print(len(name))

# Print the first letter of the string
print("The first letter of the string is " + name[0][:1])

# Print the last letter of the string
print("The last letter is " + name[16])

# Print the entire string in uppercase
print(name.__str__().upper())

# Print the string in Title Case
print(name.__str__().title())

# Print a message indicating whether the string consists of only alphabetic characters
print("Is the string all alphabetic?")
print(name.__str__().isalpha())

# Print the string after it has been split into individual words
print(name.__str__().split())

# Print one additional string method / i'm going to make the list all lower case
print(name.__str__().lower())





from imaplib import Int2AP


i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i2 = int(input())
d2 = float(input())
s2 = input()
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
i += i2
print(i)
# Print the sum of the double variables on a new line.
d += d2
print(d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)
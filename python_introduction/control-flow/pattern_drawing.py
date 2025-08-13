# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))
# Initialize row counter
row = 0
# Use a while loop to iterate over each row
while row < size:
    # Use a for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing all asterisks in the row
    print()
    # Increment the row counter
    row += 1

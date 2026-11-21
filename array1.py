# Accept scores from user
scores = list(map(int, input("Enter scores separated by space: ").split()))

# Calculate sum and average
total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
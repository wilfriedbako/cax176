grade = float(input("Enter your grade (0-100): "))

if grade >= 90:
    result = "A"
elif grade >= 80:
    result = "B"
elif grade >= 70:
    result = "C"
elif grade >= 60:
    result = "D"
else:
    result = "F"

print(f"Your grade is: {result}")

message = (
    "Congratulations! You passed!"
    if grade >= 70
    else "Keep trying. You can do better next time!"
)

print(message)


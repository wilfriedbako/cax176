import math
import random
import platform


random_number = random.randint(1, 100)
square_root = math.sqrt(random_number)
floored_root = math.floor(square_root)
operating_system = platform.system()
python_version = platform.python_version()


print(f"Random Number: {random_number}")
print(f"Square Root (floored): {floored_root}")
print(f"Operating System: {operating_system}")
print(f"Python Version: {python_version}")

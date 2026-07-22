# Requires colorama; install with: pip install colorama

from colorama import Fore, Style, init

init()

print(Fore.GREEN + "Colorama is working!")
print(Fore.BLUE + "This text is blue.")
print(Fore.RED + "This text is red.")
print(Style.RESET_ALL)
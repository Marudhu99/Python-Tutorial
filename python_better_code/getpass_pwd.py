from getpass import getpass

username = input("username:")
# The line `password = getpass("password: ")` is prompting the user to enter a password, and the
# `getpass` function is used to securely hide the input while the user is typing. The entered password
# is then stored in the `password` variable.
password = getpass("password: ")

print("Login successfully") if password == 'Marudhu' else print("login failed")
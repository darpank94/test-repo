name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome to this interactive program.")


age = input("Please enter your age: ")
try:
    age = int(age)
    if age < 0:
      print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")
except ValueError:
    print("Invalid input. Please enter a number for age.")

city = input("Please enter your city: ")
print(f"I hope the weather in {city} is pleasant!")

print("Thank you for interacting with me!")



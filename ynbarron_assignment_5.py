# Step counter 
# current number = int input for user 
# while loops for sequences to run
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    step_count = step_count + 1
print(1)
print("Steps:", step_count)
print()
#Test for divisors w user input
print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {current_number - 1}...")

Int = 2
while Int < current_number:
    if current_number % Int == 0:
        print(current_number, "is not prime")
        print(f"(divisible by {Int}")
        break
    Int = Int + 1

if Int == current_number and current_number > 1:
    print(current_number, "is prime!")
print()

# challenge 3 Multiplication table 
#add in row and collum to get tabled configured correctly
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("    ", end="")  


for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Print each row
for row in range(1, 11):
    print(f"{row:2}", end=" ") 
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()  


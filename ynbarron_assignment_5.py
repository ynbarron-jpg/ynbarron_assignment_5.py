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

print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {current_number - 1}...")

Int = 2
while Int < current_number:
    if current_number % Int == 0:
        print(current_number, "is not prime!")
        print("(divisible by", Int, ")")
        break
    Int = Int + 1

if Int == current_number and current_number > 1:
    print(current_number, "is prime!")
print()

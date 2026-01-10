def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide (P, Q):
    return P / Q
print(" select your desired operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = input("enter choice a/ b/ c/ d:")
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("INVALID BROTHA")















name: str = input("yout name: ")

age: int

try:
    age = int(input("your age: "))
    print(f"{name}-{age}")
except Exception as e:
    print("bad")
    

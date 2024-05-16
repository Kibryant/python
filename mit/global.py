counter = 0


def increment_counter():
    global counter
    counter += 1


print("Before increment:", counter)
increment_counter()
print("After increment:", counter)

"""Task 9: Make generator, that takes first and last items to iterate"""


def slice_generator(start, end):
    """generator function"""
    if start <= end:
        for item in range(end - start + 1):
            yield item + start
    else:
        print("Incorrect range limits")


def run_generator(start, end):
    for item in slice_generator(start, end):
        print(item)


print("\nTest 1: classic")
run_generator(1, 3)

print("\nTest 2: bigger range")
run_generator(45, 68)

print("\nTest 3: Incorrect input start>end")
run_generator(65, 36)

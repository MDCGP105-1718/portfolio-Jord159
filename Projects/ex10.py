high = int(input("High: "))
low = int(input("Low: "))
def FizzBuzz(high, low):
    x = low
    while x <= high:
        if x%3 == 0:
            if x%5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print(x)
        x = x + 1
FizzBuzz(high, low)

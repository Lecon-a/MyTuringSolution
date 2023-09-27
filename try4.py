# def main():
#     # x_value = int(input("What's x? "))
#     for x_value in range(-100000000000, 1000000000000):
#         if f1(x_value) == f2(x_value):
#             print(f"Function 1 result is: {f1(x_value)}")
#             print(f"Function 2 result is: {f2(x_value)}")

# def f1(x):
#     return round(x**3 + x/2)

# def f2(x):
#     return round(x**2 + x)

# def f3(x):
#     return x**2 + 1

# if __name__=="__main__":
#     main()

def amani():
    text = input("Text: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    for a in text:
        if a.casefold().strip() not in vowels:
            print(a, end='')
    print()

amani()
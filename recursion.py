# O(n)
def print_num(n):
    print(n)

    # a base case
    # code tell us to stop running to function
    if n == 0:
        return

    # recursive case ( take us to the next problem)
    print_num(n - 1)

# print_num(4)

# O(2^n)
def double_print_num(n):
    print(n)
    if n == 0:
        return 

    double_print_num(n - 1)
    double_print_num(n - 1)
    return

double_print_num(3)

# def fibonacci(n):
#     # base case
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1


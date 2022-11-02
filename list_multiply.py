# list_multiply.py
# write a function that multiplies each element of a list by 2

def list_multiply(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2


def main():
    lst = [5, 2.5, 100, -10]
    print(lst)
    print(list_multiply(lst))
    print(lst)
    

main()

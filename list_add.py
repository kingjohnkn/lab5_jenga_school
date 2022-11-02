# list_add.py
# Write a function that constructs and returns a new lsit using
# the elements of a given list that are greater than 5

def list_add(lst):
    new_lst = []
    for i in lst:
        if i > 5:
            new_lst.append(i)
            
    return new_lst

def main():
    lst = [5, 2.5, 100, -10, 10, 100000, -10]
    list_add(lst)
    print(f"Original list: {lst}")
    new_lst = list_add(lst)
    print(f"New list: {new_lst}")
    

main()

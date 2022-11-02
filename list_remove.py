# list_remove.py
# Write a functoin that removes elements in a list less than 5

def remove_elements(lst):
    for i in lst:
        if i < 5:
            lst.remove(i)
    
def main():
    lst = [5, 2.5, 100, -10]
    print(lst)
    remove_elements(lst)
    print(lst)
    

main()
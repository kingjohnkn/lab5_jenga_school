# list_change.py
# See what happens when you modify a list inside a function

def list_change(lst):
    lst = [1, 2, 3]
    
def main():
    lst = [5, 2.5, 100, -10]
    print(lst)
    list_change(lst)
    print(lst)
    
    
main()

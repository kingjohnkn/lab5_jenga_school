# list_product.py
# find the product of the elements of a given lsit
# and returns the result

def list_product(lst):
    
    product = 1
    for i in lst:
        product = i * product
        
    return(product)

def main():
    lst = [5, 2.5, 100, -10]
    print(lst)
    print(list_product(lst))
    

main()

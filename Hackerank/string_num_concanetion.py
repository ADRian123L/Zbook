def concatenate(n : int) -> None:
    num_string : str = str()
     
    for i in range(1, n + 1):
        num_string += str(i)
    
    print(num_string)
        
if __name__ == '__main__':
    n = int(input())
    concatenate(n)
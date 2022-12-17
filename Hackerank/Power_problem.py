def power(n : list) -> None:
    """The function prints the power of a 
    range of numbers."""
    if n in range(0, 21):
        for i in range(n):
            print(i **2)
    return None


if __name__ == '__main__':
    n = int(input())
    power(n)
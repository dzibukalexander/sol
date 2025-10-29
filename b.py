def min_operations(n, k, s):
    operations = 0
    i = 0
    
    while i < n:
        if s[i] == 'F':
            operations += 1
            i += k
            continue
        i += 1
    
    return operations

def main():
    n, k = map(int, input().split())
    s = input().strip()
    
    result = min_operations(n, k, s)
    print(result)

def test_cases():
    assert min_operations(6, 3, "TFTTTF") == 2
    assert min_operations(10, 2, "FTTTTTTTTF") == 2
    assert min_operations(5, 2, "TTTTT") == 0
    assert min_operations(4, 2, "FFFF") == 2
    assert min_operations(5, 3, "FTTTT") == 1
    assert min_operations(5, 3, "TTTTF") == 1
    assert min_operations(6, 2, "FTFTFT") == 3
    assert min_operations(4, 1, "FTFT") == 2    
    assert min_operations(5, 5, "FFFFF") == 1
    assert min_operations(3, 5, "FFF") == 1
    assert min_operations(8, 3, "FFTFFTFF") == 3
    
    print("Все основные тесты пройдены!")

if __name__ == "__main__":
    test_cases()

    # main()
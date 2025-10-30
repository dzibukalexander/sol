import math
from collections import Counter

def max_income(n, y, prices):
    counter = Counter(prices)    
    max_price = max(prices)
    
    max_profit = -1e18 # -10**18
    
    for x in range(2, max_price + 2):
        total_income = 0
        new_price_freq = Counter()
        
        for price in prices:
            new_price = math.ceil(price/x) # (price + x - 1) // x
            total_income += new_price
            new_price_freq[new_price] += 1
        
        printed_tags = 0
        for new_price, count in new_price_freq.items():
            available_old = counter.get(new_price, 0)
            if available_old < count:
                printed_tags += (count - available_old)
            
        profit = total_income - printed_tags * y
        max_profit = max(max_profit, profit)
    
    return max_profit

def main():
    n, y = map(int, input().split())
    prices = list(map(int, input().split()))
    
    result = max_income(n, y, prices)
    print(result)

def test_cases():
    print("Запуск тестов...")
    
    result1 = max_income(5, 51, [50, 150, 50, 148, 150])
    assert result1 == 31, f"Тест 1 не пройден: ожидалось 31, получено {result1}"
    
    result2 = max_income(3, 1000000000, [42, 42, 42])
    assert result2 == -2999999937, f"Тест 2 не пройден: ожидалось -2999999937, получено {result2}"
    
    result3 = max_income(4, 10, [100, 100, 100, 100])
    # При x=2: новые цены [50,50,50,50], нужно напечатать 4 ценника
    # доход = 200 - 40 = 160
    # При x=3: новые цены [34,34,34,34], доход = 136 - 40 = 96
    # При x=4: новые цены [25,25,25,25], доход = 100 - 40 = 60
    # При x=5: новые цены [20,20,20,20], доход = 80 - 40 = 40
    # Максимум при x=2
    print(f"Тест 3: результат {result3}")
    
    result4 = max_income(1, 5, [10])
    # При x=2: новая цена 5, нужно напечатать 1 ценник, доход = 5 - 5 = 0
    # При x=3: новая цена 4, доход = 4 - 5 = -1
    # При x=4: новая цена 3, доход = 3 - 5 = -2
    # При x=5: новая цена 2, доход = 2 - 5 = -3
    # При x=6: новая цена 2, доход = 2 - 5 = -3
    # При x=10: новая цена 1, доход = 1 - 5 = -4
    # Максимум 0
    assert result4 == 0, f"Тест 4 не пройден: ожидалось 0, получено {result4}"
    
    # Тест 5: Дорогие ценники
    result5 = max_income(3, 100, [10, 20, 30])
    print(f"Тест 5: результат {result5}")
    
    # Тест 6: Дешевые ценники
    result6 = max_income(3, 1, [10, 20, 30])
    print(f"Тест 6: результат {result6}")
    
    # Тест 7: Граничный случай - минимальные значения
    result7 = max_income(1, 1, [1])
    # При x=2: новая цена 1, доход = 1
    print(f"Тест 7: результат {result7}")
    
    print("Все основные тесты пройдены!")

if __name__ == "__main__":
    test_cases()
    
    # main()
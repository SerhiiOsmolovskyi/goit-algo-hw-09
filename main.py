import time

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    Завжди бере найбільшу доступну монету, поки сума не буде зменшена до нуля.
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    result = {}  # Словник для збереження кількості кожного номіналу
    
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin  # Визначаємо кількість монет даного номіналу
            amount %= coin  # Оновлюємо залишок суми
    
    return result

def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для знаходження мінімальної кількості монет.
    Використовує метод збереження мінімальної кількості монет для кожної проміжної суми.
    """
    coins = [1, 2, 5, 10, 25, 50]  # Доступні номінали монет, впорядковані за зростанням
    dp = [float('inf')] * (amount + 1)  # Масив для збереження мінімальної кількості монет для кожної суми
    dp[0] = 0  # Базовий випадок: для суми 0 потрібно 0 монет
    coin_used = [-1] * (amount + 1)  # Масив для відновлення шляху вибору монет
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:  # Якщо використання поточної монети дає меншу кількість
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin  # Запам'ятовуємо, яку монету використали
    
    if dp[amount] == float('inf'):
        return {}  # Якщо сума недосяжна, повертаємо порожній словник
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]  # Відновлюємо використані монети
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin  # Зменшуємо залишок суми
    
    return result

# Порівняння продуктивності
amount = 147  # Тестова сума для видачі решти

# Вимірювання часу роботи жадібного алгоритму
start_greedy = time.time()
greedy_result = find_coins_greedy(amount)
end_greedy = time.time()
total_time_greedy = end_greedy - start_greedy

# Вимірювання часу роботи алгоритму динамічного програмування
start_dp = time.time()
dp_result = find_min_coins(amount)
end_dp = time.time()
total_time_dp = end_dp - start_dp

# Вивід результатів у консоль
print("Жадібний алгоритм:", greedy_result, "Час виконання:", total_time_greedy)
print("Динамічне програмування:", dp_result, "Час виконання:", total_time_dp)

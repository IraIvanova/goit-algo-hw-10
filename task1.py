def find_coins_greedy(coins: list, amount: int):
    coins_to_be_used = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            coins_to_be_used[coin] = count
            amount -= count * coin

    return coins_to_be_used


'''
- Створюємо масив change довжиною amount + 1 (щоб можна було звертатись до попередніх значень при обчисленні поточної суми) 
і заповнюємо всі елементи дуже великим значенням (float('inf')), оскільки на початку ми ще не знаємо мінімальну кількість монет для жодної суми.
Виняток - change[0], який дорівнює 0, тому що для суми 0 не потрібно жодної монети.
- Створюємо цикл від 1 до amount, тобто поступово обчислюємо мінімальну кількість монет для кожної суми.
- Всередині циклу перебираємо всі доступні монети coins.
Тобто для кожної поточної суми (1, 2, 3 і т.д.) пробуємо використати кожну монету та знайти найкращу можливу комбінацію.
- Перевіряємо, чи номінал монети менший або дорівнює поточній сумі.
Якщо так, знаходимо попередню суму: current_sum - coin
і беремо вже готове значення з масиву change, тобто мінімальну кількість монет для цієї попередньої суми.
- Далі перевіряємо, чи буде новий варіант кращим: 
чи кількість монет для попередньої суми + 1 поточна монета менша за поточне значення в change[current_sum].
- Якщо новий варіант кращий, оновлюємо значення в масиві change. Таким чином у масиві change завжди зберігається мінімальна кількість монет для кожної суми.
'''


def min_coin_change(coins, amount):
    change = [float('inf')] * (amount + 1)
    used_coin = [0] * (amount + 1)
    change[0] = 0

    for current_sum in range(1, amount + 1):
        for coin in coins:
            if coin <= current_sum:
                previous = change[current_sum - coin]

                if previous + 1 < change[current_sum]:
                    change[current_sum] = previous + 1
                    used_coin[current_sum] = coin

    if change[amount] == float('inf'):
        return {}

    result = {}

    while amount > 0:
        coin = used_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return dict(sorted(result.items()))


if __name__ == '__main__':
    coins_ = [50, 25, 10, 5, 2, 1]
    amount_ = 113
    print("Greedy algorithm: ", find_coins_greedy(coins_, amount_))
    print("Dynamic programming: ", min_coin_change(coins_, amount_))

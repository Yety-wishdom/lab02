def erathos(n):
    # Создаем пустой список для хранения простых чисел
    primes = []
    # Создаем список, заполненный значениями True до n
    sieve = [True] * (n + 1)

    # Для каждого числа от 2 до n
    for p in range(2, n + 1):
        # Если число не отмечено как составное
        if sieve[p] == True:
            # Добавляем его в список простых чисел
            primes.append(p)
            # Отмечаем все кратные p числа как составные
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    return primes

n = 35
result = erathos(n)
print(result)
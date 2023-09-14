def main():
    # Определить номиналы банкнот
    denominations = [64, 32, 16, 8, 4, 2, 1]

    # Попросите пользователя ввести сумму
    amount = int(input("Введите сумму: "))

    # Рассчитать количество банкнот, необходимое для каждого номинала
    counts = []
    for denomination in denominations:
        count = amount // denomination
        counts.append(count)
        amount -= count * denomination

    # Вывод количества банкнот, необходимых для каждого номинала
    for denomination, count in zip(denominations, counts):
        if count > 0:
            print(f"{count} x {denomination}")

if __name__ == "__main__":
    main()
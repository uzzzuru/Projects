def main():
    result = 0

    for i in range(int(input("Введите количество чисел в последовательности: "))):
        number = int(input(f"Введите число №{i + 1}: "))
        if number % 5 == 0 and number > result:
            result = number

    print(f"\nРезультат: {result}")


if __name__ == "__main__":
    main()

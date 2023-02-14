def sequency_summ(n):
    if n == 1:
        return (-1) ** (n + 1) / (2 ** (n - 1))
    return (-1) ** (n + 1) / (2 ** (n - 1)) + sequency_summ(n - 1)


print(sequency_summ(int(input("Enter elements quantity: "))))

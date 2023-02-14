def natural_sequence_summ(n):
    if n <= 1:
        return n
    return n + natural_sequence_summ(n - 1)


n = int(input("Enter elements quantity: "))
print(f"Summ of {n} natural numbers = {natural_sequence_summ(n)} by recursive function "
      f"and {n * (n + 1) / 2} by definition. Recursive function is working correctly: "
      f"{natural_sequence_summ(n) == n * (n + 1) / 2}.")

def recursive_is_even(num, even=0, odd=0):
    if num == 0:
        return f"Quantity of even and odd numbers: {even, odd}"
    else:
        last = num % 10
        if last % 2 == 0:
            even += 1
        else:
            odd += 1
        return recursive_is_even(num // 10, even, odd)


print(recursive_is_even(int(input("Enter number: "))))

import math

reversed_num, num_length = 0, 0


def recursive_reverse_number(num):
    global reversed_num, num_length
    if num > 0:
        current_num = num % 10
        if current_num == 0:
            reversed_num = reversed_num * 10
        else:
            reversed_num = (reversed_num * 10) + current_num
        num_length += 1
        recursive_reverse_number(num // 10)
    return f"Reversed number: {reversed_num:0{num_length}d}"


print(recursive_reverse_number(int(input("Enter number to reverse: "))))

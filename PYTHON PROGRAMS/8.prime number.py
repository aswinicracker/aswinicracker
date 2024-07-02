def prime(x, y):
    prime_list = []
    for i in range(x, y + 1):  # Include y in the range
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# Driver program
starting_range = 0
ending_range = 100
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are:", lst)


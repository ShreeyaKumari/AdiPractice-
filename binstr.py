def split_into_two_balanced_substrings(s):
    total_zeros = s.count('0')
    total_ones = s.count('1')

    if (total_zeros + total_ones) % 2 != 0:
        return -1

    half_zeros, half_ones = total_zeros // 2, total_ones // 2
    count_zeros = count_ones = 0


    for i in range(len(s)):
        if s[i] == '0':
            count_zeros += 1
        else:
            count_ones += 1

        if count_zeros == half_zeros and count_ones == half_ones:
            return s[:i+1], s[i+1:]

    return -1

binary_str = "0010"
result = split_into_two_balanced_substrings(binary_str)

if result == -1:
    print("No possible split with equal 0's and 1's")
else:
    print("Two Balanced Substrings:", result)

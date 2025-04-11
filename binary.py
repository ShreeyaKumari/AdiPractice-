def split_binary_string(s):
    count0 = count1 = 0
    substrings = []
    start = 0

    for i in range(len(s)):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

        if count0 == count1:
            substrings.append(s[start:i+1])
            start = i + 1
            count0 = count1 = 0

    if not substrings:
        return -1
    
    return substrings

binary_str = "0100110101"
result = split_binary_string(binary_str)

if result == -1:
    print("No possible split with equal 0's and 1's")
else:
    print("Balanced Substrings:", result)

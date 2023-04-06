with open('input.txt', 'r') as file:
    k = int(file.readline())
    s = file.readline()
    letters = set(s)
    n = len(s)
    max_beauty = 0
    for letter in letters:
        left = 0
        right = 0
        borrowings = 0
        current_beaty = 0
        while right < n:
            if s[right] != letter:
                borrowings += 1
                while borrowings > k:
                    if s[left] != letter:
                        borrowings -= 1
                    current_beaty -= 1
                    left += 1
            right += 1
            current_beaty += 1
            max_beauty = max(max_beauty, current_beaty)
    print(max_beauty)
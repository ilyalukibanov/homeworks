with open('input.txt', 'r') as file:
    A = file.readline()
    B = file.readline()
    C = file.readline()
    As = int(A[:2])*60*60+int(A[3:5])*60+int(A[6:])
    Bs = int(B[:2])*60*60+int(B[3:5])*60+int(B[6:])
    Cs = int(C[:2])*60*60+int(C[3:5])*60+int(C[6:])
    if As > Cs:
        Cs += 24*60*60 
    time_difference = (Cs-As)
    Bs += time_difference // 2
    Bs += 1 if time_difference % 2 else 0
    Bs %= 24*60*60 
    h = Bs // 3600
    m = (Bs % 3600) // 60
    s = (Bs % 3600) % 60
    print(f'{h:02d}:{m:02d}:{s:02d}')
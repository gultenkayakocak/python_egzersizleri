def üçgen_mi(demet):
    if (abs(demet[0] + demet[1]) > demet[2] and abs(demet[0] + demet[2]) > demet[1] and abs(demet[1] + demet[2]) >
            demet[0]): #abs mutlak değerini alır
        return True
    else:
        return False


liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]

print(list(filter(üçgen_mi, liste)))
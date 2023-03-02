with open("notlar.txt", "r", encoding="utf-8") as file:
    kalan = list()
    gecen = list()
    for satir in file:
        satir = satir[:-1]
        satir_elemanlari = satir.split(" ")
        if (satir_elemanlari[2] == "FF"):
            kalan.append(satir + "\n")
        else:
            gecen.append(satir + "\n")
    with open("gecenler.txt", "w", encoding="utf-8") as file1:
        for i in gecen:
            file1.write(i)

    with open("kalanlar.txt", "w", encoding="utf-8") as file2:
        for i in kalan:
            file2.write(i)
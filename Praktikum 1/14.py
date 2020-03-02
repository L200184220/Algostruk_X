def formatRupiah(x):
    x = str(x)
    y = list(x)
    if len(x) > 9:
        print("tidak boleh lebih dari atau sama dengan 1 miliar")
    if len(x) < 4:
        print("Rp.", x)
    if 3 < len(x) < 7 :
        y.insert(-3,".")
        print("Rp.", end = " ")
        for i in y :
            print(i, end = "")
    if 6 < len(x) < 10 :
        y.insert(-3,".")
        y.insert(-7,".")
        print("Rp.", end = " ")
        for i in y :
            print(i, end = "")

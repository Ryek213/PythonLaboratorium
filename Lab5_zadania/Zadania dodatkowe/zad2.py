def znajdz_max(*args):
    print(args)

    max_w = args[0]
    for i in args:
        max_w = max(max_w, i)

    return max_w


print(znajdz_max(5, 4, 2, 53, 132, -54, 41, -43, -2, 65, 151, 43))

def get_magic_triangle(n):
    magic_traingle = []
    for i in range(n):
        if i < 2:
            magic_traingle.append([1]*(i+1))
        else:
            magic_traingle.append([])
            for y in range(i+1):
                if y == 0 or y == i:
                    magic_traingle[i].append(1)
                else:
                    result = magic_traingle[i-1][y-1] + magic_traingle[i-1][y]
                    magic_traingle[i].append(result)
    return magic_traingle


print(get_magic_triangle(5))
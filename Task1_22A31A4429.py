def strob_num(n):
    result= logic(n, n)
    return result

def logic(n, length):
    if n == 0: 
        return [""]
    if n == 1: 
        return ["1", "0", "8"]
    mids = logic(n - 2, length)
    res = []
    for mid in mids:
        if n != length:
            res.append("0" + mid + "0")
        res.append("8" + mid + "8")
        res.append("1" + mid + "1")
        res.append("9" + mid + "6")
        res.append("6" + mid + "9")
    return res

n=int(input("Enter the N: "))
print(strob_num(n))

def quarters(next_quarter=0.0):
    while True:
        yield next_quarter
        next_quarter += 0.25

def drive():
    rst = list()
    for x in quarters():
        rst.append(x)
        if x >= 1.0:
            break
    return rst

print(drive())
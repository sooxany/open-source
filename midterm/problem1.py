total = 0
T = 100

for k in range(0,T+1):
    total += 1/(((4*k)+1))*((4*k)+3)

res = 8 * total

print(res)
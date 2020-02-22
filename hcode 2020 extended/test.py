t = [1, 1, 22, 3, 4, 5, 5]
print(t[::-1][:3])
print(len(t))

tab=[2, 3, 1, 4, 5]

r = len(tab)

print('before', tab)
for i in range(r):
    swapped = False
    for x in range(1, r-i):
        if tab[x] < tab[x-1]:
            tab[x], tab[x-1] = tab[x-1], tab[x]
            swapped = True
    if swapped == False:
        break

print('after', tab)
# d = {'bejour' : 8, 'bijour' : 9, 'bej' : 16}
# print(d.keys())
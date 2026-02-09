a = {1, 2, 3}
b = {3, 4, 5}
birga = a | b
print(birga)  # {1, 2, 3, 4, 5}


a = {'olma', 'banan', 'shaftoli'}
b = {'banan', 'apelsin', 'shaftoli'}
umumiy = a & b
print(umumiy)  # {'banan', 'shaftoli'}



a = {10, 20, 30, 40}
b = {30, 40}
farq = a - b
print(farq)  # {10, 20}



a = {1,2,3}
b = {3,4,5}
faqat_bittasida = a ^ b
print(faqat_bittasida)  # {1, 2, 4, 5}



kichik = {1, 2}
katta = {1, 2, 3, 4, 5}
ichida = kichik.issubset(katta)
print(ichida)  # True






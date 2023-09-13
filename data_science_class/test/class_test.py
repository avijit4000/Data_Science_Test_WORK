print('Hi')
for i in range(1,11):
    print('2 x',i, "=", (2*i))




print('___________________________')

for j in range(0, 20, 3):
    if j == 15:
        break
    print(j)

print('___________________________')

for j in range(0, 20, 3):
    if j == 15:
        continue
    print(j)

print('___________________________')

for i in range(10):
    if i%2!=0:
        continue
    else:
        print(i)
print('___________________________')
for j in range(1,5):
    for i in range(1,11):
        print(j,'x',i, "=", (j*i))

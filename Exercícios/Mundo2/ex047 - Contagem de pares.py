# forma menos eficiente
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('Acabou')

# forma mais eficiente
for i in range(2, 51, 2):
    print(i, end=' ')
print('Acabou')

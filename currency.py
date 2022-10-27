limit = int(input("Enter the number of coins: "))
coins = []

for i in range(limit):
    coins.append(int(input("Enter the value of coins: ")))

coins.sort()
matrix = []
print(f"The entered coin is: {coins}")
note = int(input("Enter the value of Currency: "))

for i in range(limit):

    a = []
    for j in range(1, note + 1):
        if j % coins[i] == 0:
            a.append(j/coins[i])
        elif j % coins[i] != 0 and i == 0:
            a.append(999)
        elif i > 0:
            if j - coins[i] < 0:
                a.append(matrix[i - 1][j - 1])
            else:
                q = j - coins[i]
                data = a[q] + 1
                mindata = min(data, matrix[i - 1][j - 1])
                a.append(mindata)
    matrix.append(a)

# for i in range(limit):
#     for j in range(note):
#         print(matrix[i][j], end="   ")
#     print("\n")

i = limit - 1
j = note - 1
x = []
while i - j <= 0:
    if (matrix[i][j] - matrix[i - 1][j]) == 0:
        i = i - 1
        if i == 0:
            x.append(coins[i])
            break
    else:
        x.append(coins[i])
        j = j - (coins[i])


y = list(dict.fromkeys(x))

sum = 0
for num in y:
    flag = x.count(num)
    print(f"{flag} * {num}")
    sum = sum + flag

print(f"Minumum number of coin = {sum}")

























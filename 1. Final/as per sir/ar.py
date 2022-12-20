t = input("")
x = [None]*t
y = [[None]*t]*t

for i in range(1, t+1):
    x[i-1] = i;

    for j in range(1, t+1):
        y[i-1][j-1] = j;

print(x)
print(y)

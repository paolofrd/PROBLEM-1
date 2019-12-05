import matplotlib.pyplot as plt
n = 0
y = []
x = list(range(0,90))
for n in range (0,100):
    if n < 9:
        i = (n*n)-7
        y.append(i)
    elif n >= 10:
        while n >= 10:
            n = n-10
            if n < 9:
                i = (n*n)-7
                y.append(i)
plt.stem(x,y,use_line_collection=True)
plt.show()
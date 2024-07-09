import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,6,1)
y1 = x**2
y2 = (x**2)/2

fig = plt.figure()
fig.add_subplot(2,1,1)
plt.ylabel("f(x)")
plt.xlabel("x")
fig.add_subplot(2,1,2)
plt.plot(x,y1,"k:", label="y1")
plt.plot(x,y2,"b-", label="y2")
plt.legend(loc="upper left")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show()

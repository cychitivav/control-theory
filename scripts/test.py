import control as ct
import matplotlib.pyplot as plt
# from control.matlab import *

sys = ct.ss(1, 1, 1, 1)

print(sys)

t, y = ct.step_response(sys)

print(t.shape)

plt.figure()
plt.plot(t,y)
plt.show()
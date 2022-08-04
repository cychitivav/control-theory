import control as ct
import matplotlib.pyplot as plt
# from control.matlab import *

A = [[0, 1], [-2, -10]]
B = [[0], [2]]
C = [1, 0]
D = 0

sys = ct.ss(A,B,C,D)

print(sys)

t, y = ct.step_response(sys)

print(t.shape)

plt.figure(1)
plt.title("Step Response")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.plot(t,y)
plt.grid()
plt.pause(5)
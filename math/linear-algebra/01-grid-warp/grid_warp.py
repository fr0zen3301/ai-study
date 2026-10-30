import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

M = np.array([[1, 3], [-2, 0]])
v = np.array([-1, 2])
n = 6

ax.set_xlim(-n, n)
ax.set_ylim(-n, n)

# vertical lines
for x in range(-n, n + 1):
    ax.plot([x, x], [-n, n], color="lightgray")
    p1 = np.array([x, -n])
    p2 = np.array([x, n])
    q1 = M @ p1
    q2 = M @ p2
    ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color="blue", alpha=0.5, linewidth=1, zorder=3) 

# horizontal lines
for y in range(-n, n + 1):
    ax.plot([-n, n], [y, y], color="lightgray")
    p1 = np.array([-n, y])
    p2 = np.array([n, y])
    q1 = M @ p1
    q2 = M @ p2
    ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color="blue", alpha=0.5, linewidth=1, zorder=3)

ax.set_aspect("equal")

# zorder determines the drawing order of plot elements along the depth axis
ax.quiver(0, 0, *M[:, 0], label="i-hat", angles="xy", scale_units="xy", scale=1, color="green", zorder=4)
ax.quiver(0, 0, *M[:, 1], label="j-hat", angles="xy", scale_units="xy", scale=1, color="red", zorder=4)

# drawing v
ax.quiver(0, 0, *v, label="v", angles="xy", scale_units="xy", scale=1, color="orange", alpha=0.4, zorder=5)
ax.quiver(0, 0, *(M @ v), label="M @ v", angles="xy", scale_units="xy", scale=1, color="orange", zorder=5)

print(v, M @ v)

ax.legend(loc="upper right", bbox_to_anchor=(-0.12, 1))
plt.savefig("grid.png", bbox_inches="tight")

plt.show()

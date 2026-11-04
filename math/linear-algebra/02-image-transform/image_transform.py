import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("black_hole.jpg")
k = 8
img = img[::k, ::k]
h, w = img.shape[:2]

rows, cols = np.indices((h, w))
xs = cols.ravel() - w / 2
ys = h / 2 - rows.ravel()  # rows count down, y counts up
points = np.vstack([xs, ys])
colors = img.reshape(-1, 3) / 255

M = np.array([[0, -1],
              [1,  0]])
moved = M @ points


def draw_grid(ax, A, lim, step=20, **style):
    """Grid lines after applying A. Only each line's two endpoints get
    transformed, which works because linear maps keep lines straight"""
    ticks = np.arange(-step * (lim // step), lim, step)
    far = 3 * lim  # long lines, so shears leave no gaps
    for c in ticks:
        vertical = np.array([[c, c], [-far, far]])  # each column is one endpoint
        horizontal = np.array([[-far, far], [c, c]])
        for line in (vertical, horizontal):
            x, y = A @ line
            ax.plot(x, y, zorder=3, **style)


def draw_basis(ax, A, length=40):
    """Columns of A = where î and ĵ land"""
    for col, color, label in ((0, "lime", r"$\hat{\imath}$"),
                              (1, "blue", r"$\hat{\jmath}$")):
        vx, vy = A[:, col] * length
        ax.annotate("", xy=(vx, vy), xytext=(0, 0), zorder=4,
                    arrowprops=dict(arrowstyle="->", color=color, lw=2.5))
        ax.text(vx * 1.15, vy * 1.15, label, color=color, fontsize=14, zorder=4)


lim = np.abs(np.hstack([points, moved])).max() + 10
I = np.eye(2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
for ax, A, pts, title in ((ax1, I, points, "Before"),
                          (ax2, M, moved, f"After: M = {np.round(M, 2).tolist()}")):
    draw_grid(ax, I, lim, color="gray", lw=0.5, alpha=0.3)
    draw_grid(ax, A, lim, color="tab:blue", lw=0.8, alpha=0.6)
    ax.scatter(pts[0], pts[1], c=colors, s=4, marker="s", zorder=2)
    draw_basis(ax, A)
    ax.set_aspect("equal")
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_title(title)

plt.show()

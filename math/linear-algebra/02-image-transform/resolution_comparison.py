import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

img = plt.imread("black_hole.jpg")
print(img.shape, img.dtype)  # (2160, 3840, 3) uint8

top, bottom, left, right = 1080, 1350, 2304, 2784
crop = img[top:bottom, left:right]

ks = [1, 2, 3]
names = {1: "UHD", 2: "Full HD", 3: "HD"}

fig, axes = plt.subplots(len(ks) + 1, 1, figsize=(10, 24))

# Panel 1: the full image, with a white box showing where the zoom comes from.
axes[0].imshow(img)
axes[0].add_patch(
    Rectangle((left, top), right - left, bottom - top,
              fill=False, edgecolor="white", linewidth=2)
)
axes[0].set_title("Full image (3840×2160), zoom area marked")
axes[0].axis("off")

# Panels 2–4 - each window at its resolution
for ax, k in zip(axes[1:], ks):
    h, w = img[::k, ::k].shape[:2]               # size of the whole image at this k
    ax.imshow(crop[::k, ::k], interpolation="nearest")  # sharp squares, no smoothing
    ax.set_title(f"k={k}: {w}×{h} ({names[k]})")
    ax.axis("off")

fig.tight_layout()
fig.savefig("resolution-comparison.png", bbox_inches="tight", dpi=100)
plt.show()
import os, csv, random
random.seed(42)

os.makedirs("data/raw", exist_ok=True)
path = "data/raw/data.csv"

with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["x", "y"])
    for i in range(100):
        x = i
        y = 2 * x + 1 + random.randint(-3, 3)  # y ≈ 2x+1 + noise kecil
        w.writerow([x, y])

print(f"wrote {path}")
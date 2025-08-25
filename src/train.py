import csv, math, json, os

xs, ys = [], []
with open("data/raw/data.csv") as f:
    r = csv.DictReader(f)
    for row in r:
        xs.append(float(row["x"]))
        ys.append(float(row["y"]))

def pearson(x, y):
    n = len(x)
    mx = sum(x)/n
    my = sum(y)/n
    num = sum((xi-mx)*(yi-my) for xi, yi in zip(x, y))
    den = math.sqrt(sum((xi-mx)**2 for xi in x) * sum((yi-my)**2 for yi in y))
    return num/den if den else 0.0

corr = pearson(xs, ys)

os.makedirs("metrics", exist_ok=True)
with open("metrics/score.json", "w") as f:
    json.dump({"pearson_corr": round(corr, 4)}, f, indent=2)

os.makedirs("models", exist_ok=True)
with open("models/model.txt", "w") as f:
    f.write("y ≈ 2x + 1  # dummy model\n")

print("pearson_corr:", round(corr, 4))
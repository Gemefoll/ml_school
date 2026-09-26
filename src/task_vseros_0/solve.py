import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full", auto_download=["ipynb"])

with app.setup:
    import marimo as mo
    import pandas as pd
    import numpy as np


@app.cell
def _():
    data = pd.read_csv("src/task_vseros_0/items_A.csv")
    dvt = pd.read_csv("src/task_vseros_0/also_viewed_A.csv")
    return data, dvt


@app.cell
def _(data):
    len(data[(data["in_stock"] == 1) & (data["rating"] >= 4.5)])
    return


@app.cell
def _(data):
    data[data["category"] == "laptops"].groupby("brand")["price"].mean()
    return


@app.cell
def _(data):
    len(data[(data["rating"] >= 4.5) & (data["price"] >= 50000) & (data["in_stock"] == 1)])
    return


@app.cell
def _(data, dvt):
    data.loc[dvt["item_to"].unique()].groupby("category")["item_id"].size().rename("cnt").to_csv("src/task_vseros_0/answer4.csv")
    return


@app.cell
def _(data, dvt):
    groups = (np.zeros(500) - 1)
    t = 0
    def dfs(v):
        if groups[v] != -1:
            return
        groups[v] = t
        for i in (np.r_[dvt[dvt["item_from"] == v]["item_to"], dvt[dvt["item_to"] == v]["item_from"]] - 1):
            dfs(i)
    
    for i in range(500):
        if groups[i] == -1:
            dfs(i)
            t += 1
    datac = data.copy()
    datac["cluster_num"] = groups + 1
    len(set(datac[datac["category"] == "phones"]["cluster_num"]) | set(datac[datac["category"] == "accessories"]["cluster_num"]))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    1. 113
    2. Gamma
    3. 25
    4. file
    5. 45
    """)
    return


if __name__ == "__main__":
    app.run()

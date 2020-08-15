import pandas as pd
import os

def load(dataset):
    if dataset == "olympics": 
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "olympics.csv"), index_col=0)
    if dataset == "diamonds": 
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "diamonds.csv"), index_col=0)
    if dataset == "unemployment":
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "unemployment.csv"), 
            index_col=0, parse_dates=True).squeeze().rename("rate")
    raise ValueError(f"There is no {dataset} dataset, please check your spelling")
import pandas as pd
import os

def load(dataset):
    if dataset == "olympics": 
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "olympics.csv"), index_col=0)
    if dataset == "diamonds": 
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "diamonds.csv"), index_col=0)
    if dataset == "S&P500": 
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "S&P500.csv"), 
            index_col=0, parse_dates=True)
    if dataset == "unemployment":
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "unemployment.csv"), 
            index_col=0, parse_dates=True).squeeze().rename("rate")
    if dataset == "electricity":
        return pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "electricity.csv"), 
            index_col=0, parse_dates=True).squeeze().rename("IP")
    raise ValueError(f"There is no {dataset} dataset, please check your spelling")
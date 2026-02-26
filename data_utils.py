import pandas as pd


def load_data():
    # CSV is in the same folder as app.py on GitHub/Streamlit Cloud
    df = pd.read_csv("global_retail_sales.csv")
    return df


def slice_data(df, column, value):
    return df[df[column] == value]


def dice_data(df, filters: dict):
    for col, val in filters.items():
        df = df[df[col] == val]
    return df


def group_and_sum(df, group_col, metric):
    return df.groupby(group_col)[metric].sum().reset_index()


def drill_down(df, year):
    return (
        df[df["year"] == year]
        .groupby("month_name")["revenue"]
        .sum()
        .reset_index()
    )


def compare_years(df, year1, year2):
    y1 = df[df["year"] == year1]["revenue"].sum()
    y2 = df[df["year"] == year2]["revenue"].sum()
    return {
        "year1": float(y1),
        "year2": float(y2),
        "difference": float(y2 - y1),
    }

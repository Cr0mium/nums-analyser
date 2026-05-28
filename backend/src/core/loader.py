import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # basic cleaning
    df.columns = [col.strip().lower() for col in df.columns]

    return df
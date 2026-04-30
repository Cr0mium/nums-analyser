# src/main.py

from core.loader import load_csv
from core.detector import detect_schema


def main():
    df = load_csv("input/data.csv")

    schema = detect_schema(df)

    print("Schema:")
    print(schema)


if __name__ == "__main__":
    main()
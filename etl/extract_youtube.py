import pandas as pd

def extract_youtube_data(file_path):
    df = pd.read_csv(file_path)
    print("Data Sample:")
    print(df.head(3))
    return df

if __name__ == "__main__":
    df = extract_youtube_data("data/USvideos.csv")

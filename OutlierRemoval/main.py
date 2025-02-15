import sys
import pandas as pd
import numpy as np

def remove_outliers_zscore(df, threshold=3):
    """
    Removes outliers from the dataset using the Z-score method.
    Any data point with a Z-score above the threshold is considered an outlier.
    """
    numeric_cols = df.select_dtypes(include=[np.number])  # Select only numeric columns
    z_scores = np.abs((numeric_cols - numeric_cols.mean()) / numeric_cols.std())
    df_no_outliers = df[(z_scores < threshold).all(axis=1)]
    return df_no_outliers

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_csv>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file.replace(".csv", "_new.csv")
    
    try:
        df = pd.read_csv(input_file)
        df_cleaned = remove_outliers_zscore(df)
        df_cleaned.to_csv(output_file, index=False)
        print(f"Outliers removed. Cleaned dataset saved as {output_file}")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()

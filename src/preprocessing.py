import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Cleans the customer data:
    - Drops unneeded columns like CustomerID
    - Handles missing values
    - Scales numerical features
    Returns scaled data and cleaned DataFrame.
    """
    df_cleaned = df.drop(columns=["CustomerID"], errors='ignore')
    df_cleaned = df_cleaned.dropna()

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_cleaned)

    return scaled_data, df_cleaned

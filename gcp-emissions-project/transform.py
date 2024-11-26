import pandas as pd
import numpy as np

def transform_data(df):
    # Add computed columns
    df['formatted_date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['device_type_category'] = np.where(df['device_type'].str.lower().str.contains('phone'), 'Mobile', 'Other')
    df['total_emissions'] = df['media_emissions'] + df['creative_emissions']

    # Drop unwanted columns
    df.drop(['unnecessary_column'], axis=1, inplace=True, errors='ignore')

    return df

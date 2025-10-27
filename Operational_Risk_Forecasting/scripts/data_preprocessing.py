import pandas as pd

def load_and_preprocess(path='../data/operational_risk_data.csv'):
    df = pd.read_csv(path, parse_dates=['Date'])
    df['Loss_Lag1'] = df['Operational_Losses'].shift(1).fillna(0)
    df = pd.get_dummies(df, columns=['Department','Event_Type'], drop_first=True)
    return df

if __name__ == "__main__":
    df = load_and_preprocess()
    df.to_csv('../data/processed_data.csv', index=False)
    print("Data preprocessing complete!")

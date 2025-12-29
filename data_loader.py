import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        df = pd.read_csv(self.path)
        df['order_date'] = pd.to_datetime(df['order_date'])
        return df

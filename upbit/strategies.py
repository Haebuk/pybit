import numpy as np
import pyupbit

class UpbitStrategy:
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.df = pyupbit.get_ohlcv(ticker)

    def volatility(self, k=0.5):
        yesterday = self.df.iloc[-2]
        today = self.df.iloc[-1]
        today_open = today['open']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * k
        return target

    def get_yesterday_ma5(self):
        close = self.df['close']
        ma = close.rolling(5).mean()
        return ma.iloc[-2]

class BackTest(UpbitStrategy):
    def __init__(self, ticker):
        super().__init__(ticker)

    def volatility(self, k=0.5):
        df = self.df.copy()
        df['range'] = (df['high'] - df['low']) * k
        df['target'] = df['open'] + df['range'].shift(1)
        df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
        ror = df['ror'].cumprod()[-2]
        return ror
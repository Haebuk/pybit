import pyupbit
from upbit import upbit_utils, strategies

if __name__ == "__main__":
    upbit = upbit_utils.init_upbit()
    back_test = strategies.BackTest(ticker="KRW-BTC")
    print(back_test.volatility())
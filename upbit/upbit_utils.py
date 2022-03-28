import os
import pyupbit

def init_upbit():
    return pyupbit.Upbit(os.environ["UPBIT_ACCESS_KEY"], os.environ["UPBIT_SECRET_KEY"])
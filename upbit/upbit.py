import pyupbit

def init_upbit(access_key, secret_key):
    return pyupbit.Upbit(access_key, secret_key)
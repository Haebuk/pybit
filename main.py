from upbit import upbit
import config

if __name__ == "__main__":
    upbit = upbit.init_upbit(config.ACCESS_KEY, config.SECRET_KEY)
    print(upbit)
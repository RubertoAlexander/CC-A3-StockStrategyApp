# import talib
import numpy as np
import pandas as pd
import ta

def run(data: dict, buy_rules: str, sell_rules: str):

    STARTING_CAP = 10000
    capital = 10000
    units = 0

    data_df = pd.DataFrame.from_dict(data)
    data_df = ta.utils.dropna(data_df)

    indicators = {}

    rules = buy_rules + sell_rules
    print(rules)
    # data_df["indicators"] = {}
    if "stoch" in rules:
        stoch = ta.momentum.StochasticOscillator(
            data_df["high"], data_df["low"], data_df["close"]
            )
        indicators["stochk"] = stoch.stoch().values
        indicators["stochd"] = stoch.stoch_signal().values

    if "rsi" in rules:
        rsi = ta.momentum.rsi(data_df["close"])
        indicators["rsi"] = rsi.values

    if "sma" in rules:
        sma_50 = ta.trend.SMAIndicator(data_df["close"], 50)
        indicators["sma50"] = sma_50.sma_indicator().values
        sma_20 = ta.trend.SMAIndicator(data_df["close"], 20)
        indicators["sma20"] = sma_20.sma_indicator().values
        print("added sma")

    if "macd" in rules:
        macd = ta.trend.MACD(data_df["close"])
        indicators["macdhist"] = macd.macd_signal().values
        print("added macd")
    
    win_trades = 0; lose_trades = 0; bought_price = 0; num_trades = 0
    for i, price in enumerate(data_df["close"]):

        if price:
            last_price = price

            # Check buys
            for rule in buy_rules.split(","):
                if rule == "stoch": b = stoch_buy(i, indicators["stochk"], indicators["stochd"])
                elif rule == "rsi": b = rsi_buy(i, indicators["rsi"])
                elif rule == "macd": b = macd_buy(i, indicators["macdhist"])
                elif rule == "sma": b = sma_buy(i, indicators["sma20"], indicators["sma50"])

                if b and units == 0:
                    units = buy(price, capital)
                    capital = 0
                    bought_price = price
                    break

            # Check sells
            for rule in sell_rules.split(","):
                if rule == "stoch": s = stoch_sell(i, indicators["stochk"], indicators["stochd"])
                elif rule == "rsi": s = rsi_sell(i, indicators["rsi"])
                elif rule == "macd": s = macd_sell(i, indicators["macdhist"])
                elif rule == "sma": s = sma_sell(i, indicators["sma20"], indicators["sma50"])
                if s and units > 0:
                    capital = sell(price, units)
                    units = 0
                    if price > bought_price: win_trades+=1
                    else: lose_trades +=1
                    num_trades+=1
                    break
    
    if units > 0:
        capital = sell(last_price, units)
        units = 0
        if price > bought_price: win_trades+=1
        else: lose_trades +=1
        num_trades+=1

    if num_trades:
        win_pct = win_trades / num_trades
        lose_pct = lose_trades / num_trades
    else:
        win_pct = 0
        lose_pct = 0

    print("Capital:", capital)
    print("Profit:", (capital - STARTING_CAP) / STARTING_CAP)
    return {
        "profit": (capital - STARTING_CAP) / STARTING_CAP,
        "trades": num_trades,
        "win": win_pct,
        "lose": lose_pct
    }

def buy(price, capital):
    units = capital / price
    return units

def sell(price, units):
    capital = price * units
    return capital

def stoch_buy(i, k, d):
    # if len(k) and len(d):
    if k[i-1] < 20 and d[i-1] < 20:
        if k[i-1] < d[i-1]:
            if k[i] > d[i]:
                return True
    
    return False

def stoch_sell(i, k, d):
    # if len(k) and len(d):
    if k[i-1] > 80 and d[i-1] > 80:
        if k[i-1] > d[i-1]:
            if k[i] < d[i]:
                return True
    
    return False

def rsi_buy(i, r):
    if r[i-1] < 30 and r[i] > 30:
        return True

    return False

def rsi_sell(i, r):
    if r[i-1] > 70 and r[i] < 70:
        return True

    return False

def macd_buy(i, mhist):
    if mhist[i-2] < mhist[i-1] and mhist[i-1] < mhist[i]:
        return True

    return False

def macd_sell(i, mhist):
    if mhist[i-2] > mhist[i-1] and mhist[i-1] > mhist[i]:
        return True
    
    return False

def sma_buy(i, sma20, sma50):
    if sma20[i-1] < sma50[i-1] and sma20[i] > sma50[i]:
        return True
    
    return False

def sma_sell(i, sma20, sma50):
    if sma20[i-1] > sma50[i-1] and sma20[i] < sma50[i]:
        return True
    
    return False
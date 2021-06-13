import talib
import numpy as np

def run(data: dict, buy_rules: str, sell_rules: str):

    STARTING_CAP = 10000
    capital = 10000
    units = 0

    rules = buy_rules + sell_rules
    print(rules)
    data["indicators"] = {}
    if "stoch" in rules:
        data["indicators"]["stochk"], data["indicators"]["stochd"] = talib.STOCH(
            np.array(data["high"], dtype=np.double), np.array(data["low"], dtype=np.double), np.array(data["close"], dtype=np.double)
            )
        print("added stoch")

    if "rsi" in rules:
        data["indicators"]["rsi"] = talib.RSI(
            np.array(data["close"], dtype=np.double)
            )
        print("added rsi")

    if "sma" in rules:
        data["indicators"]["sma50"] = talib.SMA(
            np.array(data["close"], dtype=np.double), 
            timeperiod=50
            )
        data["indicators"]["sma20"] = talib.SMA(
            np.array(data["close"], dtype=np.double), 
            timeperiod=20
            )
        print("added sma")

    if "macd" in rules:
        data["indicators"]["macd"], data["indicators"]["macdsignal"], data["indicators"]["macdhist"] = talib.MACD(
            np.array(data["close"], dtype=np.double)
            )
        print("added macd")
    
    win_trades = 0; lose_trades = 0; bought_price = 0; num_trades = 0
    for i, price in enumerate(data["close"]):

        if price:
            last_price = price

            # Check buys
            for rule in buy_rules.split(","):
                if rule == "stoch": b = stoch_buy(i, data["indicators"]["stochk"], data["indicators"]["stochd"])
                elif rule == "rsi": b = rsi_buy(i, data["indicators"]["rsi"])
                elif rule == "macd": b = macd_buy(i, data["indicators"]["macdhist"])
                elif rule == "sma": b = sma_buy(i, data["indicators"]["sma20"], data["indicators"]["sma50"])

                if b and units == 0:
                    units = buy(price, capital)
                    capital = 0
                    bought_price = price
                    break

            # Check sells
            for rule in sell_rules.split(","):
                if rule == "stoch": s = stoch_sell(i, data["indicators"]["stochk"], data["indicators"]["stochd"])
                elif rule == "rsi": s = rsi_sell(i, data["indicators"]["rsi"])
                elif rule == "macd": s = macd_sell(i, data["indicators"]["macdhist"])
                elif rule == "sma": s = sma_sell(i, data["indicators"]["sma20"], data["indicators"]["sma50"])
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
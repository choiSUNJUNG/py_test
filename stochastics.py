import time
import pyupbit
import datetime
import openpyxl

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_sto(ticker):
    """stochastics 구하기"""
    "%K(14일주기), %D(5_%Ks), %D_Slow(3_%Ds)"
    df = pyupbit.get_ohlcv(ticker, interval="day", count=84)
    df['min_14'] = df['low'].rolling(14).min()
    df['max_14'] = df['high'].rolling(14).max()
    df.min = df['min_14']
    df.max = df['max_14']
    df['sto_K_14'] = (df['close'] - df.min) / (df.max - df.min) * 100   #stochastics_fast의 %K
    df['sto_D_5'] = df['sto_K_14'].rolling(5).mean()    #stochastics_slow의 %K
    df['sto_DS_3'] = df['sto_D_5'].rolling(3).mean()    #stochastics_slow의 %D
    return df

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

def get_daily_gap(ticker):
#     """하루 가격차의 50% 산출"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    # prev_low = df['low'].shift(1)
    df['prev_low'] = df['low'].shift(1)
    df['decision_price'] = df['high'] - ((df['high'] - df['low']) * 0.5) 
    return df


print("autotrade start")
# excel table 생성
wb = openpyxl.Workbook()
wb.save('upbit_deal_data.xlsx')
sheet = wb.active
# cell name : time, cur_pr, high, low, k, ref_pr, prev_low, sell 
# sheet.append(['time', 'cur_price', 'high', 'low', 'k', 'ref_price', 'prev_low', 'buy-sell'])
# wb.save('upbit_deal_data.xlsx')
df = get_sto("KRW-DOGE")
if df.iloc[-1]['sto_D_5'] < 30 and df.iloc[-1]['sto_D_5'] > df.iloc[-1]['sto_DS_3'] :
    print("buy 조건")
else :
    print("wait 조건")

# df.to_excel("dd12.xlsx")

# 자동매매 시작
# print(ma5_1, ma5_2, ma5_3)
# print(ma20_1, ma20_2, ma20_3)
# print(ma60_1, ma60_2, ma60_3)
import yfinance as yf

def get_current_stock_price(symbol):
    try:
        # 삼성전자 주식의 정보를 가져옵니다.
        stock = yf.Ticker(symbol)
        
        # 현재 주가를 가져옵니다.
        current_price = stock.history(period='1d')['Close'][0]
        
        return current_price
    except Exception as e:
        print("Error:", e)
        return None

# 삼성전자의 주식 심볼
samsung_symbol = "005930.KS"

samsung_buy_price = 72800

# 현재 주가를 가져와서 프린트합니다.
current_price = get_current_stock_price(samsung_symbol)

def calculate_difference(a, b):
    difference = abs(a - b)
    return difference

def calculate_difference_rate(a, b):
    rate = (a / b) * 100
    return rate

difference = calculate_difference(current_price, samsung_buy_price)

rate = calculate_difference_rate(difference, samsung_buy_price)


# 숫자를 소수점 셋째 자리에서 반올림하여 출력하는 예시
rounded_rate = round(rate, 2)
##print(rounded_number)  # 10.568 출력

#samsung_answer = numcurrent_price
if current_price is not None:
    print("삼성전자 수익금:", int(difference), "원")
    print("삼성전자 수익률:", rounded_rate, "%")
else:
    print("현재 주가를 가져오는 데 실패했습니다.")

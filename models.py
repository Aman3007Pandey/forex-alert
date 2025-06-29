import requests
import os
from dotenv import load_dotenv
from gmail import send_gmail

load_dotenv()
API_KEY = os.getenv("API_KEY")

class CurrencyPair:
    def __init__(self, symbol: str, lower: float, upper: float):
        self.symbol = symbol
        self.lower = lower
        self.upper = upper

    def fetch_price(self) -> float | None:
        url = f"https://api.twelvedata.com/price?symbol={self.symbol}&apikey={API_KEY}"
        res = requests.get(url).json()
        return float(res['price']) if 'price' in res else None
    
    def fetch_price_all(symbols: list[str]) -> dict:
        print("fetching pirce from twelveDATA API")
        joined = ",".join(symbols)
        url = f"https://api.twelvedata.com/price?symbol={joined}&apikey={API_KEY}"
        res = requests.get(url).json()

        result = {}
        for symbol, data in res.items():
            try:
                result[symbol] = float(data["price"])
            except:
                result[symbol] = None
        return result

    # def check_and_alert(self) -> dict:
    #     price = self.fetch_price()
    #     if price is None:
    #         return {"symbol": self.symbol, "status": "error", "message": "Failed to fetch price"}

    #     if self.lower <= price <= self.upper:
    #         subject = f"💱 Alert: {self.symbol} at {price}"
    #         body = f"{self.symbol} is within your alert range ({self.lower}–{self.upper})"
    #         send_gmail(subject, body)
    #         return {"symbol": self.symbol, "status": "alert_sent", "price": price}
    #     else:
    #         return {"symbol": self.symbol, "status": "no_alert", "price": price}

    def check_and_alert(self,price) -> dict:
        print("reached check & Alert")
        if price is None:
            print("PRICE IS COMING TO BE NONE")
            return f"symbol : ${self.symbol}, status :ERROR"
        
        if self.lower <= price <= self.upper:
            
            body = f"✅ {self.symbol} is within your alert range ({self.lower}–{self.upper}) ,Current Price :{price}"
            return body
        else:
            body = f"❌ {self.symbol} is outside your alert range ({self.lower}–{self.upper} ,Current Price :{price})"
            return body
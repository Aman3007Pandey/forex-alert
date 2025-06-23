from fastapi import FastAPI
from gmail import send_gmail
from config import CURRENCY_PAIRS
from models import CurrencyPair
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

app=FastAPI()

def scheduled_get_all():
    symbols = list(CURRENCY_PAIRS.keys())
    price_map = CurrencyPair.fetch_price_all(symbols)
    results = []
    for symbol, pair in CURRENCY_PAIRS.items():
        price = price_map.get(symbol)
        if price:
            results.append(pair.check_and_alert(price))

    return {" [SCHEDULED] results": results}


scheduler = BackgroundScheduler()
scheduler.add_job(
    scheduled_get_all,
    CronTrigger(minute=30, hour='8-23')  # 8:30, 9:30, ..., 23:30
)
# scheduler.add_job(scheduled_get_all, 'interval', seconds=10)
scheduler.start()
scheduled_get_all()

@app.get("/check")
def check(symbol:str="EUR/USD"):
    pair=CURRENCY_PAIRS.get(symbol)
    if not pair:
        return {"status": "error", "message": f"{symbol} not tracked"}
    return pair.check_and_alert()

@app.get("/check_all")
def check_all():
    results=[ symbol.check_and_alert() for symbol in CURRENCY_PAIRS.values()]
    return {"Results " + results}

@app.get("/get_all")
def get_all():
    symbols = list(CURRENCY_PAIRS.keys())
    price_map = CurrencyPair.fetch_price_all(symbols)
    results = []
    for symbol, pair in CURRENCY_PAIRS.items():
        price = price_map.get(symbol)
        if price:
            results.append(pair.check_and_alert(price))

    return {"results": results}

    
if __name__ == "__main__":
    
    try:
        while True:
            time.sleep(58)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


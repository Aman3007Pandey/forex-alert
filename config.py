from models import CurrencyPair
from models import CurrencyPair_V2
CURRENCY_PAIRS = {
   
    "AUD/USD": CurrencyPair("AUD/USD", 0.65340, 0.65475),
    "USD/CAD": CurrencyPair("USD/CAD", 1.3803, 1.3837),
    "EUR/USD": CurrencyPair("EUR/USD", 1.16315, 1.16400),
    "GBP/USD": CurrencyPair("GBP/USD", 1.36000, 1.36313),
    "CAD/JPY": CurrencyPair("CAD/JPY", 105.626, 105.726),
    "EUR/GBP": CurrencyPair("EUR/GBP", 1.2500, 1.2600),
    "EUR/CHF": CurrencyPair("EUR/CHF", 0.92800, 0.93200),
    "EUR/JPY": CurrencyPair("EUR/JPY", 1.2500, 1.2600),
    "GBP/JPY": CurrencyPair("GBP/JPY", 198.918, 199.765),
    "EUR/CAD": CurrencyPair("EUR/CAD", 1.2500, 1.2600),
    "USD/CHF": CurrencyPair("USD/CHF", 1.2500, 1.2600),
    "USD/JPY": CurrencyPair("USD/JPY", 1.2500, 1.2600)
}

CURRENCY_PAIRS_V2 = {
    "USD/CAD": CurrencyPair_V2("USD/CAD",[[1.38036,1.38378],[1.35922,1.36264]]),
    "GBP/USD": CurrencyPair_V2("GBP/USD", [[1.35249, 1.35983],[1.33508,1.34093],[1.31174,1.31708],[1.27865,1.28399]]),
    "USD/JPY": CurrencyPair_V2("USD/JPY", [[150.119,150.939],[141.759,142.579],[136.363,137.182],[156.090,156.910]]),
    "CAD/JPY": CurrencyPair_V2("CAD/JPY", [[108.828,109.573],[105.398,105.856],[104.082,104.363],[102.051,102.798]])
}
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
    "CAD/JPY": CurrencyPair_V2("CAD/JPY", [[108.828,109.573],[105.398,105.856],[104.082,104.363],[102.051,102.798]]),
    "AUD/USD": CurrencyPair_V2("AUD/USD", [[0.64025,0.64560],[0.66507,0.66789],[0.68431,0.68818]]),
    "GBP/JPY": CurrencyPair_V2("GBP/JPY", [[196.044,196.815],[190.997,191.768],[186.231,187.352]]),
    "EUR/USD": CurrencyPair_V2("EUR/USD", [[1.04507,1.05092],[1.06878,1.07463],[1.09650,1.10235],[1.11713,1.12298],[1.13869,1.14454],[1.16762,1.17347]]),
    "EUR/GBP": CurrencyPair_V2("EUR/GBP", [[0.83026,0.83213],[0.84143,0.84337],[0.85156,0.85350],[0.86405,0.86592],[0.86927,0.87121]])
    
}
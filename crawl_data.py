import yfinance as yf

tickers = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        tickers.append(line.strip())

for i, ticker in enumerate(tickers):
    ticker_company = yf.Ticker(ticker)
    df = ticker_company.history(period='max', interval='1d')
    if df.shape[0] > 0:
        df.to_csv('data/{}.csv'.format(ticker))


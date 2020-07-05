import zipline
from zipline.api import order, record, symbol
import pandas as pd


def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 1)
    record(AAPL=data.current(symbol('AAPL'), 'price'))

df = pd.read_csv('AAPL.csv',index_col=['Date'])
df.index = pd.to_datetime(df.index)
data = df[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

# 실행
result = zipline.run_algorithm(start=data.index[0], end=data.index[-1], initialize=initialize, capital_base=1000,
                               handle_data=handle_data, data=data)

import matplotlib.pyplot as plt
ax1 = plt.subplot(211)
result.portfolio_value.plot(ax=ax1)
ax1.set_ylabel('Portfolio Value')
ax2 = plt.subplot(212, sharex=ax1)
result.AAPL.plot(ax=ax2)
ax2.set_ylabel('AAPL Stock Price')
#
# import pyfolio as pf
# backtest_df = result.copy()
# returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(backtest_df)
#
# # pf.create_returns_tear_sheet(result['returns'])
# pf.create_full_tear_sheet(returns=returns.fillna(0), positions=positions,
#                           transactions=transactions,
#                           benchmark_rets=None)
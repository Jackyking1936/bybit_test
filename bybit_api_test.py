#%% session establish
from pybit.unified_trading import HTTP
session = HTTP(testnet=True)

#%% 取得公告
print(session.get_announcement(
    locale="zh-TW",
    limit=1,
))

# %% Get Server Time
print(session.get_server_time())

# %% Get Kline
print(session.get_kline(
    category="inverse",
    symbol="BTCUSD",
    interval=60,
    start=1670601600000,
    end=1670608800000,
))
# %%

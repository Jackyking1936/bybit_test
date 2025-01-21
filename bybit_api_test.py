#%%
from pybit.unified_trading import HTTP
session = HTTP(testnet=True)
print(session.get_announcement(
    locale="en-US",
    limit=1,
))
# %%

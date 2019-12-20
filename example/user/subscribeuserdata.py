import logging
from binance import RequestClient
from binance import SubscriptionClient
from binance.constant.test import *
from binance.model import *
from binance.exception.binanceapiexception import BinanceApiException

from binance.base.printobject import *

# Start user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
listen_key = request_client.start_user_data_stream(accountType=AccountType.SPOT)
# result = request_client.start_user_data_stream(accountType=AccountType.MARGIN)
print("listenKey: ", listen_key)

# Keep user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.keep_user_data_stream(accountType=AccountType.SPOT, listenKey=listen_key)
# result = request_client.keep_user_data_stream(accountType=AccountType.MARGIN, listenKey=listen_key)
print("Result: ", result)

# logger = logging.getLogger("binance-client")
# logger.setLevel(level=logging.INFO)
# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(handler)

# sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


# def callback(data_type: 'SubscribeMessageType', event: 'any'):
#     if data_type == SubscribeMessageType.RESPONSE:
#         print("Event ID: ", event)
#     elif  data_type == SubscribeMessageType.PAYLOAD:
#         PrintBasic.print_obj(event)
#         sub_client.unsubscribe_all()
#     else:
#         print("Unknown Data:")
#     print()


# def error(e: 'BinanceApiException'):
#     print(e.error_code + e.error_message)

# sub_client.subscribe_user_data_event("btcusdt", callback, error)
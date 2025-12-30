#!/usr/bin/env python3
"""
Quick reproduction script - triggers the error in ~10 seconds.
"""

import sys
import time
import logging
from pathlib import Path

sdk_path = Path(__file__).parent / "lib/v3-bitget-api-sdk/bitget-python-sdk-api"
sys.path.insert(0, str(sdk_path))

from bitget.ws.bitget_ws_client import BitgetWsClient
import bitget.utils as c

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

print("Creating WebSocket connection...")
client = BitgetWsClient(c.contract_ws_url, need_login=False).build()

print("Waiting 3 seconds...")
time.sleep(3)

print("Closing WebSocket (but __keep_connected timer still running)...")
client.close()

print("Waiting 60 seconds for __keep_connected to fire...")
print("Watch for 'Connection is already closed' error:\n")
time.sleep(60)

print("\n✓ If you saw the error above, the issue is reproduced!")

#!/usr/bin/env python3

import time
from datetime import datetime
from typing import Union

import pynng
from proto import sidepit_api_pb2
from constants import PROTOCOL, ADDRESS, CLIENT_PORT
from sidepit_nng_client import SidepitClient

from dotenv import load_dotenv
import os




def main() -> None:

    load_dotenv()
    sidepit_id = os.getenv("SIDEPIT-ID")
    secret_key = os.getenv("SIDEPIT-SECRET")


    server_address = f"{PROTOCOL}{ADDRESS}:{CLIENT_PORT}"
    client = SidepitClient(server_address)

    print(f"Connected to server at {server_address}")

    # Example usage
    orderid=client.send_new_order(
        side=-1,
        size=1,
        price=1000,
        ticker="USDBTCH25",
        user_id=sidepit_id,
        wif=secret_key,
    )

    print(f"Sent new order with order id: {orderid}")

    cancelorderid=client.send_cancel_order(
        order_id=orderid,
        user_id=sidepit_id,
        wif=secret_key,
    )

    print(f"Sent cancel order with order id: {cancelorderid}")
    # client.send_auction_bid(
    #     epoch=1234567890,
    #     hash_value="hash_value",
    #     ordering_salt="ordering_salt_value",
    #     bid=500,
    #     user_id=b"user_id",
    #     wif=secret_key,
    # )

    print("Sent new order")

    client.close_connection()


if __name__ == "__main__":
    main()
from solana.rpc.async_api import AsyncClient


import os

from local_server.config import settings

def connect_solana(): 
    network_rpc = settings.SOLANA_RPC
    solana_client = AsyncClient(network_rpc)
    return solana_client


solana_client = connect_solana()
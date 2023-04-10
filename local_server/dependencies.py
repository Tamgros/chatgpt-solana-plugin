from solana.rpc.async_api import AsyncClient


import os

from local_server.main import settings

def connect_solana(): 
    network_rpc = settings.SOLANA_RPC
    solana_client = AsyncClient(network_rpc)
    return solana_client



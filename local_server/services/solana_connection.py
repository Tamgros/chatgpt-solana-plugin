from solana.rpc.async_api import AsyncClient

import os

from config import Settings

# from src.chatgpt_plugin.app.config import DevelopmentConfig, ProductionConfig, TestingConfig

def connect_solana(config): 
    network_rpc = Settings().SOLANA_RPC
    solana_client = AsyncClient(network_rpc)
    return solana_client

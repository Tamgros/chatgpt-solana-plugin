from fastapi import APIRouter, Depends
from pydantic import BaseModel, validator
from local_server.dependencies import solana_client
from typing import Annotated, Any, List
from nacl.signing import VerifyKey  
from solders.pubkey import Pubkey
import json

class LatestBlockhash(BaseModel):
    latest_blockhash: str

router = APIRouter(
    prefix="/solana",
    tags=["solana"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get('/get_latest_blockhash')
async def get_latest_blockhash() -> LatestBlockhash:
    """Gets the latest blockhash

    The Solana blockchain uses latest blockhash to prevent duplicate transcations. 
    """
    async with solana_client as client:
        recent_blockhash = await client.get_latest_blockhash()
        print(recent_blockhash.value.blockhash)
        return {"latest_blockhash": f'{recent_blockhash.value.blockhash}'}

class PublicKey(BaseModel):
    pk: Annotated[str, "this is a E"]

    # @validator("pk")
    # @classmethod
    # def check_pk(cls, value):
    #     if not VerifyKey(value):
    #         raise ValueError("Not a valid public key.")
    #     return value

class AccountInfo(BaseModel):
    lamports: int | None
    owner: Any | None
    data: Any
    executable: bool | None
    rentEpoch: int| None


@router.post('/get_account_info')
async def get_accoung_info(
    account: Annotated[PublicKey, "this is the account public key"]
    # ):
    ) -> Annotated[AccountInfo, "this is the account info"]:
    """Gets the latest account info for a provided public key

    The Solana blockchain stores data into accounts associated with cryptographic public keys 
    """

    resp =  await solana_client.get_account_info_json_parsed(Pubkey.from_string(account.pk))


    resp_dict = json.loads(resp.value.to_json())

    return resp_dict



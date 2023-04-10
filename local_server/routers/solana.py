from fastapi import APIRouter, Depends
from local_server.dependencies import solana_client

# solana_client = connect_solana()

router = APIRouter(
    prefix="/solana",
    tags=["solana"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get('/get_latest_blockhash')
async def get_latest_blockhash():
    """Gets the latest blockhash

    The Solana blockchain uses latest blockhash to prevent duplicate transcations. 
    """
    async with solana_client as client:
        recent_blockhash = await client.get_latest_blockhash()
        print(recent_blockhash.value.blockhash)
        return jsonify({"latest_blockhash": f'{recent_blockhash.value.blockhash}'})
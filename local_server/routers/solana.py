from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/solana",
    tags=["solana"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
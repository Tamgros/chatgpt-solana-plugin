from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Echo(BaseModel):
    hello: str | None = None

class EchoOut(BaseModel):
    input: str | None
    extra: bool | None = True


@router.post("/echo")
async def echo(data: Echo) -> EchoOut:
    """_summary_

    Returns:
        _type_: _description_
    """
    # data = await request.get_json()
    print(data)
    return {"input": data, "extra": True}
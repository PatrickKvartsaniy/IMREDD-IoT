from pydantic import BaseModel


class SecurityData(BaseModel):
    value: int

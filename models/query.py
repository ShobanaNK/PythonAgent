from pydantic import BaseModel, Field

class Query(BaseModel):
    userid: str = Field(pattern=r'^[A-Za-z0-9]+$', description="Unique userid")
    usermessage: str = Field(alias='query')
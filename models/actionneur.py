from pydantic import BaseModel, Field, ConfigDict
from typeActionneur import TypeActionneur


class Actionneur(BaseModel):
    id: int
    typeActionneur: TypeActionneur
    actif: bool

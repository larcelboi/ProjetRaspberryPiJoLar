from pydantic import BaseModel, Field, ConfigDict
from typeCapteur import TypeCapteur


class Capteur(BaseModel):
    id: int
    typeCapteur: TypeCapteur
    valeur: float

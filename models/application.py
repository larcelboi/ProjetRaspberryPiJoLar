from pydantic import BaseModel, Field, ConfigDict


class Application(BaseModel):
    seuilTemperature: float
    seuilCO2: float

    def activerVentilateur():
        pass

    def desactiverVentilateur():
        pass

    def modifierSeuilTemperature():
        pass

    def modifierSeuilCO2():
        pass

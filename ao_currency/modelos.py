from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class MoedaModel(BaseModel):
    """Modelo Pydantic para representar a moeda angolana."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    valor: Decimal = Field(..., description="Valor monetário em Decimal")
    simbolo: str = Field(default="Kz", description="Símbolo da moeda")
    iso: str = Field(default="AOA", description="Código ISO da moeda")
    
    @property
    def inteiro(self) -> int:
        return int(self.valor)
    
    @property
    def centavos(self) -> int:
        return int(round((self.valor - self.inteiro) * 100))

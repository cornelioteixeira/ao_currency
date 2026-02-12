from decimal import Decimal
from typing import Union
from .modelos import MoedaModel
from .sanitizador import SanitizadorMoeda
from .formatador import FormatadorMoeda
from .extenso import ExtensoMotor

class AngolaMoeda:
    """Classe principal de interface para desenvolvedores (Developer Friendly)."""
    
    def __init__(self, valor: Union[str, int, float, Decimal] = 0):
        valor_sanitizado = SanitizadorMoeda.sanitizar(valor)
        self._model = MoedaModel(valor=valor_sanitizado)

    @property
    def valor(self) -> Decimal:
        return self._model.valor

    @property
    def valor_formatado(self) -> str:
        """Retorna apenas o valor numérico com separadores de milhares (ex: 1.500,00)."""
        return self.formatar(incluir_simbolo=False)

    def formatar(self, usar_iso: bool = False, incluir_simbolo: bool = True) -> str:
        """Retorna o valor formatado como string (ex: 1.500,00 Kz)."""
        return FormatadorMoeda.formatar(
            valor=self._model.valor,
            iso=self._model.iso,
            simbolo=self._model.simbolo,
            usar_iso=usar_iso,
            incluir_simbolo=incluir_simbolo
        )

    def por_extenso(self) -> str:
        """Retorna o valor por extenso."""
        return ExtensoMotor.para_extenso(self._model.valor)

    @classmethod
    def de_extenso(cls, texto: str) -> 'AngolaMoeda':
        """Cria uma instância a partir de um texto por extenso."""
        valor = ExtensoMotor.extenso_para_numero(texto)
        return cls(valor)

    def __str__(self):
        return self.formatar()

    def __repr__(self):
        return f"<AngolaMoeda(valor={self._model.valor})>"

from decimal import Decimal, ROUND_HALF_UP

class FormatadorMoeda:
    """Motor para formatação de moeda seguindo o padrão bancário de Angola."""
    
    @staticmethod
    def formatar(valor: Decimal, iso: str = "AOA", simbolo: str = "Kz", usar_iso: bool = False, incluir_simbolo: bool = True) -> str:
        """
        Formata o valor para o padrão: 1.500,00 Kz ou 1.500,00 AOA
        """
        d = valor.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
        
        # Formata com vírgula para milhar e ponto para decimal temporariamente
        formatted = f"{d:,.2f}"
        
        # Troca para o padrão angolano (Ponto para milhar, vírgula para decimal)
        # 1,500.00 -> 1.500,00
        formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")
        
        if not incluir_simbolo:
            return formatted
            
        sufixo = iso if usar_iso else simbolo
        return f"{formatted} {sufixo}"

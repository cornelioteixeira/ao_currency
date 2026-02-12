import re
from decimal import Decimal, ROUND_HALF_UP

class SanitizadorMoeda:
    """Motor de Regex para limpar e normalizar entradas de valor monetário."""
    
    @staticmethod
    def sanitizar(valor) -> Decimal:
        """
        Limpa inputs sujos e converte para Decimal.
        Ex: 'Kz 1.500,50' -> Decimal('1500.50')
        """
        if isinstance(valor, (int, float, Decimal)):
            return Decimal(str(valor))
        
        if not isinstance(valor, str):
            raise ValueError(f"Tipo de entrada inválido: {type(valor)}")
            
        # Remove símbolos, espaços e letras (exceto pontos e vírgulas)
        clean_str = re.sub(r'[^\d.,]', '', valor)
        
        if not clean_str:
            return Decimal("0.00")
        
        # Lógica de detecção de formato (Europeu vs Americano)
        if ',' in clean_str and '.' in clean_str:
            # Caso tenha ambos, verificamos qual vem depois para definir o separador decimal
            if clean_str.find('.') < clean_str.find(','): # 1.000,00 -> 1000.00
                clean_str = clean_str.replace('.', '').replace(',', '.')
            else: # 1,000.00 -> 1000.00
                clean_str = clean_str.replace(',', '')
        elif ',' in clean_str:
            # Caso tenha apenas vírgula, assumimos que é o separador decimal (1000,00)
            # A menos que seja algo como 1,000 (sem casas decimais) - mas em Angola , é decimal
            clean_str = clean_str.replace(',', '.')
            
        try:
            return Decimal(clean_str)
        except Exception as e:
            raise ValueError(f"Não foi possível converter '{valor}' em um valor numérico válido.") from e

from decimal import Decimal
from num2words import num2words

class ExtensoMotor:
    """Motor para conversão de números para extenso e vice-versa."""
    
    UNIDADES = {
        'zero': 0, 'um': 1, 'uma': 1, 'dois': 2, 'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
        'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10, 'onze': 11, 'doze': 12,
        'treze': 13, 'catorze': 14, 'quinze': 15, 'dezasseis': 16, 'dezassete': 17,
        'dezoito': 18, 'dezanove': 19, 'vinte': 20, 'trinta': 30, 'quarenta': 40,
        'cinquenta': 50, 'sessenta': 60, 'setenta': 70, 'oitenta': 80, 'noventa': 90,
        'cem': 100, 'cento': 100, 'duzentos': 200, 'trezentos': 300, 'quatrocentos': 400,
        'quinhentos': 500, 'seiscentos': 600, 'setecentos': 700, 'oitocentos': 800, 'novecentos': 900
    }
    
    MULTIPLICADORES = {
        'mil': 1000, 
        'milhão': 1000000, 'milhões': 1000000, 
        'bilhão': 1000000000, 'bilhões': 1000000000
    }

    @staticmethod
    def para_extenso(valor: Decimal) -> str:
        """Converte um número Decimal para extenso no padrão Angolano."""
        inteiro = int(valor)
        centavos = int(round((valor - inteiro) * 100))
        
        txt_int = num2words(inteiro, lang='pt')
        label_int = "Kwanza" if inteiro == 1 else "Kwanzas"
        res = f"{txt_int} {label_int}"
        
        if centavos > 0:
            txt_cent = num2words(centavos, lang='pt')
            label_cent = "cêntimo" if centavos == 1 else "cêntimos"
            res += f" e {txt_cent} {label_cent}"
        
        return res.capitalize()

    @staticmethod
    def extenso_para_numero(texto: str) -> Decimal:
        """
        Converte texto por extenso para um número Decimal.
        Lógica baseada em tokens.
        """
        texto = texto.lower().replace(' e ', ' ').replace('kwanzas', '').replace('kwanza', '').replace('cêntimos', '').replace('cêntimo', '').strip()
        
        # Simplificação: se houver vírgula ou 'e' para centavos, tratamos apenas a parte inteira por agora
        # para manter a robustez no processamento básico pedido.
        partes = texto.split()
        total = 0
        corrente = 0
        
        for p in partes:
            if p in ExtensoMotor.UNIDADES:
                corrente += ExtensoMotor.UNIDADES[p]
            elif p in ExtensoMotor.MULTIPLICADORES:
                if corrente == 0: corrente = 1
                total += corrente * ExtensoMotor.MULTIPLICADORES[p]
                corrente = 0
        
        return Decimal(str(total + corrente))

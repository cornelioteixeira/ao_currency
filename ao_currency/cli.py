import argparse
import sys
from .moeda import AngolaMoeda

def main():
    parser = argparse.ArgumentParser(
        description="CLI para manipulação de Moeda Angolana (Kwanza).",
        prog="ao-currency"
    )
    
    parser.add_argument(
        "valor",
        help="O valor a ser processado (ex: '2.500,50', '1000' ou extenso 'mil kwanzas')"
    )
    
    parser.add_argument(
        "-f", "--formatar",
        action="store_true",
        help="Formata o valor para o padrão bancário angolano"
    )
    
    parser.add_argument(
        "-e", "--extenso",
        action="store_true",
        help="Converte o valor para extenso"
    )
    
    parser.add_argument(
        "-n", "--numero",
        action="store_true",
        help="Mostra apenas o número com separadores de milhares"
    )
    
    parser.add_argument(
        "--iso",
        action="store_true",
        help="Usa o código ISO (AOA) em vez do símbolo (Kz)"
    )
    
    args = parser.parse_args()
    
    try:
        # Tenta detectar se é extenso primeiro se contiver letras
        if any(c.isalpha() for c in args.valor) and "kwanzas" in args.valor.lower():
            moeda = AngolaMoeda.de_extenso(args.valor)
        else:
            moeda = AngolaMoeda(args.valor)
            
        if args.extenso:
            print(moeda.por_extenso())
        elif args.numero:
            print(moeda.valor_formatado)
        elif args.formatar:
            print(moeda.formatar(usar_iso=args.iso))
        else:
            # Padrão: mostra tudo um pouco
            print(f"Valor: {moeda.valor_formatado}")
            print(f"Formatado: {moeda.formatar(usar_iso=args.iso)}")
            print(f"Extenso: {moeda.por_extenso()}")
            
    except Exception as e:
        print(f"Erro: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

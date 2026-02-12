# ao-currency-pro

Biblioteca profissional para manipulação de Moeda Angolana (Kwanza).

## CLI Interface

A biblioteca inclui uma ferramenta de linha de comando:

```bash
# Formatação rápida
python3 -m ao_currency.cli "1500,50" --formatar

# Conversão para extenso
python3 -m ao_currency.cli "2500000" --extenso

# Conversão inversa (Extenso para Número)
python3 -m ao_currency.cli "Dois milhões de kwanzas" --numero
```

## Instalação
```bash
pip install .
```

## Como usar

```python
from ao_currency import AngolaMoeda

# Criar a partir de string suja
moeda = AngolaMoeda(" Kz 1.250,50 ")

# Formatação
print(moeda.formatar())          # 1.250,50 Kz
print(moeda.formatar(usar_iso=True)) # 1.250,50 AOA

# Extenso
print(moeda.por_extenso())        # Um mil duzentos e cinquenta kwanzas e cinquenta cêntimos

# Criar a partir de extenso
moeda_v2 = AngolaMoeda.de_extenso("Mil quinhentos kwanzas")
print(moeda_v2.valor)             # 1500.00
```

## Funcionalidades
- **Sanitizador:** Limpa qualquer entrada (Excel, formatado AGT, string bruta).
- **Formatador:** Segue o padrão bancário angolano.
- **Motores Modularizados:** Fácil de estender e manter.
- **Tipagem Forte:** Usa Pydantic e Decimal para precisão financeira.

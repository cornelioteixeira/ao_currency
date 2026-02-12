---
sidebar_position: 3
---

# Uso Básico

Aprenda a utilizar os motores principais da biblioteca.

## A Classe `AngolaMoeda`

Esta é a interface principal "developer friendly".

```python
from ao_currency import AngolaMoeda

# Criando instâncias de diversas formas
m1 = AngolaMoeda("Kz 1.500,50")
m2 = AngolaMoeda(2500)
m3 = AngolaMoeda.de_extenso("Dois mil kwanzas")

# Exibição
print(m1.formatar()) # 1.500,50 Kz
print(m3.valor)      # 2000.00
```

## Formatação

Você pode controlar prefixos e códigos ISO.

```python
moeda = AngolaMoeda(1250)

print(moeda.formatar())                  # 1.250,00 Kz
print(moeda.formatar(usar_iso=True))      # 1.250,00 AOA
print(moeda.valor_formatado)              # 1.250,00
```

## Conversão para Extenso

```python
moeda = AngolaMoeda(2500000.50)
print(moeda.por_extenso()) 
# Dois milhões e quinhentos mil kwanzas e cinquenta cêntimos
```

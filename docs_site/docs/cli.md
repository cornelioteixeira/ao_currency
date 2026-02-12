---
sidebar_position: 4
---

# Interface de Linha de Comando (CLI)

A `ao-currency-pro` vem com uma CLI poderosa para manipulação rápida via terminal.

## Uso Básico

Se você instalou a lib via pip, o comando `ao-currency` estará disponível globalmente. Caso contrário, use `python3 -m ao_currency.cli`.

```bash
ao-currency "1.500,50"
```

## Opções Disponíveis

| Flag | Descrição |
| :--- | :--- |
| `-f, --formatar` | Retorna o valor formatado (ex: 1.500,00 Kz) |
| `-e, --extenso` | Retorna o valor por extenso |
| `-n, --numero` | Retorna apenas o número com separadores |
| `--iso` | Usa 'AOA' em vez de 'Kz' na formatação |

## Exemplos Reais

### Formatação Rápida
```bash
ao-currency "2500" --formatar
# Saída: 2.500,00 Kz
```

### De Extenso para Número
```bash
ao-currency "Cinco milhões de kwanzas" --numero
# Saída: 5.000.000,00
```

### Combo de Informações
Se nenhum flag for passado, a CLI exibe um resumo:
```bash
ao-currency "3.500,75"
```

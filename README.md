# SAMPA Configurator

<!--toc:start-->
- [SAMPA Configurator](#sampa-configurator)
  - [**O projeto ainda está em fase de desenvolvimento**](#o-projeto-ainda-está-em-fase-de-desenvolvimento)
  - [Instalação](#instalação)
  - [Utilizando](#utilizando)
<!--toc:end-->

## **O projeto ainda está em fase de desenvolvimento**

## Instalação

Para o desenvolvimento e gerenciamento do projeto utilizamos [Poetry](https://python-poetry.org).

Para instalar Poetry utilize:

```shell
pipx install poetry
```

Depois, para instalar as dependências, no mesmo diretório onde clonou este repositório,
utilize:

```shell
poetry install
```

## Utilizando

Na mesma pasta em que está o arquivo rode:

```shell
poetry shell
```

Depois, utilize as funções do sampaconfigurator.

## Ler um registrador específico da FPGA

Utilize a função fpga-read

```shell
sampaconfigurator fpga-read --port [PORT] --address [ADDRESS]
```

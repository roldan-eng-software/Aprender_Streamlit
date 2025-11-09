# Aprender Streamlit

Repositório de estudo e demonstrações com Streamlit. Contém uma página principal (`Hello.py`) e várias páginas de demonstração dentro da pasta `pages/`.

## Visão geral

Este projeto serve como um _playground_ para demonstrar recursos do Streamlit (plotagens, mapas, DataFrames, etc.).

- Página principal: `Hello.py` (conteúdo de boas-vindas e navegação)
- Páginas de demonstração: `pages/1_📈_Plotting_Demo.py`, `pages/2_🌍_Mapping_Demo.py`, `pages/3_📊_DataFrame_Demo.py`
- Dependências listadas em `requirements.txt`

## Pré-requisitos

- Git
- Python 3.10+ (recomendado). Este projeto foi testado com Python 3.13 no ambiente local.
- Acesso à internet para baixar pacotes e, em algumas demos, dados remotos.

## Passos para configurar (rápido)

1. Clone o repositório:

```bash
git clone https://github.com/roldan-eng-software/Aprender_Streamlit.git
cd Aprender_Streamlit
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
# criar venv (padrão: venv)
python -m venv venv

# ativar (Linux/macOS)
source venv/bin/activate

# ativar (Windows PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Instale as dependências listadas:

```bash
pip install -r requirements.txt
```

4. Verifique as versões instaladas (opcional):

```bash
python -c "import pandas as pd, numpy as np, streamlit as st; print('pandas', pd.__version__); print('numpy', np.__version__); print('streamlit', st.__version__)"
```

## Como executar o projeto

Você tem duas opções comuns:

- Rodar a página principal `Hello.py` (recomendado para navegar pelas demos):

```bash
streamlit run Hello.py
```

- Rodar o `app.py` (caso exista e você prefira uma entrada única):

```bash
streamlit run app.py
```

Depois de iniciar, abra o navegador no endereço mostrado (por padrão `http://localhost:8501`).

## Navegação entre páginas

Este repositório usa a pasta padrão `pages/` do Streamlit para páginas secundárias. A página principal `Hello.py` também inclui um painel lateral com botões que descobrem automaticamente os arquivos na pasta `pages/` e permitem navegar entre as demos.

Observações:
- Cada arquivo em `pages/` pode definir `st.set_page_config(page_title=..., page_icon=...)` para controlar o título mostrado.
- Se a navegação não aparecer, verifique se os arquivos `.py` estão dentro da pasta `pages/` e se o Streamlit está sendo executado a partir do diretório raiz do projeto.

## Como adicionar dependências

1. Instale o pacote no ambiente virtual:

```bash
pip install nome-do-pacote
```

2. Atualize o `requirements.txt` com as versões instaladas (recomendado):

```bash
pip freeze | grep -E "streamlit|pandas|numpy|pydeck|altair" > requirements.txt
# ou para atualizar manualmente, edite requirements.txt
```

3. Commit e push das mudanças:

```bash
git add requirements.txt
git commit -m "chore: atualizar requirements"
git push
```

## Desenvolvimento local (boas práticas)

- Sempre ative o `venv` antes de instalar pacotes ou executar o Streamlit.
- Use commits pequenos e mensagens claras.
- Mantenha `requirements.txt` atualizada para que outros possam replicar o ambiente.

## Testes rápidos

- Certifique-se de que o Streamlit abre e as páginas em `pages/` são acessíveis.

```bash
streamlit run Hello.py
# ou
streamlit run pages/1_📈_Plotting_Demo.py
```

## Fluxo Git / GitHub

1. Crie branchs para funcionalidades quando necessário:

```bash
git checkout -b feature/minha-nova-demo
```

2. Após implementar, commit e push:

```bash
git add .
git commit -m "feat: adicionar demo X"
git push --set-upstream origin feature/minha-nova-demo
```

3. Abra um Pull Request no GitHub e faça revisão antes de mesclar no `main`.

## Integração contínua (opcional)

Sugestão: adicionar um workflow GitHub Actions que instala as dependências e executa checagens básicas (lint, testes). Isto ajuda a garantir que PRs não quebrem o projeto.

## Estrutura de arquivos (resumo)

```
Aprender_Streamlit/
├─ Hello.py                # página principal
├─ app.py                  # entrada alternativa (ex: app genérica)
├─ requirements.txt
├─ pages/                  # páginas Streamlit secundárias (navegação automática)
│  ├─ 1_📈_Plotting_Demo.py
│  ├─ 2_🌍_Mapping_Demo.py
│  └─ 3_📊_DataFrame_Demo.py
└─ README.md
```

## Suporte / contato

Se precisar de ajuda, abra uma issue no repositório ou entre em contato com o mantenedor: roldan.eng.software@gmail.com

---

Documento gerado automaticamente para que qualquer pessoa possa reconstruir o ambiente e executar as demos no futuro.

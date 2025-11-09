import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Bem vindo ao Streamlit! 👋")

#st.sidebar.success("Selecione a pagina.")

st.markdown(
    """
    O Streamlit é uma estrutura de aplicativo de código aberto criada especificamente para projetos de Machine Learning e Ciência de Dados.  
👈 Selecione uma demonstração na barra lateral para ver alguns exemplos do que o Streamlit pode fazer!  

### Quer saber mais?
- Confira [streamlit.io](https://streamlit.io)  
- Veja nossa [documentação](https://docs.streamlit.io)  
- Faça uma pergunta em nossos [fóruns da comunidade](https://discuss.streamlit.io)  

### Veja demonstrações mais complexas
- Use uma rede neural para [analisar o conjunto de imagens de carros autônomos da Udacity](https://github.com/streamlit/demo-self-driving)  
- Explore um [conjunto de dados de transporte da cidade de Nova York](https://github.com/streamlit/demo-uber-nyc-pickups)

"""
)

# Lista automática de páginas (mostra botões na sidebar que navegam para cada página em `pages/`)
import os
import re

def _discover_pages():
    pages_dir = os.path.join(os.path.dirname(__file__), "pages")
    discovered = []
    if not os.path.isdir(pages_dir):
        return discovered

    for fname in sorted(os.listdir(pages_dir)):
        if not fname.endswith(".py"):
            continue
        fpath = os.path.join(pages_dir, fname)
        title = None
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            m = re.search(r"set_page_config\(.*page_title\s*=\s*['\"]([^'\"]+)['\"]", content, re.DOTALL)
            if m:
                title = m.group(1)
        except Exception:
            # se falhar, ignore e use o nome do arquivo
            title = None

        if not title:
            # remove a extensão e underscore/emoji extras para um rótulo legível
            title = os.path.splitext(fname)[0]
            # opcional: substituir underscores por espaços
            title = title.replace("_", " ")

        discovered.append((title, fname))

    return discovered

'''
pages = _discover_pages()
if pages:
    st.sidebar.markdown("### Demonstrações")
    for title, fname in pages:
        # botão que seta parâmetro de query 'page' para que o Streamlit abra a página
        if st.sidebar.button(title):
            # define o parâmetro de query que Streamlit usa para navegar entre páginas
            st.experimental_set_query_params(page=title)
            st.experimental_rerun()
'''
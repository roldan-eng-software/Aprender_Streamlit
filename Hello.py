import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Bem vindo ao Streamlit! 👋")

st.sidebar.success("Selecione a pagina.")

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
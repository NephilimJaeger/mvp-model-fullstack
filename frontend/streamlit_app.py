import streamlit as st
import requests

API_URL = "http://localhost:8000/neo"

def add_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def create_form():
    """Cria o formulário para entrada de dados."""
    with st.form(key='neo_form'):
        name = st.text_input("Nome do Objeto")
        est_diamenter_min = st.number_input("Diâmetro Estimado Mínimo (em km)", min_value=0)
        est_diameter_max = st.number_input("Diâmetro Estimado Máximo (em km", min_value=0)
        relative_velocity = st.number_input("Velocidade Relativa (em km/h)", min_value=0)
        submit_button = st.form_submit_button(label='Enviar')
    return name, est_diamenter_min, est_diameter_max, relative_velocity, submit_button

def send_data_to_api(data):
    """Envia os dados para o endpoint da API e retorna a resposta."""
    response = requests.post(API_URL, json=data)
    return response

def display_result(response):
    """Exibe o resultado da predição na tela."""
    if response.status_code == 200:
        result = response.json()
        st.success(f"Objeto: {result['name']}")
        st.info(f"Mensagem: {result['message']}")
        st.warning(f"Perigoso: {'Sim' if result['hazardous'] else 'Não'}")
    else:
        st.error("Erro ao fazer a predição. Tente novamente.")

def main():
    """Função principal que orquestra o fluxo do aplicativo."""
    st.title("Predição de Objetos Próximos à Terra")

    add_background_image("https://apod.nasa.gov/apod/image/2408/2024_07_28_Olbers_Kunka_Kunetice_1500px.png")
    
    # Cria o formulário e obtém os dados
    name, est_diamenter_min, est_diameter_max, relative_velocity, submit_button = create_form()
    
    # Quando o botão de envio for clicado
    if submit_button:
        # Dados a serem enviados para o endpoint
        data = {
            "name": name,
            "est_diamenter_min": est_diamenter_min,
            "est_diameter_max": est_diameter_max,
            "relative_velocity": relative_velocity
        }
        
        # Envia os dados para o endpoint e obtém a resposta
        response = send_data_to_api(data)
        
        # Exibe o resultado
        display_result(response)

if __name__ == "__main__":
    main()
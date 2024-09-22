import streamlit as st
import requests

class NeoPredictionApp:
    API_URL = "http://localhost:8000/neo"
    IMAGE_URL = "https://apod.nasa.gov/apod/image/2408/2024_07_28_Olbers_Kunka_Kunetice_1500px.png"

    def __init__(self):
        self.name = ""
        self.est_diamenter_min = 0.0
        self.est_diameter_max = 0.0
        self.relative_velocity = 0.0

    def add_background_image(self):
        """Adiciona uma imagem de plano de fundo ao aplicativo Streamlit."""
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("{self.IMAGE_URL}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    def create_form(self):
        """Cria o formulário para entrada de dados."""
        with st.form(key='neo_form'):
            self.name = st.text_input("Nome do Objeto")
            self.est_diamenter_min = st.number_input("Diâmetro Estimado Mínimo (em km)", min_value=0.0, format="%.4f")
            self.est_diameter_max = st.number_input("Diâmetro Estimado Máximo (em km)", min_value=0.0, format="%.4f")
            self.relative_velocity = st.number_input("Velocidade Relativa (em km/h)", min_value=0.0, format="%.4f")
            submit_button = st.form_submit_button(label='Enviar')
        return submit_button

    def send_data_to_api(self):
        """Envia os dados para o endpoint da API e retorna a resposta."""
        data = {
            "name": self.name,
            "est_diamenter_min": self.est_diamenter_min,
            "est_diameter_max": self.est_diameter_max,
            "relative_velocity": self.relative_velocity
        }
        response = requests.post(self.API_URL, json=data)
        return response

    def display_result(self, response):
        """Exibe o resultado da predição na tela."""
        if response.status_code == 200:
            result = response.json()
            st.success(f"Objeto: {result['name']}")
            st.info(f"Mensagem: {result['message']}")
            st.warning(f"Perigoso: {'Sim' if result['hazardous'] else 'Não'}")
        else:
            try:
                error_message = response.json().get('detail', 'Erro desconhecido.')
            except ValueError:
                error_message = response.text
            st.error(f"{error_message}")

    def run(self):
        """Função principal que orquestra o fluxo do aplicativo."""
        st.title("Esse asteróide vai nos matar?")

        self.add_background_image()
        
        submit_button = self.create_form()
        
        if submit_button:
            # Verifica se todos os campos estão preenchidos
            if not self.name or self.est_diamenter_min == 0.0 or self.est_diameter_max == 0.0 or self.relative_velocity == 0.0:
                st.error("Por favor, preencha todos os campos antes de enviar.")
            else:
                response = self.send_data_to_api()
                
                self.display_result(response)

if __name__ == "__main__":
    app = NeoPredictionApp()
    app.run()
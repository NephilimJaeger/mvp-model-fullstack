import subprocess
import threading

def run_fastapi():
    """Inicia o servidor FastAPI."""
    subprocess.run(["uvicorn", "backend.app:app", "--reload"])

def run_streamlit():
    """Inicia o servidor Streamlit."""
    subprocess.run(["streamlit", "run", "frontend/streamlit_app.py"])

if __name__ == "__main__":
    # Criar threads para cada servidor
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    streamlit_thread = threading.Thread(target=run_streamlit, daemon=True)

    # Iniciar as threads
    fastapi_thread.start()
    streamlit_thread.start()

    # Manter o script principal ativo enquanto as threads daemon estão rodando
    fastapi_thread.join()
    streamlit_thread.join()
# Multiplication Game Web
# Created by Jhonatas Góis
# Build version: 2.0 (Web Streamlit)
import streamlit as st
from random import sample

# --- CONFIGURAÇÃO DA PÁGINA (Deixa o app bonito no celular) ---
st.set_page_config(page_title="Multiplication Game", page_icon="🎲", layout="centered")

# --- INICIALIZAÇÃO DA MEMÓRIA DO JOGO (Session State) ---
if "fase" not in st.session_state:
    st.session_state.fase = "configuracao"  # Pode ser: configuracao, jogando, resultado
    st.session_state.tabuada = 0
    st.session_state.ordem_perguntas = []
    st.session_state.indice_atual = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0
    st.session_state.mensagem_erro = ""

# --- TÍTULO DA APLICAÇÃO ---
st.title("🎲 Multiplication Game")
st.caption("Created by Jhonatas Góis | Build version: 2.0 (Web)")
st.markdown("---")

# --- FASE 1: ESCOLHA DA TABUADA ---
if st.session_state.fase == "configuracao":
    st.subheader("Qual tabuada deseja estudar?")

    # Campo para o usuário digitar ou selecionar o número
    tabuada_escolhida = st.number_input("Digite um número inteiro (Ex: 7):", min_value=1, max_value=100, value=7,
                                        step=1)

    if st.button("Iniciar Treino 🚀", use_container_width=True):
        st.session_state.tabuada = tabuada_escolhida
        # Ordena de forma aleatória e única, números de 1 a 10 (exatamente como seu original!)
        st.session_state.ordem_perguntas = sample(range(1, 11), 10)
        st.session_state.indice_atual = 0
        st.session_state.acertos = 0
        st.session_state.erros = 0
        st.session_state.mensagem_erro = ""
        st.session_state.fase = "jogando"
        st.rerun()

# --- FASE 2: O JOGO EM ANDAMENTO ---
elif st.session_state.fase == "jogando":
    # Descobre qual é o número atual da pergunta
    idx = st.session_state.indice_atual
    numero_atual = st.session_state.ordem_perguntas[idx]
    tabuada = st.session_state.tabuada

    # Barra de progresso para o jogador ver quantas faltam
    st.progress(idx / 10, text=f"Pergunta {idx + 1} de 10")

    # Exibe a pergunta com destaque visual
    st.info(f"### Quanto é: {numero_atual} x {tabuada} ?")

    # Campo de resposta (Aceita a tecla ENTER do teclado como clique no botão)
    resposta = st.number_input("Sua resposta:", value=None, placeholder="Digite o resultado e clique em Confirmar",
                               step=1, key=f"resp_{idx}")

    # Exibe mensagem caso o jogador tenha errado anteriormente na mesma pergunta
    if st.session_state.mensagem_erro:
        st.error(st.session_state.mensagem_erro)

    if st.button("Confirmar Resposta Verificada 🎯", use_container_width=True):
        if resposta is None:
            st.warning("Por favor, digite uma resposta antes de confirmar!")
        else:
            validador = numero_atual * tabuada

            if resposta == validador:
                st.session_state.acertos += 1
                st.session_state.mensagem_erro = ""  # Limpa erros anteriores

                # Avança para a próxima pergunta
                if st.session_state.indice_atual < 9:
                    st.session_state.indice_atual += 1
                else:
                    st.session_state.fase = "resultado"  # Fim do jogo se chegou na décima
                st.rerun()
            else:
                st.session_state.erros += 1
                st.session_state.mensagem_erro = "❌ Valor incorreto! Tente novamente."
                st.rerun()

# --- FASE 3: TELA DE DESEMPENHO (FIM DO JOGO) ---
elif st.session_state.fase == "resultado":
    st.balloons()  # Efeito visual de comemoração na tela!
    st.subheader("📊 Desempenho do Jogador")

    # Exibe os resultados em colunas organizadas
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"### Acertos: {st.session_state.acertos}")
    with col2:
        st.error(f"### Erros: {st.session_state.erros}")

    st.markdown("---")

    if st.button("🔄 Treinar outra tabuada", use_container_width=True):
        st.session_state.fase = "configuracao"
        st.rerun()

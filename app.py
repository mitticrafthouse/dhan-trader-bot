import streamlit as st

st.set_page_config(page_title="Dhan Trader Bot", layout="wide")

st.title("Dhan Trader Bot Dashboard")
st.caption("Streamlit dashboard for monitoring and controlling the bot")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Dhan API Key", type="password")
    api_secret = st.text_input("Dhan API Secret", type="password")
    client_id = st.text_input("Client ID")
    mode = st.selectbox("Mode", ["paper", "live"], index=0)

    st.divider()
    st.subheader("Controls")
    start_btn = st.button("Start Bot", type="primary")
    stop_btn = st.button("Stop Bot")

if "bot_running" not in st.session_state:
    st.session_state.bot_running = False
if "logs" not in st.session_state:
    st.session_state.logs = []

def add_log(msg):
    st.session_state.logs.insert(0, msg)
    st.session_state.logs = st.session_state.logs[:50]

if start_btn:
    if not api_key or not api_secret or not client_id:
        st.error("Please fill API Key, API Secret, and Client ID.")
    else:
        st.session_state.bot_running = True
        add_log(f"Bot start requested in {mode} mode")
        st.success("Bot start requested.")

if stop_btn:
    st.session_state.bot_running = False
    add_log("Bot stop requested")
    st.info("Bot stop requested.")

col1, col2, col3 = st.columns(3)
col1.metric("Status", "Running" if st.session_state.bot_running else "Stopped")
col2.metric("Mode", mode)
col3.metric("Logs", len(st.session_state.logs))

st.subheader("Activity Log")
for log in st.session_state.logs:
    st.write(f"- {log}")
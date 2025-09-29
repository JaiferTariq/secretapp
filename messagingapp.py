import base64
import streamlit as st

# ---------- Functions ----------
def encode_message(message: str) -> str:
    return base64.b64encode(message.encode()).decode()

def decode_message(encoded: str) -> str:
    try:
        return base64.b64decode(encoded.encode()).decode()
    except Exception:
        return "❌ Invalid code! Make sure it was encoded with this app."

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Secret Messenger", page_icon="🔒", layout="centered")

st.title("🔒 Secret Messenger")
st.write("Send secret messages to your friends! Copy-paste the encoded text and share it.")

mode = st.radio("Choose an action:", ["Encode a message", "Decode a message"])

if mode == "Encode a message":
    text = st.text_area("Enter your secret message:")
    if st.button("Encode"):
        if text.strip():
            encoded = encode_message(text)
            st.success("✅ Encoded message:")
            st.code(encoded)
        else:
            st.warning("Please enter a message first!")

else:  # Decode mode
    text = st.text_area("Paste the encoded message:")
    if st.button("Decode"):
        if text.strip():
            decoded = decode_message(text)
            st.success("✅ Decoded message:")
            st.code(decoded)
        else:
            st.warning("Please enter an encoded message first!")

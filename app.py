import streamlit as st

st.set_page_config(page_title="talentScout", layout = "wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.markdown("<h1>TalentScout Hiring Assistant </h1>", unsafe_allow_html=True)
st.write("Your AI-powered assistant for initial candidate screening.")

left_col, right_col = st.columns([2,1])

with left_col:
    
    st.subheader("Chat")
    st.markdown("<div class = 'chat-container>", unsafe_allow_html=True)
    
    messages = [
        {"role" : "bot", "content": "Hello, I'm TalentScout, your AI hiring assistant."},
        {"role" : "bot", "content" : "Let's start with your **full name**."},
        {"role" : "bot", "content" : "John Doe"},
        {"role" : "bot", "content": "Great! Now share your **email address**."},
    ]
    
    for msg in messages:
        
        if msg["role"] == "user" :
            st.markdown(f"<div class = 'msg user-msg'>{msg['content']}</div>", unsafe_allow_html = True)
        else:
            st.markdown(f"<div class = 'msg bot-msg'>{msg['content']}</div>", unsafe_allow_html = True)
    
    st.markdown("</div>", unsafe_allow_html = True)
    st.text_input("type your message")
    
with right_col :
    st.subheader("Candidate Summary")
    st.write("**Full Name:** John Doe")
    st.write("**Email:** johndoe@example.com")
    st.write("**Phone:** Not provided")
    st.write("**Experience:** Not provided")
    st.write("**Desired Position:** Not provided")
    st.write("**Location:** Not provided")
    st.write("**Tech Stack:** Not provided")
    
#-------------SIDEBAR-------------#

st.sidebar.title("Instructions")
st.sidebar.markdown("""
**How it works:**
- Enter your details step by step.
- Declare your tech stack clearly (e.g., Python, Django, PostgreSQL).
- The bot will generate 3-5 technical questions based on your stack.
- Type 'exit' to finish.
""")
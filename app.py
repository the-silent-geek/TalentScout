import streamlit as st
from model import generate_response 

st.set_page_config(page_title="talentScout", layout = "wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    

left_col, right_col = st.columns([2,1])

with left_col:
    st.markdown("""
    <div class="header-container">
        <h1>TalentScout Hiring Assistant</h1>
        <p>Your AI-powered assistant for initial candidate screening.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [("AI", "Hello! I'm TalentScout. Type 'exit' to stop.")]

    st.markdown("<h2 style='text-align:center;'>Chat</h2>", unsafe_allow_html=True)

    chat_container = st.container()
    with chat_container:
        for role, msg in st.session_state.messages:
            if role == "User":
                st.markdown(f"<div class='msg user-msg'>{msg}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='msg bot-msg'>{msg}</div>", unsafe_allow_html=True)
    
    # Input form (prevents adding text until Enter is pressed)
    with st.form("chat_input_form", clear_on_submit=True):
        st.markdown('<div class="chat-input-row">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input("", key="user_input", placeholder="Type your message...")
        with col2:
            submitted = st.form_submit_button("Send")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted and user_input:
        if user_input.lower() == "exit":
            st.session_state.messages.append(("AI", "Chat ended. Thank you!"))
        else:
            st.session_state.messages.append(("User", user_input))
            ai_response = generate_response(user_input, st.session_state.messages)
            st.session_state.messages.append(("AI", ai_response))
    
        st.rerun()
    
with right_col:
    st.markdown(
        """
        <div class="summary-container">
            <h3>Candidate Summary</h3>
            <p><strong>Full Name:</strong> John Doe</p>
            <p><strong>Email:</strong> johndoe@example.com</p>
            <p><strong>Phone:</strong> Not provided</p>
            <p><strong>Experience:</strong> Not provided</p>
            <p><strong>Desired Position:</strong> Not provided</p>
            <p><strong>Location:</strong> Not provided</p>
            <p><strong>Tech Stack:</strong> Not provided</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
#-------------SIDEBAR-------------#

st.sidebar.title("Instructions")
st.sidebar.markdown("""
**How it works:**
- Enter your details step by step.
- Declare your tech stack clearly (e.g., Python, Django, PostgreSQL).
- The bot will generate 3-5 technical questions based on your stack.
- Type 'exit' to finish.
""")
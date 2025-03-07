import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Meter By Asmara Faisal", page_icon="🔑", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}"
    .stTextInput {width: 60% !imporant; margin:}
    .stButton button {width: 50%; background-color #4cafac; color: white; font-size: 18px; }
    .stButton button:hover { background-color: #458ae0;}
</style>
""", unsafe_allow_html=True)

#page decription
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")
 
#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increassed score by 1
    else:
        feedback.append("❌Password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should include **both upercase (A-Z) and lowercase (a-z) letters**.")
    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("❌Password should include **at least one number (0_9) **.")

       # special characters
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**. ")

    #disply result
    if score == 4:
        st.success("☑️ **Strong password** -Your password is secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate passord** - Consider improveing security by adding more feature")
    else:
        st.error("❌ **Week password** -follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("🔎 **Improve your password** ."):
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

    #Button working
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password first!")   #if password is empty show warning! 

import streamlit as st
from streamlit import session_state as ss
from PIL import Image
import os

def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def show_sidebar_logo():
    logo_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'empresa.png')

    if not os.path.exists(logo_path):
        st.sidebar.error(f"Logo não encontrado no caminho: {logo_path}")
        return

    try:
        logo = Image.open(logo_path)
    except Exception as e:
        st.sidebar.error(f"Erro ao carregar o logo: {e}")
        return

    logo_html = f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{image_to_base64(logo)}" style="width: 150px;" alt="Logo">
    </div>
    """
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)

    if 'name' in ss:
        st.sidebar.markdown(f"<div style='text-align: center; margin-top: 10px;'>Bem-vindo, {ss['name']} 😀</div>", unsafe_allow_html=True)


#DEFAULT PAGE (ALL USERS VIEW)
def HomeNav():
    st.sidebar.page_link("streamlit_app.py", label="Home", icon='🏠')
def LoginNav():
    st.sidebar.page_link("pages/account.py", label="Account", icon='🧾')

# ADMIN PAGE (ONLY ADMIN ROLE)
def Page1admin():
    st.sidebar.page_link("pages/page1.py", label="Admin page", icon='🃏')

# USERS PAGE (ONLY USERS ROLE)
def Page2user():
    st.sidebar.page_link("pages/page2.py", label="Users page", icon='📊')


def MenuButtons(user_roles=None):
    if user_roles is None:
        user_roles = {}

    if 'authentication_status' not in ss:
        ss.authentication_status = False

    show_sidebar_logo()
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)


    # DEFAULT PAGE (ALL USERS VIEW)
    HomeNav()
    LoginNav()

    if ss["authentication_status"]:


        admins = [k for k, v in user_roles.items() if v == 'admin']
        users = [k for k, v in user_roles.items() if v == 'user']
        # If you want to do more RBAC, you can create more authentication status (example: operator = [k for k, v in user_roles.items() if v == 'operator'])
       

        if ss.username in admins:
            Page1admin()

        if ss.username in users:
            Page2user()     

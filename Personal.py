import streamlit as st
import info
from PIL import Image
from AcademicPage import show_academic_page
from ProfessionalPage import show_professional_page

try:
    from streamlit_stl import stl_from_file
    STL_VIEWER_AVAILABLE = True
except ImportError:
    STL_VIEWER_AVAILABLE = False

st.set_page_config(layout="wide", page_title="About Elan McClain")

def nav():
    st.sidebar.title("Navigation")

    personal = st.sidebar.button("Personal", use_container_width=True)
    academic = st.sidebar.button("Academic", use_container_width=True)
    professional = st.sidebar.button("Professional", use_container_width=True)

    if 'page' not in st.session_state:
        st.session_state.page = "Personal"

    if personal:
        st.session_state.page = "Personal"
    elif academic:
        st.session_state.page = "Academic"
    elif professional:
        st.session_state.page = "Professional"

    return st.session_state.page

def sidebar():
    st.sidebar.markdown("---")
    try:
        img = Image.open(info.pic)
        img = img.rotate(-90, expand=True)
        st.sidebar.image(img, width=150)
    except:
        st.sidebar.write("Profile picture not available")

    st.sidebar.title("Connect with Me")

    link = f'<a href="{info.linkurl}" target="_blank"><img src="{info.linkedin}" alt="LinkedIn" width="30" height="30"></a>'
    st.sidebar.markdown(link, unsafe_allow_html=True)

    email = f'<a href="mailto:{info.email}"><img src="{info.emailimg}" alt="Email" width="30" height="30"></a>'
    st.sidebar.markdown(email, unsafe_allow_html=True)

    st.sidebar.write(f"📞 {info.phone}")

def about():
    st.header("About Me")

    try:
        img = Image.open("Images/FullSelfie.jpg")
        img = img.rotate(90, expand=True)
        st.image(img, width=400)
    except:
        st.write("Full picture not found")

    st.write(info.about)
    st.write("**What I'm passionate about:**")
    st.write("• Problem solving and innovative technology solutions")
    st.write("• Leading teams and making positive impacts")
    st.write("• Continuous learning and growth")
    st.write("• Having Fun!")
    st.write("---")

def projects():
    st.header("Projects")
    for name, pinfo in info.projects.items():
        with st.expander(f"{name}"):
            if isinstance(pinfo, tuple):
                text = pinfo[0]
                img = pinfo[1] if len(pinfo) > 1 else None
                link = pinfo[2] if len(pinfo) > 2 else None
                model = pinfo[3] if len(pinfo) > 3 else None

                st.write(text)

                if img:
                    try:
                        st.image(img, width=300)
                    except:
                        st.write("Image not found")

                if link:
                    st.markdown(f"[**Play the Game!**]({link})")

                if model:
                    if STL_VIEWER_AVAILABLE:
                        if isinstance(model, list):
                            model_cols = st.columns(len(model))
                            for m_col, m in zip(model_cols, model):
                                with m_col:
                                    try:
                                        stl_from_file(
                                            file_path=m,
                                            color="#4B9CD3",
                                            material="material",
                                            auto_rotate=True,
                                            opacity=1,
                                            height=400,
                                            key=f"stl_{name}_{m}",
                                        )
                                    except Exception:
                                        st.info(f"Couldn't load the 3D model — make sure '{m}' exists in your project folder.")
                        else:
                            try:
                                stl_from_file(
                                    file_path=model,
                                    color="#4B9CD3",
                                    material="material",
                                    auto_rotate=True,
                                    opacity=1,
                                    height=400,
                                    key=f"stl_{name}",
                                )
                            except Exception:
                                st.info(f"Couldn't load the 3D model — make sure '{model}' exists in your project folder.")
                    else:
                        st.info("Interactive 3D model support isn't installed. Run `pip install streamlit-stl` to enable it.")
            else:
                st.write(pinfo)
    st.write("---")

def hobbies():
    st.header("Hobbies & Interests")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_area(
            "Cars",
            value="One of my favorite hobbies is working on, appreciating, and driving fun cars. I have owned numerous fun cars since I was 15 and I've worked on all of them. This is my current car, a 1999 Pontiac Firebird Formula with a 6 speed transmission.",
            height=160,
            disabled=True,
            label_visibility="collapsed",
        )
        try:
            st.image("Images/mycar.jpg", use_container_width=True)
        except:
            st.write("Image not found")

    with col2:
        st.text_area(
            "Motorcycles",
            value="My other great automotive-adjacent intrest is motorcycles. In addition to my sportbike I am riding in the picture below with my dad I also enjoy riding and working on ebikes and dirtbikes.",
            height=160,
            disabled=True,
            label_visibility="collapsed",
        )
        try:
            st.image("Images/bike.jpg", use_container_width=True)
        except:
            st.write("Image not found")

    with col3:
        st.text_area(
            "Outdoors",
            value="I am also an avid fan of being outdoors, when I can get out of the city I enjoy hiking, mountain biking, camping, fishing, and any other way to enjoy the beauty of nature.",
            height=160,
            disabled=True,
            label_visibility="collapsed",
        )
        try:
            st.image("Images/outdoors.jpg", use_container_width=True)
        except:
            st.write("Image not found")

    st.write("---")

def personal_page():
    st.title("Elan McClain - About Me")
    st.write("**Welcome to my Website!** Explore my journey as a Mechanical Engineering student at Georgia Tech.")

    try:
        with open("Elan-Mcclain-Resume.pdf", "rb") as f:
            st.download_button(
                label="PDF Resume Here",
                data=f,
                file_name="Elan-Mcclain-Resume.pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.warning("Resume PDF not found — add 'Elan-Mcclain-Resume.pdf' to this folder to enable the download button.")

    st.write("---")

    about()
    projects()
    hobbies()

page = nav()
sidebar()

if page == "Personal":
    personal_page()
elif page == "Academic":
    show_academic_page()
elif page == "Professional":
    show_professional_page()

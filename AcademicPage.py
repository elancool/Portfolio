import streamlit as st
import info
from PIL import Image, ImageOps

def show_academic_page():
    st.title("Academic")
    st.write("**A look at my education and academic background.**")
    st.write("---")

    st.header("Education")
    for e in info.edu:
        with st.expander(f"{e['Degree']} — {e['Institution']}"):
            st.write(f"**Location:** {e['Location']}")
            st.write(f"**Graduation Date:** {e['Graduation Date']}")
            if e.get("Photo"):
                try:
                    img = Image.open(e["Photo"])
                    img = ImageOps.exif_transpose(img)
                    st.image(img, width=250)
                except Exception:
                    st.write(f"Image not found: {e['Photo']}")

    st.write("---")

    st.header("Relevant Coursework")
    st.text_area(
        "List courses that are relevant to your field of study",
        value="- CS1301 — Intro to Computing (Learned Python)\n"
              "- Chem1310 — General Chemistry for Engineers\n"
              "- Math1551 - Differential Calculus\n"
              "- Math 1552 - Integral Calculus\n"
              "- Physics 2211 - Intro to Physics 1\n"
              "- CS1371 - Computing for Engineers (Matlab)\n",
        height=160,
        disabled=True,
        label_visibility="collapsed",
    )

    st.write("---")

    st.header("Extracurricular Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])

    with tab1:
        st.subheader("Leadership")
        for title, (details, img) in info.lead.items():
            with st.expander(f"{title}"):
                if img:
                    try:
                        pimg = Image.open(img)
                        pimg = ImageOps.exif_transpose(pimg)
                        st.image(pimg, width=250)
                    except:
                        st.write("Image not found")
                for bullet in details:
                    st.write(bullet)

    with tab2:
        st.subheader("Community Service")
        for title, details in info.activities.items():
            with st.expander(f"{title}"):
                if isinstance(details, list):
                    for bullet in details:
                        st.write(bullet)
                else:
                    st.write(details)
    st.write("---")

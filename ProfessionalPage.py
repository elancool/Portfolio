import streamlit as st
import info

def show_professional_page():
    st.title("Professional")
    st.write("**My work experience, skills, and professional projects.**")
    st.write("---")

    st.header("Work Experience")
    for job, details in info.exp.items():
        with st.expander(job):
            st.write(f"**Dates:** {details['dates']}")
            for bullet in details["bullets"]:
                st.write(f"- {bullet}")
            for img in details.get("images", []):
                try:
                    st.image(img, width=250)
                except Exception:
                    st.write(f"Image not found: {img}")

    st.write("---")

    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Technical Skills")
        st.text_area(
            "Technical Skills",
            value="""- some Fusion360 experience
- Python
- GSuite & Microsoft Office
- Conversational Spanish""",
            height=130,
            disabled=True,
            label_visibility="collapsed",

        )
    with col2:
        st.subheader("Soft Skills")
        st.text_area(
            "Soft Skills",
            value="""- Communication
- Presentation & Public Speaking
- Leadership
- Critical Thinking & Problem Solving
- Adaptability""",
            height=130,
            disabled=True,
            label_visibility="collapsed",
        )

    st.write("---")

    st.header("Professional Certifications")
    st.text_area(
        "List any job-relevant certifications",
        value="""Microsoft Office Specialist - Word - Certiport 2022,
Microsoft Office Specialist - Excel - Certiport 2023""",
        height=90,
        disabled=True,
        label_visibility="collapsed",
    )
    st.write("---")

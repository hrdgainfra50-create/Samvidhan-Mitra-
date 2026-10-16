import streamlit as st

st.title("🇮🇳 Samvidhan Mitra")
st.write("AI Companion for Constitutional & Sustainable Solutions")

st.sidebar.header("📊 Solution Impact Tracker")
st.sidebar.text("Constitutional Alignment")
st.sidebar.progress(90)
st.sidebar.text("Sustainability Index")
st.sidebar.progress(85)

problem = st.text_input("Apni samasya batayein (e.g. kachra, traffic):")

if problem:
    st.success("Analysis Complete!")
    st.markdown("### 📜 1. Constitutional Lens")
    st.write("Article 21 (Right to Life) aur Article 48A (Environment Protection) ke tehat.")
    
    st.markdown("### 💡 2. Innovative & Sustainable Solution")
    st.write(f"'{problem}' ke liye community-led smart tracking system.")
    
    st.markdown("### 📊 Metrics")
    st.table({
        "Parameter": ["Constitutional Fit", "Sustainability", "Ethics"],
        "Score": ["95%", "High Impact", "100% Transparent"]
    })

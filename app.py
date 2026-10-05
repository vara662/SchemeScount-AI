import streamlit as st
from PIL import Image
from ocr import extract_text
from redact import redact
from extractor import extract_fields
from engine import evaluate

st.set_page_config(page_title="SchemeScout AI", page_icon="🧭")
st.title("🧭 SchemeScout AI")
st.caption("Upload a certificate → we find government schemes you may be eligible for")

file = st.file_uploader("Upload certificate (JPG/PNG)", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file)
    st.image(img, width=350)

    text = redact(extract_text(img))
    with st.expander("Extracted text (sensitive IDs masked)"):
        st.text(text)

    f = extract_fields(text)
    st.subheader("Verify extracted details")
    c1, c2 = st.columns(2)
    income = c1.number_input("Annual income (₹)", value=f["income"] or 0, step=1000)
    age = c2.number_input("Age", value=f["age"] or 0)
    gender = c1.selectbox("Gender", ["", "Male", "Female", "Transgender"],
                          index=["", "Male", "Female", "Transgender"].index(f["gender"] or ""))
    district = c2.text_input("District", f["district"] or "")
    community = c1.text_input("Community", f["community"] or "")

    if st.button("Find schemes"):
        profile = {"income": income or None, "age": age or None,
                   "gender": gender or None, "district": district or None,
                   "community": community or None}
        results = evaluate(profile)

        for label, key, icon in [("Eligible", "eligible", "✅"),
                                 ("Needs more info", "needs_info", "❓"),
                                 ("Not eligible", "not_eligible", "❌")]:
            group = [r for r in results if r["status"] == key]
            if group:
                st.subheader(f"{icon} {label}")
                for r in group:
                    with st.expander(r["scheme"]["name"]):
                        st.write(r["scheme"]["description"])
                        for line in r["reasons"]:
                            st.write(line)
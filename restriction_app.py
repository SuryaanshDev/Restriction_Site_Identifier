import streamlit as st
from Bio.Seq import Seq
from Bio.Restriction import AllEnzymes, Analysis

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Restriction Site Identifier",
    layout="centered"
)

st.title("Restriction Site Identifier (600+ Enzymes)")
st.write(
    "This app identifies restriction enzyme recognition sites "
    "using BioPython's full enzyme database."
)

# -------------------------------
# DNA Input
# -------------------------------
dna_input = st.text_area(
    "Enter DNA Sequence",
    placeholder="Example: GAATTCCGGATCCAAGCTT"
)

# -------------------------------
# Run Analysis
# -------------------------------
if st.button("Analyze Restriction Sites"):

    if not dna_input:
        st.warning("Please enter a DNA sequence.")
    else:
        try:
            dna_seq = Seq(dna_input.upper())

            analysis = Analysis(AllEnzymes, dna_seq)
            results = analysis.full()

            found_any = False

            for enzyme, sites in results.items():
                if sites:
                    found_any = True
                    st.subheader(str(enzyme))
                    st.write(f"**Recognition site:** {enzyme.site}")
                    st.write(f"**Cut positions:** {sites}")

            if not found_any:
                st.error("No restriction sites found in the given sequence.")

        except Exception as e:
            st.error(f"Invalid DNA sequence or error occurred: {e}")


import streamlit as st
from Bio import SeqIO
import base64

st.set_page_config(page_title="Simple FASTA File Parser", layout="wide")

st.markdown("<h1 style='text-align: center;'>🧬 Simple FASTA File Parser</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Upload a FASTA file and parse sequence details easily!</h4>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your FASTA file (.fasta or .fa)", type=["fasta", "fa"])

if uploaded_file:
    sequences = list(SeqIO.parse(uploaded_file, "fasta"))
    st.success(f"✅ Parsed {len(sequences)} sequence(s) successfully!")

    st.markdown("### 📝 Sequence Summary:")
    seq_data = []
    for seq_record in sequences:
        seq_data.append({
            "Sequence ID": seq_record.id,
            "Length": len(seq_record.seq),
            "First 50 Bases": str(seq_record.seq[:50])
        })

    st.table(seq_data)

    result_text = "\n\n".join([f">{s.id}\n{s.seq}" for s in sequences])
    b64 = base64.b64encode(result_text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="parsed_sequences.txt">📥 Download Parsed Sequences as TXT</a>'
    st.markdown(href, unsafe_allow_html=True)

st.markdown("""<hr><p style='text-align: center; color: #888888;'>Created by Anjali Jadhav | FYBI | MGM's College of CS & IT, Nanded</p>""", unsafe_allow_html=True)

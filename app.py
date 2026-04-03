
import streamlit as st
import pandas as pd
import math

st.set_page_config(
    page_title="BARAI-GENOME",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@400;600&display=swap');
html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; background-color: #0a0a1a; color: #e0e0e0; }
.stApp { background: linear-gradient(135deg, #0a0a1a 0%, #0d1b2a 100%); }
h1 { font-family: 'Orbitron', monospace !important; background: linear-gradient(90deg, #1a8cff, #00d4ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.4rem !important; letter-spacing: 6px; text-align: center; padding: 10px 0; }
.subtitle { text-align: center; color: #1a8cff; font-size: 0.85rem; letter-spacing: 3px; margin-top: -15px; margin-bottom: 25px; opacity: 0.8; }
.stTextArea textarea { background-color: #1a0000 !important; color: #ff6b6b !important; border: 2px solid #ff3333 !important; border-radius: 8px !important; font-family: monospace !important; }
.stTextArea label { color: #ff6b6b !important; font-weight: 600; letter-spacing: 1px; }
.stSelectbox > div > div { background-color: #1a0000 !important; border: 2px solid #ff3333 !important; color: #ff6b6b !important; border-radius: 8px !important; }
.stSelectbox label { color: #ff6b6b !important; font-weight: 600; }
.stButton > button { background: linear-gradient(90deg, #cc0000, #ff3333) !important; color: #ffffff !important; font-family: 'Orbitron', monospace !important; font-weight: 700 !important; border: none !important; border-radius: 8px !important; padding: 12px 30px !important; letter-spacing: 2px !important; width: 100% !important; }
.stCode, code, pre { background-color: #001a00 !important; border: 2px solid #00cc44 !important; color: #00ff66 !important; border-radius: 8px !important; }
.result-header { color: #00ff66; font-size: 1rem; letter-spacing: 2px; margin-top: 15px; font-weight: 700; }
.stDownloadButton > button { background: linear-gradient(90deg, #006622, #00cc44) !important; color: #ffffff !important; border: none !important; border-radius: 8px !important; width: 100% !important; font-weight: 700 !important; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #000510, #000d1a) !important; border-right: 2px solid #1a8cff44 !important; }
.info-card { background: #000d1a; border: 1px solid #1a8cff33; border-radius: 10px; padding: 12px; margin-bottom: 10px; }
.info-label { color: #1a8cff; font-size: 0.75rem; letter-spacing: 1px; }
.info-value { color: #ffffff; font-weight: 600; font-size: 0.9rem; }
.footer { text-align: center; color: #1a8cff55; font-size: 0.75rem; letter-spacing: 2px; margin-top: 30px; padding: 15px; border-top: 1px solid #1a8cff22; }
.section-box-red { border: 1px solid #ff333333; border-radius: 10px; padding: 15px; margin-bottom: 10px; background: #0d0000; }
.section-box-green { border: 1px solid #00cc4433; border-radius: 10px; padding: 15px; background: #000d00; }
.cai-box { background: #000d1a; border: 2px solid #1a8cff; border-radius: 10px; padding: 15px; text-align: center; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

codon_usage_data = {
    "BRRI dhan29": {
        "A":{"GCT":0.40,"GCC":0.30,"GCA":0.20,"GCG":0.10},
        "R":{"CGT":0.15,"CGC":0.30,"CGA":0.10,"CGG":0.15,"AGA":0.20,"AGG":0.10},
        "N":{"AAT":0.35,"AAC":0.65},"D":{"GAT":0.40,"GAC":0.60},
        "C":{"TGT":0.30,"TGC":0.70},"Q":{"CAA":0.35,"CAG":0.65},
        "E":{"GAA":0.55,"GAG":0.45},"G":{"GGT":0.15,"GGC":0.50,"GGA":0.25,"GGG":0.10},
        "H":{"CAT":0.35,"CAC":0.65},"I":{"ATT":0.25,"ATC":0.55,"ATA":0.20},
        "L":{"TTA":0.05,"TTG":0.10,"CTT":0.15,"CTC":0.25,"CTA":0.05,"CTG":0.40},
        "K":{"AAA":0.35,"AAG":0.65},"F":{"TTT":0.30,"TTC":0.70},
        "P":{"CCT":0.25,"CCC":0.30,"CCA":0.30,"CCG":0.15},
        "S":{"TCT":0.10,"TCC":0.25,"TCA":0.10,"TCG":0.05,"AGT":0.10,"AGC":0.40},
        "T":{"ACT":0.20,"ACC":0.40,"ACA":0.25,"ACG":0.15},
        "W":{"TGG":1.00},"Y":{"TAT":0.30,"TAC":0.70},
        "V":{"GTT":0.20,"GTC":0.30,"GTA":0.15,"GTG":0.35},"M":{"ATG":1.00},
    },
    "BRRI dhan28": {
        "A":{"GCT":0.35,"GCC":0.25,"GCA":0.25,"GCG":0.15},
        "R":{"CGT":0.20,"CGC":0.25,"CGA":0.15,"CGG":0.10,"AGA":0.20,"AGG":0.10},
        "N":{"AAT":0.45,"AAC":0.55},"D":{"GAT":0.50,"GAC":0.50},
        "C":{"TGT":0.40,"TGC":0.60},"Q":{"CAA":0.45,"CAG":0.55},
        "E":{"GAA":0.60,"GAG":0.40},"G":{"GGT":0.20,"GGC":0.35,"GGA":0.30,"GGG":0.15},
        "H":{"CAT":0.40,"CAC":0.60},"I":{"ATT":0.30,"ATC":0.50,"ATA":0.20},
        "L":{"TTA":0.10,"TTG":0.15,"CTT":0.20,"CTC":0.20,"CTA":0.05,"CTG":0.30},
        "K":{"AAA":0.40,"AAG":0.60},"F":{"TTT":0.35,"TTC":0.65},
        "P":{"CCT":0.30,"CCC":0.25,"CCA":0.30,"CCG":0.15},
        "S":{"TCT":0.15,"TCC":0.25,"TCA":0.15,"TCG":0.05,"AGT":0.15,"AGC":0.25},
        "T":{"ACT":0.25,"ACC":0.35,"ACA":0.25,"ACG":0.15},
        "W":{"TGG":1.00},"Y":{"TAT":0.35,"TAC":0.65},
        "V":{"GTT":0.25,"GTC":0.25,"GTA":0.20,"GTG":0.30},"M":{"ATG":1.00},
    },
    "Balam": {
        "A":{"GCT":0.45,"GCC":0.20,"GCA":0.25,"GCG":0.10},
        "R":{"CGT":0.25,"CGC":0.20,"CGA":0.15,"CGG":0.10,"AGA":0.20,"AGG":0.10},
        "N":{"AAT":0.50,"AAC":0.50},"D":{"GAT":0.55,"GAC":0.45},
        "C":{"TGT":0.45,"TGC":0.55},"Q":{"CAA":0.50,"CAG":0.50},
        "E":{"GAA":0.65,"GAG":0.35},"G":{"GGT":0.25,"GGC":0.20,"GGA":0.40,"GGG":0.15},
        "H":{"CAT":0.45,"CAC":0.55},"I":{"ATT":0.35,"ATC":0.40,"ATA":0.25},
        "L":{"TTA":0.15,"TTG":0.20,"CTT":0.25,"CTC":0.20,"CTA":0.05,"CTG":0.15},
        "K":{"AAA":0.55,"AAG":0.45},"F":{"TTT":0.40,"TTC":0.60},
        "P":{"CCT":0.35,"CCC":0.20,"CCA":0.30,"CCG":0.15},
        "S":{"TCT":0.20,"TCC":0.20,"TCA":0.20,"TCG":0.05,"AGT":0.20,"AGC":0.15},
        "T":{"ACT":0.30,"ACC":0.30,"ACA":0.25,"ACG":0.15},
        "W":{"TGG":1.00},"Y":{"TAT":0.40,"TAC":0.60},
        "V":{"GTT":0.30,"GTC":0.20,"GTA":0.20,"GTG":0.30},"M":{"ATG":1.00},
    },
    "Kataribhog": {
        "A":{"GCT":0.38,"GCC":0.22,"GCA":0.28,"GCG":0.12},
        "R":{"CGT":0.18,"CGC":0.22,"CGA":0.18,"CGG":0.12,"AGA":0.18,"AGG":0.12},
        "N":{"AAT":0.48,"AAC":0.52},"D":{"GAT":0.52,"GAC":0.48},
        "C":{"TGT":0.42,"TGC":0.58},"Q":{"CAA":0.52,"CAG":0.48},
        "E":{"GAA":0.62,"GAG":0.38},"G":{"GGT":0.22,"GGC":0.28,"GGA":0.32,"GGG":0.18},
        "H":{"CAT":0.42,"CAC":0.58},"I":{"ATT":0.32,"ATC":0.45,"ATA":0.23},
        "L":{"TTA":0.12,"TTG":0.18,"CTT":0.22,"CTC":0.18,"CTA":0.08,"CTG":0.22},
        "K":{"AAA":0.58,"AAG":0.42},"F":{"TTT":0.38,"TTC":0.62},
        "P":{"CCT":0.32,"CCC":0.22,"CCA":0.32,"CCG":0.14},
        "S":{"TCT":0.18,"TCC":0.22,"TCA":0.18,"TCG":0.05,"AGT":0.18,"AGC":0.19},
        "T":{"ACT":0.28,"ACC":0.32,"ACA":0.28,"ACG":0.12},
        "W":{"TGG":1.00},"Y":{"TAT":0.38,"TAC":0.62},
        "V":{"GTT":0.28,"GTC":0.22,"GTA":0.22,"GTG":0.28},"M":{"ATG":1.00},
    },
    "Chinigura": {
        "A":{"GCT":0.30,"GCC":0.35,"GCA":0.20,"GCG":0.15},
        "R":{"CGT":0.12,"CGC":0.35,"CGA":0.08,"CGG":0.18,"AGA":0.18,"AGG":0.09},
        "N":{"AAT":0.30,"AAC":0.70},"D":{"GAT":0.35,"GAC":0.65},
        "C":{"TGT":0.25,"TGC":0.75},"Q":{"CAA":0.30,"CAG":0.70},
        "E":{"GAA":0.45,"GAG":0.55},"G":{"GGT":0.12,"GGC":0.48,"GGA":0.28,"GGG":0.12},
        "H":{"CAT":0.28,"CAC":0.72},"I":{"ATT":0.20,"ATC":0.62,"ATA":0.18},
        "L":{"TTA":0.04,"TTG":0.08,"CTT":0.12,"CTC":0.28,"CTA":0.04,"CTG":0.44},
        "K":{"AAA":0.28,"AAG":0.72},"F":{"TTT":0.22,"TTC":0.78},
        "P":{"CCT":0.18,"CCC":0.35,"CCA":0.28,"CCG":0.19},
        "S":{"TCT":0.08,"TCC":0.28,"TCA":0.08,"TCG":0.04,"AGT":0.08,"AGC":0.44},
        "T":{"ACT":0.15,"ACC":0.45,"ACA":0.22,"ACG":0.18},
        "W":{"TGG":1.00},"Y":{"TAT":0.22,"TAC":0.78},
        "V":{"GTT":0.15,"GTC":0.35,"GTA":0.12,"GTG":0.38},"M":{"ATG":1.00},
    },
    "Najirshail": {
        "A":{"GCT":0.42,"GCC":0.25,"GCA":0.22,"GCG":0.11},
        "R":{"CGT":0.22,"CGC":0.25,"CGA":0.12,"CGG":0.12,"AGA":0.20,"AGG":0.09},
        "N":{"AAT":0.42,"AAC":0.58},"D":{"GAT":0.48,"GAC":0.52},
        "C":{"TGT":0.38,"TGC":0.62},"Q":{"CAA":0.42,"CAG":0.58},
        "E":{"GAA":0.58,"GAG":0.42},"G":{"GGT":0.18,"GGC":0.30,"GGA":0.38,"GGG":0.14},
        "H":{"CAT":0.38,"CAC":0.62},"I":{"ATT":0.28,"ATC":0.52,"ATA":0.20},
        "L":{"TTA":0.08,"TTG":0.14,"CTT":0.28,"CTC":0.28,"CTA":0.06,"CTG":0.16},
        "K":{"AAA":0.48,"AAG":0.52},"F":{"TTT":0.32,"TTC":0.68},
        "P":{"CCT":0.28,"CCC":0.24,"CCA":0.32,"CCG":0.16},
        "S":{"TCT":0.22,"TCC":0.22,"TCA":0.12,"TCG":0.04,"AGT":0.18,"AGC":0.22},
        "T":{"ACT":0.25,"ACC":0.38,"ACA":0.22,"ACG":0.15},
        "W":{"TGG":1.00},"Y":{"TAT":0.32,"TAC":0.68},
        "V":{"GTT":0.22,"GTC":0.28,"GTA":0.18,"GTG":0.32},"M":{"ATG":1.00},
    },
}

aa_to_codons = {
    "A":["GCT","GCC","GCA","GCG"],"R":["CGT","CGC","CGA","CGG","AGA","AGG"],
    "N":["AAT","AAC"],"D":["GAT","GAC"],"C":["TGT","TGC"],"Q":["CAA","CAG"],
    "E":["GAA","GAG"],"G":["GGT","GGC","GGA","GGG"],"H":["CAT","CAC"],
    "I":["ATT","ATC","ATA"],"L":["TTA","TTG","CTT","CTC","CTA","CTG"],
    "K":["AAA","AAG"],"M":["ATG"],"F":["TTT","TTC"],"P":["CCT","CCC","CCA","CCG"],
    "S":["TCT","TCC","TCA","TCG","AGT","AGC"],"T":["ACT","ACC","ACA","ACG"],
    "W":["TGG"],"Y":["TAT","TAC"],"V":["GTT","GTC","GTA","GTG"],"*":["TAA","TAG","TGA"]
}
codon_to_aa = {c: aa for aa, codons in aa_to_codons.items() for c in codons}

def extract_orf(dna):
    dna = dna.upper().replace(" ", "").replace("\n", "")
    start = dna.find("ATG")
    if start == -1:
        return ""
    for i in range(start, len(dna)-2, 3):
        if dna[i:i+3] in ["TAA","TAG","TGA"]:
            return dna[start:i+3]
    return dna[start:]

def translate(dna):
    protein, codons = [], []
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        aa = codon_to_aa.get(codon, "X")
        if aa == "*":
            break
        protein.append(aa)
        codons.append(codon)
    return "".join(protein), codons

def calculate_cai(codons, variety):
    usage = codon_usage_data.get(variety, {})
    w_values = []
    for codon in codons:
        aa = codon_to_aa.get(codon)
        if aa and aa in usage and aa != "*":
            aa_usage = usage[aa]
            max_freq = max(aa_usage.values())
            codon_freq = aa_usage.get(codon, 0.01)
            w = codon_freq / max_freq if max_freq > 0 else 0.01
            w_values.append(math.log(max(w, 0.01)))
    if not w_values:
        return 0.0
    return round(math.exp(sum(w_values) / len(w_values)), 4)

def get_cai_grade(cai):
    if cai >= 0.80: return "EXCELLENT", "#00ff66"
    elif cai >= 0.60: return "GOOD", "#ffcc00"
    elif cai >= 0.40: return "MODERATE", "#ff9900"
    else: return "POOR", "#ff3333"

def optimize_with_trace(protein, original_codons, variety):
    usage = codon_usage_data.get(variety, {})
    optimized, trace = [], []
    for i, aa in enumerate(protein):
        original = original_codons[i] if i < len(original_codons) else "---"
        if aa in usage and usage[aa]:
            codon = max(usage[aa], key=usage[aa].get)
            freq = usage[aa][codon]
            reason = "High frequency codon selected"
        else:
            codon = aa_to_codons.get(aa, ["???"])[0]
            freq = 0.0
            reason = "Default fallback codon"
        optimized.append(codon)
        trace.append({"Position":i+1,"AA":aa,"Original Codon":original,"Optimized Codon":codon,"Frequency":round(freq,2),"Reason":reason})
    return "".join(optimized), pd.DataFrame(trace)

with st.sidebar:
    st.markdown("<div style='font-family:Orbitron,monospace;color:#1a8cff;font-size:1.1rem;letter-spacing:3px;text-align:center;margin-bottom:15px;'>🧬 BARAI-GENOME</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="info-card"><div class="info-label">STUDENT ID</div><div class="info-value">2206017</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><div class="info-label">DEPARTMENT</div><div class="info-value">Biotechnology & Genetic Engineering</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><div class="info-label">UNIVERSITY</div><div class="info-value">Sylhet Agricultural University</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><div class="info-label">VERSION</div><div class="info-value">v1.1 · 2026</div></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<div style='color:#1a8cff;font-size:0.75rem;letter-spacing:1px;'>📊 FEATURES</div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#fff;font-size:0.85rem;margin-top:5px;'>✅ All 20 Amino Acids<br>✅ CAI Scoring<br>✅ 6 Rice Varieties<br>✅ FASTA Export</div>", unsafe_allow_html=True)

st.markdown('<h1>🧬 BARAI-GENOME</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">EXPLAINABLE CODON OPTIMIZER · CAI SCORING · BANGLADESHI RICE VARIETIES</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="large")

with col1:
    st.markdown('<div class="section-box-red">', unsafe_allow_html=True)
    dna_input = st.text_area("🔴 Enter DNA Sequence", height=200, placeholder="Paste your DNA sequence here...")
    variety = st.selectbox("🔴 Select Rice Variety", list(codon_usage_data.keys()))
    run = st.button("⚡ RUN OPTIMIZATION")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run:
        if not dna_input.strip():
            st.warning("Please enter a DNA sequence.")
        else:
            orf = extract_orf(dna_input)
            if not orf:
                st.error("No ATG start codon found.")
            else:
                protein, original_codons = translate(orf)
                optimized, trace_df = optimize_with_trace(protein, original_codons, variety)
                _, optimized_codons = translate(optimized)
                original_cai = calculate_cai(original_codons, variety)
                optimized_cai = calculate_cai(optimized_codons, variety)
                grade, grade_color = get_cai_grade(optimized_cai)
                st.markdown('<div class="section-box-green">', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="cai-box">
                    <div style="color:#1a8cff;font-size:0.75rem;letter-spacing:2px;">CODON ADAPTATION INDEX (CAI)</div>
                    <div style="display:flex;justify-content:space-around;margin-top:10px;">
                        <div><div style="color:#aaa;font-size:0.75rem;">BEFORE</div>
                        <div style="font-family:Orbitron,monospace;font-size:1.8rem;color:#ff6b6b;">{original_cai}</div></div>
                        <div style="color:#1a8cff;font-size:2rem;margin-top:10px;">→</div>
                        <div><div style="color:#aaa;font-size:0.75rem;">AFTER</div>
                        <div style="font-family:Orbitron,monospace;font-size:1.8rem;color:#00ff66;">{optimized_cai}</div></div>
                        <div><div style="color:#aaa;font-size:0.75rem;">GRADE</div>
                        <div style="font-family:Orbitron,monospace;font-size:1.2rem;color:{grade_color};">{grade}</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown('<div class="result-header">🟢 ORF FOUND</div>', unsafe_allow_html=True)
                st.code(orf)
                st.markdown('<div class="result-header">🟢 PROTEIN SEQUENCE</div>', unsafe_allow_html=True)
                st.code(protein)
                st.markdown('<div class="result-header">🟢 OPTIMIZED DNA</div>', unsafe_allow_html=True)
                st.code(optimized)
                st.markdown('<div class="result-header">🟢 CODON TRACE TABLE</div>', unsafe_allow_html=True)
                st.dataframe(trace_df, use_container_width=True)
                fasta = f">original_sequence\n{orf}\n>optimized_{variety}_CAI_{optimized_cai}\n{optimized}"
                st.download_button("⬇ Download FASTA", fasta, file_name=f"BARAI_GENOME_{variety}.fasta")
                st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2026 BARAI-GENOME · ID: 2206017 · BGE · Sylhet Agricultural University</div>', unsafe_allow_html=True)

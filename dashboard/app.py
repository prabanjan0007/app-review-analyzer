import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="App Review Analyzer", page_icon="🧭", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "raw" / "reviews.csv"

if "light_mode" not in st.session_state:
    st.session_state.light_mode = False

if st.session_state.light_mode:
    BG, CARD, TEXT, MUTED, BORDER, GRID = "#f4f7fb", "rgba(255,255,255,.88)", "#172033", "#617089", "rgba(30,41,59,.12)", "rgba(30,41,59,.10)"
else:
    BG, CARD, TEXT, MUTED, BORDER, GRID = "#080d1c", "rgba(20,28,48,.78)", "#f8fafc", "#94a3b8", "rgba(148,163,184,.18)", "rgba(148,163,184,.12)"

st.markdown(f'''
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap");
html,body,[class*="css"]{{font-family:Inter,sans-serif}}
.stApp{{background:radial-gradient(circle at 5% 0%,rgba(99,102,241,.16),transparent 28%),radial-gradient(circle at 95% 8%,rgba(14,165,233,.12),transparent 28%),{BG};color:{TEXT}}}
.main .block-container{{max-width:1500px;padding:1.4rem 2rem 3rem}}
h1,h2,h3,h4,p,label{{color:{TEXT}!important}}
[data-testid="stHeader"]{{background:transparent}}
[data-testid="stToolbar"]{{visibility:hidden}}
div[data-baseweb="select"]>div{{background:{CARD};color:{TEXT};border:1px solid {BORDER};border-radius:10px}}
div[data-baseweb="select"] span{{color:{TEXT}}}
.stButton>button{{width:100%;min-height:42px;border-radius:10px;border:1px solid {BORDER};background:{CARD};color:{TEXT};font-weight:600}}
.stButton>button:hover{{border-color:rgba(99,102,241,.65)}}
.brand{{padding:1.35rem 1.55rem;border:1px solid {BORDER};border-radius:20px;background:linear-gradient(135deg,rgba(99,102,241,.17),rgba(14,165,233,.08)),{CARD};box-shadow:0 14px 38px rgba(0,0,0,.22);backdrop-filter:blur(14px)}}
.brand-row{{display:flex;align-items:center;gap:14px}}
.brand-icon{{width:52px;height:52px;display:grid;place-items:center;border-radius:14px;font-size:28px;background:linear-gradient(135deg,#6366f1,#06b6d4)}}
.brand-title{{font-size:1.45rem;font-weight:800;letter-spacing:-.03em}}
.brand-subtitle{{color:{MUTED};margin-top:4px;font-size:.9rem}}
.hero{{margin:1.25rem 0 1rem}}
.hero-title{{font-size:clamp(1.8rem,3vw,2.55rem);font-weight:800;letter-spacing:-.04em}}
.hero-subtitle{{color:{MUTED};font-size:.98rem}}
.section-title{{font-size:1.18rem;font-weight:800;margin:1.6rem 0 .8rem}}
.metric-card{{min-height:145px;padding:1.05rem 1.1rem;border-radius:17px;border:1px solid {BORDER};background:linear-gradient(145deg,rgba(255,255,255,.045),transparent 65%),{CARD};box-shadow:0 14px 38px rgba(0,0,0,.18);backdrop-filter:blur(12px)}}
.metric-label{{color:{MUTED};font-size:.82rem;font-weight:600;text-transform:uppercase;letter-spacing:.04em}}
.metric-value{{color:{TEXT};font-size:2rem;line-height:1.15;font-weight:800;margin-top:.65rem}}
.metric-note{{color:{MUTED};font-size:.78rem;margin-top:.45rem}}
.assessment{{margin:1rem 0 1.5rem;padding:.9rem 1.05rem;border-radius:14px;border:1px solid rgba(99,102,241,.30);background:linear-gradient(90deg,rgba(99,102,241,.15),rgba(14,165,233,.08))}}
.footer{{text-align:center;color:{MUTED};font-size:.78rem;padding:2rem 0 .5rem}}
</style>
''', unsafe_allow_html=True)

def sentiment_from_text(text):
    try:
        from textblob import TextBlob
        p = TextBlob(str(text)).sentiment.polarity
        return "Positive" if p > .08 else ("Negative" if p < -.08 else "Neutral")
    except Exception:
        return "Neutral"

def normalize_sentiment(value):
    s = str(value).strip().lower()
    if s in {"positive","pos","1"}: return "Positive"
    if s in {"negative","neg","-1"}: return "Negative"
    return "Neutral"

def theme_chart(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT, family="Inter, sans-serif"),
        margin=dict(l=25,r=25,t=70,b=30),
        legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(color=TEXT)),
        hoverlabel=dict(bgcolor=BG,font_color=TEXT,bordercolor=BORDER),
    )
    fig.update_xaxes(gridcolor=GRID, zerolinecolor=GRID, tickfont=dict(color=MUTED))
    fig.update_yaxes(gridcolor=GRID, zerolinecolor=GRID, tickfont=dict(color=MUTED))
    return fig

def title(fig, main, sub):
    fig.update_layout(title=dict(
        text=f"<b>{main}</b><br><span style='font-size:12px;color:{MUTED}'>{sub}</span>",
        x=.02, xanchor="left", y=.97))
    return fig

if not DATA_FILE.exists():
    st.error(f"Dataset not found: {DATA_FILE}")
    st.stop()

try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error(f"Could not read reviews.csv: {e}")
    st.stop()

df.columns = [str(c).strip().lower() for c in df.columns]
if "rating" not in df.columns:
    st.error("reviews.csv must contain a 'rating' column.")
    st.stop()

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df = df.dropna(subset=["rating"]).copy().reset_index(drop=True)
df["rating"] = df["rating"].clip(0,5)

sent_col = next((c for c in ["sentiment","sentiment_label","sentiment_category"] if c in df.columns), None)
if sent_col:
    df["sentiment"] = df[sent_col].apply(normalize_sentiment)
elif "review" in df.columns:
    df["sentiment"] = df["review"].fillna("").apply(sentiment_from_text)
else:
    df["sentiment"] = df["rating"].apply(lambda x: "Positive" if x >= 4 else ("Negative" if x <= 2 else "Neutral"))

app_col = next((c for c in ["application","app","app_name","application_name"] if c in df.columns), None)

a,b = st.columns([5,1])
with a:
    st.markdown('''
    <div class="brand"><div class="brand-row">
    <div class="brand-icon">🧭</div><div>
    <div class="brand-title">App Review Analyzer</div>
    <div class="brand-subtitle">User feedback, rating and sentiment intelligence</div>
    </div></div></div>
    ''', unsafe_allow_html=True)
with b:
    st.write("")
    if st.button("☀️ Light Mode" if not st.session_state.light_mode else "🌙 Dark Mode"):
        st.session_state.light_mode = not st.session_state.light_mode
        st.rerun()

st.markdown('''
<div class="hero"><div class="hero-title">Rating & Reviews Dashboard</div>
<div class="hero-subtitle">Monitor user satisfaction, feedback trends and review sentiment.</div></div>
''', unsafe_allow_html=True)

f1,f2,f3 = st.columns([1,1,.42])
with f1:
    if app_col:
        apps = ["All Applications"] + sorted(df[app_col].dropna().astype(str).unique().tolist())
        app = st.selectbox("Application", apps)
    else:
        app = "All Applications"
        st.selectbox("Application", ["Mobile App"], disabled=True)
with f2:
    review_type = st.selectbox("Review Type", ["All Reviews","Positive","Neutral","Negative"])
with f3:
    st.write(""); st.write("")
    if st.button("🔄 Refresh"): st.rerun()

filtered = df.copy()
if app_col and app != "All Applications":
    filtered = filtered[filtered[app_col].astype(str) == app]
if review_type != "All Reviews":
    filtered = filtered[filtered["sentiment"] == review_type]
if filtered.empty:
    st.warning("No reviews match the selected filters.")
    st.stop()

total = len(filtered)
avg = filtered["rating"].mean()
pos = int((filtered["sentiment"]=="Positive").sum())
neu = int((filtered["sentiment"]=="Neutral").sum())
neg = int((filtered["sentiment"]=="Negative").sum())
pos_pct,neu_pct,neg_pct = pos/total*100,neu/total*100,neg/total*100

st.markdown('<div class="section-title">📊 Overview</div>', unsafe_allow_html=True)
metrics = [
    ("⭐","Average Rating",f"{avg:.2f}/5",f"Based on {total} reviews"),
    ("💬","Total Reviews",str(total),"Review dataset"),
    ("🟢","Positive",f"{pos_pct:.1f}%",f"{pos} reviews"),
    ("🟡","Neutral",f"{neu_pct:.1f}%",f"{neu} reviews"),
    ("🔴","Negative",f"{neg_pct:.1f}%",f"{neg} reviews"),
]
cols=st.columns(5)
for c,(icon,label_,value,note) in zip(cols,metrics):
    with c:
        st.markdown(f'''<div class="metric-card">
        <div class="metric-label">{icon} {label_}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div></div>''', unsafe_allow_html=True)

if pos_pct >= 70:
    msg,icon="Strong user satisfaction with mostly positive feedback.","🟢"
elif neg_pct >= 35:
    msg,icon="User experience shows significant areas for improvement.","🔴"
else:
    msg,icon="User experience is mixed.","🟡"
st.markdown(f'<div class="assessment"><b>Overall Assessment:</b> {icon} {msg}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">📈 App Performance Overview</div>', unsafe_allow_html=True)

c1,c2=st.columns(2)
rating_counts=filtered["rating"].round().astype(int).value_counts().reindex([1,2,3,4,5],fill_value=0)
with c1:
    fig=go.Figure(go.Pie(
        labels=[f"{x} Star" for x in rating_counts.index], values=rating_counts.values, hole=.64,
        textinfo="percent",
        marker=dict(colors=["rgba(239,68,68,.82)","rgba(249,115,22,.82)","rgba(245,158,11,.82)","rgba(34,197,94,.82)","rgba(99,102,241,.88)"],line=dict(color="rgba(255,255,255,.1)",width=1)),
        hovertemplate="<b>%{label}</b><br>%{value} reviews<extra></extra>"))
    fig.add_annotation(text=f"<b>{avg:.2f}</b><br><span style='font-size:11px'>avg rating</span>",x=.5,y=.5,showarrow=False,font=dict(size=19,color=TEXT))
    theme_chart(title(fig,"⭐ Rating Distribution","How users rated the app"))
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
with c2:
    sc=filtered["sentiment"].value_counts().reindex(["Positive","Neutral","Negative"],fill_value=0)
    fig=go.Figure(go.Pie(
        labels=sc.index,values=sc.values,hole=.64,textinfo="percent",
        marker=dict(colors=["rgba(34,197,94,.84)","rgba(245,158,11,.84)","rgba(239,68,68,.84)"],line=dict(color="rgba(255,255,255,.1)",width=1)),
        hovertemplate="<b>%{label}</b><br>%{value} reviews<extra></extra>"))
    fig.add_annotation(text=f"<b>{pos_pct:.0f}%</b><br><span style='font-size:11px'>positive</span>",x=.5,y=.5,showarrow=False,font=dict(size=19,color=TEXT))
    theme_chart(title(fig,"🧠 Sentiment Distribution","Overall user sentiment"))
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

c3,c4=st.columns([1.65,1])
with c3:
    p=filtered.reset_index(drop=True).copy()
    p["review_number"]=range(1,len(p)+1)
    fig=go.Figure(go.Scatter(
        x=p["review_number"],y=p["rating"],mode="lines+markers",name="Rating",
        line=dict(width=3,color="rgba(96,165,250,.96)",shape="spline"),
        marker=dict(size=7,color="rgba(167,139,250,.96)",line=dict(width=1,color="rgba(255,255,255,.3)")),
        fill="tozeroy",fillcolor="rgba(59,130,246,.10)",
        hovertemplate="<b>Review %{x}</b><br>Rating: %{y:.1f}<extra></extra>"))
    fig.update_yaxes(range=[0,5.5],dtick=1)
    fig.update_xaxes(title_text="Review sequence")
    theme_chart(title(fig,"📈 Rating Dynamics","Rating movement across reviews"))
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
with c4:
    fig=go.Figure(go.Indicator(
        mode="gauge+number",value=pos_pct,
        number=dict(suffix="%",font=dict(size=34,color=TEXT)),
        title=dict(text="Positive Sentiment Score",font=dict(size=16,color=TEXT)),
        gauge=dict(axis=dict(range=[0,100],tickwidth=1,tickcolor="rgba(255,255,255,.22)"),
                   bar=dict(color="rgba(139,92,246,.88)",thickness=.24),bgcolor="rgba(255,255,255,.025)",borderwidth=0,
                   steps=[dict(range=[0,40],color="rgba(239,68,68,.12)"),dict(range=[40,70],color="rgba(245,158,11,.12)"),dict(range=[70,100],color="rgba(34,197,94,.12)")])
    ))
    theme_chart(title(fig,"🎯 Sentiment Score","Percentage of positive reviews"))
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

if "review" in filtered.columns:
    st.markdown('<div class="section-title">💬 Review Snapshot</div>', unsafe_allow_html=True)
    snap=filtered[["review","rating","sentiment"]].copy()
    snap["review"]=snap["review"].astype(str).str.slice(0,140)
    snap.columns=["Review","Rating","Sentiment"]
    st.dataframe(snap.head(8),use_container_width=True,hide_index=True)

st.markdown('<div class="footer">Mobile App Review Analyzer • Streamlit + Plotly</div>',unsafe_allow_html=True)

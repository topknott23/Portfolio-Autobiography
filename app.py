import streamlit as st
import pandas as pd
import altair as alt
import time

st.set_page_config(
    page_title="Joel Theo Gallarde",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #D6C9BC;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 4rem;
        max-width: 860px;
    }

    /* ---- Typography ---- */
    .hero-name {
        font-size: 2.6rem;
        font-weight: 700;
        color: #F5EFE8;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 10px;
    }
    .hero-role {
        font-size: 1rem;
        color: #C4A882;
        font-weight: 500;
        letter-spacing: 0.01em;
        margin-bottom: 28px;
    }
    .page-label {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #C4A882;
        margin-bottom: 6px;
    }
    .page-title {
        font-size: 1.9rem;
        font-weight: 700;
        color: #F5EFE8;
        letter-spacing: -0.025em;
        margin-bottom: 6px;
    }
    .page-desc {
        font-size: 0.95rem;
        color: #9E9088;
        margin-bottom: 32px;
        line-height: 1.6;
    }
    .section-title {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9E9088;
        margin-bottom: 14px;
        margin-top: 28px;
        padding-bottom: 6px;
        border-bottom: 1px solid #2C2319;
    }

    /* ---- Cards ---- */
    .card {
        background: #1C1712;
        border: 1px solid #2C2319;
        border-radius: 10px;
        padding: 20px 22px;
        margin-bottom: 14px;
    }
    .card-accent {
        background: #1C1712;
        border: 1px solid #2C2319;
        border-left: 3px solid #C4A882;
        border-radius: 10px;
        padding: 18px 22px;
        margin-bottom: 14px;
    }

    /* ---- Stat Row ---- */
    .stat-item {
        padding: 16px 18px;
        background: #1C1712;
        border: 1px solid #2C2319;
        border-radius: 9px;
    }
    .stat-val {
        font-size: 1.35rem;
        font-weight: 700;
        color: #C4A882;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }
    .stat-key {
        font-size: 0.73rem;
        color: #9E9088;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 3px;
    }

    /* ---- Tags ---- */
    .tag {
        display: inline-block;
        background: #14110E;
        color: #9E9088;
        border: 1px solid #2C2319;
        border-radius: 5px;
        padding: 2px 9px;
        font-size: 0.77rem;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .tag-highlight {
        background: rgba(196,168,130,0.1);
        color: #C4A882;
        border-color: rgba(196,168,130,0.3);
        font-weight: 600;
    }

    /* ---- Project Card ---- */
    .proj-num {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        color: #C4A882;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .proj-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #F5EFE8;
        margin-bottom: 4px;
        letter-spacing: -0.01em;
    }
    .proj-sub {
        font-size: 0.82rem;
        color: #C4A882;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .proj-body {
        font-size: 0.9rem;
        color: #D6C9BC;
        line-height: 1.7;
        margin-bottom: 14px;
    }

    /* ---- Story ---- */
    .chapter-num {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        color: #C4A882;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .chapter-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #F5EFE8;
        margin-bottom: 10px;
        letter-spacing: -0.01em;
    }
    .chapter-body {
        font-size: 0.9rem;
        color: #D6C9BC;
        line-height: 1.75;
    }
    .chapter-block {
        padding-bottom: 24px;
        margin-bottom: 24px;
        border-bottom: 1px solid #2C2319;
    }

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {
        background: #111009;
        border-right: 1px solid #231D16;
    }
    .sb-label {
        font-size: 0.67rem;
        font-weight: 700;
        letter-spacing: 0.09em;
        text-transform: uppercase;
        color: #6B5E52;
        margin-bottom: 8px;
        margin-top: 20px;
    }
    .sb-link {
        font-size: 0.82rem;
        color: #B5A598;
        line-height: 2.1;
        text-decoration: none;
    }

    /* Nav buttons in sidebar */
    section[data-testid="stSidebar"] div.stButton > button {
        width: 100%;
        border-radius: 7px;
        font-size: 0.88rem;
        font-weight: 500;
        padding: 0.48rem 0.9rem;
        margin-bottom: 3px;
        text-align: left;
        justify-content: flex-start;
        transition: all 0.12s ease;
        letter-spacing: 0.005em;
    }
    section[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
        background: transparent;
        border: 1px solid transparent;
        color: #A89A8E;
    }
    section[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
        background: #1C1712;
        border-color: #2C2319;
        color: #F5EFE8;
    }
    section[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
        background: #C4A882;
        border: 1px solid #C4A882;
        color: #111009;
        font-weight: 600;
    }
    section[data-testid="stSidebar"] div.stButton > button[kind="primary"]:hover {
        background: #CEB48F;
        border-color: #CEB48F;
    }

    /* Main content buttons */
    div.block-container div.stButton > button {
        border-radius: 7px;
        border: 1px solid #2C2319;
        background: #1C1712;
        color: #D6C9BC;
        font-weight: 500;
        font-size: 0.88rem;
        padding: 0.48rem 1rem;
        transition: all 0.12s ease;
    }
    div.block-container div.stButton > button:hover {
        border-color: #C4A882;
        color: #C4A882;
    }

    /* Form inputs */
    .stTextInput input, .stTextArea textarea {
        background: #111009 !important;
        border: 1px solid #2C2319 !important;
        border-radius: 7px !important;
        color: #F5EFE8 !important;
        font-size: 0.9rem !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #C4A882 !important;
        box-shadow: 0 0 0 1px rgba(196,168,130,0.4) !important;
    }

    /* Divider */
    hr {
        border-color: #2C2319 !important;
        margin: 28px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

valid_pages = ["Home", "Autobiography", "Skills", "Projects", "Contact"]

if "page" not in st.session_state or st.session_state.page not in valid_pages:
    st.session_state.page = "Home"
if "likes" not in st.session_state:
    st.session_state.likes = 14

with st.sidebar:
    st.markdown(f"""
    <div style="padding: 18px 0 16px; border-bottom: 1px solid #231D16; margin-bottom: 4px;">
        <div style="width: 38px; height: 38px; border-radius: 8px; background: #C4A882;
                    display: flex; align-items: center; justify-content: center;
                    font-weight: 800; font-size: 0.95rem; color: #111009;
                    letter-spacing: -0.02em; margin-bottom: 12px;">JG</div>
        <div style="font-size: 0.97rem; font-weight: 700; color: #F5EFE8; line-height: 1.3;">Joel Theo C. Gallarde</div>
        <div style="font-size: 0.78rem; color: #C4A882; margin-top: 3px; font-weight: 500;">BS Computer Science</div>
        <div style="font-size: 0.75rem; color: #6B5E52; margin-top: 2px;">CIT-University · Class of 2026</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-label">Navigate</div>', unsafe_allow_html=True)
    for p in valid_pages:
        is_active = st.session_state.page == p
        if st.button(p, key=f"nav_{p}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.page = p
            st.rerun()

    st.markdown('<div class="sb-label">Endorse</div>', unsafe_allow_html=True)
    col_e, col_n = st.columns([1, 1])
    with col_e:
        if st.button("+ Endorse", key="endorse_btn", use_container_width=True):
            st.session_state.likes += 1
            st.rerun()
    with col_n:
        st.markdown(
            f"<div style='padding-top: 8px; font-size: 0.82rem; color: #9E9088;'>"
            f"<strong style='color:#D6C9BC'>{st.session_state.likes}</strong> so far</div>",
            unsafe_allow_html=True
        )

    st.markdown('<div class="sb-label">Contact</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 0.8rem; line-height: 2.1; color: #B5A598;">
        <div><a href="mailto:gallardejoeltheo@gmail.com" style="color:#C4A882; text-decoration:none;">gallardejoeltheo@gmail.com</a></div>
        <div><a href="https://github.com/topknott23" target="_blank" style="color:#9E9088; text-decoration:none;">github.com/topknott23</a></div>
        <div><a href="https://linkedin.com/in/joeltheogallarde" target="_blank" style="color:#9E9088; text-decoration:none;">linkedin.com/in/joeltheogallarde</a></div>
        <div style="color:#6B5E52;">09934123624</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 28px; font-size: 0.7rem; color: #4A3F36;'>CSIT 349 · Applied AI</div>", unsafe_allow_html=True)


if st.session_state.page == "Home":
    st.markdown('<div class="page-label">Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-name">Joel Theo C. Gallarde</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-role">Computer Science Student · Game Developer · Full-Stack Engineer</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom: 28px;">
        <div style="font-size: 0.95rem; line-height: 1.8; color: #D6C9BC;">
            BSCS student at <strong style="color:#F5EFE8">CIT-University</strong>, consistent Honor Student with a 4.59 GWA.
            Selected to represent CIT-U at the <strong style="color:#F5EFE8">GDAP ICon 2026 Game Showcase</strong> at SM Seaside City, Cebu.
            I build 2D games in Godot 4 and full-stack web applications with React, Next.js, and Supabase.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("4.59 GWA", "Honor Student"),
        ("ICon 2026", "GDAP Showcase"),
        ("CodeChum", "Java & C Certified"),
        ("2028", "Expected Graduation"),
    ]
    for col, (val, key) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-item">
                <div class="stat-val">{val}</div>
                <div class="stat-key">{key}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)

    col_l, col_r = st.columns([3, 2])
    with col_l:
        st.markdown("""
        <div class="card">
            <div style="font-size: 0.88rem; font-weight: 600; color: #F5EFE8; margin-bottom: 12px;">What I work on</div>
            <div style="font-size: 0.9rem; color: #D6C9BC; line-height: 1.75;">
                <div style="margin-bottom: 10px;"><strong style="color:#F5EFE8">Game Development</strong> &mdash; 2D game loops, collision systems, state machines, and character mechanics in Godot 4 (GDScript) and C++.</div>
                <div style="margin-bottom: 10px;"><strong style="color:#F5EFE8">Full-Stack Web</strong> &mdash; Responsive frontends in React.js and Next.js, backed by Node.js, Express, and Supabase (PostgreSQL).</div>
                <div><strong style="color:#F5EFE8">Software Foundations</strong> &mdash; Object-oriented programming in Java and C++, data structures, and procedural C systems.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown("""
        <div class="card">
            <div style="font-size: 0.88rem; font-weight: 600; color: #F5EFE8; margin-bottom: 12px;">Quick Facts</div>
            <div style="font-size: 0.85rem; color: #D6C9BC; line-height: 2.1;">
                <div>Talisay City, Cebu, PH</div>
                <div>CIT - University (BSCS)</div>
                <div>Honor Student · 4.59 GWA</div>
                <div>High Honors HS Grad, 2024</div>
                <div>Wildcats PlayLab</div>
                <div>GDSC CIT-U</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-accent">
        <div style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #C4A882; margin-bottom: 6px;">Open to Opportunities</div>
        <div style="font-size: 0.92rem; color: #D6C9BC; line-height: 1.7;">
            Looking for an <strong style="color:#F5EFE8">internship or junior developer role</strong> in game development, software engineering, or full-stack web. Eager to contribute to real production code and learn alongside experienced engineers.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Explore</div>', unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3)
    for col, label, page in zip([b1, b2, b3], ["My Story", "Skills & Certs", "Projects"], ["Autobiography", "Skills", "Projects"]):
        with col:
            if st.button(label, key=f"home_{page}", use_container_width=True):
                st.session_state.page = page
                st.rerun()


elif st.session_state.page == "Autobiography":
    st.markdown('<div class="page-label">Background</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">My Story</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-desc">From Talisay City to representing CIT-U at GDAP ICon 2026.</div>', unsafe_allow_html=True)

    chapters = [
        ("01", "Early Curiosity & High Honors (2024)",
         "Growing up in Tuburan, Cebu, my fascination with technology began with gaming. Playing games evolved into wanting to understand how they worked — how hitboxes detect collisions, how player states transition cleanly, how memory manages sprites. Throughout Junior and Senior High School I balanced that curiosity with academic discipline, graduating with <strong style='color:#F5EFE8'>High Honors in 2024</strong> as a consistent honor student."),
        ("02", "BSCS at CIT-University & Academic Standing",
         "Entering the <strong style='color:#F5EFE8'>BS Computer Science</strong> program at CIT-University was the formal start of my engineering education. I worked through data structures, algorithmic analysis, OOP in Java and C++, and structured C — earning CodeChum certifications along the way. Through consistent effort I reached <strong style='color:#F5EFE8'>Honor Student standing with a 4.59 GWA</strong>."),
        ("03", "Game Programming & Mire: Protocol Zero",
         "Outside coursework I poured time into game development with the <strong style='color:#F5EFE8'>Wildcats PlayLab</strong>, learning Godot 4, GDScript, and 2D physics. Together with my team I co-developed <strong style='color:#F5EFE8'>Mire: Protocol Zero</strong> — an objective-based 2D multiplayer arena game with five character classes, custom cooldown systems, collision pipelines, and dynamic camera tracking. Working inside 60 FPS frame budgets taught me to write edge-case-resilient, performance-conscious code."),
        ("04", "GDAP ICon 2026 — SM Seaside City Cebu",
         "In September 2026 I was selected as a University Representative for CIT-U at the <strong style='color:#F5EFE8'>Imaginators Convention (ICon 2026)</strong>, co-organized by the Game Developers Association of the Philippines (GDAP) at SM Seaside City Cebu. Pitching and demoing <em>Mire: Protocol Zero</em> to industry professionals, collecting live player feedback, and troubleshooting edge-case bugs under real convention pressure was one of the most defining experiences of my CS journey so far."),
        ("05", "Community & What's Next",
         "As an active member of <strong style='color:#F5EFE8'>GDSC CIT-U</strong>, I participate in peer workshops on React.js, Next.js, and Supabase. With graduation expected in 2028, my next step is an internship where I can write production-grade code, learn from senior engineers, and keep growing as a developer."),
    ]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    for i, (num, title, body) in enumerate(chapters):
        is_last = (i == len(chapters) - 1)
        st.markdown(f"""
        <div class="{'chapter-block' if not is_last else ''}">
            <div class="chapter-num">Chapter {num}</div>
            <div class="chapter-title">{title}</div>
            <div class="chapter-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


elif st.session_state.page == "Skills":
    st.markdown('<div class="page-label">Technical Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Skills & Certifications</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-desc">Aligned with my CV, coursework, and production projects.</div>', unsafe_allow_html=True)

    skills_data = pd.DataFrame([
        {"Technology": "Godot 4 / GDScript", "Category": "Game & Graphics", "Level": 92, "Experience": "5 months"},
        {"Technology": "Git & GitHub",        "Category": "Developer Tools",  "Level": 88, "Experience": "2 years"},
        {"Technology": "Java (OOP Cert.)",    "Category": "Languages",        "Level": 88, "Experience": "1 year"},
        {"Technology": "C++",                 "Category": "Languages",        "Level": 85, "Experience": "1.5 years"},
        {"Technology": "C (Structured Cert.)","Category": "Languages",        "Level": 85, "Experience": "1 year"},
        {"Technology": "React.js / Next.js",  "Category": "Web & Backend",    "Level": 84, "Experience": "1 year"},
        {"Technology": "Supabase / PostgreSQL","Category": "Web & Backend",   "Level": 82, "Experience": "1 year"},
        {"Technology": "JavaScript / TS",     "Category": "Languages",        "Level": 82, "Experience": "1 year"},
        {"Technology": "Tailwind CSS / Vite", "Category": "Web & Backend",    "Level": 82, "Experience": "1 year"},
        {"Technology": "Node.js / Express",   "Category": "Web & Backend",    "Level": 80, "Experience": "1 year"},
        {"Technology": "Kotlin",              "Category": "Languages",        "Level": 78, "Experience": "1 year"},
    ])

    col_f1, col_f2 = st.columns([2, 2])
    with col_f1:
        cat = st.selectbox("Category", ["All"] + sorted(skills_data["Category"].unique().tolist()))
    with col_f2:
        min_lvl = st.slider("Minimum level (%)", 0, 100, 70)

    filtered = skills_data.copy()
    if cat != "All":
        filtered = filtered[filtered["Category"] == cat]
    filtered = filtered[filtered["Level"] >= min_lvl]

    if not filtered.empty:
        chart = alt.Chart(filtered).mark_bar(color="#C4A882", cornerRadiusEnd=3).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100]), title="Level (%)",
                    axis=alt.Axis(labelColor="#6B5E52", gridColor="#1C1712", titleColor="#6B5E52")),
            y=alt.Y("Technology:N", sort="-x", title=None,
                    axis=alt.Axis(labelColor="#D6C9BC")),
            tooltip=["Technology", "Category", "Level", "Experience"]
        ).properties(height=max(220, len(filtered) * 34), background="transparent").configure_view(strokeOpacity=0)
        st.altair_chart(chart, use_container_width=True)

        st.dataframe(
            filtered.rename(columns={"Level": "Level (%)"})[["Technology", "Category", "Level (%)", "Experience"]],
            hide_index=True,
            use_container_width=True
        )
    else:
        st.info("No results. Adjust the filters above.")

    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("""
        <div class="card">
            <div style="font-size: 0.92rem; font-weight: 600; color: #F5EFE8;">CITU Java Object-Oriented Programming</div>
            <div style="font-size: 0.78rem; color: #C4A882; margin: 4px 0 8px;">CodeChum &middot; May 2026</div>
            <div style="font-size: 0.85rem; color: #D6C9BC; line-height: 1.6;">OOP principles, class hierarchies, interfaces, and algorithmic problem-solving.</div>
        </div>
        """, unsafe_allow_html=True)
    with cc2:
        st.markdown("""
        <div class="card">
            <div style="font-size: 0.92rem; font-weight: 600; color: #F5EFE8;">CITU C Programming 1</div>
            <div style="font-size: 0.78rem; color: #C4A882; margin: 4px 0 8px;">CodeChum &middot; April 2025</div>
            <div style="font-size: 0.85rem; color: #D6C9BC; line-height: 1.6;">Procedural logic, memory pointers, and structured C syntax assessments.</div>
        </div>
        """, unsafe_allow_html=True)


elif st.session_state.page == "Projects":
    st.markdown('<div class="page-label">Work</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Projects & Showcases</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-desc">Games, convention showcases, and full-stack software.</div>', unsafe_allow_html=True)

    projects = [
        ("01", "Mire: Protocol Zero", "2D Multiplayer Arena Game · Godot 4 & GDScript",
         "ICon 2026 Featured Title",
         "Featured at the GDAP Imaginators Convention (ICon 2026), SM Seaside City Cebu. Built a Capture-the-Core gameplay loop with tactical coordination and strategic combat. Programmed five character classes with cooldown systems, FSM-based state logic, and ultimate abilities. Configured custom 2D physics, dynamic camera tracking, and sprite rendering pipelines for stable 60 FPS performance.",
         ["Godot 4", "GDScript", "2D Physics", "State Machines", "Multiplayer"]),
        ("02", "Wildcats PlayLab / GDAP Showcase", "Game Developer & University Representative · SM Seaside City Cebu, Sep 2026",
         "CIT-U University Rep",
         "Represented CIT-University at ICon 2026, presenting student-built games to studio leaders and industry professionals. Ran live booth playtests, collected real-time player feedback, and applied rapid gameplay balance changes between exhibition sessions.",
         ["GDAP", "Live Demo", "Player Testing", "Game Balance"]),
        ("03", "Full-Stack Web App (Supabase)", "React.js · Next.js · Node.js · Supabase (PostgreSQL)",
         "Full-Stack",
         "Responsive web application with a React/Next.js frontend and Tailwind CSS. Backed by Node.js REST APIs and Supabase for cloud PostgreSQL, row-level security auth, and file storage.",
         ["React.js", "Next.js", "Supabase", "PostgreSQL", "Tailwind CSS"]),
    ]

    for num, title, sub, badge, body, tags in projects:
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="card" style="margin-bottom: 16px;">
            <div class="proj-num">Project {num}</div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
                <div class="proj-title">{title}</div>
                <span class="tag tag-highlight" style="flex-shrink:0; margin-left:10px;">{badge}</span>
            </div>
            <div class="proj-sub">{sub}</div>
            <div class="proj-body">{body}</div>
            <div>{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)


elif st.session_state.page == "Contact":
    st.markdown('<div class="page-label">Let\'s Talk</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Get in Touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-desc">Reach out via email or any of the links below.</div>', unsafe_allow_html=True)

    col_form, col_info = st.columns([3, 2])

    with col_form:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name")
            email = st.text_input("Email")
            reason = st.selectbox("Reason", ["Internship Opportunity", "Game Dev Collaboration", "Software Project", "General"])
            message = st.text_area("Message", placeholder="Your message here...")
            sent = st.form_submit_button("Send Message", use_container_width=True)

        if sent:
            if not name.strip() or not message.strip():
                st.error("Please fill in your name and message.")
            else:
                with st.spinner("Sending..."):
                    time.sleep(0.6)
                st.success(f"Message received, {name}. I'll get back to you soon.")

    with col_info:
        st.markdown("""
        <div class="card">
            <div style="font-size: 0.88rem; font-weight: 600; color: #F5EFE8; margin-bottom: 14px;">Contact Details</div>
            <div style="font-size: 0.85rem; color: #D6C9BC; line-height: 2.3;">
                <div>Talisay City, Cebu, Philippines</div>
                <div><a href="mailto:gallardejoeltheo@gmail.com" style="color:#C4A882; text-decoration:none;">gallardejoeltheo@gmail.com</a></div>
                <div style="color: #9E9088;">09934123624</div>
                <div><a href="https://github.com/topknott23" target="_blank" style="color:#9E9088; text-decoration:none;">github.com/topknott23</a></div>
                <div><a href="https://linkedin.com/in/joeltheogallarde" target="_blank" style="color:#9E9088; text-decoration:none;">linkedin.com/in/joeltheogallarde</a></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        cv_text = """JOEL THEO C. GALLARDE
Talisay City, Cebu, Philippines | 09934123624
gallardejoeltheo@gmail.com | github.com/topknott23 | linkedin.com/in/joeltheogallarde

EDUCATION
CIT - University, Cebu City
BS Computer Science (BSCS) — Expected 2028
Honor Student | GWA: 4.59

Senior & Junior High School — Graduated 2024
High Honors; Consistent Honor Student

EXPERIENCE
Wildcats PlayLab / GDAP Showcase — Sep 2026
Game Developer & University Representative, ICon 2026
SM Seaside City Cebu

- Co-developed and showcased Mire: Protocol Zero at GDAP ICon 2026
- Presented to industry professionals and gathered live player feedback
- Optimized gameplay balance and fixed edge-case bugs under event conditions

Google Developer Student Clubs (GDSC CIT-U) — Aug 2024–Present
Active Member

PROJECTS
Mire: Protocol Zero — Godot 4, GDScript
- Objective-based 2D multiplayer arena game, ICon 2026 featured title
- 5 character classes, cooldown FSMs, 2D physics pipelines

Full-Stack Web App — React.js, Next.js, Supabase (PostgreSQL)

CERTIFICATIONS
CITU Java OOP Certification (CodeChum, May 2026)
CITU C Programming 1 Certification (CodeChum, April 2025)

SKILLS
Languages: C++, Java, C, GDScript, JavaScript, TypeScript, Kotlin, SQL
Game: Godot 4, 2D Physics, State Machines, Animation Player
Web: React.js, Next.js, Node.js, Express, Supabase, Tailwind CSS, Vite
Tools: Git, GitHub, Docker, Postman, Vercel, VS Code"""

        st.download_button(
            "Download CV (TXT)",
            data=cv_text,
            file_name="Joel_Theo_Gallarde_CV.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#4A3F36; font-size:0.78rem; padding: 6px 0;'>"
    "Joel Theo C. Gallarde &middot; CIT-University &middot; Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
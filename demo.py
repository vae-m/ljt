import streamlit as st
import random
import os
import base64

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="朵朵大王天天开心",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# 读取背景图（Base64 确保云端显示）
# ======================
bg_image_path = "picture/01.jpg"
bg_image_b64 = None

if os.path.exists(bg_image_path):
    try:
        with open(bg_image_path, "rb") as f:
            bg_image_b64 = base64.b64encode(f.read()).decode()
    except:
        bg_image_b64 = None

# ======================
# CSS：文字直接叠加在图片上，无白框
# ======================
if bg_image_b64:
    bg_style = f"""
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
        color: white; /* 默认文字白色 */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
        line-height: 1.7;
    }}
    """
else:
    bg_style = ".stApp { background: #222; color: white; }"

st.markdown(f"""
<style>
    {bg_style}
    
    #MainMenu, header, footer {{visibility: hidden;}}
    
    h1 {{
        text-align: center;
        font-weight: 600;
        font-size: 1.8em;
        color: white;
        margin: 2rem 0 1.5rem;
        letter-spacing: 1px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
    }}
    
    .quote-text {{
        font-size: 1.3em;
        text-align: center;
        line-height: 1.8;
        color: white;
        font-weight: 500;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        max-width: 600px;
        margin: 2rem auto;
        padding: 1.5rem;
    }}
    
    /* 按钮：透明爱心，带阴影 */
    .stButton > button {{
        background: transparent;
        border: none;
        font-size: 1.6em;
        color: white;
        margin: 1.2rem auto;
        display: block;
        transition: all 0.25s ease;
        width: auto;
        height: auto;
        padding: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
    }}
    .stButton > button:hover {{
        color: #ffcccb;
        transform: scale(1.2);
    }}
    .stButton > button:active {{
        transform: scale(1.05);
    }}
    
    .personal {{
        font-size: 1.1em;
        text-align: center;
        color: white;
        font-weight: 500;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        max-width: 600px;
        margin: 2rem auto;
        padding: 1.5rem;
    }}
    
    .footer {{
        text-align: center;
        color: #ddd;
        font-size: 0.9em;
        margin-top: 2.5rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(255,255,255,0.3);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 语录库（温柔自然）
# ======================
quotes = [
    "今天也要开心呀！",
    "你笑起来真好看。",
    "希望你每天都被温柔对待。",
    "累了就休息，别太辛苦自己。",
    "你值得所有美好。",
    "今天的你，也很棒！",
    "记得多喝水，按时吃饭。",
    "世界很大，但你很重要。",
    "开心是一种选择，你选对了。",
    "愿你眼里有光，心中有爱。",
    "平凡的日子，也因你而闪亮。",
    "慢慢来，一切都来得及。",
    "你开心，我就开心。",
    "今天有什么好事发生吗？",
    "你就是你，不需要完美。"
]

# ======================
# 主内容（直接叠加在图片上）
# ======================
st.title("朵朵大王天天开心")

# 切换语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

st.markdown(f"""
<div class="quote-text">
    {st.session_state.current_quote}
</div>
""", unsafe_allow_html=True)

# 专属文字
st.markdown("""
<div class="personal">
朵朵大王：<br>
我只是希望你每天都能开开心心的。<br>
如果累了，就看看这里。<br>
我一直都在。
</div>
""", unsafe_allow_html=True)

# 页脚
st.markdown("""
<div class="footer">
Made for you • 愿你天天开心
</div>
""", unsafe_allow_html=True)

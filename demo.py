import streamlit as st
import random
import os

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="刘家彤天天开心",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# 主内容：先显示背景图（全屏）
# ======================
bg_image_path = "picture/01.jpg"

# 全屏背景图（固定在底层）
if os.path.exists(bg_image_path):
    # 使用 st.image 显示背景
    st.markdown(
        """
        <style>
        .bg-image {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -2;
        }
        .overlay {
            position: relative;
            z-index: 1;
            background: rgba(255, 255, 255, 0.88);
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # 用 st.image 输出图片，并添加 class
    st.image(bg_image_path, use_column_width=True, caption="")
    st.markdown('<div class="overlay">', unsafe_allow_html=True)
else:
    st.markdown('<div style="background:#fcfcfc; min-height:100vh; padding:20px;">', unsafe_allow_html=True)

# ======================
# 内容区（在 overlay 内）
# ======================
st.markdown(
    """
    <style>
    .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
        color: #222;
        line-height: 1.7;
    }
    #MainMenu, header, footer {visibility: hidden;}
    
    h1 {
        text-align: center;
        font-weight: 600;
        font-size: 1.6em;
        color: #e74c3c;
        margin: 1.8rem 0 1.4rem;
        letter-spacing: 1px;
    }
    
    .quote-box {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 620px;
        box-shadow: 0 8px 30px rgba(231, 76, 60, 0.12);
        border: 1px solid #f8f8f8;
    }
    .quote-text {
        font-size: 1.3em;
        text-align: center;
        line-height: 1.8;
        color: #1a1a1a;
        font-weight: 500;
    }
    
    .stButton > button {
        background: transparent;
        border: none;
        font-size: 1.6em;
        color: #e74c3c;
        margin: 1.2rem auto;
        display: block;
        transition: all 0.25s ease;
        width: auto;
        height: auto;
        padding: 0;
    }
    .stButton > button:hover {
        color: #c0392b;
        transform: scale(1.2);
    }
    .stButton > button:active {
        transform: scale(1.05);
    }
    
    .personal {
        background: white;
        padding: 1.8rem;
        border-radius: 16px;
        margin: 2rem auto;
        max-width: 620px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(231, 76, 60, 0.12);
        font-size: 1.2em;
        color: #1a1a1a;
        font-weight: 500;
    }
    
    .footer {
        text-align: center;
        color: #aaa;
        font-size: 0.95em;
        margin-top: 2.5rem;
        padding-top: 1rem;
        border-top: 1px solid #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("刘家彤天天开心")

# 语录库
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

# 切换语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

st.markdown(f"""
<div class="quote-box">
    <div class="quote-text">{st.session_state.current_quote}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="personal">
家彤：<br>
我只是希望你每天都能开开心心的。<br>
如果累了，就看看这里。<br>
我一直都在。
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
Made for you • 愿你天天开心
</div>
""", unsafe_allow_html=True)

# 关闭 overlay
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import random
import os

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
# 隐藏默认元素
# ======================
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    
    /* 所有文字内容水平居中 */
    .centered-content {
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .title {
        font-weight: 600;
        font-size: 1.8em;
        margin: 1rem 0;
        color: #333;
    }
    
    .quote {
        font-size: 1.3em;
        line-height: 1.7;
        margin: 1.5rem 0;
        color: #222;
    }
    
    .personal {
        font-size: 1.1em;
        margin: 1.5rem 0;
        color: #444;
        line-height: 1.6;
    }
    
    .footer {
        color: #777;
        font-size: 0.9em;
        margin-top: 2rem;
    }
    
    /* 按钮居中 */
    .stButton > button {
        display: block;
        margin: 1.5rem auto;
        font-size: 1.6em;
        border: none;
        background: transparent;
        color: #e74c3c;
    }
    .stButton > button:hover {
        color: #e91e63;
        transform: scale(1.1);
        transition: transform 0.2s;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# 显示图片（左右居中）
# ======================
bg_path = "picture/demo2.jpg"
if os.path.exists(bg_path):
    st.image(bg_path, use_container_width=True)  # 自动居中，宽度适配
else:
    st.warning("图片 picture/demo2.jpg 未找到，仅显示文字内容。")

# ======================
# 文字内容（全部左右居中）
# ======================
st.markdown('<div class="centered-content">', unsafe_allow_html=True)

st.markdown('<div class="title">朵朵大王天天开心</div>', unsafe_allow_html=True)

# 语录库
quotes = [
    "朵朵，你是一个很温柔的人呀！",
    "朵王记得自信。",
    "愿你被这个世界温柔以待。",
    "累了就休息，别太辛苦自己。",
    "你值得所有美好。",
    "今天的你，也很棒！",
    "记得多喝水，按时吃饭。",
    "世界很大，但你很重要。",
    "我爱你有种左灯右行的冲突。",
    "愿你眼里有光，心中有爱。",
    "我的人生暗淡如水，谢谢你照进来的光。",
    "慢慢来，一切都来得及。",
    "努力挣钱，给朵朵花",
    "谢谢你在世界的角落里把我找到",
    "我喜欢的是完整的你。"
]

# 初始化语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# 切换按钮
if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

st.markdown(f'<div class="quote">{st.session_state.current_quote}</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>如果累了，就休息一下。<br>我会一直等着朵朵的。</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="footer">Made for you • 愿你天天开心</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

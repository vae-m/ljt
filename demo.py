import streamlit as st
import random
import time
import os

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="peaceful love",
    page_icon="📜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# 极简 CSS：新增图片样式（柔和、不抢眼）
# ======================
st.markdown("""
<style>
    .stApp {
        background: #fdf6f0;
        font-family: "STKaiti", "KaiTi", "华文楷体", serif;
        color: #3e3e3e;
        line-height: 1.7;
    }
    
    #MainMenu, header, footer {visibility: hidden;}
    
    h1 {
        text-align: center;
        font-weight: 400;
        font-size: 1.4em;
        color: #5a5a5a;
        margin: 2rem 0 1.5rem;
        letter-spacing: 2px;
    }
    
    .quote-box {
        background: rgba(255, 250, 240, 0.6);
        border: 1px solid #e8e0d5;
        border-radius: 4px;
        padding: 1.4rem;
        margin: 1.8rem 0;
        font-size: 1.05em;
        position: relative;
    }
    .quote-box::before {
        content: "“";
        position: absolute;
        top: -10px;
        left: 10px;
        font-size: 2.2em;
        color: #c9b8a5;
        font-family: serif;
    }
    .quote-box::after {
        content: "”";
        position: absolute;
        bottom: -20px;
        right: 15px;
        font-size: 2.2em;
        color: #c9b8a5;
        font-family: serif;
    }
    
    .author {
        text-align: right;
        font-size: 0.9em;
        color: #8a8a8a;
        margin-top: 0.8rem;
    }
    
    .stButton > button {
        background: transparent;
        border: none;
        color: #8a8a8a;
        font-size: 0.95em;
        padding: 0.4rem 0;
        margin: 0.5rem auto;
        display: block;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        color: #5a5a5a;
        transform: scale(1.02);
    }
    
    .personal {
        font-family: "STXingkai", "华文行楷", cursive;
        font-size: 1.1em;
        text-align: center;
        margin: 1.5rem 0;
        color: #4a4a4a;
        opacity: 0.9;
    }
    
    /* 图片容器：圆角、阴影、居中 */
    .photo-container {
        text-align: center;
        margin: 1.8rem 0;
        opacity: 0;
        animation: fadeIn 1s forwards;
    }
    @keyframes fadeIn {
        to { opacity: 1; }
    }
    .photo-container img {
        max-width: 90%;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border: 1px solid #f0e8e0;
    }
    
    .footer {
        text-align: center;
        color: #b0a89e;
        font-size: 0.8em;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #f0e8e0;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 王小波语录
# ======================
quotes = [
    "静下来想你，觉得一切都美好得不可思议。",
    "我和你就像两个小孩子，围着一个神秘的果酱罐，一点一点地尝它。",
    "你是非常可爱的人，真应该遇到最好的人，我也真希望我就是。",
    "不管我本人多么平庸，我总觉得对你的爱很美。",
    "我希望我们是一对海豚，永远在水里游，永远不分离。",
    "你要是愿意，我就永远爱你；你要是不愿意，我就永远相思。",
    "我们应当在一起，否则就太伤天害理了。",
    "你的名字，是我见过最短的情诗。"
]

# ======================
# 主内容
# ======================
st.title("love in peace")

# 随机语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# ✅ 修复1: 为第一个按钮添加唯一 key
if st.button("·", key="change_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

st.markdown(f"""
<div class="quote-box">
    {st.session_state.current_quote}
    <div class="author">—— 王小波</div>
</div>
""", unsafe_allow_html=True)

# 专属文字
st.markdown("""
<div class="personal">
致家彤：<br>
有些话不必说尽，<br>
如同月光不必照亮整片海。<br>
但你知道，<br>
我在。
</div>
""", unsafe_allow_html=True)

# ======================
# 含蓄的「查看美照」功能
# ======================
st.markdown("<div style='text-align:center; margin:1.5rem 0; color:#a89e95;'>· · ·</div>", unsafe_allow_html=True)

# ✅ 修复2: 为照片按钮添加 key（虽然标签不同，但加 key 更规范）
if st.button("· ·", key="view_photo"):
    # 检查图片是否存在
    photo_path = "picture/01.jpg"
    if os.path.exists(photo_path):
        st.markdown('<div class="photo-container">', unsafe_allow_html=True)
        st.image(photo_path, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div style="text-align:center; color:#b0a89e; font-size:0.95em; margin:1rem 0;">'
            '照片正在路上…</div>',
            unsafe_allow_html=True
        )

# ✅ 修复3: 为心跳按钮添加唯一 key（避免和第一个按钮冲突）
if st.button("·", key="heartbeat"):
    placeholder = st.empty()
    for _ in range(3):
        placeholder.markdown("<div style='text-align:center; font-size:1.2em; color:#a89e95;'>…</div>", unsafe_allow_html=True)
        time.sleep(0.4)
        placeholder.empty()
        time.sleep(0.2)
    placeholder.markdown("<div style='text-align:center; font-size:1.2em; color:#a89e95;'>❤</div>", unsafe_allow_html=True)
    time.sleep(1)
    placeholder.empty()

# 页脚
st.markdown("""
<div class="footer">
我见众生皆草木，唯有见你是青山。<br>
—— 灵感源自《爱你就像爱生命》
</div>
""", unsafe_allow_html=True)

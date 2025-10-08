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
# 检查图片
# ======================
bg_path = "picture/demo2.jpg"
image_exists = os.path.exists(bg_path)

# ======================
# CSS：图片居中 + 文字叠加（用相对定位）
# ======================
st.markdown(
    """
    <style>
    /* 隐藏默认元素 */
    #MainMenu, header, footer {visibility: hidden;}
    
    /* 图片容器：居中，保持比例 */
    .image-container {
        position: relative;
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }
    
    /* 图片样式 */
    .bg-image {
        width: 100%;
        height: auto;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    /* 文字叠加层 */
    .text-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        padding: 20px;
        max-width: 70%;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
        z-index: 2;
    }
    
    /* 标题 */
    .title {
        font-weight: 600;
        font-size: 1.8em;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    
    /* 语录 */
    .quote {
        font-size: 1.3em;
        line-height: 1.7;
        margin: 1.2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    
    /* 专属文字 */
    .personal {
        font-size: 1.1em;
        margin: 1.2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    
    /* 页脚 */
    .footer {
        color: #ddd;
        font-size: 0.9em;
        margin-top: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    
    /* 按钮 */
    .stButton > button {
        background: transparent;
        border: none;
        color: white;
        font-size: 1.6em;
        margin: 1rem auto;
        display: block;
        width: auto;
        padding: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    .stButton > button:hover {
        color: #ffcccb;
        transform: scale(1.15);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# 主内容
# ======================
if image_exists:
    # 先显示图片（居中）
    st.image(bg_path, use_container_width=False)  # 保持原始比例
    
    # 再叠加文字（用 st.markdown + 绝对定位）
    st.markdown(
        """
        <div class="image-container">
            <div class="text-overlay">
                <div class="title">朵朵大王天天开心</div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown('<div style="background:#222; padding:20px; text-align:center; color:white;">', unsafe_allow_html=True)

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

# 切换语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

st.markdown(f'<div class="quote">{st.session_state.current_quote}</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>如果累了，就休息一下。<br>我会一直等着朵朵的。</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="footer">Made for you • 愿你天天开心</div>', unsafe_allow_html=True)

# 关闭容器
if image_exists:
    st.markdown('</div></div>', unsafe_allow_html=True)
else:
    st.markdown('</div>', unsafe_allow_html=True)



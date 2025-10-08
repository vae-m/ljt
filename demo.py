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
# 检查图片是否存在
# ======================
bg_path = "picture/demo2.jpg"
image_exists = os.path.exists(bg_path)

# ======================
# 工具函数：将图片转为 base64
# ======================
def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ======================
# CSS 样式
# ======================
st.markdown(
    """
    <style>
    /* 隐藏默认元素 */
    #MainMenu, header, footer {visibility: hidden;}

    /* 图片容器：居中，限制最大宽度 */
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
        display: block;
    }

    /* 文字叠加层：绝对居中 */
    .text-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        padding: 20px;
        max-width: 80%;
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
        line-height: 1.6;
    }

    /* 页脚 */
    .footer {
        color: #ddd;
        font-size: 0.9em;
        margin-top: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }

    /* 按钮容器居中 */
    .button-container {
        text-align: center;
        margin-top: 20px;
    }

    /* 按钮样式 */
    .stButton > button {
        background: transparent;
        border: none;
        color: white;
        font-size: 1.6em;
        padding: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    .stButton > button:hover {
        color: #ffcccb;
        transform: scale(1.15);
        transition: transform 0.2s;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# 语录库
# ======================
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
    "愿你眼里有光，心中有爱.",
    "我的人生暗淡如水，谢谢你照进来的光。",
    "慢慢来，一切都来得及。",
    "努力挣钱，给朵朵花",
    "谢谢你在世界的角落里把我找到",
    "我喜欢的是完整的你。"
]

# 初始化语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# ======================
# 主内容区域
# ======================
if image_exists:
    try:
        img_base64 = get_image_base64(bg_path)
        st.markdown(
            f"""
            <div class="image-container">
                <img src="data:image/jpg;base64,{img_base64}" class="bg-image">
                <div class="text-overlay">
                    <div class="title">朵朵大王天天开心</div>
                    <div class="quote">{st.session_state.current_quote}</div>
                    <div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>如果累了，就休息一下。<br>我会一直等着朵朵的。</div>
                    <div class="footer">Made for you • 愿你天天开心</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error("图片加载失败，请检查 picture/demo2.jpg 是否存在。")
        image_exists = False

# 如果图片不存在，显示纯色背景内容
if not image_exists:
    st.markdown(
        f"""
        <div style="background:#222; padding:40px; text-align:center; color:white; 
                    border-radius:12px; max-width:600px; margin:0 auto; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
            <div class="title">朵朵大王天天开心</div>
            <div class="quote">{st.session_state.current_quote}</div>
            <div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>如果累了，就休息一下。<br>我会一直等着朵朵的。</div>
            <div class="footer">Made for you • 愿你天天开心</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================
# 按钮：居中显示
# ======================
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

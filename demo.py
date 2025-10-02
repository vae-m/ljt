import streamlit as st
import random
import time
import os

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="quiet affection",
    page_icon="🤍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# 检查背景图是否存在
# ======================
background_path = "picture/01.jpg"
has_background = os.path.exists(background_path)

# ======================
# CSS：背景图 + 极简 UI
# ======================
if has_background:
    # 有背景图：使用伪元素叠加柔光层
    bg_style = f"""
    .stApp {{
        background-image: url('picture/01.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(253, 246, 240, 0.85); /* 米白柔光层 */
        z-index: -1;
    }}
    """
else:
    # 无背景图：纯色背景
    bg_style = """
    .stApp {
        background: #fdf6f0;
    }
    """

st.markdown(f"""
<style>
    {bg_style}
    
    /* 全局字体 */
    .stApp {{
        font-family: "STKaiti", "KaiTi", "华文楷体", serif;
        color: #3e3e3e;
        line-height: 1.7;
    }}
    
    /* 隐藏默认元素 */
    #MainMenu, header, footer {{visibility: hidden;}}
    
    /* 标题 */
    h1 {{
        text-align: center;
        font-weight: 400;
        font-size: 1.3em;
        color: #5a5a5a;
        margin: 2.2rem 0 1.6rem;
        letter-spacing: 1.5px;
        text-shadow: 0 1px 2px rgba(255,255,255,0.7);
    }}
    
    /* 语录卡片 */
    .quote-box {{
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(4px);
        border-radius: 8px;
        padding: 1.6rem;
        margin: 1.8rem auto;
        max-width: 600px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        position: relative;
        border: 1px solid rgba(230, 220, 210, 0.5);
    }}
    .quote-text {{
        font-size: 1.1em;
        text-align: center;
        line-height: 1.8;
    }}
    .quote-author {{
        text-align: right;
        font-size: 0.95em;
        color: #8a8a8a;
        margin-top: 1rem;
        font-style: normal;
    }}
    
    /* 按钮：极简圆点 */
    .stButton > button {{
        background: transparent;
        border: none;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        margin: 0.8rem auto;
        display: block;
        position: relative;
        transition: all 0.3s ease;
        box-shadow: 0 0 0 2px rgba(138, 138, 138, 0.3);
    }}
    .stButton > button:hover {{
        background: rgba(138, 138, 138, 0.15);
        transform: scale(1.15);
        box-shadow: 0 0 0 3px rgba(138, 138, 138, 0.5);
    }}
    
    /* 专属文字 */
    .personal {{
        font-family: "STXingkai", "华文行楷", cursive;
        font-size: 1.15em;
        text-align: center;
        margin: 1.8rem auto;
        max-width: 600px;
        color: #4a4a4a;
        opacity: 0.92;
        background: rgba(255, 255, 255, 0.7);
        padding: 1.2rem;
        border-radius: 8px;
        backdrop-filter: blur(4px);
    }}
    
    /* 页脚 */
    .footer {{
        text-align: center;
        color: #a89e95;
        font-size: 0.85em;
        margin-top: 3rem;
        padding-top: 1.2rem;
        border-top: 1px solid rgba(240, 232, 224, 0.6);
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 多元语录库（含蓄、温柔、不尴尬）
# ======================
quotes = [
    # 王小波
    ("静下来想你，觉得一切都美好得不可思议。", "王小波"),
    ("我和你就像两个小孩子，围着一个神秘的果酱罐，一点一点地尝它。", "王小波"),
    ("不管我本人多么平庸，我总觉得对你的爱很美。", "王小波"),
    
    # 木心
    ("从前的日色变得慢，车，马，邮件都慢，一生只够爱一个人。", "木心"),
    ("你是我的，半截的诗，不许别人更改一个字。", "木心"),
    
    # 里尔克（冯至译）
    ("我认出风暴而激动如大海。", "里尔克"),
    ("有何胜利可言？挺住意味着一切。", "里尔克"),
    
    # 中国古诗
    ("山有木兮木有枝，心悦君兮君不知。", "《越人歌》"),
    ("愿我如星君如月，夜夜流光相皎洁。", "范成大"),
    ("晓看天色暮看云，行也思君，坐也思君。", "唐寅"),
    
    # 现代温柔短句
    ("世界很大，幸好有你。", "佚名"),
    ("遇见你，是我今生最美的意外。", "佚名"),
    ("你站在桥上看风景，看风景的人在楼上看你。", "卞之琳"),
    ("我见众生皆草木，唯有见你是青山。", "佚名"),
    ("你的名字，是我见过最短的情诗。", "佚名")
]

# ======================
# 主内容
# ======================
st.title("quiet affection")

# 随机语录
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# 按钮：切换语录（唯一 key）
if st.button("", key="next_quote"):  # 按钮文字为空，只显示圆点
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

quote_text, author = st.session_state.current_quote
st.markdown(f"""
<div class="quote-box">
    <div class="quote-text">{quote_text}</div>
    <div class="quote-author">—— {author}</div>
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

# 页脚
st.markdown("""
<div class="footer">
In silence, I love you.<br>
</div>
""", unsafe_allow_html=True)

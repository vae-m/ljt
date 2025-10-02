import streamlit as st
import time
import random

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="致刘家彤",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# 自定义 CSS 样式（关键！让界面变好看）
# ======================
st.markdown("""
<style>
    /* 全局背景：淡粉色渐变 */
    .stApp {
        background: linear-gradient(135deg, #fff9f9 0%, #f0f8ff 100%);
        font-family: 'Microsoft YaHei', 'STHeiti', sans-serif;
    }
    
    /* 标题样式 */
    h1 {
        color: #e74c3c !important;
        text-align: center;
        font-weight: 600;
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #c0392b !important;
        text-align: center;
        font-weight: 500;
    }
    
    /* 卡片样式 */
    .quote-card {
        background: white;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin: 20px 0;
        border-left: 4px solid #e74c3c;
        transition: transform 0.3s ease;
    }
    .quote-card:hover {
        transform: translateY(-3px);
    }
    
    .quote-text {
        font-size: 1.2em;
        line-height: 1.6;
        color: #2c3e50;
        font-style: italic;
    }
    
    .quote-author {
        text-align: right;
        color: #7f8c8d;
        font-weight: 500;
        margin-top: 10px;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(to right, #e74c3c, #e67e22);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 25px;
        font-size: 1.1em;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(231, 76, 60, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(231, 76, 60, 0.4);
    }
    
    /* 隐藏 Streamlit 默认菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ======================
# 王小波经典语录（精选）
# ======================
quotes = [
    "你好哇，李银河！——今天我感到非常烦闷，我想念你。",
    "我会不爱你吗？不爱你？不会。爱你就像爱生命。",
    "你要是愿意，我就永远爱你；你要是不愿意，我就永远相思。",
    "我和你就像两个小孩子，围着一个神秘的果酱罐，一点一点地尝它，看看里面有多少甜。",
    "不管我本人多么平庸，我总觉得对你的爱很美。",
    "你是非常可爱的人，真应该遇到最好的人，我也真希望我就是。",
    "静下来想你，觉得一切都美好得不可思议。",
    "我希望我们是一对海豚，永远在水里游，永远不分离。"
]

# ======================
# 主界面
# ======================
st.title("💌 致 刘家彤")

st.markdown("<h2>爱你就像爱生命</h2>", unsafe_allow_html=True)

# 显示随机语录卡片
if st.button("✨ 点我，换一句王小波的情话"):
    quote = random.choice(quotes)
else:
    quote = quotes[0]  # 默认第一句

st.markdown(f"""
<div class="quote-card">
    <div class="quote-text">“{quote}”</div>
    <div class="quote-author">—— 王小波《爱你就像爱生命》</div>
</div>
""", unsafe_allow_html=True)

# 专属告白区
st.markdown("### 💌 给刘家彤的话")
st.markdown("""
<div style="background:white; padding:20px; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
    <p style="font-size:1.1em; line-height:1.7; color:#2c3e50;">
    家彤：<br>
    遇见你，是我今生最美的意外。<br>
    你的笑容像春天的风，吹散我所有的阴霾。<br>
    愿我们像王小波和李银河一样，<br>
    在平凡的日子里，彼此照亮，彼此深爱。<br><br>
    <strong>我爱你，就像爱生命。</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# 心跳动画（可选）
if st.button("❤️ 点击查看我的心跳"):
    placeholder = st.empty()
    for i in range(5):
        placeholder.markdown(f"<h1 style='text-align:center; color:#e74c3c;'>❤️ ❤️ ❤️</h1>", unsafe_allow_html=True)
        time.sleep(0.3)
        placeholder.markdown(f"<h1 style='text-align:center; color:#e74c3c;'> 💓 💓 💓 </h1>", unsafe_allow_html=True)
        time.sleep(0.3)
    placeholder.empty()

# 页脚
st.markdown("""
<br><br>
<div style="text-align:center; color:#95a5a6; font-size:0.9em;">
    Made with 💖 for 刘家彤 | 灵感来自王小波《爱你就像爱生命》
</div>
""", unsafe_allow_html=True)
import streamlit as st
import random
import os

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="朵朵大王生日快乐！",
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
    
    /* 柔和背景（无图时使用） */
    .main-content {
        background: linear-gradient(135deg, #fff9fb, #f0f7ff);
        padding: 20px;
        border-radius: 16px;
        max-width: 700px;
        margin: 0 auto;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }
    
    /* 图片样式 */
    .stImage > img {
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        display: block;
        margin: 0 auto 24px auto;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .stImage > img:hover {
        transform: scale(1.02);
    }
    
    /* 文字内容居中 */
    .centered-text {
        text-align: center;
        padding: 0 16px;
    }
    
    .title {
        font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
        font-weight: 700;
        font-size: 2.0em;
        margin: 1.2rem 0;
        color: #e91e63;
        animation: fadeInDown 1s ease-out;
    }
    
    .quote {
        font-size: 1.4em;
        line-height: 1.7;
        margin: 1.6rem 0;
        color: #333;
        font-weight: 500;
    }
    
    .personal {
        font-size: 1.15em;
        margin: 1.6rem 0;
        color: #555;
        line-height: 1.7;
    }
    
    .fortune {
        background: #fff8e1;
        border-left: 4px solid #ffc107;
        padding: 12px;
        border-radius: 0 8px 8px 0;
        margin: 1.2rem auto;
        max-width: 90%;
        font-size: 1.05em;
        color: #5d4037;
    }
    
    .footer {
        color: #888;
        font-size: 0.95em;
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 6px;
    }
    
    /* 按钮 */
    .stButton > button {
        display: block;
        margin: 1.8rem auto;
        font-size: 1.8em;
        border: none;
        background: transparent;
        color: #e91e63;
        padding: 0;
        cursor: pointer;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        color: #d81b60;
        transform: scale(1.2);
    }
    
    /* 动画 */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* 爱心点击特效 */
    .heart {
        position: absolute;
        font-size: 24px;
        color: #e91e63;
        pointer-events: none;
        animation: floatUp 1.2s forwards;
        z-index: 1000;
    }
    @keyframes floatUp {
        0% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
        100% {
            opacity: 0;
            transform: translateY(-80px) scale(1.5);
        }
    }
    </style>
    
    <script>
    // 点击图片出爱心
    document.addEventListener('click', function(e) {
        if (e.target.tagName === 'IMG') {
            const heart = document.createElement('div');
            heart.innerHTML = '💖';
            heart.className = 'heart';
            heart.style.left = (e.pageX - 12) + 'px';
            heart.style.top = (e.pageY - 12) + 'px';
            document.body.appendChild(heart);
            setTimeout(() => {
                heart.remove();
            }, 1200);
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

# ======================
# 显示图片
# ======================
bg_path = "picture/我们.jpg"
image_exists = os.path.exists(bg_path)

if image_exists:
    st.image(bg_path, use_container_width=True)
else:
    # 无图时加一点装饰
    st.markdown('<div style="text-align:center; margin-bottom:20px; color:#999;">🖼️ 图片未找到</div>', unsafe_allow_html=True)

# ======================
# 主内容容器
# ======================
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<div class="centered-text">', unsafe_allow_html=True)

# 标题
st.markdown('<div class="title">朵朵大王天天开心</div>', unsafe_allow_html=True)

# 语录库
quotes = [
    "你是最好的人",
    "有你真好",
    "愿你被这个世界温柔以待。",
    "她不一样，我喜欢她",
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

# 显示语录
st.markdown(f'<div class="quote">“{st.session_state.current_quote}”</div>', unsafe_allow_html=True)

# 专属寄语
st.markdown(
    '<div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>天天开心，永远幸福。<br>我会一直陪着朵朵的。</div>',
    unsafe_allow_html=True
)

# ✨ 新增：每日小惊喜（朵朵运势）
fortunes = [
    "今天会有小惊喜哦～",
    "朵朵今天会收到好消息！",
    "记得对自己好一点 ❤️",
    "今天适合吃甜品！",
    "有人正在偷偷想你呢～",
    "朵朵的笑容是最棒的魔法！",
    "今天走路会捡到快乐！",
    "好运正在向你跑来～"
]

if 'today_fortune' not in st.session_state:
    st.session_state.today_fortune = random.choice(fortunes)

st.markdown(f'<div class="fortune">✨ 朵朵今日运势：{st.session_state.today_fortune}</div>', unsafe_allow_html=True)

# 页脚
st.markdown('<div class="footer"><span>👑</span> Made for 朵朵大王 <span>💖</span></div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

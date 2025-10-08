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
# 图片列表
# ======================
image_files = ["picture/01.jpg", "picture/demo2.jpg"]
valid_images = [f for f in image_files if os.path.exists(f)]

# ======================
# 工具函数：图片转 base64
# ======================
def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ======================
# CSS + JavaScript 轮播
# ======================
if valid_images:
    # 预加载所有图片的 base64
    img_b64_list = []
    for img in valid_images:
        try:
            img_b64_list.append(get_image_base64(img))
        except:
            pass

    if img_b64_list:
        images_js = "[" + ",".join([f"'data:image/jpg;base64,{b64}'" for b64 in img_b64_list]) + "]"
        st.markdown(
            f"""
            <style>
            #MainMenu, header, footer {{visibility: hidden;}}

            .carousel-container {{
                position: relative;
                width: 100%;
                max-width: 800px;
                margin: 0 auto;
                overflow: hidden;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            }}

            .carousel-slide {{
                display: none;
                width: 100%;
            }}
            .carousel-slide.active {{
                display: block;
            }}

            .carousel-image {{
                width: 100%;
                height: auto;
                display: block;
            }}

            /* 文字叠加层 */
            .text-overlay {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: white;
                text-align: center;
                padding: 20px;
                max-width: 80%;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
                z-index: 10;
                pointer-events: none; /* 防止遮挡点击 */
            }}

            .title {{ font-weight: 600; font-size: 1.8em; margin: 0.5rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }}
            .quote {{ font-size: 1.3em; line-height: 1.7; margin: 1.2rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }}
            .personal {{ font-size: 1.1em; margin: 1.2rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); line-height: 1.6; }}
            .footer {{ color: #ddd; font-size: 0.9em; margin-top: 2rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.8); }}

            /* 轮播控制按钮 */
            .carousel-btn {{
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                background: rgba(0,0,0,0.5);
                color: white;
                border: none;
                width: 40px;
                height: 40px;
                border-radius: 50%;
                font-size: 18px;
                cursor: pointer;
                z-index: 20;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .prev {{ left: 10px; }}
            .next {{ right: 10px; }}
            .carousel-btn:hover {{
                background: rgba(0,0,0,0.8);
            }}

            /* 按钮容器 */
            .button-container {{
                text-align: center;
                margin-top: 20px;
            }}
            .stButton > button {{
                background: transparent;
                border: none;
                color: white;
                font-size: 1.6em;
                padding: 0;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
            }}
            .stButton > button:hover {{
                color: #ffcccb;
                transform: scale(1.15);
                transition: transform 0.2s;
            }}
            </style>

            <div class="carousel-container" id="carousel">
                <!-- 图片由 JS 动态插入 -->
            </div>

            <div class="text-overlay">
                <div class="title">朵朵大王天天开心</div>
                <div class="quote" id="quote-text">{st.session_state.get('current_quote', '加载中...')}</div>
                <div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>如果累了，就休息一下。<br>我会一直等着朵朵的。</div>
                <div class="footer">Made for you • 愿你天天开心</div>
            </div>

            <button class="carousel-btn prev" onclick="changeSlide(-1)">‹</button>
            <button class="carousel-btn next" onclick="changeSlide(1)">›</button>

            <script>
            const images = {images_js};
            let currentIndex = 0;
            const carousel = document.getElementById('carousel');

            function updateCarousel() {{
                // 清空
                carousel.innerHTML = '';
                // 创建当前图片
                const img = document.createElement('img');
                img.src = images[currentIndex];
                img.className = 'carousel-image';
                img.onclick = () => changeSlide(1); // 点击图片切换
                carousel.appendChild(img);
            }}

            function changeSlide(direction) {{
                currentIndex = (currentIndex + direction + images.length) % images.length;
                updateCarousel();
            }}

            // 自动轮播（每5秒）
            setInterval(() => {{
                currentIndex = (currentIndex + 1) % images.length;
                updateCarousel();
            }}, 5000);

            // 初始化
            updateCarousel();
            </script>
            """,
            unsafe_allow_html=True
        )
    else:
        valid_images = []  # 无有效图片

# ======================
# 语录逻辑（独立于图片）
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

if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# 更新语录按钮
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    # 通过 JS 更新语录（避免整页刷新影响轮播状态）
    st.markdown(
        f"""
        <script>
        document.getElementById('quote-text').innerText = "{st.session_state.current_quote}";
        </script>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 无图片时的降级显示
# ======================
if not valid_images:
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

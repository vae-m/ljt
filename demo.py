import streamlit as st
import random
import os
from PIL import Image
import io

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
    
    /* 图片预览样式 */
    .image-preview {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    .image-thumb {
        width: 60px;
        height: 60px;
        object-fit: cover;
        border-radius: 8px;
        cursor: pointer;
        border: 2px solid transparent;
        transition: all 0.2s;
    }
    .image-thumb:hover {
        transform: scale(1.1);
        border-color: #e91e63;
    }
    .image-thumb.active {
        border-color: #e91e63;
        box-shadow: 0 0 10px rgba(233, 30, 99, 0.3);
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
        if (e.target.tagName === 'IMG' && e.target.className !== 'image-thumb') {
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
# 定义可选的图片列表
# ======================
image_options = [
    "picture/demo2.jpg",
    "picture/我们.jpg", 
    "picture/01.jpg",
    "picture/2.jpg"
]

# ======================
# 检查图片有效性的函数
# ======================
def is_valid_image(filepath):
    """检查图片文件是否有效"""
    if not os.path.exists(filepath):
        return False
    
    try:
        # 检查文件大小
        if os.path.getsize(filepath) == 0:
            return False
        
        # 尝试用PIL打开图片
        with Image.open(filepath) as img:
            img.verify()  # 验证文件完整性
        return True
    except (IOError, SyntaxError, Exception):
        return False

def get_available_images():
    """获取所有可用的有效图片"""
    available = []
    for img_path in image_options:
        if is_valid_image(img_path):
            available.append(img_path)
    return available

# ======================
# 初始化session_state
# ======================
# 初始化当前图片
if 'current_image' not in st.session_state:
    available_images = get_available_images()
    if available_images:
        st.session_state.current_image = random.choice(available_images)
    else:
        st.session_state.current_image = None

# 初始化所有可用图片列表
if 'available_images' not in st.session_state:
    st.session_state.available_images = get_available_images()

# 初始化语录
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

if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

# 初始化运势
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

# ======================
# 侧边栏 - 图片选择器
# ======================
with st.sidebar:
    st.markdown("### 📸 图片设置")
    
    # 显示可用图片状态
    available_images = st.session_state.available_images
    if available_images:
        st.success(f"✅ 找到 {len(available_images)} 张可用图片")
        
        # 随机更换按钮
        if st.button("🔄 随机更换图片", use_container_width=True):
            current = st.session_state.current_image
            other_images = [img for img in available_images if img != current]
            if other_images:
                st.session_state.current_image = random.choice(other_images)
            else:
                st.session_state.current_image = random.choice(available_images)
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 直接选择图片")
        
        # 创建缩略图选择器
        cols = st.columns(2)
        for idx, img_path in enumerate(available_images):
            col_idx = idx % 2
            img_name = os.path.basename(img_path)
            
            # 检查是否是当前选中的图片
            is_active = (st.session_state.current_image == img_path)
            
            # 显示缩略图
            try:
                with Image.open(img_path) as img:
                    # 创建缩略图
                    img.thumbnail((100, 100))
                    
                    # 将图片转换为bytes
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='JPEG')
                    
                    # 显示图片和选择按钮
                    with cols[col_idx]:
                        st.image(img_bytes, use_column_width=True, caption=img_name)
                        if st.button(f"选择", key=f"select_{idx}", use_container_width=True):
                            st.session_state.current_image = img_path
                            st.rerun()
            except:
                # 如果无法生成缩略图，显示文件名
                with cols[col_idx]:
                    st.error(f"❌ {img_name}")
    else:
        st.error("❌ 未找到可用图片")
        st.info("请确保在 picture/ 文件夹中放置以下图片：")
        st.write("- demo2.jpg")
        st.write("- 我们.jpg")
        st.write("- 01.jpg")
        st.write("- 2.jpg")

# ======================
# 主页面 - 显示图片
# ======================
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)

if st.session_state.current_image and is_valid_image(st.session_state.current_image):
    try:
        # 显示图片名称
        image_name = os.path.basename(st.session_state.current_image)
        st.markdown(f'<div style="color:#666; margin-bottom:8px; font-size:0.9em;">📸 {image_name}</div>', 
                   unsafe_allow_html=True)
        
        # 显示主图片
        st.image(st.session_state.current_image, use_container_width=True)
        
        # 显示提示
        st.markdown('<div style="color:#999; font-size:0.8em; margin-top:5px;">点击图片有惊喜 💖</div>', 
                   unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ 无法显示图片: {image_name}")
        st.info("图片可能已损坏，正在尝试选择其他图片...")
        
        # 尝试选择其他图片
        available_images = get_available_images()
        if available_images:
            st.session_state.current_image = random.choice(available_images)
            st.rerun()
        else:
            st.session_state.current_image = None
else:
    # 显示替代内容
    st.markdown("""
    <div style="text-align:center; padding:40px; background:#f8f9fa; border-radius:12px;">
        <div style="font-size:48px; margin-bottom:20px;">🖼️</div>
        <h3 style="color:#666;">暂无可用图片</h3>
        <p style="color:#999;">请检查图片文件是否存在且格式正确</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 主内容容器
# ======================
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<div class="centered-text">', unsafe_allow_html=True)

# 标题
st.markdown('<div class="title">朵朵大王天天开心</div>', unsafe_allow_html=True)

# 切换语录按钮
if st.button("💖", key="next_quote"):
    st.session_state.current_quote = random.choice(quotes)
    st.rerun()

# 显示语录
st.markdown(f'<div class="quote">"{st.session_state.current_quote}"</div>', unsafe_allow_html=True)

# 专属寄语
st.markdown(
    '<div class="personal">朵朵大王：<br>每天每时每刻每分每秒都要开心。<br>天天开心，永远幸福。<br>我会一直陪着朵朵的。</div>',
    unsafe_allow_html=True
)

# 今日运势
st.markdown(f'<div class="fortune">✨ 朵朵今日运势：{st.session_state.today_fortune}</div>', unsafe_allow_html=True)

# 页脚
st.markdown('<div class="footer"><span>👑</span> Made for 朵朵大王 <span>💖</span></div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# ======================
# 底部刷新按钮（可选）
# ======================
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 刷新页面", use_container_width=True):
        # 刷新所有状态
        available_images = get_available_images()
        if available_images:
            st.session_state.current_image = random.choice(available_images)
        st.session_state.current_quote = random.choice(quotes)
        st.session_state.today_fortune = random.choice(fortunes)
        st.rerun()

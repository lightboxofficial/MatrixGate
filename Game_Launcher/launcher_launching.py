from ursina import *
import time

app = Ursina()

# ===== 配置 =====
loading_tips = [  # 可自定义提示语列表
    "正在加载游戏资源...",
    "正在初始化世界...",
    "正在生成地形...",
    "正在加载角色模型...",
    "正在准备音效...",
    "正在优化性能...",
    "正在连接服务器...",
    "正在检查更新...",
    "正在加载剧情...",
    "即将进入游戏！"
]
tip_switch_interval = 3  # 每条提示语显示时间（秒）
window_color = "#000000B3"  # 半透明高级黑（B3 ≈ 70% 不透明度）
window_border_color = "#80808080"  # 半透明高级灰（80 ≈ 50% 不透明度）
progress_bar_color = "#F5D76E"  # 马卡龙金色（直接十六进制）
window_size = 0.4  # 窗口占屏幕宽度的比例（40%）

# ===== 背景 =====
background = Entity(
    model="quad",
    texture="background1.png",  # 确保图片在 assets/ 目录下
    scale=(1920, 1080),  # 根据背景图实际分辨率调整
    z=-1
)

# ===== 中央小窗口 =====
window = Entity(
    parent=camera.ui,
    model="quad",
    color=window_color,
    scale=(window_size, window_size * 0.7),  # 宽高比可调整
    position=(0, 0),
)

# 窗口描边（用 4 个细条模拟圆角矩形）
border_thickness = 0.003
border_offset = window_size / 2 - border_thickness
Entity(parent=window, model="quad", color=window_border_color, scale=(window_size + border_thickness*2, border_thickness), position=(0, border_offset))  # 上
Entity(parent=window, model="quad", color=window_border_color, scale=(window_size + border_thickness*2, border_thickness), position=(0, -border_offset))  # 下
Entity(parent=window, model="quad", color=window_border_color, scale=(border_thickness, window_size * 0.7 + border_thickness*2), position=(-border_offset, 0))  # 左
Entity(parent=window, model="quad", color=window_border_color, scale=(border_thickness, window_size * 0.7 + border_thickness*2), position=(border_offset, 0))  # 右

# ===== 进度条 =====
progress_bar_bg = Entity(
    parent=window,
    model="quad",
    #color=rgba(100, 100, 100, 0.3) #原来的错误代码
    color="#6464644D",  # 半透明深灰色（替代 rgba(100, 100, 100, 0.3)）
    scale=(0.9, 0.1),
    position=(0, -0.2),
)

progress_bar = Entity(
    parent=progress_bar_bg,
    model="quad",
    color=progress_bar_color,
    scale=(0, 1),  # 初始宽度为 0
    position=(-progress_bar_bg.scale_x/2, 0),  # 左对齐
    origin=(-0.5, 0),  # 缩放原点在左侧
)

# ===== 提示语文本 =====
tip_text = Text(
    parent=window,
    text=loading_tips[0],
    color=color.white,
    scale=2,
    position=(0, 0.3),
    origin=(0, 0)
)

# ===== 动态更新逻辑 =====
current_tip_index = 0
last_tip_switch_time = time.time()
progress = 0  # 进度值（0~1）

def update():
    global current_tip_index, last_tip_switch_time, progress

    # 轮播提示语
    if time.time() - last_tip_switch_time > tip_switch_interval:
        current_tip_index = (current_tip_index + 1) % len(loading_tips)
        tip_text.text = loading_tips[current_tip_index]
        last_tip_switch_time = time.time()

    # 模拟进度增加（实际游戏中替换为你的加载逻辑）
    progress += 0.005
    progress_bar.scale_x = min(progress, 1)  # 限制最大为 1
    progress_bar.x = -progress_bar_bg.scale_x/2  # 保持左对齐

    # 加载完成后跳转（示例）
    if progress >= 1:
        print("加载完成！")
        # 这里可以切换到游戏主场景，例如：
        # destroy(window)
        # application.pause()  # 停止加载界面

app.run()
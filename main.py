# ==================== 1. 页面配置与初始化 ====================
st.set_page_config(page_title="浪花男子心动日常", page_icon="💖", layout="centered")

# 初始化所有核心状态
if "stage" not in st.session_state:
    st.session_state.stage = "menu"
if "player_role" not in st.session_state:
    st.session_state.player_role = "经纪人"
if "target_member" not in st.session_state:
    st.session_state.target_member = "丈君"
if "current_day" not in st.session_state:
    st.session_state.current_day = 1
if "current_turn" not in st.session_state:
    st.session_state.current_turn = 1
if "total_score" not in st.session_state:
    st.session_state.total_score = 0
if "last_dialogue_result" not in st.session_state:
    st.session_state.last_dialogue_result = None
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "random_event" not in st.session_state:
    st.session_state.random_event = None
if "daily_gacha_result" not in st.session_state:
    st.session_state.daily_gacha_result = None
if "active_buff" not in st.session_state:
    st.session_state.active_buff = None

# ==================== 2. 剧本导入与安全获取 ====================
STORIES = {}
try:
    from stories.dajiang import DAJIANG_STORY
    from stories.gaogong import GAOGONG_STORY
    from stories.jo import JO_STORY
    from stories.kento import KENTO_STORY
    from stories.micchi import MICCHI_STORY
    from stories.purin import PURIN_STORY
    from stories.ryuche import RYUCHE_STORY

    STORIES = {
        "大酱": DAJIANG_STORY,
        "高恭": GAOGONG_STORY,
        "丈君": JO_STORY,
        "谦杜": KENTO_STORY,
        "米七": MICCHI_STORY,
        "布丁": PURIN_STORY,
        "流星": RYUCHE_STORY,
    }
except ImportError:
    STORIES = {}


def get_member_story(member_name, role="经纪人", day=1, turn=1):
    member_dict = STORIES.get(member_name, {})
    if not isinstance(member_dict, dict):
        return None

    role_dict = member_dict.get(role, next(iter(member_dict.values()), {}))
    if not isinstance(role_dict, dict):
        return None

    day_dict = role_dict.get(
        day, role_dict.get(str(day), next(iter(role_dict.values()), {}))
    )
    if not isinstance(day_dict, dict):
        return None

    turns_dict = day_dict.get("turns", {})
    return turns_dict.get(turn, turns_dict.get(str(turn), None))
# ==================== 3. 基础数据源 ====================
MEMBERS = {
    "丈君": {
        "trait": "⚾ 大阪搞笑担当 · 热血野球少年",
        "color": "蓝色",
        "img": "https://i.pinimg.com/1200x/26/b4/6e/26b46e13a5c9b81f9ef8cf4b2031a618.jpg",
    },
    "大酱": {
        "trait": "☀️ 绝对C位 · 演技派小太阳",
        "color": "红色",
        "img": "https://i.pinimg.com/1200x/fc/52/5e/fc525e14da8aac5bc7ee94bb625bf08f.jpg",
    },
    "布丁": {
        "trait": "🍮 微笑队长 · 美食家兼主唱",
        "color": "绿色",
        "img": "https://i.pinimg.com/1200x/c6/53/9c/c6539ce73f6c358cf4bd8fcd12c1935e.jpg",
    },
    "高恭": {
        "trait": "🎮 自恋帅哥 · 游戏宅系帅哥",
        "color": "紫色",
        "img": "https://i.pinimg.com/736x/23/e5/0d/23e50dceb8f34d93b23e564d6242bbb2.jpg",
    },
    "流星": {
        "trait": "✨ 可爱天花板 · 美妆小达人",
        "color": "橙色",
        "img": "https://i.pinimg.com/736x/5a/d5/65/5ad565a277abf02809e1557df4cef95d.jpg",
    },
    "米七": {
        "trait": "🌸 撕漫男神 · 纯爱系长腿弟弟",
        "color": "粉色",
        "img": "https://i.pinimg.com/736x/17/cb/00/17cb00f7a1374a85b1d6d1f0131ee71f.jpg",
    },
    "谦杜": {
        "trait": "🎨 潮流担当 · 淘气时尚小恶魔",
        "color": "黄色",
        "img": "https://i.pinimg.com/1200x/47/1a/59/471a59c662b0affdee44776e34946118.jpg",
    },
}

ROLES = ["经纪人", "青梅竹马", "在日学生or打工人"]

# -----------------------------------------------------------------------------
# 3. 标题与选择区域 (已用 if stage == "menu" 包裹，解决封面重叠问题)
# -----------------------------------------------------------------------------
    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        player_role = st.selectbox("1️⃣ 请选择你的身份：", ROLES)
        st.session_state.player_role = player_role

    with col_sel2:
        member_names = list(MEMBERS.keys())
        target_member = st.selectbox("2️⃣ 请选择你想攻略的成员：", member_names)
        st.session_state.target_member = target_member

    # 渲染选中成员的图片
    m_info = MEMBERS[st.session_state.target_member]
    st.image(m_info["img"], use_container_width=True)

    st.markdown("---")
# -----------------------------------------------------------------------------
# 4. 主界面渲染 (顶部标题、扭蛋机与背包)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="gacha-box">
        <h3 style="margin-top:0; color:#b45309; font-size: 1.2rem;">🎲 每日运势与道具扭蛋机</h3>
        <p style="font-size: 0.9rem; color: #78350f; margin-bottom: 10px;">消耗10积分抽取恋爱道具，并在背包中手动点击使用以获得增益效果！</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col_g1, col_g2 = st.columns(2)
with col_g1:
    if st.button("✨ 测测今天大势心动成员", use_container_width=True):
        if 'MEMBERS' in globals():
            lucky_name, lucky_data = random.choice(list(MEMBERS.items()))
            st.session_state.daily_gacha_result = (lucky_name, lucky_data)

with col_g2:
    if st.button("🎁 抽取心动道具 (消耗10积分)", use_container_width=True):
        if st.session_state.total_score >= 10:
            st.session_state.total_score -= 10
            items_pool = [
                ("🍬 恋爱加倍糖果", "下一次选择获得双倍好感积分！"),
                ("🎧 读心耳机", "精准洞察真实心意，额外+15积分！"),
                ("📸 SSR限定拍立得", "增加全盘浪漫氛围与结局甜度！"),
                ("🥤 冰爽解暑饮料", "恢复元气，额外+10积分！"),
                ("🕵️‍♂️ 黑色鸭舌帽", "低调伪装神器，免疫一次轻度偷拍危机！"),
                ("📜 紧急公关手稿", "遭遇绯闻时自动触发，大幅度降低负面好感损失！"),
                ("📱 备用双卡手机", "防止私生饭骚扰与紧急联络专用，增加容错率！"),
                ("☕ 专属应援手摇杯", "满含心意的特调饮品，全选项好感度小幅额外+5!"),
                ("🎟️ VIP前排观演门票", "近距离接触的心动暴击，好感获取效率大幅提升！"),
                ("🕶️ 明星同款墨镜", "闪避一次记者的长焦镜头抓拍，维持神秘感与安全度！"),
                ("📜 绝密通告行程单", "提前获知对方动向，精准制造偶遇，额外+20积分！"),
                ("🌹 手作永生玫瑰", "浪漫值直接拉满，有机会触发隐藏甜蜜对话剧情！"),
                ("🍫 手工黑巧礼盒", "甜而不腻的心意表达，关键时刻化解尴尬气氛！"),
                ("🌙 星空定制项链", "专属浪漫信物，大幅提升最终结局的甜度与评级！"),
                ("🐾 宠物协力萌爪", "利用可爱萌宠助攻，瞬间融化冰冷防备，额外+12积分！"),
            ]
            item_name, item_desc = random.choice(items_pool)
            st.session_state.inventory.append(item_name)
            st.success(f"成功获得道具：{item_name}（{item_desc}）!")
        else:
            st.warning("积分不足10分,快去剧情里增加好感吧！")

if st.session_state.get("daily_gacha_result"):
    lname, ldata = st.session_state.daily_gacha_result
    st.info(f"✨ 今日运势大吉！今日最强心动电波对象是：**{lname}**（特点：{ldata['trait']}）。快去选择他开启剧情吧！")

# 背包与 Buff 道具栏
if st.session_state.get("inventory"):
    st.markdown("---")
    st.write("🎒 **你的恋爱道具背包：**")
    cols_inv = st.columns(len(st.session_state.inventory))
    for idx, item in enumerate(st.session_state.inventory):
        with cols_inv[idx]:
            if st.button(f"使用 {item}", key=f"inv_{idx}"):
                st.session_state.active_buff = item
                st.session_state.inventory.pop(idx)
                st.success(f"已激活道具：{item}!")
                st.rerun()

if st.session_state.active_buff:
    st.markdown(f"> ⚡ **当前生效增益Buff:** `{st.session_state.active_buff}`")

st.markdown("---")
# =============================================================================
# 5. 主剧情关卡与随机事件核心逻辑
# =============================================================================
if st.session_state.stage == "menu":
    # 菜单界面的代码...
    pass

elif st.session_state.stage == "playing":
    st.markdown("---")

    # 定义当前攻略角色名称（供突发事件和文本使用）
    m_name = st.session_state.get("target_member", "成员")

    # 1. 如果刚好有上一幕互动反馈的结果，先展示出来
    if st.session_state.last_dialogue_result:
        q_title, user_choice_text, char_reply, score_gain = st.session_state.last_dialogue_result
        st.markdown(
            f"""
            <div style="background-color: #fdf2f8; border-left: 4px solid #db2777; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
                <p style="margin: 0; color: #9d174d; font-weight: bold;">💬 上一幕互动回顾：{q_title}</p>
                <p style="margin: 5px 0 0 0; color: #4b5563;">你的选择：{user_choice_text if user_choice_text else '顺利化解危机'}</p>
                <p style="margin: 8px 0 0 0; color: #1f2937; font-size: 1.05rem;"><b>{m_name} 回应：</b> {char_reply}</p>
                <p style="margin: 5px 0 0 0; color: #059669; font-size: 0.9rem;">✨ 好感度变动：+{score_gain} 分</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# 获取当前玩家的状态参数
current_target = st.session_state.get("target_member", "丈君")
current_role = st.session_state.get("player_role", "经纪人")
current_day = st.session_state.get("current_day", 1)
current_turn = st.session_state.get("current_turn", 1)

for idx, choice in enumerate(choices_list):
    if len(choice) == 3:
        btn_text, reply_text, base_score = choice
    else:
        btn_text, reply_text, base_score = choice[0], "……（温柔地看着你笑）", 20

    if st.button(btn_text, key=f"choice_{current_day}_{current_turn}_{idx}", use_container_width=True):
        # 计算 Buff 加成
        actual_score = base_score
            if st.session_state.active_buff == "🍬 恋爱加倍糖果":
                actual_score *= 2
                st.session_state.active_buff = None  
                st.toast("🍬 恋爱加倍糖果生效！好感积分翻倍！", icon="✨")
            elif st.session_state.active_buff == "🎧 读心耳机":
                actual_score += 15
                st.session_state.active_buff = None
                st.toast("🎧 读心耳机生效：额外 +15 积分！", icon="✨")
            elif st.session_state.active_buff in ["☕ 专属应援手摇杯", "🥤 冰爽解暑饮料"]:
                actual_score += 10
                st.session_state.active_buff = None
                st.toast("☕ 道具加成生效：额外 +10 积分！", icon="✨")
            elif st.session_state.active_buff == "🌙 星空定制项链":
                actual_score += 25
                st.session_state.active_buff = None
                st.toast("🌙 星空定制项链生效：大幅提升结局甜度，额外 +25 积分！", icon="💖")

            # 累加积分  
            st.session_state.total_score += actual_score

            # 记录历史与最新结果
            st.session_state.last_dialogue_result = (
                act_title,
                btn_text,
                reply_text,
                actual_score
            )

            # 推进到下一幕并清空上一幕缓存
            st.session_state.current_act += 1
            st.rerun()

        # 3. 检查是否有突发事件触发 (40% 概率)
        if st.session_state.get("current_event") is None and random.random() < 0.4:
            events_pool = [
                {
                    "title": "🚨 突发危机：文春记者的长焦镜头",
                    "desc": f"在约会途中，街角突然闪过一道可疑的快门闪光灯！有八卦记者正在试图偷拍你和 {m_name} 的亲密合影！"
                },
                {
                    "title": "⚡ 突发危机：热情粉丝与私生饭围堵",
                    "desc": f"由于近期人气暴涨，你们在离开咖啡厅时突然被大批粉丝和围观人群堵在门口，场面一度有些混乱！"
                },
                {
                    "title": "🌧️ 突发危机：突如其来的暴雨袭城",
                    "desc": f"原本晴朗的天空瞬间下起倾盆大雨，街上的行人纷纷避雨，你们的计划被打乱了。"
                },
                {
                    "title": "📋 突发危机：经纪人突击查岗",
                    "desc": f"手机突然疯狂震动！经纪人的夺命连环Call打了过来，质问大明星现在到底在哪里、有没有偷偷旷工跑去约会！"
                },
                {
                    "title": "🚲 突发状况：自行车链条突然脱落",
                    "desc": f"骑车载着 {m_name} 经过坂道时，单车的链条突然卡死脱落！两人狼狈地推着车，却在夕阳下笑作一团。"
                },
                {
                    "title": "🍙 突发日常：深夜便利店的半价便当争夺战",
                    "desc": f"深夜在街角罗森便利店抢最后一份半价炸鸡块时，你和 {m_name} 的手同时按在了包装盒上！"
                },
                {
                    "title": "🐱 突发趣事：路遇厚脸皮的流浪肥猫“碰瓷”",
                    "desc": f"回家的巷子里，一只橘猫突然大摇大摆地躺在你们脚边打滚赖着不走，{m_name} 蹲下来笑得毫无偶像包袱。"
                },
                {
                    "title": "💸 突发社死：出站时Suica卡余额不足",
                    "desc": f"急着出站时，闸机突然发出刺耳的“哔哔”声将你拦下，身后排着长队，{m_name} 忍俊不禁地帮你在旁边充了值。"
                },
                {
                    "title": "📻 突发心动：店内突然播放他的成名曲",
                    "desc": f"在安静的中古CD店或咖啡馆里，店里的音响突然毫无征兆地放起了 {m_name} 的出道单曲，气氛瞬间变得微妙又浪漫。"
                },
                {
                    "title": "🥞 突发状况：亲手做的日式料理“惨遭翻车”",
                    "desc": f"你信心满满地做了一份厚蛋烧/咖喱，结果端上桌时卖相惨不忍睹，{m_name} 却一脸视死如归地笑着说要全部吃光。"
                }
            ]
            
            st.session_state.current_event = random.choice(events_pool)
            st.rerun()
# -----------------------------------------------------------------------------
# 6. 游戏流程控制 (突发事件弹窗处理)
# -----------------------------------------------------------------------------
if st.session_state.random_event:
    ev = st.session_state.random_event
    ev_title = ev['title']
    ev_desc = ev['desc']
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%); border: 2px solid #fb7185; padding: 20px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(225,29,72,0.15);">
            <h3 style="margin-top:0; color: #9f1239; font-size: 1.3rem;">⚡ 【心动危机 / 突发事件】{ev_title}</h3>
            <p style="font-size: 1.05rem; color: #44403c; line-height: 1.6;">{ev_desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # 点击后清空事件，返回正常剧情流程
    if st.button("✅ 完美化解危机", use_container_width=True):
        st.session_state.random_event = None 
        st.rerun()

    # 初始化道具触发标志
    item_triggered = False

# 检查道具自动触发
    inventory = st.session_state.get("inventory", [])
    if "文春" in ev_title:
        if "🕵️‍♂️ 黑色鸭舌帽" in inventory:
            st.success("✨ 【道具自动触发：黑色鸭舌帽】低调伪装成功！你们完美避开了文春记者的长枪短炮！")
            inventory.remove("🕵️‍♂️ 黑色鸭舌帽")
            item_triggered = True
        elif "📜 紧急公关手稿" in inventory:
            st.success("✨ 【道具自动触发：紧急公关手稿】手稿发挥作用，团队迅速稳住了媒体风向！")
            inventory.remove("📜 紧急公关手稿")
            item_triggered = True
    elif "私生饭" in ev_title:
        if "📱 备用双卡手机" in inventory:
            st.success("✨ 【道具自动触发：备用双卡手机】及时联络到安保人员精准清场，安全脱身！")
            inventory.remove("📱 备用双卡手机")
            item_triggered = True
    elif "暴雨" in ev_title:
        if "🥤 冰爽解暑饮料" in inventory:
            st.success("✨ 【道具自动触发：冰爽解暑饮料】虽然外面下暴雨，但手里的冰饮意外带来一抹甜意！")
            inventory.remove("🥤 冰爽解暑饮料")
            item_triggered = True

            if item_triggered:
                st.info("💡 携带了正确道具，顺利化解危机，额外获得 **+25 积分**！")
                if st.button("💖 携手化解危机，继续心动行程", use_container_width=True):
                    st.session_state.total_score += 25
                    st.session_state.current_event = None
                    st.rerun()
            else:
                col_ev1, col_ev2 = st.columns(2)
                
                if "文春" in ev_title:
                    st.markdown(f"**{m_name} 看着远处的长焦镜头，眼神微冷：\"啧，这群记者还真是阴魂不散。\"**")
                    with col_ev1:
                        if st.button("📸 大方直面镜头，直接挽紧他的手臂", use_container_width=True):
                            st.session_state.total_score += 20
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🏃‍♂️ 拽起他的衣角，闪身躲进旁边的盲区", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                            
                elif "私生饭" in ev_title:
                    st.markdown(f"**{m_name} 微微蹙眉，将你护在身后，语气低沉：\"别看他们，跟着我走。\"**")
                    with col_ev1:
                        if st.button("🛡️ 配合他的保护，迅速低头快步离开", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🎭 反客为主，当众假装你们在吵架转移视线", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "暴雨" in ev_title:
                    st.markdown(f"**{m_name} 看着倾盆而下的雨幕，无奈地脱下外套帮你挡雨：\"这天气还真是说变就变。\"**")
                    with col_ev1:
                        if st.button("☂️ 钻进同一件外套下，紧紧贴在一起避雨", use_container_width=True):
                            st.session_state.total_score += 20
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🏃‍♂️ 笑着拉他一起踩水坑，享受雨中狂奔", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()

                elif "经纪人" in ev_title:
                    st.markdown(f"**{m_name} 看着震个不停的手机，露出一抹恶作剧般的坏笑：\"要接吗？\"**")
                    with col_ev1:
                        if st.button("📱 帮他直接挂断并关机：\"今天休假，天王老子来了也没用！\"", use_container_width=True):
                            st.session_state.total_score += 20
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🗣️ 拿过手机一本正经地帮他编借口请假", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()

                elif "自行车链条" in ev_title:
                    st.markdown(f"**{m_name} 蹲在地上擦了擦手上的黑油，抬头冲你爽朗一笑：\"看来只能步行啦。\"**")
                    with col_ev1:
                        if st.button("🚲 载他回去（推车漫步夕阳）", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🥤 罚他今晚请喝抹茶拿铁压惊！", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "便利店" in ev_title:
                    st.markdown(f"**{m_name} 压低帽檐，隔着玻璃冲你挑眉坏笑：\"兼职的小员工，这份炸鸡块我要了。\"**")
                    with col_ev1:
                        if st.button("🍙 大方让给他：「大明星辛苦啦，这个让给你。」", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("🛡️ 叉腰护住便当：「先到先得！这可是本打工人的夜宵！」", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "流浪肥猫" in ev_title:
                    st.markdown(f"**{m_name} 毫无偶像包袱地蹲在路边，伸手逗弄着胖橘猫：\"你看它，眼神跟你生气时一模一样。\"**")
                    with col_ev1:
                        if st.button("🐾 蹲下来温柔撸猫：「好可爱啊……像谁呢哼？」", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("💢 假装吃醋拍拍他的肩：「怎么，眼里只有猫没有我了？」", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "Suica卡" in ev_title:
                    st.markdown(f"**{m_name} 看着闸机屏幕上的残高不足，忍不住轻笑出声：\"关键时刻还得靠本大爷吧。\"**")
                    with col_ev1:
                        if st.button("羞涩道谢：「谢谢大明星慷慨解囊，回头请吃章鱼烧！」", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("理直气壮挑眉：「花青梅/男友的钱天经地义！」", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "成名曲" in ev_title:
                    st.markdown(f"**{m_name} 微微一顿，有些不好意思地拉了拉你的衣角：\"……怎么突然放这个。\"**")
                    with col_ev1:
                        if st.button("小声哼唱并戳他手臂：「听，是你的歌耶！」", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("坏笑着拉他快走：「走啦，在这里听自己的歌不害羞吗？」", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                elif "料理翻车" in ev_title:
                    st.markdown(f"**{m_name} 看着盘子里黑乎乎的厚蛋烧，表情瞬间凝固又化为宠溺：\"……这是要谋杀亲夫吗？\"**")
                    with col_ev1:
                        if st.button("视死如归自己尝一口：「呃……其实咸淡刚刚好！」", use_container_width=True):
                            st.session_state.total_score += 15
                            st.session_state.current_event = None
                            st.rerun()
                    with col_ev2:
                        if st.button("吐舌头耍赖：「虽然卖相差了点，但心意满分噢！」", use_container_width=True):
                            st.session_state.total_score += 18
                            st.session_state.current_event = None
                            st.rerun()

                if st.button("💥 应对失误导致有些小狼狈（扣除部分积分）", use_container_width=True):
                    st.session_state.total_score -= 25
                    st.session_state.current_event = None
                    st.rerun()
# -------------------------------------------------------------
# 阶段二：游戏进行中
# -------------------------------------------------------------
elif st.session_state.stage == "playing":
    current_target = st.session_state.get('target_member', st.session_state.get('target', '丈君'))
    current_role = st.session_state.get('player_role', st.session_state.get('role', '经纪人'))
    
    st.info(f"当前身份：**{current_role}** | 攻略对象：**{current_target}**")
    
# ==================== 最新适配剧情提取逻辑 ====================
current_target = st.session_state.get("target_member", "丈君")
current_role = st.session_state.get("player_role", "经纪人")
current_day = st.session_state.get("current_day", 1)
current_turn = st.session_state.get("current_turn", 1)

# 读取字典里的回合数据
act_data = get_member_story(
    current_target, current_role, current_day, current_turn
)

if act_data and isinstance(act_data, dict):
    # 1. 渲染标题
    title = act_data.get("title", f"第 {current_turn} 回合")
    st.markdown(f"### 🎬 {title}")

    # 2. 渲染台词
    desc = act_data.get("desc", "")
    desc_text = "".join(desc) if isinstance(desc, (list, tuple)) else str(desc)
    st.markdown(
        f"<div class='dialogue-box'>{desc_text}</div>", unsafe_allow_html=True
    )

    # 3. 获取选项列表
    choices_list = act_data.get("choices", [])
else:
    st.success("🎉 当前路线剧情已播放完毕！感谢游玩！")
    choices_list = []

# -------------------------------------------------------------
# 阶段三：游戏结束 / 结局
# -------------------------------------------------------------
elif st.session_state.stage == "game_over":
    st.success("🎉 游戏结束！感谢游玩！")
    if st.button("🔄 重新开始游戏", key="restart_game_button"):
        st.session_state.stage = "menu"
        st.session_state.current_act = 0
        st.rerun()

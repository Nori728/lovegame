import streamlit as st
import random

# -----------------------------------------------------------------------------
# 1. 基础配置与样式 (动漫乙女风格 UI)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="浪花男子心动日常", page_icon="💖", layout="centered")

st.markdown("""
<style>
    /* 核心背景与字体 */
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #fed7aa 100%);
    }
    
    /* 标题样式 */
    .otome-title {
        font-size: 2.2rem;
        color: #e11d48;
        text-align: center;
        font-weight: bold;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px #fecdd3;
    }
    
    /* 动漫乙女对话框样式 */
    .dialogue-box {
        background-color: rgba(255, 255, 255, 0.95);
        border: 2px solid #fda4af;
        border-radius: 15px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 10px 25px rgba(225, 29, 72, 0.1);
    }
    
    .speaker-tag {
        font-size: 1.1rem;
        font-weight: bold;
        color: #be123c;
        background: #ffe4e6;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .scene-desc {
        color: #78350f;
        font-style: italic;
        font-size: 0.95rem;
        margin-bottom: 12px;
        background: #fff7ed;
        padding: 8px 12px;
        border-left: 3px solid #f97316;
        border-radius: 4px;
    }
    
    .event-header {
        background: linear-gradient(90deg, #f43f5e, #fb7185);
        color: white;
        padding: 8px 15px;
        border-radius: 10px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* 抽卡结果框 & 事件结局框 */
    .gacha-box {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #fde68a;
        margin-bottom: 15px;
    }
    
    .event-box {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #7dd3fc;
        margin-bottom: 15px;
    }
    
    /* 按钮大改造：变成粉色游戏风按钮 */
    .stButton > button {
        background: linear-gradient(135deg, #fb7185 0%, #f43f5e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 6px rgba(225, 29, 72, 0.2) !important;
        transition: all 0.3s ease !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%) !important;
        box-shadow: 0 6px 12px rgba(225, 29, 72, 0.35) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active {
        transform: translateY(1px) !important;
        box-shadow: 0 2px 4px rgba(225, 29, 72, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)
# -----------------------------------------------------------------------------
# 2. 7位成员基础信息定义
# -----------------------------------------------------------------------------
MEMBERS = {
    "丈君": {
        "trait": "⚾ 大阪搞笑担当 · 热血野球少年",
        "color": "#0284c7",
        "img": "https://i.pinimg.com/1200x/26/b4/6e/26b46e13a5c9b81f9ef8cf4b2031a618.jpg",
        "greeting": "『哟！今天也要跟着本大爷一起充满活力地前进哦！』"
    },
    "大酱": {
        "trait": "☀️ 绝对C位 · 演技派小太阳",
        "color": "#e11d48",
        "img": "https://i.pinimg.com/1200x/cd/08/52/cd0852d71e894d1046c702fbeb9f6a25.jpg",
        "greeting": "『能在这里遇见你，感觉今天的幸运值已经加满了～』"
    },
    "大桥": {
        "trait": "🍮 微笑队长 · 美食家兼主唱",
        "color": "#16a34a",
        "img": "https://i.pinimg.com/736x/6e/1e/50/6e1e509e5aa92238642977764147e810.jpg",
        "greeting": "『布丁布丁！今天有好好吃饭吗？没有的话我带你去吃好吃的！』"
    },
    "恭平": {
        "trait": "🎮 自恋帅哥 · 游戏宅系帅哥",
        "color": "#9333ea",
        "img": "https://i.pinimg.com/1200x/1a/3f/c6/1a3fc6b2bef0b4e446158128f4f0316f.jpg",
        "greeting": "『照照镜子……嗯，今天依然很帅！要来跟我组队打游戏吗？』"
    },
    "流星": {
        "trait": "✨ 可爱天花板 · 美妆小达人",
        "color": "#ec4899",
        "img": "https://i.pinimg.com/736x/5a/d5/65/5ad565a277abf02809e1557df4cef95d.jpg",
        "greeting": "『wink~ 今天的妆容可是花了心思的，不许移开视线哦！』"
    },
    "米七": {
        "trait": "🌸 撕漫男神 · 纯爱系长腿弟弟",
        "color": "#2563eb",
        "img": "https://i.pinimg.com/1200x/f5/c4/df/f5c4df2c34cb393dcb1b36ca7ff8d1ce.jpg",
        "greeting": "『内个……看到你笑的话，我也会忍不住开心起来呢。』"
    },
    "谦杜": {
        "trait": "🎨 潮流担当 · 淘气时尚小恶魔",
        "color": "#d97706",
        "img": "https://i.pinimg.com/736x/e2/98/21/e298211a5e8e79b141274153e959df2e.jpg",
        "greeting": "『今天的穿搭很不错嘛～不过要不要听听本时尚专家的建议？』"
    }
  },
  # -----------------------------------------------------------------------------
# 3. 更新你的角色列表
ROLES = ["经纪人", "青梅竹马", "在日留学生or打工人"]
st.error(f"当前 MEMBERS 的类型是: {type(MEMBERS)}")
selected_member = st.selectbox("💖 选择你的心动男主角：", MEMBERS)

st.image(MEMBERS[selected_member]["img"], width=220)

# -----------------------------------------------------------------------------
# 3. 深度定制的个性化小说剧情数据库 (智能剧情生成引擎)
# -----------------------------------------------------------------------------
def get_custom_story(m_name, r_name, act):
    c_trait = MEMBERS[m_name]["trait"]
    
    titles = {
        "经纪人": [
            f"🎬 第一幕：后台倒计时的视线交汇",
            f"🎬 第二幕：深夜休息室的卸防独白",
            f"🎬 第三幕：通告间隙的秘密私奔",
            f"🎬 第四幕：镜头死角的直球对峙",
            f"🎬 第五幕：风口浪尖的坚定守护",
            f"🎬 第六幕（终章）：闪耀舞台下的永恒契约"
        ],
        "青梅竹马": [
            f"🏡 第一幕：老旧阁楼的放学后重逢",
            f"🏡 第二幕：便利店门口分食的冰淇淋",
            f"🏡 第三幕：深夜房间窗台的秘密纸条",
            f"🏡 第四幕：夏日祭烟火下的怦然心动",
            f"🏡 第五幕：争吵后的隐秘眼泪与拥抱",
            f"🏡 第六幕（终章）：经年陪伴的告白终点站"
        ],
        "在日留学生or打工人": [
            f"🗼 第一幕：异国涩谷十字路口的擦肩",
            f"🗼 第二幕：电车终点站的雨伞与温热罐装咖啡",
            f"🗼 第三幕：狭小公寓厨房里的手作料理",
            f"🗼 第四幕：樱花树下的跨国心事坦白",
            f"🗼 第五幕：异国深夜生病时的慌乱照顾",
            f"🗼 第六幕（终章）：东京塔下的浪漫长相厮守"
        ]
    }
    
    title = titles[r_name][act - 1]
    
    if m_name == "丈君":
        intro_dialogue = (m_name, f"“喂！身为你的{r_name}，本大爷可不允许你把视线移开别人哦！”")
        prologue_text = f"关西腔的爽朗笑声在耳边回荡。作为{r_name}，你与丈君（{c_trait}）一同经历的每一幕都充满了热血与欢笑。"
    elif m_name == "大酱":
        intro_dialogue = (m_name, f"“呐，今天也要跟紧我的脚步，C位身边的专属位置只留给你哦～”")
        prologue_text = f"灯光璀璨，空气中弥漫着温柔的气息。作为{r_name}，大酱（{c_trait}）正用他那双亮晶晶的眼睛深情地望着你。"
    elif m_name == "大桥":
        intro_dialogue = (m_name, f"“布丁要分你一半，不开心的时候吃甜食就会好起来的！”")
        prologue_text = f"空气里仿佛飘着淡淡的甜香。作为{r_name}，大桥（{c_trait}）标志性的治愈系笑容瞬间融化了所有的疲惫。"
    elif m_name == "恭平":
        intro_dialogue = (m_name, f"“照过镜子了吗？本大爷今天帅得连游戏通关都吸引不了我了，除了你。”")
        prologue_text = f"略带傲娇又宠溺的语气。作为{r_name}，恭平（{c_trait}）正漫不经心地把玩着手里的游戏机，耳根却悄悄红了。"
    elif m_name == "流星":
        intro_dialogue = (m_name, f"“wink~ 今天特意挑了你喜欢的发色，快夸夸我！”")
        prologue_text = f"精致的面容在微光下显得格外动人。作为{r_name}，流星（{c_trait}）凑近你身边，带着让人无法抗拒的可爱魔力。"
    elif m_name == "米七":
        intro_dialogue = (m_name, f"“内个……只要你在身边，我就觉得连风都是甜的。”")
        prologue_text = f"纯爱漫画般的氛围。作为{r_name}，米七（{c_trait}）修长的身影将你轻轻笼罩，眼底满是青涩的依恋。"
    else:  # 谦杜
        intro_dialogue = (m_name, f"“今天的穿搭可是专门为你搭配的哦，小恶魔时尚顾问满意吗？”")
        prologue_text = f"潮流感十足的街头风气息。作为{r_name}，谦杜（{c_trait}）带着恶作剧般的坏笑，轻轻拉住了你的衣角。"

    return {
        "title": title,
        "scene": f"{m_name} 与你的专属剧情现场",
        "prologue": prologue_text,
        "dialogue_intro": [intro_dialogue],
        "choices": [
            {"option": "微笑回应并靠近一步", "reply": "「……犯规了，你这样笑会让我的心跳彻底失控的。」", "affection": 20},
            {"option": "打趣化解害羞的情绪", "reply": "「哼，也就只有你敢这么调侃我了，不过……我喜欢。」", "affection": 15},
            {"option": "认真握住对方的手", "reply": "「被你这样注视着，我好像已经没办法再去想其他人了。」", "affection": 25}
        ]
    }


# -----------------------------------------------------------------------------
# 4. 突发随机事件池 (RANDOM_EVENTS_POOL)
# -----------------------------------------------------------------------------
RANDOM_EVENTS_POOL = [
    {
        "title": "突发暴雨的屋檐避难",
        "desc": "两人在回家路上突然遇到倾盆大雨，被迫挤在一个小小的便利店屋檐下，肩膀紧紧贴着……",
        "dialogue": "「雨下得好大啊……你的肩膀都湿了一片。来，往我这边靠紧一点，别着凉了。」",
        "choices": [
            {"text": "顺势靠进他怀里：「这样就不冷啦，谢谢你。」", "reply": "「真是的……心跳声这么快，全都传过来了啦。」", "score": 25},
            {"text": "把伞往他那边推：「你别淋湿了才是，我没事的。」", "reply": "「傻瓜，我一个男生淋点雨没关系……不过，被你这样关心，我有点高兴过头了。」", "score": 20}
        ]
    },
    {
        "title": "电台直播的连线袭击",
        "desc": "工作间隙突然接到了一档电台连线直播，主持人现场要求他对你说一句真心话！",
        "dialogue": "「诶？连线直播吗……咳，那我就直说了。其实不管行程多累，只要想到你在身边，我就——」",
        "choices": [
            {"text": "红着脸小声抢话：「好啦，快别在直播里说这个了！」", "reply": "「哈哈，害羞了吗？直播间的几万名粉丝可都听见咯。」", "score": 20},
            {"text": "落落大方地对着麦克风回应：「我也一样哦，一直辛苦了。」", "reply": "「……听到你这么说，我突然觉得今天所有的疲惫都瞬间消失了。」", "score": 30}
        ]
    },
    {
        "title": "猫咪咖啡厅的意外邂逅",
        "desc": "排练间隙去咖啡厅休息，一只可爱的布偶猫突然跳进你怀里，引得他吃醋地看着你……",
        "dialogue": "「喂……它在你怀里待得太久了吧？我也想要抱抱，不许偏心哦。」",
        "choices": [
            {"text": "笑着把猫抱好、顺手戳戳他的脸：「连猫的醋也吃呀？」", "reply": "「才没有吃醋……好吧，有一点点。谁让你眼里只有它没有我。」", "score": 22},
            {"text": "放下猫咪，主动拉住他的袖子：「好啦，那我只看你总行了吧。」", "reply": "「这还差不多……不准反悔哦。」", "score": 28}
        ]
    },
    {
        "title": "便利店最后一块布丁",
        "desc": "深夜去买宵夜，冰箱里只剩下最后一份他最爱的限定布丁，你们会怎么分？",
        "dialogue": "「啊……只剩最后一个了。要不，你吃吧？我看你今天录制辛苦了。」",
        "choices": [
            {"text": "用勺子挖了一口喂到他嘴边：「我们一人一半呀！」", "reply": "「唔……好甜。不过，比布丁更甜的是你喂的这一口……」", "score": 30},
            {"text": "「不行，你是寿星/大明星，你吃！」", "reply": "「那……那我分你一大半，不许拒绝，不然我会生气的。」", "score": 20}
        ]
    },
    {
        "title": "📸 文春炮的闪光灯危机",
        "desc": "深夜在街角散步时，暗处突然闪过一道刺眼的白光！文春记者带着长枪短炮从阴影里冲了出来！",
        "dialogue": "「闪光灯？！别慌，抓紧我的手，跟着我跑！」",
        "choices": [
            {"text": "紧紧反握住他的手，跟着他一路狂奔", "reply": "「甩掉了……好险！不过刚才那一瞬间，我满脑子只想保护你一个人，没顾上别的。」", "score": 35}
        ]
    },
    {
        "title": "🚨 狂热私生饭的围堵",
        "desc": "刚结束录制，停车场突然冲出几个情绪激动的私生饭和私家车，死死堵住了去路……",
        "dialogue": "「别看他们，低下头，我把你整个人护在身后！」",
        "choices": [
            {"text": "紧紧抓着他的衣角，信任地靠在他身后", "reply": "「别怕，有我在，谁也别想伤害你半根汗毛。我们马上上车。」", "score": 30}
        ]
    },
    {
        "title": "🎙️ 直播未关麦的社死瞬间",
        "desc": "以为直播已经切断，他正凑在你耳边小声呢喃情话，结果几万名在线观众把两人的亲密私语听得清清楚楚！",
        "dialogue": "「等、等一下……刚才的麦克风好像一直没关？！完蛋了，全直播间都听见了……」",
        "choices": [
            {"text": "红着脸捂住他的嘴：「都怪你啦！」", "reply": "「咳……听见就听见了吧，反正我对你说的每一句话，都是认真的。」", "score": 35},
            {"text": "大方对着镜头挥手打招呼：「大家晚安呀~」", "reply": "「……你比想象中还要大胆嘛，不过，我好喜欢你这样。」", "score": 30}
        ]
    },
    {
        "title": "🎭 颁奖后台的擦肩而过",
        "desc": "在众多同行和媒体云集的颁奖典礼后台，为了避人耳目，你们俩不得不一起躲进了一个狭窄逼仄的杂物间里。",
        "dialogue": "「空间太小了……这样贴得好近。外面都是记者和摄像机，千万别发出声音哦……」",
        "choices": [
            {"text": "大气都不敢出，紧张地抓着他的肩膀", "reply": "「心跳得这么快……是因为外面太危险，还是因为……离我太近了？」", "score": 30},
            {"text": "小声调侃：「大明星也有这么狼狈的时候呀？」", "reply": "「还不是为了能和你单独待一会儿……真是拿你没办法。」", "score": 25}
        ]
    },
    {
        "title": "🕶️ 机场同款引发的饭圈地震",
        "desc": "两人前脚刚一前一后离开机场，后脚就被火眼金睛的粉丝扒出戴了同款情侣项链，热搜瞬间爆了！",
        "dialogue": "「热搜爆了……经纪人刚才已经打电话来盘问了。不过，看着粉丝们的评论，我其实……」",
        "choices": [
            {"text": "紧张地问：「那怎么办？会不会对你工作有影响？」", "reply": "「傻瓜，我才不在乎热搜怎么说，我只担心你有没有被吓到。」", "score": 28},
            {"text": "开玩笑道：「那要不索性公开承认算了？」", "reply": "「……这可是你说的。既然你都这么勇敢了，那我可就要顺水推舟咯。」", "score": 40}
        ]
    }
]

MAX_ACT = 6  # 6幕完整流程
# -----------------------------------------------------------------------------
# 4. STORIES 剧情库
# -----------------------------------------------------------------------------
STORIES = {
    "丈君": {
        "经纪人": {
            1: {
                "title": "🎬 丈君·后台初遇：大阪式的幽默开场",
                "scene": "Location: 电视台后台休息室 | Time: 18:00 | Atmosphere: 紧迫混乱，空气中弥漫着热咖啡与化妆品的气味",
                "prologue": "开演前倒计时30分钟,后台工作人员来回穿梭。丈君正拿着台词本狂背，脸上挂着招牌式的夸张表情。",
                "dialogue_intro": [
                    ("丈君", "“糟糕糟糕！这个关西腔的梗要是东京观众不买账怎么办？经纪人，你看我这表情够滑稽吗？”"),
                    ("经纪人", "（看着他一边擦汗一边摆出搞笑鬼脸，无奈地叹了口气）"),
                ],
                "choices": [
                    {
                        "option": "配合他的梗吐槽：『别耍宝了，快把台词对完！』",
                        "dialogue_response": [
                            ("丈君", "『哈哈，不愧是我的专属经纪人，这接梗速度满分！』"),
                            ("丈君", "『好啦听你的，我现在立刻进入极度认真状态！』"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "递上一杯热茶：『辛苦啦，润润嗓子。』",
                        "dialogue_response": [
                            ("丈君", "『有你在，比喝什么都甜！不过……笑话还是要继续讲的～』"),
                            ("经纪人", "『再贫嘴小心一会儿在台上打嗝哦。』"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.4,
                            "event_title": "⚡ 突发心动：指尖的触碰",
                            "narrative": "接过茶杯时，他的指尖不小心碰到了你的手背，原本嘈杂的后台似乎瞬间安静了一秒。",
                            "dialogue": ("丈君", "“咳……那个，茶温度刚刚好，谢谢你啊。”"),
                            "bonus_affection": 5,
                        },
                    },
                    {
                        "option": "严肃地看手表：『距离上台还有5分钟，认真点。』",
                        "dialogue_response": [
                            ("丈君", "『遵命大总管！为了不让你生气，我马上进入帅气模式！』"),
                            ("丈君", "（立刻收起笑容挺直腰板，眼神变得无比专注）"),
                        ],
                        "affection": 15,
                        "random_event": None,
                    },
                ],
            },
            2: {
                "title": "🎬 丈君·深夜对谈：卸下防备的温柔",
                "scene": "Location: 酒店顶楼露台 | Time: 23:30 | Atmosphere: 微风徐徐，远方是大阪霓虹闪烁的夜景",
                "prologue": "高强度的演出终于结束，丈君一个人站在露台栏杆旁，手里的啤酒罐结满了冰汽水珠。",
                "dialogue_intro": [
                    ("经纪人", "“一个人在这里发呆？今天的演出非常成功哦。”"),
                    ("丈君", "“啊，你来了……其实在台上让大家发笑的时候，偶尔也会担心自己如果不够幽默该怎么办。”"),
                ],
                "choices": [
                    {
                        "option": "听他讲搞笑背后的压力，拍拍他肩膀",
                        "dialogue_response": [
                            ("丈君", "『哎呀，突然这么温柔我会不习惯的……不过，有你真好。』"),
                            ("丈君", "（顺势靠在你的肩膀上，深深吸了一口气）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "笑他刚才在台上滑稽的动作",
                        "dialogue_response": [
                            ("丈君", "『喂！那叫舞台表现力！不许笑话我！』"),
                            ("经纪人", "『好好好，表现力满分的大明星～』"),
                        ],
                        "affection": 15,
                        "random_event": None,
                    },
                    {
                        "option": "默默陪着他看夜景，递上热咖啡",
                        "dialogue_response": [
                            ("丈君", "『累的时候只要转头看到你在，我就充满电了。』"),
                            ("丈君", "（侧过脸看着你，月光洒在他深邃的眼眸里）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.3,
                            "event_title": "🌙 突发心动：夜风中的拥抱",
                            "narrative": "夜风忽然变大，丈君脱下外衣轻轻披在你肩膀上，并将你轻轻拉近了一点。",
                            "dialogue": ("丈君", "“别感冒了，我可不想看我的经纪人倒下。”"),
                            "bonus_affection": 10,
                        },
                    },
                ],
            },
            3: {
                "title": "☀️ 第二天：请选择今日安排",
                "scene": "Location: 酒店大堂 | Time: 09:00 | Atmosphere: 阳光明媚，新的一天行程即将开始",
                "prologue": "丈君早早等在电梯口，戴着鸭舌帽和口罩，元气满满地向你招手。",
                "dialogue_intro": [
                    ("丈君", "“早啊！今天的日程全听大经纪人安排，我们去哪？”"),
                ],
                "choices": [
                    {
                        "option": "去通告现场探班",
                        "dialogue_response": [
                            ("丈君", "『台词我都记熟啦，随时可以开始！』"),
                            ("经纪人", "『那我们出发吧，别让摄制组久等。』"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "在酒店休息对剧本",
                        "dialogue_response": [
                            ("丈君", "『有你陪着对剧本，效率都变高了呢。』"),
                            ("丈君", "（开心地拉开椅子让你坐下）"),
                        ],
                        "affection": 15,
                        "random_event": None,
                    },
                    {
                        "option": "秘密约会，小心被发现",
                        "dialogue_response": [
                            ("丈君", "『难得的休息日，今天听你的安排！』"),
                            ("丈君", "（拉低帽檐，偷偷牵起你的手走小路）"),
                        ],
                        "affection": 18,
                        "random_event": {
                            "trigger_rate": 0.5,
                            "event_title": "🚨 突发事件：路人认出！",
                            "narrative": "旁边突然有粉丝惊呼『是丈君吗？！』，丈君瞬间果断拉着你一路跑进小巷。",
                            "dialogue": ("丈君", "“呼……太刺激了！不过牵着你的手跑，感觉像在演电影。”"),
                            "bonus_affection": 8,
                        },
                    },
                ],
            },
            4: {
                "title": "🎬 丈君·近距离对峙：大阪男人的直球",
                "scene": "Location: 休息室角落 | Time: 16:00 | Atmosphere: 私密狭窄，连呼吸声都清晰可见",
                "prologue": "练习室门被关上，丈君将你一步步逼到墙边，平时的搞笑面具彻底褪去。",
                "dialogue_intro": [
                    ("丈君", "“你总是把我当成需要照顾的艺人……但我也是个男人啊。”"),
                ],
                "choices": [
                    {
                        "option": "假装板起脸：『身为艺人要稳重！』",
                        "dialogue_response": [
                            ("丈君", "『对别人我稳重，对你嘛……我只想做最真实的自己。』"),
                            ("丈君", "（眼神坚定地注视着你，没有任何退缩的意思）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "被逗笑：『好啦，不跟你贫嘴了。』",
                        "dialogue_response": [
                            ("丈君", "『别走嘛，多看看我，今天可是特意为你练习了帅气眼神。』"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "调侃他：『今天表现不错，给个好评。』",
                        "dialogue_response": [
                            ("丈君", "『光有好评不够，得加个“一辈子专属”的长期契约才行！』"),
                        ],
                        "affection": 15,
                        "random_event": None,
                    },
                ],
            },
            5: {
                "title": "🎬 丈君·突发通告：电视台的秘密同行",
                "scene": "Location: 电视台大楼门外 | Time: 20:00 | Atmosphere: 闪光灯频闪，狗仔与记者蜂拥而至",
                "prologue": "刚走出大门，不知从哪涌出一群狗仔记者，长枪短炮瞬间围了上来。",
                "dialogue_intro": [
                    ("记者", "“丈君！请问旁边的这位是你的恋人吗？！”"),
                    ("丈君", "（条件反射般地一步跨到你身前）"),
                ],
                "choices": [
                    {
                        "option": "主动帮他挡住媒体镜头",
                        "dialogue_response": [
                            ("丈君", "『谢谢你……在镜头前护着我的样子，真的很帅气。』"),
                            ("丈君", "（趁乱紧紧握了握你的手）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "开玩笑：『大明星传绯闻了怎么办？』",
                        "dialogue_response": [
                            ("丈君", "『那就顺水推舟，直接公开说你是我的人！』"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "低声提醒他注意安全",
                        "dialogue_response": [
                            ("丈君", "『放心吧，只要你在身边，我什么都不怕。』"),
                        ],
                        "affection": 15,
                        "random_event": None,
                    },
                ],
            },
            6: {
                "title": "🎬 丈君·心意确认：大阪的浪漫星空",
                "scene": "Location: 摩天轮顶端 | Time: 22:00 | Atmosphere: 绝美夜景，静谧而浪漫的私密空间",
                "prologue": "摩天轮缓缓上升至最高点，整个大阪的灯火尽收眼底。",
                "dialogue_intro": [
                    ("丈君", "“传说在摩天轮最高点许愿的人，会永远在一起……你信吗？”"),
                ],
                "choices": [
                    {
                        "option": "靠在他肩膀上：『明天还要继续努力哦。』",
                        "dialogue_response": [
                            ("丈君", "『只要想到明天能见到你，我就浑身是劲！』"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "假装嫌弃他话多",
                        "dialogue_response": [
                            ("丈君", "『嫌弃也没用，我一辈子都要缠着你！』"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "认真注视他",
                        "dialogue_response": [
                            ("丈君", "『好啦，不闹了，我认真的……谢谢你一直陪着我。』"),
                            ("丈君", "（轻轻握住你的手，深情地吻了你的手背）"),
                        ],
                        "affection": 30,
                        "random_event": {
                            "trigger_rate": 1.0,  # 结局必触发专属事件
                            "event_title": "💖 最终事件：大阪之夜的告白",
                            "narrative": "烟花正好在窗外绽放，将他的侧脸照得温柔无比。",
                            "dialogue": ("丈君", "“不是经纪人和艺人，而是作为普通人的我……想一直守护你。”"),
                            "bonus_affection": 20,
                        },
                    },
                ],
            },
        },
    },
"青梅竹马": {
    1: {
        "title": "🎬 丈君·放学路：从小打到大的欢喜冤家",
        "scene": "Location: 商业街夕阳下 | Time: 17:00 | Atmosphere: 金色的晚霞，微风吹拂，街角关东煮的香气",
        "prologue": "放学钟声响过，你和丈君一前一后走在熟悉的回家路上。这家伙正低着头一边滑手机一边傻笑，完全没注意前面的电线杆。",
        "dialogue_intro": [
            ("丈君", "“哈哈哈哈！这个关西梗太搞笑了吧，等会儿回去我要发给团员看……”"),
            ("青梅", "（看着他差点撞上电线杆，忍不住伸手抓住了他的后衣领）"),
        ],
        "choices": [
            {
                "option": "抢过他的书包：『大明星走路还敢玩手机！』",
                "dialogue_response": [
                    ("丈君", "『喂！快还给我！青梅竹马也不能在大街上损我面子啊！』"),
                    ("青梅", "『谁让你差点撞杆子！看路啦！』"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "买了两支冰淇淋分他一只",
                "dialogue_response": [
                    ("丈君", "『还是你最懂我！不过这支化得比你笑得还快！』"),
                    ("丈君", "（张大嘴一口咬掉半个，被冰得直吐舌头）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🍦 突发心动：沾到嘴角的奶油",
                    "narrative": "他吃得太急，嘴角沾了一点白色的奶油。你下意识拿出手帕帮他擦掉，他猛地愣住了。",
                    "dialogue": ("丈君", "“别、别突然凑这么近啊……我又不是小孩子了！”"),
                    "bonus_affection": 5,
                },
            },
            {
                "option": "像小时候一样揪他耳朵：『放学不准乱跑！』",
                "dialogue_response": [
                    ("丈君", "『痛痛痛！遵命青梅大人，小的马上乖乖跟你回家。』"),
                    ("丈君", "（揉着耳朵撇撇嘴，眼神里却全是纵容的笑意）"),
                ],
                "affection": 15,
                "random_event": None,
            },
        ],
    },
    2: {
        "title": "🎬 丈君·秘密基地：童年树下的真心话",
        "scene": "Location: 后山大榕树下 | Time: 18:30 | Atmosphere: 蝉鸣渐弱，树影婆娑，木盒里装着童年的回忆",
        "prologue": "两人来到了从小到大藏秘密的树洞旁，丈君拍了拍身上的灰尘，坐在草地上长舒一口气。",
        "dialogue_intro": [
            ("丈君", "“每次觉得压力大的时候，只要来到这里，就感觉又变回了当年那个无忧无虑的小孩。”"),
            ("青梅", "“毕竟这里可是我们挖过时光胶囊的地方嘛。”"),
        ],
        "choices": [
            {
                "option": "翻出以前写给彼此的幼稚信件",
                "dialogue_response": [
                    ("丈君", "『天呐快烧掉！黑历史绝对不能让你看见！』"),
                    ("丈君", "（慌乱地伸手去抢，结果两人一起摔倒在草地上）"),
                ],
                "affection": 15,
                "random_event": None,
            },
            {
                "option": "认真听他讲梦想与成名的迷茫",
                "dialogue_response": [
                    ("丈君", "『不管我以后走得多远，你永远是我第一个想分享喜悦的人。』"),
                    ("青梅", "『我会一直在台下看着你的，放心吧。』"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "🌟 突发心动：星空下的肩膀",
                    "narrative": "他轻轻靠在你的肩膀上，声音有些疲惫却无比安心。",
                    "dialogue": ("丈君", "“别动……就让我靠一小会儿， Recharge 完成我就又是那个大明星了。”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "把零食分给他吃",
                "dialogue_response": [
                    ("丈君", "『从小到大都是你在照顾我……以后换我来保护你啦。』"),
                    ("丈君", "（咔哧咔哧啃着饼干，眼神却无比认真）"),
                ],
                "affection": 20,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：青梅的晨间小互动",
        "scene": "Location: 丈君家门口 | Time: 07:30 | Atmosphere: 清晨新鲜的空气，阳光穿过树叶撒在路面上",
        "prologue": "晨光熹微，你拿着面包走到了隔壁丈君家门前。没过多久，门被猛地拉开，丈君头发蓬乱地冲了出来。",
        "dialogue_intro": [
            ("丈君", "“糟了糟了要迟到了！诶？你怎么在这里？”"),
        ],
        "choices": [
            {
                "option": "在他家门口等他上学",
                "dialogue_response": [
                    ("丈君", "『每次出门都能看到你，这种感觉真好。』"),
                    ("丈君", "（憨笑着摸了摸头，把乱糟糟的头发压低了一点）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "顺手帮他整理乱糟糟的衣领",
                "dialogue_response": [
                    ("丈君", "『哎呀别动嘛……只有你敢对我这么像老妈子。』"),
                    ("丈君", "（嘴上嫌弃，身体却乖乖站直让你帮忙整理）"),
                ],
                "affection": 18,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "💓 突发心动：慌张的呼吸",
                    "narrative": "整理衣领时你的手不小心触碰到他的颈尖，他的呼吸瞬间一滞，脸颊微微泛红。",
                    "dialogue": ("丈君", "“咳！那个……今天天气真不错哈！”"),
                    "bonus_affection": 6,
                },
            },
            {
                "option": "比赛谁先跑到学校",
                "dialogue_response": [
                    ("丈君", "『这次我绝对不会输给你的！看招！』"),
                    ("丈君", "（说完拔腿就跑，还顺便对你吐了吐舌头）"),
                ],
                "affection": 15,
                "random_event": None,
            },
        ],
    },
    4: {
        "title": "🎬 丈君·校园祭典：摊位前的并肩作战",
        "scene": "Location: 学校操场炒面摊 | Time: 13:00 | Atmosphere: 热气腾腾的炒面香气，人山人海的喧闹祭典",
        "prologue": "文化祭热火朝天地进行着，班级的炒面摊位前挤满了人，丈君挽起袖子在铁板前卖力地翻炒着。",
        "dialogue_intro": [
            ("丈君", "“呼……关西大厨特制炒面！快来买啊！……喂，你别光看着，快来帮帮我啊！”"),
        ],
        "choices": [
            {
                "option": "帮他揽客：『来看大帅哥炒面啦！』",
                "dialogue_response": [
                    ("丈君", "『喂！怎么把我当招牌了！不过……为了你，多卖几盘也行！』"),
                    ("丈君", "（炒面铲子挥得飞起，脸上全是自信的笑容）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "递上面巾纸擦汗",
                "dialogue_response": [
                    ("丈君", "『谢谢……每次看你笑，我就觉得累点也无所谓。』"),
                    ("丈君", "（接过纸巾，趁无人注意轻轻抓了抓你的手指）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🔥 突发心动：铁板前的英雄救美",
                    "narrative": "油星突然炸开，丈君瞬间一步跨过来将你揽在身后，用背部挡住了热油。",
                    "dialogue": ("丈君", "“没事吧？！笨蛋，离铁板远一点，烫到你怎么办！”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "偷吃一口炒面",
                "dialogue_response": [
                    ("丈君", "『那是留给你的！不过……你吃过的好像更甜一点。』"),
                    ("青梅", "『瞎说什么呢，这是咸口的炒面啦！』"),
                ],
                "affection": 15,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 丈君·月下表白前夜：无法掩饰的心跳",
        "scene": "Location: 祭典后的神社后山 | Time: 20:30 | Atmosphere: 远处烟花绽放的声音，近处寂静的石阶与月光",
        "prologue": "喧嚣的祭典散去，两人踱步走到后山石阶上。丈君看着远处升起的烟花，久久没有说话。",
        "dialogue_intro": [
            ("丈君", "“其实……我一直在想一个问题。关于我们两个的关系。”"),
            ("青梅", "（看着他比平时严肃得多的侧脸，心跳不由自主地加快了）"),
        ],
        "choices": [
            {
                "option": "戳他肩膀：『想什么呢这么出神？』",
                "dialogue_response": [
                    ("丈君", "『在想怎么才能名正言顺地把你从“青梅”变成“恋人”。』"),
                    ("丈君", "（转过头，眼神里藏着从未有过的炽热）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🎆 突发心动：烟花下的近距离",
                    "narrative": "巨响声中，巨大的烟花在夜空盛开，他借着噪音的掩护，猛地将你拉近到怀里。",
                    "dialogue": ("丈君", "“我不想再玩笑了，这一次我是认真的。”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "假装没听清",
                "dialogue_response": [
                    ("丈君", "『不准装傻！今天必须给我个明确回应！』"),
                    ("丈君", "（双手捧住你的脸，强迫你直视他的眼睛）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "温柔微笑",
                "dialogue_response": [
                    ("丈君", "『好啦，听你的就是了。』"),
                    ("丈君", "（看到你的笑容，紧张的表情终于松懈下来，露出了温柔的笑意）"),
                ],
                "affection": 30,
                "random_event": None,
            },
        ],
    },
    6: {
        "title": "🎬 丈君·告白结局：青梅到恋人的华丽转身",
        "scene": "Location: 神社鸟居下 | Time: 21:00 | Atmosphere: 璀璨的烟花盛开在夜空，清风拂过，浪漫气氛达到顶点",
        "prologue": "烟花在头顶轰然炸开，将夜空照得通明。丈君停下脚步，转过身认真地拉住了你的双手。",
        "dialogue_intro": [
            ("丈君", "“我不想再做你的青梅竹马了。我想做那个可以合法拥抱你、保护你一辈子的人。”"),
        ],
        "choices": [
            {
                "option": "笑着用额头抵住他的额头：『以后不准再叫我大姐头了。』",
                "dialogue_response": [
                    ("丈君", "『遵命！我的恋人大人，从今天起换我来宠你。』"),
                    ("丈君", "（将你紧紧抱入怀中，在你耳边低语）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "红着脸接受他的拥抱",
                "dialogue_response": [
                    ("丈君", "『太好了……青梅竹马什么的太慢了，我早就想成为你的唯一了！』"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "十指相扣：『走吧，去见我们的未来。』",
                "dialogue_response": [
                    ("丈君", "『嗯！手牵手，一辈子都不放开！』"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局专属100%触发事件
                    "event_title": "💖 专属结局：一辈子的契约",
                    "narrative": "月光将两人的身影拉得很长很长，从小打到大的欢喜冤家，终于在今夜落下了爱情的定音符。",
                    "dialogue": ("丈君", "“余生请多指教啦，我的专属小青梅——不，是我的女主角。”"),
                    "bonus_affection": 15,
                },
            },
        ],
    },
},
"在日留学生or打工人": {
    1: {
        "title": "🎬 丈君·异国偶遇：电车站的关西腔问候",
        "scene": "Location: 东京山手线电车站台 | Time: 18:30 | Atmosphere: 人潮拥挤的下班高峰期，电车鸣笛声与广播交织",
        "prologue": "在异国他乡的东京打工/求学，每天最疲惫的就是挤电车。站台上人头攒动，你突然在喧闹中听到了一声极其地道的大阪关西腔。",
        "dialogue_intro": [
            ("丈君", "“糟糕糟糕！东京这迷宫一样的换乘到底在哪啊……早知道不装酷一个人跑出来了！”"),
            ("在日组", "（看着他举着地图慌张转圈的样子，忍不住噗嗤一笑）"),
        ],
        "choices": [
            {
                "option": "用关西腔开玩笑打招呼：『元气吗大叔！』",
                "dialogue_response": [
                    ("丈君", "『哇！居然比我还地道！异国他乡听到这个太感动了！』"),
                    ("丈君", "（眼里瞬间亮起光，像是找到了救命稻草）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "塞给他一块家乡带的糖果",
                "dialogue_response": [
                    ("丈君", "『甜到心里去了！今天打工的疲惫瞬间一扫而空。』"),
                    ("丈君", "（剥开糖纸塞进嘴里，脸上露出极其满足的笑容）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🍬 突发心动：异国的温情",
                    "narrative": "他把糖果塞进嘴里的同时，顺手从口袋掏出一枚小巧的关西吉祥物挂件放在你手里。",
                    "dialogue": ("丈君", "“这是回礼！在这个冷冰冰的城市里，谢谢你给的温暖。”"),
                    "bonus_affection": 5,
                },
            },
            {
                "option": "帮他指路：『那边车快开了，快跑！』",
                "dialogue_response": [
                    ("丈君", "『多亏有你！不然我在东京真的要变成路痴了。』"),
                    ("丈君", "（拉着你的手腕一路狂奔，终于在车门关闭前冲了进去）"),
                ],
                "affection": 15,
                "random_event": None,
            },
        ],
    },
    2: {
        "title": "🎬 丈君·异国互助：居酒屋的深夜畅谈",
        "scene": "Location: 新宿巷弄里的深夜居酒屋 | Time: 23:00 | Atmosphere: 暖黄色的灯光，烤串的烟气，外头飘着冷雨",
        "prologue": "结束了一整天高强度的语言学校课程和打工，两人挤在狭小的居酒屋角落里，点了一桌热腾腾的关东煮。",
        "dialogue_intro": [
            ("丈君", "“呼……今天被店长训了一顿，关西话差点脱口而出。在异国打工真的太不易了啊。”"),
            ("在日组", "“理解理解，在这个城市里拼搏，谁都不容易呢。”"),
        ],
        "choices": [
            {
                "option": "听他抱怨异国生活的不易",
                "dialogue_response": [
                    ("丈君", "『幸好在东京能遇见你，不然我真的要撑不下去了。』"),
                    ("丈君", "（双手托着脸，眼神温柔地看着你）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "抢着付账：『今天这顿我请！』",
                "dialogue_response": [
                    ("丈君", "『那怎么行！说好下次我发工资请你的，不许抢！』"),
                    ("丈君", "（一把按住你拿钱包的手，神情坚决而执着）"),
                ],
                "affection": 15,
                "random_event": None,
            },
            {
                "option": "笑着递上热毛巾",
                "dialogue_response": [
                    ("丈君", "『每次看你笑，我就觉得异国他乡也没那么冷了。』"),
                    ("丈君", "（接过毛巾擦了擦手，嘴角的笑容暖意融融）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "🍺 突发心动：微醺的真心话",
                    "narrative": "喝了一小口啤酒的他脸颊微红，突然伸手轻轻盖在了你放在桌上的手上。",
                    "dialogue": ("丈君", "“说真的……在东京最幸运的事，就是遇到了同在努力的你。”"),
                    "bonus_affection": 8,
                },
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：东京街头的元气集合",
        "scene": "Location: 代代木公园&当地超市 | Time: 10:00 | Atmosphere: 明媚阳光，微风清爽，街角草坪上散落的落叶",
        "prologue": "难得两人重合的休假日，阳光洒在街道上，空气里夹杂着面包店新鲜烘焙的香气。",
        "dialogue_intro": [
            ("丈君", "“早啊！难得不用打工和上课，今天一定要把在异国积攒的压力全都释放掉！”"),
        ],
        "choices": [
            {
                "option": "约在早市一起挑新鲜食材",
                "dialogue_response": [
                    ("丈君", "『和你一起逛超市，有种在新婚过日子的错觉呢。』"),
                    ("丈君", "（推着购物车，一边往里面放你爱吃的零食）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "陪他去语言学校旁听",
                "dialogue_response": [
                    ("丈君", "『有你在旁边看着，我回答问题都更有底气了！』"),
                    ("丈君", "（课上被老师点名时，偷偷向你投来求助又骄傲的眼神）"),
                ],
                "affection": 18,
                "random_event": None,
            },
            {
                "option": "坐在公园长椅上晒太阳背单词",
                "dialogue_response": [
                    ("丈君", "『单词记不住没关系，记住你的笑容就够了。』"),
                    ("丈君", "（靠在长椅靠背上，伸了个大大的懒腰）"),
                ],
                "affection": 15,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "📖 突发心动：草坪上的小憩",
                    "narrative": "背着背着单词，他的头忽然轻轻歪斜，靠在了你的大腿上睡着了，呼吸均匀而安心。",
                    "dialogue": ("丈君", "“嗯……让我睡五分钟，别走哦……”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 丈君·异国打工突发：暴雨中的便利店",
        "scene": "Location: 便利店门口檐下 | Time: 21:30 | Atmosphere: 倾盆大雨，霓虹灯倒映在湿滑的路面上",
        "prologue": "打工下班时突降暴雨，你困在便利店门檐下。丈君一路冒雨跑来，身上湿了大半，手里却死死怀抱着一把伞。",
        "dialogue_intro": [
            ("丈君", "“呼……呼……还好你还没走！给，我从宿舍一路冲过来送伞了！”"),
        ],
        "choices": [
            {
                "option": "分他一把伞：『一起撑吧。』",
                "dialogue_response": [
                    ("丈君", "『伞太小了……这样吧，你全拿着，我淋湿没关系，别把你弄湿了。』"),
                    ("丈君", "（默默将伞柄完全倾斜向你这一边，自己的右肩全被雨水打湿）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🌧️ 突发心动：雨中的手臂交叠",
                    "narrative": "为了不让你被雨淋倒，他伸手将你紧紧揽入怀侧，两人距离近得能听到彼此的心跳声。",
                    "dialogue": ("丈君", "“再往我这边靠靠……听话，别感冒了。”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "买关东煮暖手",
                "dialogue_response": [
                    ("丈君", "『谢谢你给的温暖，东京的雨夜突然就不冷了。』"),
                    ("丈君", "（捧着热气腾腾的纸杯，哈出一口白气，眼神无比满足）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "调侃他淋湿的样子像落汤鸡",
                "dialogue_response": [
                    ("丈君", "『喂！好歹给留点面子嘛！我可是冒着大雨来救你的英雄！』"),
                    ("丈君", "（甩了甩头发上的水珠，露出搞怪的笑容）"),
                ],
                "affection": 15,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 丈君·回国倒计时：东京塔下的不舍",
        "scene": "Location: 东京铁塔展望台 | Time: 22:00 | Atmosphere: 橘红色的塔光照亮夜空，脚下是繁星般的城市灯火",
        "prologue": "签证与学业/工作阶段即将告一段落，回国的倒计时正在一分一秒流逝。两人站在巨幅玻璃窗前俯瞰夜景。",
        "dialogue_intro": [
            ("丈君", "“时间过得真快啊……感觉昨天才在电车站遇到你，怎么突然就要面对离别了。”"),
            ("在日组", "（看着窗外闪烁的东京塔，心中充满酸涩与不舍）"),
        ],
        "choices": [
            {
                "option": "看着夜景：『真舍不得这里。』",
                "dialogue_response": [
                    ("丈君", "『舍不得风景还是舍不得我？如果是后者，我可以立刻留下来。』"),
                    ("丈君", "（转过身，用从未有过的极其认真的眼神凝视着你）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "拍拍他：『别开玩笑了。』",
                "dialogue_response": [
                    ("丈君", "『我认真的！没有你的地方，哪里都不是大阪。』"),
                    ("丈君", "（一把抓住你想要抽回的手，力道大得让你无法挣脱）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "紧紧抱住他",
                "dialogue_response": [
                    ("丈君", "『嗯，回国后我们再也不分开了。』"),
                    ("丈君", "（反手将你深深拥入怀中，下巴抵在你的发间）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🗼 突发心动：塔顶的誓言",
                    "narrative": "东京塔的灯光突然熄灭（地标熄灯传说），他在黑暗降临的瞬间轻轻在你额头上落下一吻。",
                    "dialogue": ("丈君", "“听说在熄灯时许愿会成真……我的愿望是，余生一直有你。”"),
                    "bonus_affection": 10,
                },
            },
        ],
    },
    6: {
        "title": "🎬 丈君·告白结局：异国星空下的真情告白",
        "scene": "Location: 芝公园的草坪 | Time: 22:30 | Atmosphere: 塔光重亮，夜风吹拂，漫天星辰与地上的灯火交相辉映",
        "prologue": "走下展望台，公园里安静得只能听到微风吹拂树叶的声音。丈君停下脚步，转过身抱紧了你。",
        "dialogue_intro": [
            ("丈君", "“在异国他乡的这段日子，因为有你，所有的辛苦都变成了甜的。我不想只做你在异国互相扶持的朋友……”"),
        ],
        "choices": [
            {
                "option": "紧紧握住他的手：『不管回国后多远，我都在。』",
                "dialogue_response": [
                    ("丈君", "『嗯！回国后我们就公开，我的未来里绝对不能没有你！』"),
                    ("丈君", "（十指紧扣，目光坚定地注视着你）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "笑着流泪",
                "dialogue_response": [
                    ("丈君", "『不许哭哦！以后在我的个人演唱会上，你必须坐在最中间的位置看我。』"),
                    ("丈君", "（温柔地伸出大拇指擦去你眼角湿润的泪痕）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "靠在他怀里看着东京铁塔",
                "dialogue_response": [
                    ("丈君", "『好，一言为定，我们要永远在一起。』"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "💖 专属结局：跨越异国的约定",
                    "narrative": "东京塔的灯光再次亮起，将两人的倒影贴合在一起。异国打工/留学的辛苦在这一刻彻底化作最甜美的情书。",
                    "dialogue": ("丈君", "“从今天起，你就是我最宝贵的‘专属经纪人’兼‘终身伴侣’啦！”"),
                    "bonus_affection": 15,
                },
            },
        ],
    },
},
"大酱": {
    "经纪人": {
        1: {
            "title": "🎬 大酱·企划开端：天才C位的完美微笑",
            "scene": "Location: 电视台舞蹈排练室 | Time: 14:00 | Atmosphere: 柔和的阳光透过落地窗，背景放着轻快的音乐，镜子折射出汗水",
            "prologue": "正在进行新曲舞台的复盘，大吾擦着汗坐在舞蹈室地上，手里拿着自己画的舞台构想草图。",
            "dialogue_intro": [
                ("大吾", "“作为经纪人，你觉得这个舞台灯光切换的节点怎么样？我想在副歌部分给每个人都安排绝杀镜头！”"),
                ("经纪人", "（看着他闪闪发光的眼睛，拿起床边的水瓶递过去）"),
            ],
            "choices": [
                {
                    "option": "称赞他的舞台构思：『不愧是西畑大吾，考虑得太周到了！』",
                    "dialogue_response": [
                        ("大吾", "『嘿嘿，只要能让大家看到最棒的演出，这点心思算什么！有你夸奖我更有动力啦。』"),
                        ("大吾", "（眼睛弯成月牙，露出招牌式的甜美偶像微笑）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "✨ 突发心动：专业的反差萌",
                        "narrative": "他突然凑近，拿着草图在你面前晃了晃，眼里的热切与骄傲藏都藏不住。",
                        "dialogue": ("大吾", "“这可是只属于你的独家预演哦，等下的正式彩排可看不到这么近的版块！”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "提醒他注意休息别太拼",
                    "dialogue_response": [
                        ("大吾", "『好啦好啦，大吾妈妈上线！不过……听你的总没错，我会乖乖休息的。』"),
                        ("大吾", "（乖乖盘腿坐好，接过你递过来的水瓶咕噜咕噜喝水）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "递过日程表：『今天的通告压力很大哦。』",
                    "dialogue_response": [
                        ("大吾", "『交给我吧！只要看到你在这儿坐镇，我就知道今天一切都会顺顺利利。』"),
                        ("大吾", "（快速翻看行程表，自信地对你眨了眨眼）"),
                    ],
                    "affection": 15,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 大酱·深夜构思：后台的推心置腹",
            "scene": "Location: 电视台深夜休息室 | Time: 23:30 | Atmosphere: 柔和的黄光，外面安静的走廊，桌上散落着各种台本",
            "prologue": "录制结束后，休息室里只剩下你们两个人。大吾捏着眉心，仍在反复推敲明日综艺的梗与台词。",
            "dialogue_intro": [
                ("大吾", "“感觉这个金句还不够爆啊……作为C位，不把气氛拉满可不行呢。”"),
            ],
            "choices": [
                {
                    "option": "递上一杯热牛奶：『还在琢磨明天的番组台词呢？』",
                    "dialogue_response": [
                        ("大吾", "『哇，你怎么知道我卡壳了？不愧是我的最佳拍档，连这都能猜到。』"),
                        ("大吾", "（双手捂着热牛奶，长舒了一口气）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "轻轻敲打他脑袋：『劳逸结合懂不懂？』",
                    "dialogue_response": [
                        ("大吾", "『痛……好啦听你的，不看了不看了，今晚只准看你。』"),
                        ("大吾", "（抓住你敲他的手，眼神里带着一丝娇嗔与撒娇）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "坐在旁边安静陪着他",
                    "dialogue_response": [
                        ("大吾", "『有你这样默默陪着，突然觉得当C位的压力也没有那么沉重了。』"),
                        ("大吾", "（侧过头靠在沙发背上，温热的呼吸吐在你的手腕旁）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🌙 突发心动：卸下防备的瞬间",
                        "narrative": "卸去了“完美偶像”的光环，他轻轻把头靠在你的肩膀上，声音低沉而慵懒。",
                        "dialogue": ("大吾", "“让我靠五分钟……只有在你面前，我才不用做那个无坚不摧的西畑大吾。”"),
                        "bonus_affection": 8,
                    },
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：演播厅的突击早会",
            "scene": "Location: 演播厅休息室化妆间 | Time: 08:00 | Atmosphere: 吹风机的轰鸣声，化妆品的香气，清晨忙碌又充实的氛围",
            "prologue": "早上8点，距离正式录制还有半小时。大吾已经换上了利落的西装，正对着镜子做最后的表情管理。",
            "dialogue_intro": [
                ("大吾", "“早啊！今天的状态绝对满分，准备好见证我的完美舞台了吗？”"),
            ],
            "choices": [
                {
                    "option": "帮他整理西装领带",
                    "dialogue_response": [
                        ("大吾", "『近看的话……你比演播厅的灯光还要耀眼呢。』"),
                        ("大吾", "（微微低着头任由你整理，目光一刻也没有离开你的脸）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "👔 突发心动：呼吸的距离",
                        "narrative": "你拉紧领带的瞬间，他突然伸手抓住了你的手腕，将距离拉得极近。",
                        "dialogue": ("大吾", "“做经纪人照顾得这么周到……会让我产生独占你的野心哦。”"),
                        "bonus_affection": 6,
                    },
                },
                {
                    "option": "递上特制饭团：『补充元气！』",
                    "dialogue_response": [
                        ("大吾", "『太幸福了吧！今天一整天的元气C位由你承包了！』"),
                        ("大吾", "（大口咬下饭团，幸福得两眼发光）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "严肃核对脚本：『千万别临场自由发挥哦。』",
                    "dialogue_response": [
                        ("大吾", "『放心，我可是专业的大吾！绝对不会在你面前掉链子的。』"),
                        ("大吾", "（敬了个俏皮的礼，眼中闪烁着自信的光芒）"),
                    ],
                    "affection": 18,
                    "random_event": None,
                },
            ],
        },
        4: {
            "title": "🎬 大酱·镜头盲区：红白双颊的真心话",
            "scene": "Location: 舞台侧幕阴影处 | Time: 17:30 | Atmosphere: 前台喧嚣的音乐，侧幕昏暗的灯光，心跳加速的隐秘感",
            "prologue": "中场休息，他躲进摄像机拍不到的舞台侧幕。刚刚在台上面对镜头绽放完完美微笑的他，此刻脸颊透着绯红。",
            "dialogue_intro": [
                ("大吾", "“呼……刚才在台上看到你一直在台下盯着我，差点连舞步都乱了。”"),
            ],
            "choices": [
                {
                    "option": "开玩笑说他最近人气高涨",
                    "dialogue_response": [
                        ("大吾", "『人气再高有什么用，我最想看到的只有你对我一个人笑。』"),
                        ("大吾", "（在暗处轻轻拉住了你的手指，眼神真挚得让人窒息）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🎬 突发心动：镜头盲区的独占",
                        "narrative": "听到工作人员经过的脚步声，他一把将你拉进更深的阴影里，将你抵在布景板后。",
                        "dialogue": ("大吾", "“嘘……别说话。这里是摄像机拍不到的地方，也是我唯一能独占你的地方。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "假装没听见他刚才的碎碎念",
                    "dialogue_response": [
                        ("大吾", "『喂，不准装傻！我刚才那句可是极其认真的表白诶！』"),
                        ("大吾", "（有些气鼓鼓地轻轻戳了戳你的额头）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "拍拍他肩膀：『加油，C位殿下！』",
                    "dialogue_response": [
                        ("大吾", "『殿下也需要王后呀，不准跑，以后都要做我的专属观众。』"),
                        ("大吾", "（顺势揉了揉你的头发，笑容宠溺）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 大酱·突发转折：直播间的意外连线",
            "scene": "Location: 全国直播演播厅后台 | Time: 20:00 | Atmosphere: 倒计时闪烁，气氛紧张热烈，直播摄像机临场切入",
            "prologue": "生放送直播突发环节，主持人在台上面临临时提问“最感谢的幕后人员”，镜头突然切到了侧台的经纪人区域。",
            "dialogue_intro": [
                ("大吾", "“说到让我能够安心站在C位的人……当然是那位一直在幕后默默支持我的人了。”"),
                ("经纪人", "（突然被镜头拍到，心跳瞬间漏了一拍）"),
            ],
            "choices": [
                {
                    "option": "在镜头外挥手示意",
                    "dialogue_response": [
                        ("大吾", "『啊，刚才好像看到一个特别熟悉的身影……那是我心里最重要的人。』"),
                        ("大吾", "（对着你的方向眨了眨眼，引发现场粉丝一阵尖叫）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "低声用台本遮住脸",
                    "dialogue_response": [
                        ("大吾", "『别害羞嘛，虽然在直播，但我只想把视线全落在你身上。』"),
                        ("大吾", "（对着镜头落落大方地笑，眼里却全是对你的温柔）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "淡定面对突发状况",
                    "dialogue_response": [
                        ("大吾", "『有你在身边打底，就算现场直播突然断电我也一点不慌。』"),
                        ("大吾", "（下台后第一时间走到你面前，自然地拉起你的手）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "📻 突发心动：未关掉的麦克风",
                        "narrative": "走下舞台时他的无线麦克风还未完全关闭，他在你耳边低语的声音传出了微弱的回音。",
                        "dialogue": ("大吾", "“刚才在台上没敢说出口……你才是我这辈子唯一的Center。”"),
                        "bonus_affection": 10,
                    },
                },
            ],
        },
        6: {
            "title": "🎬 大酱·完美落幕：聚光灯下的专属告白",
            "scene": "Location: 演唱会散场后的空旷舞台 | Time: 21:30 | Atmosphere: 彩带纷飞后的余温，聚光灯打在舞台中央，安静而浪漫",
            "prologue": "演唱会完美收官，观众已全部退场。巨型舞台上只留下一盏聚光灯。大吾拉着你走上了舞台正中央。",
            "dialogue_intro": [
                ("大吾", "“站在这个曾经梦寐以求的C位上，我终于可以向最重要的听众做最后的总结了。”"),
            ],
            "choices": [
                {
                    "option": "微笑鼓掌：『今天的C位完美收官！』",
                    "dialogue_response": [
                        ("大吾", "『最完美的不是舞台，而是能遇见你。我的C位人生，从今以后只为你闪耀。』"),
                        ("大吾", "（在聚光灯下深深鞠躬，随后向你伸出双手）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "调侃他太会说情话",
                    "dialogue_response": [
                        ("大吾", "『这可不是套词，句句出自真心。不信的话，你摸摸我到现在还在狂跳的心。』"),
                        ("大吾", "（拉着你的手贴在他滚烫的胸口）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "紧紧握住他的手",
                    "dialogue_response": [
                        ("大吾", "『好啦，杀青快乐，我的大明星。』"),
                        ("大吾", "『不，是你的专属大吾。』"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,  # 终局100%触发事件
                        "event_title": "💖 专属结局：只为你闪耀的Center",
                        "narrative": "漫天未落尽的金切片在聚光灯下闪烁，他把你揽入怀中，在空无一人的千人场馆里印下深情一吻。",
                        "dialogue": ("大吾", "“谢谢你一直做我的光。从今往后，台上我是大家的偶像，台下我只是你一个人的西畑大吾。”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"青梅竹马": {
    1: {
        "title": "🎬 大酱·童年回忆：演剧部门口的巧合",
        "scene": "Location: 学校演剧部活动室门口 | Time: 18:00 | Atmosphere: 橘黄色的夕阳余晖，社团大楼传来的台词朗读声",
        "prologue": "社团活动结束，你路过演剧部门口，正好撞见刚结束排练的大吾靠在门框上翻看剧本。",
        "dialogue_intro": [
            ("大吾", "“诶？你怎么还没回家？是在专门等我吗？”"),
            ("青梅", "（晃了晃手里的东西，露出一丝调侃的笑容）"),
        ],
        "choices": [
            {
                "option": "笑话他小时候演话剧穿女装的黑历史",
                "dialogue_response": [
                    ("大吾", "『求求你快把那段记忆格式化！怎么每次都被你翻出来当把柄！』"),
                    ("大吾", "（捂着脸哀嚎，红着耳朵瞪了你一眼）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "带了热腾腾的关东煮探望",
                "dialogue_response": [
                    ("大吾", "『呜哇，还是你对我最最好！小时候分我零食，现在还管我夜宵。』"),
                    ("大吾", "（开心地接过关东煮，眼睛笑得弯弯的）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🍡 突发心动：分享的温热",
                    "narrative": "他夹起一块萝卜吹了吹，下意识地先递到你嘴边。",
                    "dialogue": ("大吾", "“张嘴~啊——这块最入味了，第一口先奖励给我的小青梅！”"),
                    "bonus_affection": 5,
                },
            },
            {
                "option": "催促他赶紧排练台词",
                "dialogue_response": [
                    ("大吾", "『遵命青梅大人！为了不让你久等，我马上进入天才演员模式！』"),
                    ("大吾", "（立刻站直身体，正色对你敬了个礼）"),
                ],
                "affection": 18,
                "random_event": None,
            },
        ],
    },
    2: {
        "title": "🎬 大酱·天台风波：梦想与少年的秘密",
        "scene": "Location: 学校教学楼天台 | Time: 12:30 | Atmosphere: 晴朗的天空，微风拂过网栏，台阶上的树荫",
        "prologue": "午休时间，大吾一个人坐在天台角落看云发呆，神情难得有些落寞。你轻手轻脚走过去在他身边坐下。",
        "dialogue_intro": [
            ("大吾", "“青梅……你说，我真的能站在最大的舞台上，成为大家都认可的演员吗？”"),
        ],
        "choices": [
            {
                "option": "静静听他倾诉对未来的不安",
                "dialogue_response": [
                    ("大吾", "『只要有你在背后支持我，不管前面的路多难，我都有勇气跑下去。』"),
                    ("大吾", "（侧过头凝视着你，眼神格外炽热而坚定）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "☁️ 突发心动：紧靠的肩膀",
                    "narrative": "一阵清风吹过，他顺势将头靠在你的肩膀上，深深吸了一口气。",
                    "dialogue": ("大吾", "“就借你的肩膀靠一小会儿……只要有你在身边，我的不安就全消失了。”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "塞给他一颗薄荷糖：『别想太多。』",
                "dialogue_response": [
                    ("大吾", "『嗯，瞬间清醒了。从小到大，你的薄荷糖总能治好我的焦虑。』"),
                    ("大吾", "（把糖果含进嘴里，露出招牌式的甜美笑容）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "开玩笑说以后要收他版权费",
                "dialogue_response": [
                    ("大吾", "『那我把自己整个人打包抵押给你，够不够付版权费呀？』"),
                    ("大吾", "（凑到你面前，笑眯眯地对你眨了眨眼）"),
                ],
                "affection": 18,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：晨光中的自行车后座",
        "scene": "Location: 上学途中的林荫大道 | Time: 07:40 | Atmosphere: 清晨新鲜的空气，穿过树叶刺破阴影的金色阳光",
        "prologue": "清晨的街道上，大吾踩着自行车顺着斜坡滑下，在你面前优雅地刹停。",
        "dialogue_intro": [
            ("大吾", "“早啊！今天天气这么好，要不要享受一下天才演员西畑大吾的专属接送服务？”"),
        ],
        "choices": [
            {
                "option": "拍拍自行车后座：『上来吧，带你去吃限定早餐。』",
                "dialogue_response": [
                    ("大吾", "『每次坐在你车后座，微风吹过来，我都觉得时间可以永远停在这。』"),
                    ("大吾", "（坐上后座，伸手轻轻环住了你的腰）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "抱怨他骑得太快抓紧他的衣角",
                "dialogue_response": [
                    ("大吾", "『抓紧咯！为了多听你叫几声，我可要加速了！』"),
                    ("大吾", "（坏笑着猛踩脚踏板，迎风欢快地冲下斜坡）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "安静地吃着手里的小面包",
                "dialogue_response": [
                    ("大吾", "『有你在身边的清晨，连空气都是甜滋滋的草莓味。』"),
                    ("大吾", "（微微偏过头看你，嘴角挂着满足的弧度）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "🚴‍♂️ 突发心动：微风中的心跳",
                    "narrative": "急刹车时你撞上了他的后背，他快速伸手稳稳抓住你的双手放在他腰间。",
                    "dialogue": ("大吾", "“抱紧我，掉下去的话我可是会心疼的哦。”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 大酱·文化祭前夜：道具房的密室心跳",
        "scene": "Location: 文化祭舞台后台道具房 | Time: 19:30 | Atmosphere: 昏暗的灯光，堆满舞台道具的狭小空间，外面的微风吹动窗帘",
        "prologue": "文化祭前夜，道具房里摆满了各种复杂的道具服装。你和大吾正在整理最后的演出用品，门却不小心被风吹上锁住了。",
        "dialogue_intro": [
            ("大吾", "“完蛋，门锁上了……看来在别人发现之前，我们得在这里呆一会儿了。”"),
        ],
        "choices": [
            {
                "option": "帮他整理乱糟糟的演出服",
                "dialogue_response": [
                    ("大吾", "『太近了……闻到你身上的味道，我连剧本台词全忘光了。』"),
                    ("大吾", "（低下头任由你收拾，眼神越来越深沉）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🎭 突发心动：密室里的幽香",
                    "narrative": "狭小的空间让气温急剧上升，他突然抓住你正在整理衣领的手，将你轻轻按在墙边。",
                    "dialogue": ("大吾", "“别动……再动的话，我可不敢保证自己还能维持‘青梅竹马’的界限了。”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "开玩笑：『大明星紧张啦？』",
                "dialogue_response": [
                    ("大吾", "『才没有！面对几万人都没怂过，面对你我才不是紧张……是心动。』"),
                    ("大吾", "（不服气地嘟囔着，脸颊却微微泛起红晕）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "递上矿泉水：『润润嗓子。』",
                "dialogue_response": [
                    ("大吾", "『谢谢你……如果今晚演出成功，我要第一个把花献给你。』"),
                    ("大吾", "（接过水喝了一口，微笑着向你许下承诺）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 大酱·星光月下：无法藏匿的目光",
        "scene": "Location: 学校后山观景台 | Time: 21:00 | Atmosphere: 皎洁的月光，远处城市的万家灯火，耳边清脆的蝉鸣",
        "prologue": "演出大获成功，后夜祭的欢呼声在远处回荡。大吾拉着你偷偷跑到了没有人的后山山顶。",
        "dialogue_intro": [
            ("大吾", "“呼……终于只有我们两个人了。其实今晚，我有个秘密一直想告诉你。”"),
        ],
        "choices": [
            {
                "option": "戳他红透的耳朵：『发烧啦？』",
                "dialogue_response": [
                    ("大吾", "『才不是发烧，是因为某人靠得太近，我的心跳彻底失控了。』"),
                    ("大吾", "（一把抓住你捣乱的手指，扣在自己的掌心里）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "假装看向夜空风景",
                "dialogue_response": [
                    ("大吾", "『别看风景了，难道我还不够好看吗？快把视线转过来嘛。』"),
                    ("大吾", "（有些吃醋地挡在你面前，强迫你的眼睛里只有他）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "温柔地回握住他的手",
                "dialogue_response": [
                    ("青梅", "『好啦，不逗你了。』"),
                    ("大吾", "『这可是你主动牵的，不许反悔哦！』"),
                    ("大吾", "（紧紧扣住你的五指，脸上露出了最灿烂的笑容）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🌙 突发心动：月色真美",
                    "narrative": "夜风吹过，他在月光下慢慢低头，温热的呼吸贴近了你的侧脸。",
                    "dialogue": ("大吾", "“今晚的月色真的很美……但我眼里，只有你。”"),
                    "bonus_affection": 10,
                },
            },
        ],
    },
    6: {
        "title": "🎬 大酱·终章告白：青梅竹马的直球反击",
        "scene": "Location: 两人从小一起玩耍的公园秋千旁 | Time: 21:30 | Atmosphere: 柔和的街灯，漫天星辰，静谧而深情的氛围",
        "prologue": "月光下，大吾站在秋千前，神情是从未有过的认真与炽热。他深深地吸了一口气，凝视着你的眼睛。",
        "dialogue_intro": [
            ("大吾", "“从小到大，我一直习惯了你在我身边。但我不想再当你的‘青梅竹马’了……我想做那个独占你的男朋友。”"),
        ],
        "choices": [
            {
                "option": "笑着承认心意：『其实我也早就喜欢你了。』",
                "dialogue_response": [
                    ("大吾", "『真的吗？！太好了……我还以为要单恋一辈子呢！从今以后，你就是我唯一的女主角！』"),
                    ("大吾", "（激动地一把把你抱起来转了个圈）"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "💖 专属结局：青梅恋人的誓言",
                    "narrative": "微风拂过公园的树梢，从小陪伴彼此长大的两个人，终于在今夜揭开了深藏多年的心意。",
                    "dialogue": ("大吾", "“未来的每一部戏、每一个舞台、每一段人生……我都只想和你一起走下去。”"),
                    "bonus_affection": 15,
                },
            },
            {
                "option": "轻声拥抱他：『以后也请多指教。』",
                "dialogue_response": [
                    ("大吾", "『遵命！我的青梅恋人，往后余生，我的剧本里全都是你。』"),
                    ("大吾", "（用力环住你的腰，将头埋在你的颈窝里）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "傲娇地哼了一声",
                "dialogue_response": [
                    ("大吾", "『哼什么哼，不管你怎么傲娇，这辈子你都别想逃出我的手掌心啦！』"),
                    ("大吾", "（宠溺地刮了刮你的鼻子，顺势牵住了你的手）"),
                ],
                "affection": 28,
                "random_event": None,
            },
        ],
    },
},
"青梅竹马": {
    1: {
        "title": "🎬 大酱·童年回忆：演剧部门口的巧合",
        "scene": "Location: 学校演剧部活动室门口 | Time: 18:00 | Atmosphere: 橘黄色的夕阳余晖，社团大楼传来的台词朗读声",
        "prologue": "社团活动结束，你路过演剧部门口，正好撞见刚结束排练的大吾靠在门框上翻看剧本。",
        "dialogue_intro": [
            ("大吾", "“诶？你怎么还没回家？是在专门等我吗？”"),
            ("青梅", "（晃了晃手里的东西，露出一丝调侃的笑容）"),
        ],
        "choices": [
            {
                "option": "笑话他小时候演话剧穿女装的黑历史",
                "dialogue_response": [
                    ("大吾", "『求求你快把那段记忆格式化！怎么每次都被你翻出来当把柄！』"),
                    ("大吾", "（捂着脸哀嚎，红着耳朵瞪了你一眼）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "带了热腾腾的关东煮探望",
                "dialogue_response": [
                    ("大吾", "『呜哇，还是你对我最最好！小时候分我零食，现在还管我夜宵。』"),
                    ("大吾", "（开心地接过关东煮，眼睛笑得弯弯的）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🍡 突发心动：分享的温热",
                    "narrative": "他夹起一块萝卜吹了吹，下意识地先递到你嘴边。",
                    "dialogue": ("大吾", "“张嘴~啊——这块最入味了，第一口先奖励给我的小青梅！”"),
                    "bonus_affection": 5,
                },
            },
            {
                "option": "催促他赶紧排练台词",
                "dialogue_response": [
                    ("大吾", "『遵命青梅大人！为了不让你久等，我马上进入天才演员模式！』"),
                    ("大吾", "（立刻站直身体，正色对你敬了个礼）"),
                ],
                "affection": 18,
                "random_event": None,
            },
        ],
    },
    2: {
        "title": "🎬 大酱·天台风波：梦想与少年的秘密",
        "scene": "Location: 学校教学楼天台 | Time: 12:30 | Atmosphere: 晴朗的天空，微风拂过网栏，台阶上的树荫",
        "prologue": "午休时间，大吾一个人坐在天台角落看云发呆，神情难得有些落寞。你轻手轻脚走过去在他身边坐下。",
        "dialogue_intro": [
            ("大吾", "“青梅……你说，我真的能站在最大的舞台上，成为大家都认可的演员吗？”"),
        ],
        "choices": [
            {
                "option": "静静听他倾诉对未来的不安",
                "dialogue_response": [
                    ("大吾", "『只要有你在背后支持我，不管前面的路多难，我都有勇气跑下去。』"),
                    ("大吾", "（侧过头凝视着你，眼神格外炽热而坚定）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "☁️ 突发心动：紧靠的肩膀",
                    "narrative": "一阵清风吹过，他顺势将头靠在你的肩膀上，深深吸了一口气。",
                    "dialogue": ("大吾", "“就借你的肩膀靠一小会儿……只要有你在身边，我的不安就全消失了。”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "塞给他一颗薄荷糖：『别想太多。』",
                "dialogue_response": [
                    ("大吾", "『嗯，瞬间清醒了。从小到大，你的薄荷糖总能治好我的焦虑。』"),
                    ("大吾", "（把糖果含进嘴里，露出招牌式的甜美笑容）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "开玩笑说以后要收他版权费",
                "dialogue_response": [
                    ("大吾", "『那我把自己整个人打包抵押给你，够不够付版权费呀？』"),
                    ("大吾", "（凑到你面前，笑眯眯地对你眨了眨眼）"),
                ],
                "affection": 18,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：晨光中的自行车后座",
        "scene": "Location: 上学途中的林荫大道 | Time: 07:40 | Atmosphere: 清晨新鲜的空气，穿过树叶刺破阴影的金色阳光",
        "prologue": "清晨的街道上，大吾踩着自行车顺着斜坡滑下，在你面前优雅地刹停。",
        "dialogue_intro": [
            ("大吾", "“早啊！今天天气这么好，要不要享受一下天才演员西畑大吾的专属接送服务？”"),
        ],
        "choices": [
            {
                "option": "拍拍自行车后座：『上来吧，带你去吃限定早餐。』",
                "dialogue_response": [
                    ("大吾", "『每次坐在你车后座，微风吹过来，我都觉得时间可以永远停在这。』"),
                    ("大吾", "（坐上后座，伸手轻轻环住了你的腰）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "抱怨他骑得太快抓紧他的衣角",
                "dialogue_response": [
                    ("大吾", "『抓紧咯！为了多听你叫几声，我可要加速了！』"),
                    ("大吾", "（坏笑着猛踩脚踏板，迎风欢快地冲下斜坡）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "安静地吃着手里的小面包",
                "dialogue_response": [
                    ("大吾", "『有你在身边的清晨，连空气都是甜滋滋的草莓味。』"),
                    ("大吾", "（微微偏过头看你，嘴角挂着满足的弧度）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "🚴‍♂️ 突发心动：微风中的心跳",
                    "narrative": "急刹车时你撞上了他的后背，他快速伸手稳稳抓住你的双手放在他腰间。",
                    "dialogue": ("大吾", "“抱紧我，掉下去的话我可是会心疼的哦。”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 大酱·文化祭前夜：道具房的密室心跳",
        "scene": "Location: 文化祭舞台后台道具房 | Time: 19:30 | Atmosphere: 昏暗的灯光，堆满舞台道具的狭小空间，外面的微风吹动窗帘",
        "prologue": "文化祭前夜，道具房里摆满了各种复杂的道具服装。你和大吾正在整理最后的演出用品，门却不小心被风吹上锁住了。",
        "dialogue_intro": [
            ("大吾", "“完蛋，门锁上了……看来在别人发现之前，我们得在这里呆一会儿了。”"),
        ],
        "choices": [
            {
                "option": "帮他整理乱糟糟的演出服",
                "dialogue_response": [
                    ("大吾", "『太近了……闻到你身上的味道，我连剧本台词全忘光了。』"),
                    ("大吾", "（低下头任由你收拾，眼神越来越深沉）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🎭 突发心动：密室里的幽香",
                    "narrative": "狭小的空间让气温急剧上升，他突然抓住你正在整理衣领的手，将你轻轻按在墙边。",
                    "dialogue": ("大吾", "“别动……再动的话，我可不敢保证自己还能维持‘青梅竹马’的界限了。”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "开玩笑：『大明星紧张啦？』",
                "dialogue_response": [
                    ("大吾", "『才没有！面对几万人都没怂过，面对你我才不是紧张……是心动。』"),
                    ("大吾", "（不服气地嘟囔着，脸颊却微微泛起红晕）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "递上矿泉水：『润润嗓子。』",
                "dialogue_response": [
                    ("大吾", "『谢谢你……如果今晚演出成功，我要第一个把花献给你。』"),
                    ("大吾", "（接过水喝了一口，微笑着向你许下承诺）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 大酱·星光月下：无法藏匿的目光",
        "scene": "Location: 学校后山观景台 | Time: 21:00 | Atmosphere: 皎洁的月光，远处城市的万家灯火，耳边清脆的蝉鸣",
        "prologue": "演出大获成功，后夜祭的欢呼声在远处回荡。大吾拉着你偷偷跑到了没有人的后山山顶。",
        "dialogue_intro": [
            ("大吾", "“呼……终于只有我们两个人了。其实今晚，我有个秘密一直想告诉你。”"),
        ],
        "choices": [
            {
                "option": "戳他红透的耳朵：『发烧啦？』",
                "dialogue_response": [
                    ("大吾", "『才不是发烧，是因为某人靠得太近，我的心跳彻底失控了。』"),
                    ("大吾", "（一把抓住你捣乱的手指，扣在自己的掌心里）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "假装看向夜空风景",
                "dialogue_response": [
                    ("大吾", "『别看风景了，难道我还不够好看吗？快把视线转过来嘛。』"),
                    ("大吾", "（有些吃醋地挡在你面前，强迫你的眼睛里只有他）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "温柔地回握住他的手",
                "dialogue_response": [
                    ("青梅", "『好啦，不逗你了。』"),
                    ("大吾", "『这可是你主动牵的，不许反悔哦！』"),
                    ("大吾", "（紧紧扣住你的五指，脸上露出了最灿烂的笑容）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🌙 突发心动：月色真美",
                    "narrative": "夜风吹过，他在月光下慢慢低头，温热的呼吸贴近了你的侧脸。",
                    "dialogue": ("大吾", "“今晚的月色真的很美……但我眼里，只有你。”"),
                    "bonus_affection": 10,
                },
            },
        ],
    },
    6: {
        "title": "🎬 大酱·终章告白：青梅竹马的直球反击",
        "scene": "Location: 两人从小一起玩耍的公园秋千旁 | Time: 21:30 | Atmosphere: 柔和的街灯，漫天星辰，静谧而深情的氛围",
        "prologue": "月光下，大吾站在秋千前，神情是从未有过的认真与炽热。他深深地吸了一口气，凝视着你的眼睛。",
        "dialogue_intro": [
            ("大吾", "“从小到大，我一直习惯了你在我身边。但我不想再当你的‘青梅竹马’了……我想做那个独占你的男朋友。”"),
        ],
        "choices": [
            {
                "option": "笑着承认心意：『其实我也早就喜欢你了。』",
                "dialogue_response": [
                    ("大吾", "『真的吗？！太好了……我还以为要单恋一辈子呢！从今以后，你就是我唯一的女主角！』"),
                    ("大吾", "（激动地一把把你抱起来转了个圈）"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "💖 专属结局：青梅恋人的誓言",
                    "narrative": "微风拂过公园的树梢，从小陪伴彼此长大的两个人，终于在今夜揭开了深藏多年的心意。",
                    "dialogue": ("大吾", "“未来的每一部戏、每一个舞台、每一段人生……我都只想和你一起走下去。”"),
                    "bonus_affection": 15,
                },
            },
            {
                "option": "轻声拥抱他：『以后也请多指教。』",
                "dialogue_response": [
                    ("大吾", "『遵命！我的青梅恋人，往后余生，我的剧本里全都是你。』"),
                    ("大吾", "（用力环住你的腰，将头埋在你的颈窝里）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "傲娇地哼了一声",
                "dialogue_response": [
                    ("大吾", "『哼什么哼，不管你怎么傲娇，这辈子你都别想逃出我的手掌心啦！』"),
                    ("大吾", "（宠溺地刮了刮你的鼻子，顺势牵住了你的手）"),
                ],
                "affection": 28,
                "random_event": None,
            },
        ],
    },
},
"在日留学生or打工人": {
    1: {
        "title": "🎬 大酱·异国咖啡厅：关西少年的异国巧遇",
        "scene": "Location: 涩谷街头古着咖啡馆 | Time: 16:00 | Atmosphere: 咖啡香气缭绕，窗外熙熙攘攘的东京人流，角落里的关西口音",
        "prologue": "在东京打工/求学的你，在兼职的咖啡馆里意外遇到了刚结束排练、正对着菜单发愁的关西少年大吾。",
        "dialogue_intro": [
            ("大吾", "“那个……请问这里推荐哪种咖啡？普通话太标准了我有点紧张……”"),
            ("打工人", "（笑着抬起头，用熟悉的语气招呼他）"),
        ],
        "choices": [
            {
                "option": "递给他一张打工情报纸",
                "dialogue_response": [
                    ("大吾", "『哇！救命恩人出现！在东京正愁找不到靠谱兼职呢，太感谢你了！』"),
                    ("大吾", "（如获至宝地接过去，两眼发光地认真实录）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "用关西腔调侃：『这不是大明星嘛。』",
                "dialogue_response": [
                    ("大吾", "『别笑话我啦，异国他乡讨生活不容易，听到乡音差点哭出来。』"),
                    ("大吾", "（不好意思地揉了揉鼻子，眼神里泛着亲切）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "请他喝了一杯热可可",
                "dialogue_response": [
                    ("大吾", "『甜到心坎里了！今天在东京的所有疲惫被你一杯热可可全治愈了。』"),
                    ("大吾", "（捧着马克杯喝了一大口，露出无比满足的笑容）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "☕ 突发心动：暖暖的甜意",
                    "narrative": "他沾了一嘴白色的奶泡，有些憨态可掬地凑近你，眼睛亮晶晶的。",
                    "dialogue": ("大吾", "“在异国他乡能遇到你，绝对是我这段时间最幸运的事，没有之一！”"),
                    "bonus_affection": 5,
                },
            },
        ],
    },
    2: {
        "title": "🎬 大酱·深夜列车：异国他乡的守候",
        "scene": "Location: JR山手线末班电车 | Time: 23:45 | Atmosphere: 车厢空旷寂静，微弱的广播声，窗外飞逝的东京霓虹夜景",
        "prologue": "结束了一天高强度的兼职/学业，你踏上深夜列车，意外发现大吾也坐在车厢角落，面露疲态却依然眼神清亮。",
        "dialogue_intro": [
            ("大吾", "“这么晚才下班吗？辛苦啦……快坐到我旁边来。”"),
        ],
        "choices": [
            {
                "option": "靠在车窗边听他讲梦想",
                "dialogue_response": [
                    ("大吾", "『不管以后能不能回国出道，只要在东京能天天见到你，我就觉得超满足。』"),
                    ("大吾", "（侧过脸看着窗外倒影中的你，嘴角微微上扬）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "🚃 突发心动：微醺的依偎",
                    "narrative": "列车猛地一晃，他下意识地伸手揽住你的肩膀，将你稳稳护在怀里。",
                    "dialogue": ("大吾", "“小心！抱歉啊……不过这个距离，我可以稍微贪心一小会儿吗？”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "分给他半块三明治",
                "dialogue_response": [
                    ("大吾", "『深夜加班有你投喂，感觉自己像个被全世界宠爱的小孩。』"),
                    ("大吾", "（开心地点点头，小口小口地品尝着）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "提醒他终点站快到了",
                "dialogue_response": [
                    ("大吾", "『哎呀，真希望这条列车永远没有终点，这样就能和你多待一会儿。』"),
                    ("大吾", "（轻声叹了口气，眼神里写满了不舍）"),
                ],
                "affection": 18,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：银座街头的晴空漫步",
        "scene": "Location: 银座步行者天国 | Time: 13:00 | Atmosphere: 阳光明媚，微风正好，热闹非凡的异国街头",
        "prologue": "难得的休息日，大吾约你出来散心。穿梭在繁华的街头，漂泊异乡的孤单似乎被阳光一扫而空。",
        "dialogue_intro": [
            ("大吾", "“今天天气这么好，一定要把异国他乡的烦恼统统抛在脑后才行！”"),
        ],
        "choices": [
            {
                "option": "帮他拍一张元气满满的照片",
                "dialogue_response": [
                    ("大吾", "『把我拍帅一点！这张照片我要当作一辈子的护身符。』"),
                    ("大吾", "（对着镜头比了个俏皮的比心手势）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "顺路买了两份铜锣烧分食",
                "dialogue_response": [
                    ("大吾", "『东京的甜品虽然好吃，但感觉还是跟你一起吃的最对味。』"),
                    ("大吾", "（分了大半块馅料满满的铜锣烧给你）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "提醒他注意看红绿灯",
                "dialogue_response": [
                    ("大吾", "『遵命！只要牵着你的手，就算东京的十字路口再大我也不会迷路。』"),
                    ("大吾", "（理直气壮地伸手拉住了你的手套）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "🚦 突发心动：斑马线的过界",
                    "narrative": "绿灯倒计时闪烁，他握紧你的手带着你在人潮中小跑过马路，掌心炽热。",
                    "dialogue": ("大吾", "“看吧，只要两个人在一起，多复杂的路口都能顺利通过！”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 大酱·暴雨危机：异国屋檐下的紧靠",
        "scene": "Location: 便利店外的避雨屋檐下 | Time: 18:30 | Atmosphere: 突如其来的滂沱大雨，雨滴砸在伞面上的噼啪声，寒冷空气中交织的呼吸",
        "prologue": "突然袭来的暴雨将你们困在便利店门口，冰冷的雨水倾泻，两人的距离被狭小的屋檐无限拉近。",
        "dialogue_intro": [
            ("大吾", "“哇！这场雨也太大了……还好有你在身边，不然我可要冻僵在东京街头了。”"),
        ],
        "choices": [
            {
                "option": "把唯一的围巾分他一半",
                "dialogue_response": [
                    ("大吾", "『好暖……不仅是围巾，连我的心都被你塞得满满当当的了。』"),
                    ("大吾", "（主动凑近你，把围巾往你的方向又系紧了一点）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🌧️ 突发心动：围巾里的体温",
                    "narrative": "两个人共用一条围巾，彼此鼻息相闻，他微微低头就能碰到你的额头。",
                    "dialogue": ("大吾", "“这算不算异国他乡里，只有我们两个人的秘密温室？”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "开玩笑说像电视剧里的场景",
                "dialogue_response": [
                    ("大吾", "『那我们就是这部剧里最幸福的主角，不接受任何悲剧结尾哦！』"),
                    ("大吾", "（对你眨眨眼，笑得阳光灿烂）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "安静地看着雨打芭蕉",
                "dialogue_response": [
                    ("大吾", "『有你在身边挡风雨，哪怕东京下整个月的暴雨我也不怕。』"),
                    ("大吾", "（侧头看着你的侧影，眼神温柔得能溢出水来）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 大酱·归国抉择：东京塔下的不舍诀别",
        "scene": "Location: 芝公园东京塔下 | Time: 20:00 | Atmosphere: 橘红色的塔灯耀眼夺目，夜风吹拂着两人的发丝，空气中弥漫着离别的伤感",
        "prologue": "归期临近，大吾即将回国开启全新的偶像事业，而你们站在耀眼的东京塔下，面对未知的未来。",
        "dialogue_intro": [
            ("大吾", "“快要回去了呢……在东京这段最艰难的日子里，因为有你，我才坚持了下来。”"),
        ],
        "choices": [
            {
                "option": "鼓励他勇敢回国追逐梦想",
                "dialogue_response": [
                    ("大吾", "『不管我飞得多高，我的心永远留在这个东京的傍晚，留给你。』"),
                    ("大吾", "（眼中闪烁着坚定与不舍的光芒）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "默默红了眼眶不说话",
                "dialogue_response": [
                    ("大吾", "『不许哭！你一哭我的心都要碎了……等我成功，一定会来接你！』"),
                    ("大吾", "（心疼地伸手抹去你眼角的湿意）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "紧紧拥抱住他",
                "dialogue_response": [
                    ("打工人", "『嗯，我等你，一言为定！』"),
                    ("大吾", "（把你紧紧贴在他的胸口，听着他失控的心跳）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🗼 突发心动：地标下的誓言",
                    "narrative": "东京塔的灯光瞬间闪烁变幻，他在璀璨的灯影里在你耳边立下承诺。",
                    "dialogue": ("大吾", "“这塔灯作证，无论相隔多远，西畑大吾的心永远属于你。”"),
                    "bonus_affection": 10,
                },
            },
        ],
    },
    6: {
        "title": "🎬 大酱·异国完结篇：跨越山海的爱意",
        "scene": "Location: 机场接机大厅 | Time: 15:00 | Atmosphere: 阳光明媚，人潮涌动，跨越时空与距离重逢的温情",
        "prologue": "经过了遥远的思念与时间的洗礼，跨越山海的羁绊终于迎来了最璀璨的答案。",
        "dialogue_intro": [
            ("大吾", "“好久不见！距离再远，也剪不断我奔向你的脚步。”"),
        ],
        "choices": [
            {
                "option": "笑着收下他的越洋长信",
                "dialogue_response": [
                    ("大吾", "『信里的每一个字都是我对你的心意。跨越山海，我的爱意永远直奔你而来。』"),
                    ("大吾", "（双手将沉甸甸的信笺递到你手上）"),
                ],
                "affection": 35,
                "random_event": None,
            },
            {
                "option": "视频通话里隔空对视",
                "dialogue_response": [
                    ("大吾", "『屏幕再远也隔不住我对你的思念，下次见面，我要当面把情话补齐。』"),
                    ("大吾", "（对着镜头露出灿烂又深情的笑容）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "坚定地告诉他：『我去找你。』",
                "dialogue_response": [
                    ("大吾", "『真的吗？！那我马上在机场铺满鲜花，随时恭迎我的唯一定制恋人！』"),
                    ("大吾", "（惊喜地抱住你，在你发间落下一个极其温柔的吻）"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "✈️ 专属结局：跨越山海的唯一定制",
                    "narrative": "接机大厅里熙熙攘攘，他当着所有人的面紧紧牵起你的手，不再有任何顾虑。",
                    "dialogue": ("大吾", "“谢谢你跨越山海来到我身边。从今往后，不管在哪里，只要有你在，那就是我的归宿。”"),
                    "bonus_affection": 15,
                },
            },
        ],
    },
},
"大桥": {
    "经纪人": {
        1: {
            "title": "🎬 大桥·后台初见：充满治愈笑容的队长",
            "scene": "Location: 电视台演唱会后台休息室 | Time: 14:30 | Atmosphere: 柔和的休息室灯光，散落的服装架，甜甜的焦糖香气",
            "prologue": "刚结束高强度的舞蹈彩排，大桥坐在沙发起伏着肩膀喘气，看到你走进来，立刻绽放出像阳光一样治愈的微笑。",
            "dialogue_intro": [
                ("大桥", "“哇！你忙完啦？快坐快坐，刚才的彩排我有超认真跳哦！”"),
                ("经纪人", "（看着他亮晶晶的眼睛，笑着递过去手中的东西）"),
            ],
            "choices": [
                {
                    "option": "递上他最爱的布丁：『辛苦啦，甜品时间！』",
                    "dialogue_response": [
                        ("大桥", "『哇！是布丁诶！你太懂我了吧！感觉吃一口整个人都复活了～』"),
                        ("大桥", "（幸福地眯起眼睛，舀起一大勺布丁塞进嘴里）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🍮 突发心动：甜心的分享",
                        "narrative": "他挖了一大勺最嫩的布丁，小心翼翼地递到你嘴边，眼睛笑得像弯弯的月牙。",
                        "dialogue": ("布丁", "“第一口一定要分给你！这可是充满了队长爱意的特别奖励哦～”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "提醒他注意团队行程安排",
                    "dialogue_response": [
                        ("大桥", "『遵命！有贴心的经纪人大人监督，身为队长我绝对不会偷懒的！』"),
                        ("大桥", "（立正敬了个俏皮的礼，满脸元气）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "笑话他脸颊上的饭粒",
                    "dialogue_response": [
                        ("大桥", "『诶？！在哪里在哪里？好啦别笑话我了，快帮我擦掉嘛～』"),
                        ("大桥", "（凑近脸颊微微嘟嘴，眼神里带着一丝撒娇）"),
                    ],
                    "affection": 18,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 大桥·深夜排练：元气背后的温柔体贴",
            "scene": "Location: 练习室 | Time: 23:00 | Atmosphere: 镜子映射出温热的水汽，动感音乐渐息，空旷练习室里的呼吸声",
            "prologue": "深夜的练习室里只剩下布丁一个人在一遍遍重复动作，汗水湿透了他的发梢，但他眼里依然闪烁着执着。",
            "dialogue_intro": [
                ("大桥", "“呼……呼……再练一次就好，一定要把最完美的一面展现出来才可以！”"),
            ],
            "choices": [
                {
                    "option": "看他练舞汗流浃背，递上毛巾",
                    "dialogue_response": [
                        ("大桥", "『谢谢你……每次累的时候，只要看到你温柔的眼神，我就有用不完的力气。』"),
                        ("大桥", "（接过毛巾擦了擦汗，顺势握住了你的手）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "💦 突发心动：汗水与体温",
                        "narrative": "他轻轻把你拉到镜子前，从身后环住你，把头靠在你的肩膀上吸气。",
                        "dialogue": ("大桥", "“让我靠一小会儿就好……有你在身边，我觉得自己是世界上最幸运的队长。”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "笑他像个停不下来的小陀螺",
                    "dialogue_response": [
                        ("大桥", "『因为想把最完美的舞台带给大家呀，不过……最想讨好的人其实是你啦。』"),
                        ("大桥", "（对你眨眨眼，吐了吐舌头）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "劝他早点收工回后台休息",
                    "dialogue_response": [
                        ("大桥", "『好～听你的，大队长发话了，今晚的练习提前结束，陪你聊天去！』"),
                        ("大桥", "（一秒关掉音响，蹦蹦跳跳地跑到你身边）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：阳光灿烂的彩排日",
            "scene": "Location: 主舞台侧幕 | Time: 10:00 | Atmosphere: 舞台聚光灯交织，耀眼的光芒，充满朝气的彩排现场",
            "prologue": "上午的正式彩排开始，布丁站在舞台中央散发着耀眼的光彩，趁着音响调试的空档，他频频看向侧幕的你。",
            "dialogue_intro": [
                ("大桥", "“经纪人！这个站在舞台中央的队长，今天有没有稍微帅到你一点点？”"),
            ],
            "choices": [
                {
                    "option": "帮他调整麦克风高度",
                    "dialogue_response": [
                        ("大桥", "『这么照顾我，以后把我宠坏了可要负责到底哦！』"),
                        ("大桥", "（乖乖低头让你帮忙，嘴角弧度怎么也藏不住）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "递上温开水润喉",
                    "dialogue_response": [
                        ("大桥", "『谢谢你……连水都是甜的，今天演唱会的音高我一定能完美拿捏！』"),
                        ("大桥", "（捧着水杯咕噜咕噜喝完，对你露出生机勃勃的笑容）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "坐在台下做他的第一观众",
                    "dialogue_response": [
                        ("大桥", "『看到你在台下坐着，我的目光就忍不住一直跟着你跑。』"),
                        ("大桥", "（对着台下的方向做了一个比心动作，引得工作人员一阵打趣）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🎤 突发心动：台上侧目",
                        "narrative": "音乐响起的瞬间，他在聚光灯下转身，眼神穿越人群直直锁定在你身上。",
                        "dialogue": ("布丁", "“所有闪耀的瞬间，我只想第一个分享给你。”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 大桥·休息室密语：天然呆的直球攻击",
            "scene": "Location: 独属休息室 | Time: 17:00 | Atmosphere: 暖黄色的落日余晖洒进窗台，安静舒适的隐密空间",
            "prologue": "活动间隙，休息室里只剩下你们两人。布丁趴在桌子上，像一只晒太阳的大猫一样眨巴着眼睛看着你。",
            "dialogue_intro": [
                ("大桥", "“好安静呀……平时习惯了热闹，突然只有我们两个人，感觉心跳声都变得变好明显呢。”"),
            ],
            "choices": [
                {
                    "option": "戳戳他软乎乎的脸颊",
                    "dialogue_response": [
                        ("大桥", "『手感好吧？只准你一个人捏哦，别人我可不答应。』"),
                        ("大桥", "（顺势蹭了蹭你的手指，眼底满满都是依赖）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🌸 突发心动：指尖的触感",
                        "narrative": "他突然抓住你的手不放，慢慢把你的掌心贴在他微微发烫的脸颊上。",
                        "dialogue": ("大桥", "“看吧，因为你摸了我，我的脸立刻就烫起来了……”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "问他今天的表演感想",
                    "dialogue_response": [
                        ("大桥", "『表演很顺利，但最开心的不是拿第一，而是休息室里只有我和你。』"),
                        ("大桥", "（支着下巴看着你，眼神炽热得让人害羞）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "吐槽他刚才跳错了一个拍子",
                    "dialogue_response": [
                        ("大桥", "『呜哇别揭穿我！为了补偿我，今晚你要请我吃双份布丁！』"),
                        ("大桥", "（鼓起腮帮子，假装生气地哼哼）"),
                    ],
                    "affection": 18,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 大桥·突发危机：演唱会后台的停电小插曲",
            "scene": "Location: 通往主舞台的走廊 | Time: 19:15 | Atmosphere: 瞬间沉入漆黑的走廊，远方观众的尖叫声，心跳与呼吸交织",
            "prologue": "临上场前5分钟，后台突然遭遇意外停电，四周一片漆黑。慌乱中，有人不小心撞了你一下，身旁立刻伸出一只手臂将你稳稳拉入怀中。",
            "dialogue_intro": [
                ("大桥", "“别动！抓住我！呼……还好，你没有摔倒吧？”"),
            ],
            "choices": [
                {
                    "option": "在黑暗中握住他的手：『别怕，我在这。』",
                    "dialogue_response": [
                        ("布丁", "『好温暖……其实我不怕黑，但我好庆幸黑的时候你在我手边。』"),
                        ("布丁", "（十指相扣，握得紧紧的，片刻都不舍得松开）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🕯️ 突发心动：黑暗中的拥抱",
                        "narrative": "在伸手不见五指的黑暗里，他俯下身轻轻贴了贴你的额头。",
                        "dialogue": ("大桥", "“虽然看不到你的眼睛，但我能清晰听到你为我心跳的声音。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "用手机闪光灯帮他照明",
                    "dialogue_response": [
                        ("大桥", "『哇，你的光芒比灯泡还耀眼，照得我心里暖洋洋的。』"),
                        ("大桥", "（顺着光线看你，嘴角挂着温柔的笑意）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "冷静安抚慌乱的工作人员",
                    "dialogue_response": [
                        ("大桥", "『不愧是我的专属经纪人，临危不乱的样子简直帅呆了，爱了爱了！』"),
                        ("大桥", "（在你身后默默为你竖起大拇指）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 大桥·完美收官：专属队长的甜心告白",
            "scene": "Location: 演出结束后的庆功宴天台 | Time: 22:30 | Atmosphere: 繁星点点的夜空，微凉的晚风，远处的城市灯火与甜美的气氛",
            "prologue": "巡演完美落幕，庆功宴进行到一半，布丁偷偷把你带到了安静的天台上。他身上散发着淡淡的香气，眼神比今晚的星空还要闪耀。",
            "dialogue_intro": [
                ("大桥", "“作为队长，我已经把最棒的舞台献给了大家……但作为布丁，我最珍贵的心意，只想留给我的经纪人大人。”"),
            ],
            "choices": [
                {
                    "option": "微笑着送上祝贺花束",
                    "dialogue_response": [
                        ("大桥", "『谢谢你的花！不过比起花，我更想要你的专属一辈子契约！』"),
                        ("大桥", "（接过花束，却一把将你连同花朵一起拥入怀中）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "假装没听清他的甜言蜜语",
                    "dialogue_response": [
                        ("大桥", "『不准装聋！我都说得这么明显了，快做我的队长夫人/先生！』"),
                        ("大桥", "（气鼓鼓地凑近你，脸颊泛着可爱的绯红）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "轻轻靠 me 在他肩膀上",
                    "dialogue_response": [
                        ("经纪人", "『嗯，以后你的每个舞台，我都是唯一的VIP观众。』"),
                        ("大桥", "（温柔地揽住你，低头在你发间印下一个无比深情的吻）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,  # 终局100%触发事件
                        "event_title": "💖 专属结局：甜心队长的永远契约",
                        "narrative": "夜风拂过天台，他拉着你的手套上微小的戒指，在万家灯火的见证下许下一生守护的誓言。",
                        "dialogue": ("布丁", "“从今天起，我不只是舞台上的队长安利，更是你一辈子甜度超标的专属甜心！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"青梅竹马": {
    1: {
        "title": "🎬 大桥·放学路：零食分享的大男孩",
        "scene": "Location: 樱花飘落的放学小道 | Time: 16:30 | Atmosphere: 夕阳将两人的影子拉得很长，微风吹拂着校服裙摆，空气中散发着便当与甜点香气",
        "prologue": "放学铃声响起，布丁像往常一样抱住书包小跑跟在你身边，手里还拎着刚买好的便当，元气满满地跟你分享今天学校的趣事。",
        "dialogue_intro": [
            ("大桥", "“嘿嘿，今天阿姨给我准备了超丰富的便当哦！要不要分你一口？”"),
            ("青梅竹马", "（看着他毫无防备的笑容，你打趣地伸出了手）"),
        ],
        "choices": [
            {
                "option": "抢走他手里的一半便当",
                "dialogue_response": [
                    ("大桥", "『诶！那是我妈特意做的炸鸡块！不过……看在你份上，分你吃最大的一块！』"),
                    ("大桥", "（嘴上嚷嚷着，却极其顺手地把最香的那块夹到你嘴边）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "笑他走路总是毛毛躁躁的",
                "dialogue_response": [
                    ("大桥", "『才没有毛躁！我是在用最元气的步伐迎接放学后的二人时光嘛。』"),
                    ("大桥", "（理直气壮地挺起胸膛，小跑着在你面前转了个圈）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "递上一瓶冰麦茶",
                "dialogue_response": [
                    ("大桥", "『哇太救命了！青梅大人永远这么体贴，以身相许行不行呀？』"),
                    ("大桥", "（咕噜咕噜喝了大半瓶，擦擦嘴对你眨了眨眼）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🧃 突发心动：麦茶的甜意",
                    "narrative": "他喝得太急，一滴茶水顺着下巴滑落，他有些好笑地凑近你，眼底全是指向你的笑意。",
                    "dialogue": ("大桥", "“从小到大你都这么照顾我，以后我要是不赖着你一辈子，岂不是很亏？”"),
                    "bonus_affection": 5,
                },
            },
        ],
    },
    2: {
        "title": "🎬 大桥·旧琴房：钢琴声里的秘密心事",
        "scene": "Location: 学校旧教学楼琴房 | Time: 17:30 | Atmosphere: 橘黄色的斜阳洒在黑白琴键上，空气里泛着旧木头的香气，悠扬的琴声环绕",
        "prologue": "放学后的旧琴房鲜少有人来，布丁坐在钢琴前轻快地按动琴键，见你推门进来，眼神瞬间亮了起来。",
        "dialogue_intro": [
            ("大桥", "“你来啦！快坐过来，我刚写好了一段新的旋律，第一听众必须是你！”"),
        ],
        "choices": [
            {
                "option": "听他弹奏写给你的专属旋律",
                "dialogue_response": [
                    ("大桥", "『这首曲子只弹给你一个人听哦，好听吗？里面全是我藏不住的喜欢。』"),
                    ("大桥", "（指尖在琴键上飞跃，侧过脸对你露出极其温柔的笑容）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "🎹 突发心动：琴键上的合奏",
                    "narrative": "他拉过你的手放在高音区，引导着你的手指和他一起按下一个和谐的音符。",
                    "dialogue": ("布丁", "“你看，就像我们两个一样，合在一起才是最完美的乐章。”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "拍手称赞：『技术有进步嘛！』",
                "dialogue_response": [
                    ("大桥", "『那是，为了配得上你，我可是偷偷练习了成百上千遍呢。』"),
                    ("大桥", "（骄傲地抬起下巴，尾巴仿佛都要摇到天上去了）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "靠在琴键旁闭目聆听",
                "dialogue_response": [
                    ("大桥", "『看着你安静听琴的样子，我突然有了写一辈子情歌的灵感。』"),
                    ("大桥", "（放慢了弹奏的节奏，音符变得无比深情温柔）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：晨读课的偷偷传纸条",
        "scene": "Location: 高二（3）班教室角落 | Time: 07:50 | Atmosphere: 朗朗的读书声，穿堂而过的晨风，课桌下悄悄传递的小秘密",
        "prologue": "早自习的读书声此起彼伏，坐在你隔壁桌的布丁偷偷摸摸用手肘碰了碰你，趁老师不注意从桌底递过来一张叠成心形的纸条。",
        "dialogue_intro": [
            ("大桥", "“（小声咳嗽）咳……快打开看看，不许让老师发现哦！”"),
        ],
        "choices": [
            {
                "option": "打开纸条看上面的幼稚画作",
                "dialogue_response": [
                    ("大桥", "『画得是我吧？虽然丑了点，但代表我的心永远围着你转！』"),
                    ("大桥", "（见你打开纸条，对你做了一个滑稽的鬼脸）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "假装生气把纸条揉掉",
                "dialogue_response": [
                    ("大桥", "『别扔别扔！那可是我精雕细琢的爱的告白证明诶！』"),
                    ("大桥", "（急得差点在课上叫出来，委屈巴巴地用双手比心）"),
                ],
                "affection": 18,
                "random_event": None,
            },
            {
                "option": "回写一张字条塞过去",
                "dialogue_response": [
                    ("大桥", "『收到回信了！耶！今天一整天都要变成开心的布丁色啦！』"),
                    ("大桥", "（收到回信如获至宝，藏在课本后面笑得合不拢嘴）"),
                ],
                "affection": 22,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "📝 突发心动：桌底的勾指",
                    "narrative": "递还纸条时，他在课桌的掩护下悄悄勾住了你的小拇指，轻轻晃了晃。",
                    "dialogue": ("布丁", "“拉钩拉钩，今天放学后也必须和我一起回家！”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 大桥·祭典小吃街：棉花糖与心跳并存",
        "scene": "Location: 夏日祭典神社参道 | Time: 19:30 | Atmosphere: 挂满红灯笼的街道，熙熙攘攘的人群，远处的太鼓声与烤串的焦香",
        "prologue": "换上浴衣的你们穿梭在热闹的夏日祭典里，布丁手里拿着满满当当的小吃，眼睛里泛着比灯火还要耀眼的光彩。",
        "dialogue_intro": [
            ("大桥", "“哇！快看那个！祭典真的太好玩了！来，尝尝这个刚烤好的章鱼小丸子～”"),
        ],
        "choices": [
            {
                "option": "分他一口苹果糖",
                "dialogue_response": [
                    ("大桥", "『好甜……不过没有你的笑容甜，今天能和你一起逛祭典太幸福了。』"),
                    ("大桥", "（张嘴咬了一小口，眼睛笑得弯成了月牙）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🍎 突发心动：嘴角擦过的甜度",
                    "narrative": "你的嘴角沾上了一点糖衣，他下意识地伸手帮你不轻不重地擦掉，随后把手指放进嘴里。",
                    "dialogue": ("布丁", "“嘿嘿，真的超甜！不管是糖还是你……”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "帮他捞金鱼结果全军覆没",
                "dialogue_response": [
                    ("大桥", "『没关系没关系，捞不到金鱼没所谓，反正我最大的网已经把你捞进心里了。』"),
                    ("大桥", "（拍拍破掉的纸网，完全不在意，反而笑得格外开心）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "吐槽他套圈圈一个没中",
                "dialogue_response": [
                    ("大桥", "『失误失误！看我的，这次绝对把那个最大的公仔赢下来送你！』"),
                    ("大桥", "（不服输地卷起袖子，认认真真瞄准目标）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 大桥·烟花大会：人群中的深情凝视",
        "scene": "Location: 河堤草坪 | Time: 20:30 | Atmosphere: 夜空中绽放的万道彩光，轰鸣的烟花声，微风拂过的河畔夜色",
        "prologue": "巨大的烟花在夜空中轰然炸开，绚丽的光芒照亮了整座城市，周围的人群发出阵阵欢呼，而布丁却渐渐停止了呐喊，侧过身看向你。",
        "dialogue_intro": [
            ("大桥", "“（烟花轰鸣声）……你说什么？烟花太响啦，我听不清！但我想告诉你——”"),
        ],
        "choices": [
            {
                "option": "抬头看绚烂夺目的烟花",
                "dialogue_response": [
                    ("大桥", "『烟花很美，但我的视线一刻也没从你脸上移开过。』"),
                    ("大桥", "（在漫天烟火下，眼神无比专注地凝视着你的侧脸）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "被烟花声吓了一跳躲进他怀里",
                "dialogue_response": [
                    ("大桥", "『别怕别怕，我在呢。烟花会消散，但我对你的喜欢永远热烈。』"),
                    ("大桥", "（顺势将你紧紧环在怀里，帮你挡住周围的人潮）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🎆 突发心动：烟火下的拥抱",
                    "narrative": "在最璀璨的一发巨型烟花升空时，他在你耳边压低了声音，呼吸带着滚烫的温度。",
                    "dialogue": ("布丁", "“我喜欢你！不是青梅竹马的那种喜欢，是想和你谈一辈子恋爱的喜欢！”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "顺势握住他的手掌",
                "dialogue_response": [
                    ("大桥", "『哇，你的手好暖和……以后每年烟花大会都要一起看。』"),
                    ("大桥", "（反手与你十指相扣，握得紧紧的生怕把你弄丢）"),
                ],
                "affection": 28,
                "random_event": None,
            },
        ],
    },
    6: {
        "title": "🎬 大桥·告白终章：从青梅到一辈子的约定",
        "scene": "Location: 陪伴你们长大的公园秋千前 | Time: 21:30 | Atmosphere: 柔和的街灯，皎洁的月光，从小陪伴到大的熟悉怀抱与满溢的心动",
        "prologue": "烟花散尽，你们走在回家的旧路上。停在小时候常玩的秋千旁，布丁转过身，平日里大大咧咧的他此刻眼神里充满了少见的认真与虔诚。",
        "dialogue_intro": [
            ("布丁", "“从小到大，我的过去全部都有你……那么未来的几十年，你愿意继续留在我的生命里，做我的女朋友吗？”"),
        ],
        "choices": [
            {
                "option": "笑着用双手捧住他的脸：『好啦，答应你了。』",
                "dialogue_response": [
                    ("大桥", "『耶！太棒啦！从今天起，我不只是你的青梅竹马，更是你的专属男友！』"),
                    ("大桥", "（开心地将你抱起来转了个圈，脸上洋溢着世界上最灿烂的笑容）"),
                ],
                "affection": 35,
                "random_event": None,
            },
            {
                "option": "感动得眼眶微微发热",
                "dialogue_response": [
                    ("大桥", "『不哭不哭，以后有我宠着你，每一天都只会让你笑，绝对不让你掉眼泪。』"),
                    ("大桥", "（温柔地帮你拭去眼角的泪花，将你轻轻拥入怀中）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "十指紧扣奔向未来",
                "dialogue_response": [
                    ("青梅竹马", "『走咯！向着我们的幸福未来，全速前进！』"),
                    ("大桥", "（牵着你的手在月光下向前奔跑，脚下的每一步都踩在幸福的节奏上）"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "💍 专属结局：竹马的终身契约",
                    "narrative": "月光将两人的影子重叠在一起，他在你额头上轻轻印下一个带有布丁般甜美的吻。",
                    "dialogue": ("布丁", "“从青梅竹马到白头偕老，你这辈子都休想甩开我啦！”"),
                    "bonus_affection": 15,
                },
            },
        ],
    },
},
"在日留学生or打工人": {
    1: {
        "title": "🎬 大桥·异国面包房：元气满满的异国偶遇",
        "scene": "Location: 涩谷街头古着面包店 | Time: 16:00 | Atmosphere: 烤面包的浓郁焦香，窗外熙熙攘攘的东京人流，异国他乡的熟悉温情",
        "prologue": "在东京兼职/求学的你，在排队买面包时意外遇到了刚结束排练、正对着橱柜里最后一个限定面包发愁的布丁。",
        "dialogue_intro": [
            ("布丁", "“那个……请问你也要买这个吗？呜，感觉好饿，但如果你想要的话我就让给你吧……”"),
            ("在日学生or打工人", "（看着他眼巴巴的样子，笑着做出了决定）"),
        ],
        "choices": [
            {
                "option": "买下最后一个限定哈密瓜面包分他一半",
                "dialogue_response": [
                    ("大桥", "『天呐！你简直是我的救世主！在东京打工正饿得头昏眼花呢，太感动了！』"),
                    ("大桥", "（捧着半块面包眼睛发亮，像个得到宝藏的小孩）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.35,
                    "event_title": "🍞 突发心动：面包房的甜意",
                    "narrative": "他迫不及待地咬了一大口，嘴角沾了一点面粉，有些憨态可掬地凑近你。",
                    "dialogue": ("布丁", "“在异国他乡能遇到这么温柔的你，今天绝对是我这段时间最幸运的一天！”"),
                    "bonus_affection": 5,
                },
            },
            {
                "option": "用关西腔和日语夹杂打招呼",
                "dialogue_response": [
                    ("大桥", "『哈哈，你的日语口音好可爱！在这异国他乡听到熟悉的声音太亲切啦。』"),
                    ("大桥", "（不好意思地揉了揉鼻子，眼神里泛着满满的亲切感）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "帮他扶住差点倒掉的面包架",
                "dialogue_response": [
                    ("大桥", "『多亏有你眼疾手快，不然店长又要念叨我了，谢谢你天使！』"),
                    ("大桥", "（拍了拍胸口松了一口气，对你露出极为灿烂的笑容）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    2: {
        "title": "🎬 大桥·深夜便当店：打工人的互相治愈",
        "scene": "Location: 24小时深夜便当店 | Time: 23:45 | Atmosphere: 暖黄色的灯光，蒸汽弥漫的关东煮机，窗外寂静的东京夜色",
        "prologue": "结束了一天高强度的打工与学业，你踏入便当店，意外发现布丁也坐在角落的桌边，虽然面露疲态却依然眼神清亮。",
        "dialogue_intro": [
            ("大桥", "“这么晚才下班吗？辛苦啦……快坐过来，这里还有刚出锅的热气呢！”"),
        ],
        "choices": [
            {
                "option": "听他讲兼职时的各种趣事",
                "dialogue_response": [
                    ("大桥", "『虽然东京生活很辛苦，但只要下班能遇见你，所有的疲惫都烟消云散了。』"),
                    ("大桥", "（侧过脸看着窗外倒影中的你，嘴角微微上扬）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.4,
                    "event_title": "🏪 突发心动：深夜的依偎",
                    "narrative": "他讲着讲着有些困倦，头不自觉地轻轻靠在了你的肩膀上，呼吸渐渐变得平稳。",
                    "dialogue": ("布丁", "“借我靠一小会儿好不好……有你在身边，感觉连做梦都是甜的。”"),
                    "bonus_affection": 8,
                },
            },
            {
                "option": "把热腾腾的关东煮推给他",
                "dialogue_response": [
                    ("大桥", "『你也吃！我们一人一半，把冬天的寒冷全部吃掉！』"),
                    ("大桥", "（开心地点点头，把汤碗往你那边推了推）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "笑他打工时笨手笨脚的样子",
                "dialogue_response": [
                    ("大桥", "『好啦，人家那是大智若愚！不过为了在你面前表现帅气，明天开始我会加油的。』"),
                    ("大桥", "（鼓起腮帮子，装作生气的样子惹你开心）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    3: {
        "title": "☀️ 第二天：樱花树下的便当之约",
        "scene": "Location: 新宿御苑樱花树下 | Time: 13:00 | Atmosphere: 粉白色的花瓣随风飘落，明媚的春日阳光，草地上的惬意午后",
        "prologue": "难得的休息日，布丁约你出来散心。漂泊异乡的孤单与压抑，在满天落樱和阳光下被一扫而空。",
        "dialogue_intro": [
            ("大桥", "“今天天气这么好，一定要把异国他乡的烦恼统统抛在脑后才行！”"),
        ],
        "choices": [
            {
                "option": "帮他拂去肩膀上的落花",
                "dialogue_response": [
                    ("大桥", "『落花随风去，但我对你的心意就像这落英一样，永远扎根在泥土里。』"),
                    ("大桥", "（任由你的手指碰触他的肩膀，眼神无比专注温柔）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "分享亲手做的饭团",
                "dialogue_response": [
                    ("大桥", "『太好吃了！这是什么人间美味，幸福感简直爆棚！』"),
                    ("大桥", "（两口吞下一个饭团，满足地眯起了眼睛）"),
                ],
                "affection": 22,
                "random_event": None,
            },
            {
                "option": "靠着树干一起看天空发呆",
                "dialogue_response": [
                    ("大桥", "『在东京能遇到你，是我这辈子觉得最幸运的奇迹。』"),
                    ("大桥", "（悄悄伸手拉住了你的手套，掌心传过来阵阵热度）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.3,
                    "event_title": "🌸 突发心动：落樱下的侧脸",
                    "narrative": "风吹过树梢，一片花瓣落在你的发顶，他凑过来轻轻为你摘下，距离近得能听到心跳。",
                    "dialogue": ("大桥", "“不要动哦……现在的你，比这满树的樱花还要漂亮。”"),
                    "bonus_affection": 7,
                },
            },
        ],
    },
    4: {
        "title": "🎬 大桥·异国暴雨：车站前的暖心伞篷",
        "scene": "Location: 车站出口的避雨屋檐下 | Time: 18:30 | Atmosphere: 倾盆而下的雷阵雨，噼啪的雨声，狭小雨伞下的紧密贴合",
        "prologue": "突然袭来的暴雨将你们困在车站门口，冰冷的雨水倾泻，一把小小的雨伞将你们的距离拉得极近。",
        "dialogue_intro": [
            ("大桥", "“哇！这场雨也太大了……还好有你在身边，不然我可要冻僵在东京街头了。”"),
        ],
        "choices": [
            {
                "option": "主动把伞往他那边倾斜",
                "dialogue_response": [
                    ("大桥", "『你全遮过去啦！你自己肩膀都湿了……快过来，别着凉，我抱紧你就不冷了。』"),
                    ("大桥", "（一把搂住你的肩膀，把你往自己怀里贴了贴）"),
                ],
                "affection": 25,
                "random_event": {
                    "trigger_rate": 0.45,
                    "event_title": "🌧️ 突发心动：伞下的体温",
                    "narrative": "两个人共用一把小伞，雨水打湿了他的外套，但他环在你肩头的手却无比坚定炽热。",
                    "dialogue": ("布丁", "“这算不算异国他乡里，只有我们两个人的秘密温室？”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "买了两杯热可可暖手",
                "dialogue_response": [
                    ("大桥", "『谢谢你的热可可，东京的雨夜突然变得像童话一样浪漫。』"),
                    ("大桥", "（捧着可可对你眨眨眼，笑得阳光灿烂）"),
                ],
                "affection": 20,
                "random_event": None,
            },
            {
                "option": "开玩笑说要一起私奔回大阪",
                "dialogue_response": [
                    ("大桥", "『好啊好啊！现在就买机票，目的地——我们的幸福老家！』"),
                    ("大桥", "（兴奋地牵起你的手做跃跃欲试状，嘴角弧度极高）"),
                ],
                "affection": 22,
                "random_event": None,
            },
        ],
    },
    5: {
        "title": "🎬 大桥·东京塔下：归国前夕的依依不舍",
        "scene": "Location: 芝公园东京塔下 | Time: 20:00 | Atmosphere: 璀璨耀眼的橘黄色塔灯，夜风吹拂着两人的发丝，浓浓的不舍氛围",
        "prologue": "归期临近，布丁即将结束行程准备回国，而你们站在耀眼的东京塔下，面对即将到来的高山大海与时空间隔。",
        "dialogue_intro": [
            ("大桥", "“快要回去了呢……在东京这段最艰难的日子里，因为有你，我才觉得每一天都充满希望。”"),
        ],
        "choices": [
            {
                "option": "仰望东京塔璀璨的灯光",
                "dialogue_response": [
                    ("大桥", "『塔很美，但我的眼里只有你。不管以后回国多远，我的心永远留在这。』"),
                    ("大桥", "（在璀璨灯光下转过身，眼中闪烁着坚定的光芒）"),
                ],
                "affection": 25,
                "random_event": None,
            },
            {
                "option": "默默抱紧他单薄的肩膀",
                "dialogue_response": [
                    ("大桥", "『别担心，异国距离不算什么，等我回去赚够聘礼就来接你！』"),
                    ("大桥", "（心疼地回抱住你，在你耳边轻声许下承诺）"),
                ],
                "affection": 30,
                "random_event": {
                    "trigger_rate": 0.5,
                    "event_title": "🗼 突发心动：塔下的誓言",
                    "narrative": "东京塔的灯光闪烁交替，他在夜色中俯下身，轻轻在你额头上印下一个温暖的吻。",
                    "dialogue": ("大桥", "“这塔灯作证，无论隔着多远的距离，布丁的心永远属于你。”"),
                    "bonus_affection": 10,
                },
            },
            {
                "option": "约定好以后每年都要重逢",
                "dialogue_response": [
                    ("大桥", "『嗯！拉钩上吊一百年不许变，谁变谁是小狗！』"),
                    ("大桥", "（伸出小拇指和你紧紧勾在一起，破涕为笑）"),
                ],
                "affection": 28,
                "random_event": None,
            },
        ],
    },
    6: {
        "title": "🎬 大桥·异国终章：跨国恋的完美甜心结局",
        "scene": "Location: 机场接机大厅 | Time: 15:00 | Atmosphere: 阳光明媚，人潮涌动，跨越山海与时差重逢的炽热温情",
        "prologue": "经过了遥远的思念与时间的洗礼，跨越山海的异国羁绊终于迎来了最璀璨的答案。",
        "dialogue_intro": [
            ("大桥", "“好久不见！距离再远，也剪不断我奔向你的脚步！”"),
        ],
        "choices": [
            {
                "option": "收到他跨国寄来的巨型惊喜包裹",
                "dialogue_response": [
                    ("大桥", "『拆开看到我了吧？里面全是我对你的思念和一颗永远炙热的心！』"),
                    ("大桥", "（从大熊玩偶后面跳出来，给你一个巨大的惊喜）"),
                ],
                "affection": 35,
                "random_event": None,
            },
            {
                "option": "视频通话里隔空拥抱",
                "dialogue_response": [
                    ("大桥", "『虽然隔着时差，但我感觉你一直陪 me 在我身边。爱你哟！』"),
                    ("大桥", "（对着镜头贴了贴脸，眼神里满满都是眷恋）"),
                ],
                "affection": 30,
                "random_event": None,
            },
            {
                "option": "坚定踏上去找他的航班",
                "dialogue_response": [
                    ("在日留学生or打工人", "『我来找你了！再也不要分开了！』"),
                    ("大桥", "『欢迎来到我的怀抱！从今以后，再也不用隔着屏幕想念了！』"),
                ],
                "affection": 35,
                "random_event": {
                    "trigger_rate": 1.0,  # 终局100%触发事件
                    "event_title": "✈️ 专属结局：跨越山海的唯一定制",
                    "narrative": "接机大厅里熙熙攘攘，他当着所有人的面冲过来把你高高抱起转圈，不再有任何顾虑。",
                    "dialogue": ("大桥", "“谢谢你跨越山海来到我身边。从今往后，不管在哪里，只要有你在，那就是我的归宿！”"),
                    "bonus_affection": 15,
                },
            },
        ],
    },
},

"高恭": {
    "经纪人": {
        1: {
            "title": "🎬 高恭·后台初遇：傲娇少年的时尚烦恼",
            "scene": "Location: 秀场后台休息室 | Time: 13:30 | Atmosphere: 挂满华服的衣架，弥漫着香水与定型喷雾的香味，镜前少年神采飞扬却带着一丝紧张",
            "prologue": "作为新人经纪人，你刚进后台就看到高恭对着全身镜左调整右摆弄，明明很在乎造型，嘴上却依旧死要面子。",
            "dialogue_intro": [
                ("高恭", "“喂，你终于来了！快来看看，本少爷今天的造型是不是全场最耀眼的？”"),
                ("经纪人", "（看着他翘起的发尾，你笑着走上前）"),
            ],
            "choices": [
                {
                    "option": "帮他整理略显凌乱的刘海：『别臭美了，快对台词。』",
                    "dialogue_response": [
                        ("高恭", "『喂别弄乱我的发型！……不过，看在你手法不错的份上，勉强原谅你啦。』"),
                        ("高恭", "（嘴上嘟囔着，身体却十分诚实地往你这边凑了凑）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "夸奖他今天穿搭很有品味",
                    "dialogue_response": [
                        ("高恭", "『那当然，本少爷的时尚感什么时候掉过线？不过……你眼光倒还挺好。』"),
                        ("高恭", "（骄傲地扬起下巴，清亮的小眼神里透着藏不住的得意）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "✨ 突发心动：领带上的温热",
                        "narrative": "他有些手忙脚乱地整理领带却越弄越乱，最后别扭地把领带夹塞进你手里。",
                        "dialogue": ("高恭", "“咳……本少爷准许你帮我戴上！可不是我自己不会系哦！”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "板起脸催促通告时间",
                    "dialogue_response": [
                        ("高恭", "『知道了知道了，真啰嗦，跟你老妈一样……哎呀别瞪我，我马上就去总行了吧！』"),
                        ("高恭", "（缩了缩脖子，立马抓起台本乖乖站好）"),
                    ],
                    "affection": 15,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 高恭·深夜休息室：傲娇背后的认真",
            "scene": "Location: 大楼深夜练功房 | Time: 22:30 | Atmosphere: 落地镜反射着温黄的灯光，音乐声戛然而止，少年的额角渗出细密的汗珠",
            "prologue": "通告结束后，高恭并没有直接离开，而是一个人留在练习室里一遍遍重复着动作，背影执着而认真。",
            "dialogue_intro": [
                ("高恭", "“哼，你还没走啊？我可不是在偷练，只是……只是随便活动活动筋骨罢了！”"),
            ],
            "choices": [
                {
                    "option": "看他偷偷练习走秀步态，憋住笑",
                    "dialogue_response": [
                        ("高恭", "『不准笑！我在琢磨帅气的台风呢！……好啦，在你面前丢脸也无所谓啦。』"),
                        ("高恭", "（有些气急败坏地揉了揉揉发红的耳根）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "递上一瓶苏打水：『辛苦了，大帅哥。』",
                    "dialogue_response": [
                        ("高恭", "『哼，这还差不多。虽然本少爷本来就很帅，但有你递水感觉更好喝了。』"),
                        ("高恭", "（拧开瓶盖大饮了一口，眼角的余光悄悄瞄向你）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🥤 突发心动：冰汽水的甜意",
                        "narrative": "他顺手将带有些许冰汽水雾气的瓶身贴了贴你的脸颊，嘴角勾起恶作剧成功的弧度。",
                        "dialogue": ("高恭", "“看你困得眼睛都要闭上了，本少爷好心帮你提提神，不用太感谢我！”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "劝他别太在意网上的恶评",
                    "dialogue_response": [
                        ("高恭", "『我才不在意那种东西呢……只要你相信我，其他人的看法根本无所谓。』"),
                        ("高恭", "（别过头去，声音渐渐低了下来，语气里带着少有的脆弱）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：杂志拍摄现场的突击",
            "scene": "Location: 时尚杂志外景拍摄地 | Time: 10:30 | Atmosphere: 阳光洒在精心布置的布景上，快门声咔嚓作响，全场焦点聚集于一人",
            "prologue": "镜头前的少年表现力惊人，气场全开，但只要每拍完一组动作，他的视线总会第一时间飘向站在场边的你。",
            "dialogue_intro": [
                ("高恭", "“（微笑着对镜头摆 pose，眼神却偷瞄场边）……喂，刚才那组照得怎么样？”"),
            ],
            "choices": [
                {
                    "option": "在镜头外对他的pose比大拇指",
                    "dialogue_response": [
                        ("高恭", "『看到你比手势，我突然超常发挥了……摄影师说刚才那张绝对是封神之作！』"),
                        ("高恭", "（收到你的夸赞后更加劲头十足，表现得愈发卖力帅气）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "提醒他收敛一下自恋的表情",
                    "dialogue_response": [
                        ("高恭", "『这叫自信！不过……为了让你多看我两眼，我收敛一点也行啦。』"),
                        ("高恭", "（有些不服气地撇撇嘴，随后乖乖调整了面部表情）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "顺手帮他披上外套防寒",
                    "dialogue_response": [
                        ("高恭", "『……突然这么体贴干嘛，搞得我怪不好意思的（耳根微红）。』"),
                        ("高恭", "（紧了紧身上的外套，将脸半埋在领子里，耳根红透）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🧥 突发心动：外套下的余温",
                        "narrative": "他将外套分了一半披在你肩上，顺势靠得离你极近，身上带着淡淡的古龙水香气。",
                        "dialogue": ("高恭", "“风这么大，别光顾着照顾我，冻坏了我的专属经纪人谁来给我排通告？”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 高恭·化妆间对峙：嘴硬心软的少爷",
            "scene": "Location: 单人专属化妆间 | Time: 15:00 | Atmosphere: 柔和的化妆镜灯光，空气中飘着甜点香气，静谧的两人生效空间",
            "prologue": "通告间隙，高恭正靠在沙发上百无聊赖地翻着杂志，一看到你推门进来，立刻装出一副漫不经心的样子。",
            "dialogue_intro": [
                ("高恭", "“咳，你进门都不敲门的吗？本少爷正在思考人生呢！”"),
            ],
            "choices": [
                {
                    "option": "戳穿他其实一直在偷看自己",
                    "dialogue_response": [
                        ("高恭", "『哪有偷看！我是在视察工作环境……好啦好啦，我承认我的视线离不开你行了吧！』"),
                        ("高恭", "（被戳穿后脸颊瞬间泛红，把杂志啪地合上遮住脸）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🍰 突发心动：预留的甜点",
                        "narrative": "他别扭地从桌底下拿出一个精致的蛋糕盒，塞到你手里。",
                        "dialogue": ("高恭", "“这是买红豆饼顺便送的限量蛋糕！才不是本少爷排队半小时特意买给你的！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "假装要离开休息室",
                    "dialogue_response": [
                        ("高恭", "『诶别走！……我是说，台本还有不懂的地方，你留下来帮我看看嘛。』"),
                        ("高恭", "（急忙站起身拉住你的袖角，眼神闪烁着不舍）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "送他一枚定制的小胸针",
                    "dialogue_response": [
                        ("高恭", "『这个设计……勉强配得上本少爷的审美，以后天天戴着它开工！』"),
                        ("高恭", "（如获至宝地小心捧着胸针，爱不释手地别在最显眼的位置）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 高恭·突发危机：红毯前的礼服撕裂",
            "scene": "Location: 盛典红毯候场区 | Time: 19:00 | Atmosphere: 闪光灯在大门外接连闪烁，后台气氛紧张严肃，危机一触即发",
            "prologue": "临上场前五分钟，高恭的高定礼服拉链意外卡住撕裂，助理们慌成一团，高恭也有些心焦地皱起眉头。",
            "dialogue_intro": [
                ("高恭", "“怎么办啊！马上就要轮到我出场了……难道本少爷第一次走大红毯就要出丑吗？！”"),
            ],
            "choices": [
                {
                    "option": "临危不乱用针线迅速帮他缝补",
                    "dialogue_response": [
                        ("高恭", "『哇……你居然还会这个？突然觉得你简直全能得像个超人，太崇拜你了！』"),
                        ("高恭", "（低头看着你专注缝补的面容，眼底闪烁着崇拜与心动的光芒）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🧷 突发心动：呼吸交错的距离",
                        "narrative": "由于缝补需要，你贴得极近，少年的心跳声在嘈杂的后台清晰可闻。",
                        "dialogue": ("高恭", "“（喉结微动）那个……你别靠这么近，我心跳得太快，待会儿拍照该不自然了……”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "笑他毛手毛脚差点出丑",
                    "dialogue_response": [
                        ("高恭", "『不准笑！这次是个意外……多亏有你救场，不然本少爷的面子全丢光了。』"),
                        ("高恭", "（长舒一口气，虽然嘴硬但眼里全是对你的感激）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "坚定地拍拍他肩膀：『有我在呢。』",
                    "dialogue_response": [
                        ("高恭", "『嗯，只要你在背后，红毯走得再华丽我也不怕出洋相。』"),
                        ("高恭", "（原本不安的心瞬间定了下来，对你露出极为自信的笑容）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 高恭·完美收官：傲娇少年的终极直球",
            "scene": "Location: 颁奖典礼后的庆功晚宴顶楼露台 | Time: 21:30 | Atmosphere: 夜空繁星点点，远处的霓虹闪烁，晚风微凉，少年手握奖杯向你走来",
            "prologue": "高恭顺利拿下了最佳新人奖，在颁奖致辞时他就频频看向你的方向。晚宴时刻，他避开了所有的镜头与人群，独自把你约到了露台。",
            "dialogue_intro": [
                ("高恭", "“那些聚光灯和掌声虽然很棒，但如果不能和你分享，就一点意义都没有了……”"),
            ],
            "choices": [
                {
                    "option": "微笑着夸奖他今天帅呆了",
                    "dialogue_response": [
                        ("高恭", "『废话，本少爷什么时候不帅？……不过，如果你愿意做我的专属恋人，我可以考虑天天对你一个人帅。』"),
                        ("高恭", "（挺起胸膛傲娇地开场，说到后半句声音却越来越小，脸色爆红）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "假装嫌弃他太自恋",
                    "dialogue_response": [
                        ("高恭", "『嫌弃也没用！我这辈子就赖上你了，不准拒绝，听到没！』"),
                        ("高恭", "（一把拉住你的手不肯放开，眼神里全是霸道与执着）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "轻轻牵住他的手",
                    "dialogue_response": [
                        ("经纪人", "『恭喜你，今晚你是最耀眼的星。』"),
                        ("高恭", "『手这么冰……以后本少爷的专属暖手宝名额正式颁发给你了！』"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,  # 终局100%触发事件
                        "event_title": "🏆 专属结局：星光下的独家签约",
                        "narrative": "他将刚拿到的奖杯郑重地塞进你手里，随后拉着你的手揣进自己的口袋里。",
                        "dialogue": ("高恭", "“听好了，本少爷这辈子最成功的签约，不是签给了经纪公司，而是把我的一生都签给了你！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"高恭": {
    "青梅竹马": {
        1: {
            "title": "🎬 高恭·放学路：傲娇少年的恶趣味",
            "scene": "Location: 放学夕阳下的老街巷口 | Time: 16:45 | Atmosphere: 金色的余晖拉长了两人的影子，空气中弥漫着单车铃声与微风的清凉",
            "prologue": "放学路上，高恭又像往常一样凑过来找茬，手里还拿着一本上课偷偷看的漫画书，冲着你得意地挑了挑眉。",
            "dialogue_intro": [
                ("高恭", "“喂，走路那么慢乌龟都比你快！看什么呢，本大爷手里的漫画书借你开开眼？”"),
                ("青梅竹马", "（看着他这副不可一世的样子，你决定给这个傲娇少年一点“教训”）"),
            ],
            "choices": [
                {
                    "option": "抢过他的漫画书：『上课还看这个！』",
                    "dialogue_response": [
                        ("高恭", "『喂快还给我！青梅了不起啊，竟敢没收本大爷的精神粮食！』"),
                        ("高恭", "（气急败坏地踮起脚尖伸手想要抢回去，耳根却悄悄红了一大片）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "买了两支冰棒分他一只",
                    "dialogue_response": [
                        ("高恭", "『哼，勉强算你有点良心……不过这支草莓味的归我，巧克力归你。』"),
                        ("高恭", "（一把接过来撕开包装，心满意足地咬了一口，眼睛亮晶晶的）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🍦 突发心动：融化的甜意",
                        "narrative": "冰棒化得有点快，顺着他的指尖流了下来，他有些窘迫地把手往你衣服上蹭。",
                        "dialogue": ("高恭", "“喂！都怪你买这么慢的冰棒……帮我擦一下啦，本大爷的手腾不出来！”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "嫌弃他走路姿势太拽",
                    "dialogue_response": [
                        ("高恭", "『这叫帅气懂不懂！不过……在你面前我怎么走都行，别嫌弃我啦。』"),
                        ("高恭", "（有些泄气地收起吊儿郎当的步子，老老实实和你并肩走着）"),
                    ],
                    "affection": 18,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 高恭·天台秘密：夕阳下的真心话",
            "scene": "Location: 学校教学楼顶层天台 | Time: 17:20 | Atmosphere: 晚霞将天空染成绚丽的橘红，铁丝网外是呼啸而过的电车声",
            "prologue": "放学后安静的天台是你们的秘密基地，高恭毫无形象地躺在长椅上，将手臂枕在脑后，向你大吐苦水。",
            "dialogue_intro": [
                ("高恭", "“唉，排练节目真的快累死本少爷了……今天要不是为了在你面前帅气登场，我才不干呢。”"),
            ],
            "choices": [
                {
                    "option": "听他抱怨最近排练太累",
                    "dialogue_response": [
                        ("高恭", "『累死了……不过只要你肯听我发牢骚，我就感觉全身充满电了。』"),
                        ("高恭", "（侧过头静静看着你，原本抱怨的语气瞬间变得温柔缠绵）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🎧 突发心动：风吹过的耳语",
                        "narrative": "一阵微风吹过，他顺势将耳机的一只塞进你耳中，里面正放着他练习时循环的旋律。",
                        "dialogue": ("高恭", "“听到了吗？这首歌的节拍……就跟我现在的心跳一模一样。”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "拍拍他肩膀：『大明星辛苦啦。』",
                    "dialogue_response": [
                        ("高恭", "『少阴阳怪气的……不过，听你这么说我心里还挺受用的。』"),
                        ("高恭", "（傲娇地扬起下巴，嘴角却忍不住疯狂上扬）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "把耳机分他一只听歌",
                    "dialogue_response": [
                        ("高恭", "『这首歌……旋律好像我的心跳，全是因为旁边坐着你。』"),
                        ("高恭", "（耳机里流淌着舒缓的音乐，他安静地靠在栏杆边看着你出神）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：课桌椅间的秘密传话",
            "scene": "Location: 高二（3）班教室角落 | Time: 08:10 | Atmosphere: 早晨明媚的阳光透过玻璃窗洒在课桌上，空气里充满粉笔灰与青春的味道",
            "prologue": "早自习刚过，后桌的高恭就用笔戳了戳你的后背，大言不惭地把空空如也的作业本推了过来。",
            "dialogue_intro": [
                ("高恭", "“喂，青梅大人，江湖救急，今天的数学作业就靠你啦！”"),
            ],
            "choices": [
                {
                    "option": "把作业本拍在他桌上：『抄吧，大少爷。』",
                    "dialogue_response": [
                        ("高恭", "『谢啦！不愧是我的青梅大人……虽然字没我好看，但心意我收下了。』"),
                        ("高恭", "（美滋滋地翻开作业本，提笔刷刷写了起来）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "顺手拿走他一颗糖果",
                    "dialogue_response": [
                        ("高恭", "『诶！那是我特意留到现在的！……算了，看你爱吃，全送你好了。』"),
                        ("高恭", "（肉痛地看着你剥开糖纸，随后把一整盒糖都推了过来）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "提醒他下午有体育测试",
                    "dialogue_response": [
                        ("高恭", "『体育测试什么的完全不在话下……只要你在终点线等我，我绝对拿第一！』"),
                        ("高恭", "（自信满满地拍着胸脯，眼神里满是对你的胜券在握）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🏃 突发心动：终点线的目光",
                        "narrative": "他趁着老师转身的空档，用修长的手指在纸条上飞快写下一行字塞进你手里。",
                        "dialogue": ("高恭", "“如果我跑了第一名，放学后你要答应陪我去吃那家限定甜品！”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 高恭·旧校舍探险：试胆大会的意外",
            "scene": "Location: 废弃的旧校舍走廊 | Time: 18:30 | Atmosphere: 昏暗的走廊，阴森的阴影，手里微弱的手电筒光芒",
            "prologue": "学校组织试胆大会，你和高恭被分到了一组。平日里天不怕地不怕的傲娇少爷，此刻正强装镇定地走在最前面。",
            "dialogue_intro": [
                ("高恭", "“咳……不就是旧校舍吗？本大爷才不会怕这种幼稚的把戏呢，你在后面跟紧我！”"),
            ],
            "choices": [
                {
                    "option": "故意吓唬他一下",
                    "dialogue_response": [
                        ("高恭", "『幼稚！本大爷才不怕……哇！你干嘛突然抓我胳膊！……咳咳，其实我是怕你害怕才护着你的。』"),
                        ("高恭", "（被突如其来的动静吓得一哆嗦，随后反手将你紧紧护在身后）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🔦 突发心动：黑暗中的掌心",
                        "narrative": "手电筒恰好在此刻彻底熄灭，四周陷入一片漆黑，他慌乱中一把攥住了你冰凉的手。",
                        "dialogue": ("高恭", "“别出声……抓紧我，绝对不准放手，听到了没有！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "紧紧抓住他的衣角不放",
                    "dialogue_response": [
                        ("高恭", "『知道怕了吧？没事，有本大爷在这，闭上眼睛抓紧我就行。』"),
                        ("高恭", "（感受到衣角的拉扯，他的腰杆瞬间挺直了，语气里满是神气）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "找到出口手电筒突然没电",
                    "dialogue_response": [
                        ("高恭", "『别慌，牵着我的手，闭着眼睛跟我走，绝对把你安全带出去。』"),
                        ("高恭", "（黑暗中他的掌心滚烫，带着让人莫名安心的力量）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 高恭·星空天台：傲娇的最后防线",
            "scene": "Location: 试胆大会后的夜间教学楼天台 | Time: 19:30 | Atmosphere: 满天繁星，习习凉风，城市远处的霓虹灯火像碎钻般闪烁",
            "prologue": "终于逃出旧校舍后，你们双双来到天台吹风。经历了刚才的黑暗，高恭脸上的红晕在月光下显得格外清晰。",
            "dialogue_intro": [
                ("高恭", "“呼……总算出来了。喂，刚才在里面你可别想笑话我！”"),
            ],
            "choices": [
                {
                    "option": "笑他刚才吓得脸都白了",
                    "dialogue_response": [
                        ("高恭", "『胡说！本大爷那是被晚风吹的……好啦，我承认在你面前我根本没办法淡定。』"),
                        ("高恭", "（恼羞成怒地想捂住你的嘴，却在触碰你脸颊时动作猛地一僵）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "温柔地看着他没有说话",
                    "dialogue_response": [
                        ("高恭", "『别用那种眼神看着我……犯规了啊，搞得我心跳快得快要跳出来了。』"),
                        ("高恭", "（有些慌乱地别过脸去，连脖子根都红透了）"),
                    ],
                    "affection": 28,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "✨ 突发心动：星空下的靠近",
                        "narrative": "夜风微凉，他有些别扭地脱下校服外套披在你身上，借着夜色的掩护悄悄靠近。",
                        "dialogue": ("高恭", "“笨蛋……以后不准再去那么危险的地方了，我会担心的。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "主动戳了戳他的脸颊",
                    "dialogue_response": [
                        ("高恭", "『手感不错吧？……既然都被你摸了，你以后可得对我负责到底。』"),
                        ("高恭", "（顺势捉住你还没来得及收回的手指，眼底闪烁着炽热的光）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 高恭·告白终章：傲娇少年的真情告白",
            "scene": "Location: 樱花树下的小公园 | Time: 21:00 | Atmosphere: 路灯将两人的影子拉得很长，夜色温柔，空气中弥漫着花草的清香",
            "prologue": "从小到大的陪伴在这一刻终于走到了终点线前。面对平时总是嘴硬的少年，你决定率先打破僵局。",
            "dialogue_intro": [
                ("高恭", "“喂……从认识你到现在，本大爷的目光好像从来没有从你身上移开过……”"),
            ],
            "choices": [
                {
                    "option": "笑着戳他胸口：『好啦，我喜欢你。』",
                    "dialogue_response": [
                        ("高恭", "『这、这可是你先告白的哦！……不过本大爷其实暗恋你更久了。从今以后，不准再看别人！』"),
                        ("高恭", "（瞬间破功，不可置信地睁大眼睛随后露出了超级灿烂的笑容）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "傲娇地把头扭向一边",
                    "dialogue_response": [
                        ("高恭", "『扭过去也没用，既然心意相通了，这辈子你都别想逃出我的手掌心！』"),
                        ("高恭", "（霸道地把你的脸转回来，毫不犹豫地低头靠近）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "十指紧扣靠在他肩头",
                    "dialogue_response": [
                        ("高恭", "『真拿你没办法……以后本大爷的所有帅气，只展现在你一个人面前。』"),
                        ("高恭", "（反手将你的手紧紧包裹在掌心里，十指相扣再也不肯分开）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,  # 终局100%触发事件
                        "event_title": "💍 专属结局：竹马的专属契约",
                        "narrative": "月光洒满回家的路，他像小时候那样背起你，脚步稳健而充满力量。",
                        "dialogue": ("高恭", "“从青梅竹马到白头偕老，你这辈子都只能是本大爷的专属甜心！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"高恭": {
    "在日留学生or打工人": {
        1: {
            "title": "🎬 高恭·异国街头：时尚少年的落魄偶遇",
            "scene": "Location: 东京涉谷十字路口街头 | Time: 15:30 | Atmosphere: 汹涌的异国人潮，闪烁的霓虹广告牌，夏日午后炽热的阳光",
            "prologue": "在东京留学/打拼的你，在涉谷街头意外遇到了背着夸张大包小包、正对着手机地图一脸迷茫的高恭。",
            "dialogue_intro": [
                ("高恭", "“喂，那边那个！……咳，问个路，这附近究竟哪个方向才是正确的啊？”"),
                ("在日学生or打工人", "（看着他强装镇定的样子，你笑着走上前去）"),
            ],
            "choices": [
                {
                    "option": "递给他一张东京打工指南",
                    "dialogue_response": [
                        ("高恭", "『哈？本少爷堂堂潮男需要在这种地方找零工？……不过，看在你关心的份上，谢啦。』"),
                        ("高恭", "（嘴硬地一把接过指南，眼神却忍不住偷偷打量你）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "用关西腔调侃他迷路的样子",
                    "dialogue_response": [
                        ("高恭", "『谁迷路了！我只是在用独特的方式探索东京街头……好吧我确实迷路了，求带路！』"),
                        ("高恭", "（泄气地垂下双肩，原本高傲的气场瞬间烟消云散）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "请他喝了一罐冰镇汽水",
                    "dialogue_response": [
                        ("高恭", "『勉强解渴！东京的夏天虽然热，但遇到你好像也没那么讨厌了。』"),
                        ("高恭", "（拉开拉环仰头喝了一大口，冰凉的汽水压下了燥热，耳根却微微发烫）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🥤 突发心动：汽水罐的冰凉",
                        "narrative": "他把冰凉的易拉罐贴了贴你的脸颊，看着你被冰得缩脖子的样子忍不住笑出声。",
                        "dialogue": ("高恭", "“好啦，看在你这么热心肠的份上，本少爷今天就勉为其难允许你当我的专属导游了！”"),
                        "bonus_affection": 5,
                    },
                },
            ],
        },
        2: {
            "title": "🎬 高恭·深夜便利店：打工人的互怼日常",
            "scene": "Location: 东京街头24小时便利店仓库 | Time: 00:15 | Atmosphere: 货架间刺眼的荧光灯，略显局促的仓库，空气里弥漫着关东煮的香气",
            "prologue": "深夜的便利店兼职总是格外辛苦，你刚巡完货，就看到隔壁兼职的高恭正抱着一箱沉重的饮料累得气喘吁吁。",
            "dialogue_intro": [
                ("高恭", "“呼……东京的便利店打工怎么比想象中还要折腾人……”"),
            ],
            "choices": [
                {
                    "option": "看他搬货累得直喘气嘲笑他",
                    "dialogue_response": [
                        ("高恭", "『笑什么笑！这叫展现男人的力量感！……嘶，腰好酸，快帮我揉揉。』"),
                        ("高恭", "（一边嘴硬反驳，一边夸张地捶着腰把重箱子放下）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "📦 突发心动：货架后的靠近",
                        "narrative": "你帮他托了一把快要倾斜的纸箱，两人的手在箱子边缘不经意间重叠在一起。",
                        "dialogue": ("高恭", "“（触电般缩回手）……咳，这种重活本来就该本少爷来，你、你站远点看着就行！”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "分给他一个打折饭团",
                    "dialogue_response": [
                        ("高恭", "『虽然是打折的，但因为是你给的，吃起来感觉跟米其林三星一样。』"),
                        ("高恭", "（撕开包装咬了一口，眼睛亮晶晶地看着你）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "劝他别太晚兼职",
                    "dialogue_response": [
                        ("高恭", "『知道了知道了，管家婆……不过你这么关心我，我会忍不住想入非非的。』"),
                        ("高恭", "（别扭地转过身去理货，可上扬的嘴角怎么也压不住）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：原宿街头的潮流打卡",
            "scene": "Location: 原宿表参道潮流街区 | Time: 14:00 | Atmosphere: 街头此起彼伏的流行音乐，满目琳琅的潮牌橱窗，晴朗的异国天空",
            "prologue": "难得的休息日，高恭硬是拉着你来到原宿街头，美其名曰“视察东京时尚前沿”，实则是想和你一起逛街。",
            "dialogue_intro": [
                ("高恭", "“快看这家店的新款！本少爷的眼光绝对不会出错……”"),
            ],
            "choices": [
                {
                    "option": "陪他一起逛潮牌服装店",
                    "dialogue_response": [
                        ("高恭", "『眼光不错嘛，这件衣服跟你超配……不过在我眼里，你永远比衣服好看。』"),
                        ("高恭", "（顺手拿起一件外套比划在你身上，眼神里满是惊艳）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "吐槽他挑衣服眼光太挑剔",
                    "dialogue_response": [
                        ("高恭", "『时尚懂不懂！不过为了你，本少爷可以改变穿搭风格，只穿你喜欢的。』"),
                        ("高恭", "（傲娇地挑起眉毛，摆出一个自认为很帅的pose）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "坐在长椅上喝抹茶拿铁",
                    "dialogue_response": [
                        ("高恭", "『东京的街头很繁华，但我只想把视线全留在你一个人身上。』"),
                        ("高恭", "（顺势挨着你坐下，肩膀紧紧贴在一起，目光一刻也没离开过你）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🍵 突发心动：拿铁的甜香",
                        "narrative": "他趁你不注意，低头尝了一口你杯里的拿铁，随后笑得像个恶作剧得逞的孩子。",
                        "dialogue": ("高恭", "“确实挺甜的……不过，肯定没有你刚才偷看我的表情甜。”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 高恭·暴雨突袭：屋檐下的傲娇心思",
            "scene": "Location: 新宿街头店铺的狭窄屋檐下 | Time: 17:30 | Atmosphere: 倾盆而下的雷阵雨，模糊的霓虹水雾，狭小空间里的紧密依偎",
            "prologue": "逛街时突然遭遇东京猝不及防的暴雨，你们狼狈地躲进路边店铺的屋檐下，四周冰冷的雨水将温度拉低。",
            "dialogue_intro": [
                ("高恭", "“啧，这雨怎么说下就下，把本少爷精心抓的发型都快毁了……”"),
            ],
            "choices": [
                {
                    "option": "把唯一的夹克披在他身上",
                    "dialogue_response": [
                        ("高恭", "『诶你给我了那你怎么办……真笨。快过来，钻进我的外套里，这样就不淋雨了。』"),
                        ("高恭", "（一把将你拉进自己宽大的外套怀抱里，用体温替你驱散寒意）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🧥 突发心动：外套下的双人空间",
                        "narrative": "狭窄的外套空间里，两人的呼吸清晰可闻，他有些不自然地将视线移向飘雨的街道。",
                        "dialogue": ("高恭", "“别乱动……听见没有，外面雨这么大，我的心跳声都被你盖过去了。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "抱怨东京的天气阴晴不定",
                    "dialogue_response": [
                        ("高恭", "『管他什么暴雨，只要你在我身边，整个世界都是放晴的粉红色。』"),
                        ("高恭", "（极其自然地搂紧你的肩膀，语气里满是坚定与宠溺）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "用手机自拍记录雨中狼狈样",
                    "dialogue_response": [
                        ("高恭", "『不准发黑历史！……不过，如果是跟你一起拍的，就算落汤鸡也帅气。』"),
                        ("高恭", "（凑过头来和你一起看屏幕，顺便对镜头比了个耶）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 高恭·东京塔夜景：离别前的动摇",
            "scene": "Location: 六本木展望台玻璃窗前 | Time: 21:00 | Atmosphere: 俯瞰整座璀璨的东京夜景，高耸的东京塔闪烁着温暖的橘光",
            "prologue": "高恭在日本的行程即将结束，临回国前，他特意带你来到能俯瞰全城的展望台，气氛在一片灯火中变得格外安静。",
            "dialogue_intro": [
                ("高恭", "“这里的夜景……确实挺让人舍不得的。”"),
            ],
            "choices": [
                {
                    "option": "看着远处的塔灯感叹时光",
                    "dialogue_response": [
                        ("高恭", "『别看塔了，看我。明天我就要回去了……你会舍不得本大爷吗？』"),
                        ("高恭", "（双手轻轻掰过你的脸，强迫你把视线全落在他的眼睛里）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "拍拍他肩膀：『回国后加油。』",
                    "dialogue_response": [
                        ("高恭", "『一句加油可不够……你得答应跟我保持联络，或者干脆跟我一起走！』"),
                        ("高恭", "（有些急切地抓住你的手腕，少有的认真与执着溢于言表）"),
                    ],
                    "affection": 30,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🗼 突发心动：塔灯下的拥抱",
                        "narrative": "东京塔的灯光在这一刻恰好切换成告白的限定色彩，他顺势将你紧紧拥入怀中。",
                        "dialogue": ("高恭", "“异国距离算什么？本大爷才不怕跨国恋，只要你说一句舍不得我，我立刻把回国机票撕了！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "紧紧抱住他傲娇的身躯",
                    "dialogue_response": [
                        ("高恭", "『……犯规。突然这么主动，搞得我更舍不得离开东京了。』"),
                        ("高恭", "（身体僵硬了一秒，随即将你死死搂在怀里，下巴抵在你的发顶）"),
                    ],
                    "affection": 28,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 高恭·异国终章：傲娇跨国恋的完美告白",
            "scene": "Location: 东京羽田机场 / 跨国视频两端 | Time: 12:00 | Atmosphere: 机场广播声与思念交织，跨越时差的炽热爱意瞬间抵达",
            "prologue": "虽然经历了短暂的分离与时差，但有些心意跨越了山海，最终在这一刻迎来了命中注定的结局。",
            "dialogue_intro": [
                ("高恭", "“喂！听得到吗？本少爷有极其重要的话要宣布！”"),
            ],
            "choices": [
                {
                    "option": "接通跨国视频电话听他表白",
                    "dialogue_response": [
                        ("高恭", "『听好了，本少爷在日本想了你三天三夜，结论是：你绝对逃不出我的手掌心了！』"),
                        ("高恭", "（屏幕那头的高恭急得直挥手，脸上却带着势在必得的灿烂笑容）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "假装信号不好逗他着急",
                    "dialogue_response": [
                        ("高恭", "『喂喂别挂电话！我还没说完呢……我喜欢你！听到没，超级喜欢你！』"),
                        ("高恭", "（急得差点跳脚，把屏幕凑得极近，傲娇面具瞬间碎了一地）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "买机票直接飞去找他",
                    "dialogue_response": [
                        ("在日学生or打工人", "『不用打电话了，转头看看你身后。』"),
                        ("高恭", "『什么？！你真的来东京找我了？……太狡猾了，明明该由本少爷去接你的！』"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,  # 终局100%触发事件
                        "event_title": "✈️ 专属结局：跨越山海的独家契约",
                        "narrative": "他在机场到达大厅一眼认出了你，扔下行李不顾一切地冲过来将你抱离地面。",
                        "dialogue": ("高恭", "“听好了！从今以后，不管你在东京还是国内，本少爷的专属领地里永远只有你一个女主角！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"流星": {
    "经纪人": {
        1: {
            "title": "🎬 流星·后台初遇：小恶魔的甜美陷阱",
            "scene": "Location: 演唱会后台化妆间 | Time: 17:00 | Atmosphere: 忙碌的灯光、散落的服装道具，镜子前弥漫着定型喷雾的淡淡清香",
            "prologue": "作为专属经纪人的你刚推开休息室的门，流星就顶着一头华丽的造型转过身来，冲你狡黠地眨了眨眼。",
            "dialogue_intro": [
                ("流星", "“哼哼，你终于舍得来看我啦？快来看看我今天的造型有没有哪里不够完美？”"),
            ],
            "choices": [
                {
                    "option": "戳戳他亮晶晶的眼妆：『今天造型很精致嘛。』",
                    "dialogue_response": [
                        ("流星", "『那是当然，为了让你眼前一亮，我可是花了整整一小时呢。心动了吗？』"),
                        ("流星", "（顺势捉住你还没来得及收回的手指，轻轻蹭了蹭自己的脸颊）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "✨ 突发心动：闪粉的魔力",
                        "narrative": "他眼角的闪粉不小心蹭到了你的指尖上，在灯光下折射出细碎的光芒。",
                        "dialogue": ("流星", "“你看，这可是我专属的标记哦，今天不准洗掉，要一直带着它。”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "提醒他别在后台恶作剧捉弄人",
                    "dialogue_response": [
                        ("流星", "『怎么会呢，我可是乖宝宝……除非你一直不理我，那我就只好调皮一下咯。』"),
                        ("流星", "（无辜地眨巴着大眼睛，语气里却满是吃定你的小得意）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "递上行程表让他确认",
                    "dialogue_response": [
                        ("流星", "『行程全记在脑子里啦，不过……如果奖励是一个拥抱，效率会翻倍哦。』"),
                        ("流星", "（笑嘻嘻地把行程表推到一边，张开双臂眼巴巴地望着你）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 流星·深夜彩排：闪闪发光的小恶魔",
            "scene": "Location: 空无一人的巨型演播厅舞台 | Time: 23:30 | Atmosphere: 仅剩一束追光灯打在舞台中央，四周是静谧空旷的黑暗",
            "prologue": "深夜的最后一次走台，流星在空旷的舞台上练习着核心舞蹈动作，耀眼的汗水顺着精致的下颌线滑落。",
            "dialogue_intro": [
                ("流星", "“呼……看我的终极杀必死wink，这一下有没有精准狙击到你的心？”"),
            ],
            "choices": [
                {
                    "option": "看他练习wink忍不住笑出来",
                    "dialogue_response": [
                        ("流星", "『笑什么？刚才那个wink可是专门为你发射的，没接收到吗？再来一次哦。』"),
                        ("流星", "（从舞台边缘一跃而下，几步跑到你面前，又俏皮地眨了眨眼）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🥛 突发心动：深夜的温度",
                        "narrative": "你无奈地摇摇头，把早就准备好的保温杯递了过去，掌心触碰到他微凉的手腕。",
                        "dialogue": ("流星", "“只要是你给的，就算苦药我也觉得是甜的……不过里面装的肯定是我最爱的热牛奶吧？”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "递上热牛奶：『别练了，快休息。』",
                    "dialogue_response": [
                        ("流星", "『嘿嘿，有你的专属牛奶，感觉自己像个被宠坏的小王子。』"),
                        ("流星", "（满足地捧着杯子喝了一口，看向你的眼神亮晶晶的）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "夸奖他舞台魅力越来越强",
                    "dialogue_response": [
                        ("流星", "『那当然，因为台下有你在看着我呀，我要做你心里最耀眼的唯一。』"),
                        ("流星", "（骄傲地扬起下巴，随后顺势靠在你的肩膀上撒娇）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：摄影棚的突发视线",
            "scene": "Location: 现代化时尚摄影棚 | Time: 14:00 | Atmosphere: 闪光灯此起彼伏，快门声不断，空气中弥漫着高级香水与咖啡的香气",
            "prologue": "杂志大片拍摄间隙，流星刚换好一套复古造型，隔着人群冷不丁地冲着正在核对通告单的你抛了个媚眼。",
            "dialogue_intro": [
                ("流星", "（单手插兜漫步走过来，嘴角噙着一抹恶作剧得逞的坏笑）"),
            ],
            "choices": [
                {
                    "option": "假装没看到他故意抛来的媚眼",
                    "dialogue_response": [
                        ("流星", "『好呀，竟然敢无视我！看来今天不给你点“甜头”惩罚是不行了。』"),
                        ("流星", "（不满地鼓起腮帮子，身体微微前倾凑到你耳边小声抗议）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "顺手帮他调整摄像机角度",
                    "dialogue_response": [
                        ("流星", "『不用看镜头啦，把你的镜头全开在我身上，保证收视率爆表。』"),
                        ("流星", "（一把按住相机支架，炙热的目光牢牢锁死在你的脸上）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "夸他今天杂志拍得像动漫男主",
                    "dialogue_response": [
                        ("流星", "『动漫男主可没我这么专一，我的眼里从头到尾只有你一个人。』"),
                        ("流星", "（听到夸奖后笑得眉眼弯弯，尾音上扬得像一只偷腥成功的小狐狸）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "📸 突发心动：定格的目光",
                        "narrative": "摄影师趁着间隙抓拍了一张他盯着你笑的侧影，照片里满是对你藏不住的温柔。",
                        "dialogue": ("流星", "“这张照片不准发给别人哦，它是本大爷专属于你的私藏帅照。”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 流星·休息室密谈：小恶魔的直球审问",
            "scene": "Location: 艺人专属VIP休息室 | Time: 16:30 | Atmosphere: 柔软的真皮沙发，窗外是渐暗的城市霓虹，空间私密而安静",
            "prologue": "终于结束了繁重的通告，流星反锁上休息室的门，直接将你圈在沙发角落里，展开了新一轮的“严刑拷打”。",
            "dialogue_intro": [
                ("流星", "“好啦，现在闲杂人等都退下了，老实交代，今天工作的时候有没有偷偷想我？”"),
            ],
            "choices": [
                {
                    "option": "被他逼问今天有没有想他",
                    "dialogue_response": [
                        ("流星", "『不准说没有！从实招来，不然今晚我要缠着你讲一整夜的悄悄话。』"),
                        ("流星", "（双手撑在沙发背上将你困住，距离近得能感受到彼此温热的呼吸）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "💫 突发心动：逐渐逼近的距离",
                        "narrative": "看你有些害羞地别过脸，他低低地笑了一声，恶作剧般地轻轻捏了捏你的脸颊。",
                        "dialogue": ("流星", "“你看你的耳朵都红了还嘴硬，明明心里想我想得不得了嘛。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "笑骂他是个狡猾的小鬼头",
                    "dialogue_response": [
                        ("流星", "『小鬼头也只对你一个人坏心思哦，别人想看我这一面还看不到呢。』"),
                        ("流星", "（傲娇地挑起眉梢，语气里有着对你独一份的偏爱）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "揉揉他精致的头发",
                    "dialogue_response": [
                        ("流星", "『发型会乱的啦……不过，如果你是想多摸一会儿，我勉强答应你。』"),
                        ("流星", "（舒服地眯起眼睛，像只被顺毛的大型猫咪一样蹭了蹭你的掌心）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 流星·突发危机：演唱会直播前的突发状况",
            "scene": "Location: 大型演唱会后台控制台 | Time: 19:45 | Atmosphere: 倒计时紧张的滴答声，工作人员匆忙奔跑的脚步声",
            "prologue": "距离全球直播演唱会开场还有十五分钟，主控麦克风突然出现硬件故障，全场气氛瞬间凝固，流星却第一时间看向了你。",
            "dialogue_intro": [
                ("流星", "“喂，大经纪人，离上台可没时间了哦，你打算怎么英雄救美？”"),
            ],
            "choices": [
                {
                    "option": "迅速帮他解决设备故障问题",
                    "dialogue_response": [
                        ("流星", "『太厉害了吧！不愧是我的专属经纪人，简直是拯救世界的英雄，我要奖励你一个吻！』"),
                        ("流星", "（危机解除后兴奋地一把拉住你的手，险些直接在后台转起圈来）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🎤 突发心动：登台前的告白预热",
                        "narrative": "舞台倒计时音乐已经响起，他在上台前突然回过头，飞快地在你手背上印下一个温热的吻。",
                        "dialogue": ("流星", "“等我凯旋归来，接下来要处理的可是我们俩的‘私人账单’哦！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "安抚他略显紧张的情绪",
                    "dialogue_response": [
                        ("流星", "『其实我才不紧张呢，只要转头看到你在后台冲我笑，我就什么都不怕了。』"),
                        ("流星", "（反手紧紧握住你因忙碌而有些冰凉的手指，深吸了一口气恢复自信）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "开玩笑说要扣他工资当惩罚",
                    "dialogue_response": [
                        ("流星", "『扣工资？那我只好用一辈子的温柔来抵债咯，这个买卖划算吧？』"),
                        ("流星", "（狡黠地眨了眨眼，随后潇洒转身迈向璀璨耀眼的升降台）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 流星·完美谢幕：小恶魔的专属告白契约",
            "scene": "Location: 庆功宴顶层露台 | Time: 23:00 | Atmosphere: 漫天绽放的烟花，香槟塔折射出的璀璨光芒，浪漫至极的夜空",
            "prologue": "演唱会完美落幕，庆功宴后的露台上只剩下你们两个人。流星拿着切好的蛋糕走到你面前，眼底闪烁着比星光还要耀眼的光芒。",
            "dialogue_intro": [
                ("流星", "“辛苦啦我的专属经纪人，不过从现在开始，这份工作合同需要永久升级了……”"),
            ],
            "choices": [
                {
                    "option": "微笑着送上庆功蛋糕",
                    "dialogue_response": [
                        ("流星", "『谢谢！不过蛋糕没有你甜……从今天起，不准再做我的经纪人了，做我的恋人好不好？』"),
                        ("流星", "（将蛋糕稳稳放下，随后郑重而热烈地将你拥入怀中）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "假装思考一下再答应",
                    "dialogue_response": [
                        ("流星", "『这还要考虑？！不准考虑，立刻马上盖章生效，你逃不掉啦！』"),
                        ("流星", "（急切地嘟囔着，随后霸道又温柔地俯身拉近了两人的距离）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "轻轻握住他微凉的手",
                    "dialogue_response": [
                        ("流星", "『好，以后我的心只为你一个人闪闪发光。』"),
                        ("流星", "（灿烂地笑了开来，眼底泛起幸福的水光，十指紧扣再也不肯松开）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,
                        "event_title": "🌟 专属结局：顶级巨星的独家恋人",
                        "narrative": "远处的最后一束烟花在夜空中轰然炸裂，照亮了他写满深情与爱意的面容。",
                        "dialogue": ("流星", "“听好了，聚光灯属于舞台，而本大爷的所有心跳和未来，永远只属于你一个人！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
    "青梅竹马": {
        1: {
            "title": "🎬 流星·放学路：青梅竹马的恶作剧日常",
            "scene": "Location: 放学后的落日林荫小道 | Time: 16:30 | Atmosphere: 金色的夕阳把两人的影子拉得很长，书包里的漫画书与微风作伴",
            "prologue": "放学回家的路上，流星又开始不安分地围着你转圈，手里还拎着刚从便利店买的草莓牛奶冲你显摆。",
            "dialogue_intro": [
                ("流星", "“喂，走路这么慢小心被怪兽抓走哦！要不要喝一口本少爷的草莓牛奶压压惊？”"),
            ],
            "choices": [
                {
                    "option": "抢走他的草莓牛奶：『上课不听讲还喝这个！』",
                    "dialogue_response": [
                        ("流星", "『喂！快还给我！青梅了不起啊，竟敢抢本少爷的草莓牛奶！』"),
                        ("流星", "（气急败坏地蹦起来想要抢回去，傲娇的小脸上写满了不服气）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "用书本轻轻拍他脑袋",
                    "dialogue_response": [
                        ("流星", "『痛诶！把你打笨了谁来陪我上下学啊，真是的。』"),
                        ("流星", "（夸张地捂着脑袋揉了揉，眼底却带着藏不住的笑意）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "顺手塞给他一颗水果糖",
                    "dialogue_response": [
                        ("流星", "『哼，看在糖的份上原谅你啦。不过，没我的甜哦你要不要尝尝？』"),
                        ("流星", "（剥开糖纸飞快地塞进嘴里，随后冲你狡黠地眨了眨眼）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🍬 突发心动：口袋里的秘密",
                        "narrative": "他突然神秘兮兮地从口袋里掏出一颗包装精美的水果硬糖，不由分说地塞进你手里。",
                        "dialogue": ("流星", "“其实特意给你留了最大的那颗，不准转头给别人吃听见没！”"),
                        "bonus_affection": 5,
                    },
                },
            ],
        },
        2: {
            "title": "🎬 流星·秘密基地：夕阳下的真心话",
            "scene": "Location: 老旧教学楼的天台旧沙发 | Time: 17:40 | Atmosphere: 橙红色的晚霞铺满整个天际，微风中带着夏日特有的温热",
            "prologue": "放学后的秘密基地里，流星毫无形象地瘫在旧沙发上，向你抱怨着最近被选拔为练习生后魔鬼般的训练强度。",
            "dialogue_intro": [
                ("流星", "“唉……每天压腿拉筋真的快把本少爷折腾散架了。”"),
            ],
            "choices": [
                {
                    "option": "听他讲偶像是怎么辛苦练习的",
                    "dialogue_response": [
                        ("流星", "『不管别人怎么看我，我只想让你看到我最帅、最闪闪发光的一面。』"),
                        ("流星", "（原本懒散的坐姿瞬间端正起来，目光灼灼地凝视着你）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🌅 突发心动：晚霞下的对视",
                        "narrative": "夕阳的余晖洒在他卷翘的睫毛上，镀上一层好看的金边，空气仿佛在这一刻安静了下来。",
                        "dialogue": ("流星", "“所以……你会一直陪着我走到最大的舞台上，对吧？”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "拍拍他肩膀：『你一直都很棒。』",
                    "dialogue_response": [
                        ("流星", "『听到你这么夸我，比拿全校第一还要开心百倍呢。』"),
                        ("流星", "（傲娇地扬起下巴，嘴角却欢快地上扬到一个藏都藏不住的弧度）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "笑他小时候尿床的黑历史",
                    "dialogue_response": [
                        ("流星", "『呀！那段记忆不是早就被你封印了吗！不准再提了，不然我要用绝招了！』"),
                        ("流星", "（瞬间羞恼地红了脸，张牙舞爪地扑过来试图捂住你的嘴）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：晨读课的恶作剧视线",
            "scene": "Location: 高二（1）班靠窗的座位 | Time: 08:15 | Atmosphere: 早晨清透的阳光洒进教室，朗朗的读书声此起彼伏",
            "prologue": "早自习刚过大半，坐在你前桌的流星就频频转过头来，用卷成筒的课本轻轻敲击着你的桌面。",
            "dialogue_intro": [
                ("流星", "“喂，别背书啦，看看我嘛，难道课本比本少爷还好看？”"),
            ],
            "choices": [
                {
                    "option": "转过头瞪了他一眼：『看什么看！』",
                    "dialogue_response": [
                        ("流星", "『因为你好看呀，怎么看都看不够嘛。快转过去，不然我要脸红了。』"),
                        ("流星", "（嘴上这么说着，耳根却以肉眼可见的速度迅速红透了）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "把纸条团成雪球砸过去",
                    "dialogue_response": [
                        ("流星", "『好啊竟敢偷袭！看我的无敌连环纸条反击！』"),
                        ("流星", "（精准地接住纸团，飞快在上面写满字又顺着缝隙扔了回来）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "安静地做自己的试卷",
                    "dialogue_response": [
                        ("流星", "『真无聊……好啦不闹了，待会放学请你吃路口那家限定可丽饼总行了吧？』"),
                        ("流星", "（见你无动于衷，有些泄气地转过身去，却又忍不住偷偷用余光瞄你）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "💌 突发心动：课桌下的纸条",
                        "narrative": "一张精心折成爱心形状的纸条悄悄从桌子缝隙间塞了过来，上面写着歪歪扭扭的威胁。",
                        "dialogue": ("流星", "“放学不准跟别人走，否则本大爷要生气一整天！”"),
                        "bonus_affection": 7,
                    },
                },
            ],
        },
        4: {
            "title": "🎬 流星·文化祭后台：小恶魔的贴心伪装",
            "scene": "Location: 学校礼堂后台化妆间 | Time: 14:00 | Atmosphere: 嘈杂的人群，舞台剧道具的油漆味，空气里满是青春的躁动",
            "prologue": "校园文化祭的舞台即将开演，流星作为压轴嘉宾正在后台紧张地整理着演出服，看到你走进来立刻换上一副求夸奖的表情。",
            "dialogue_intro": [
                ("流星", "“快帮我看看，今天这套演出服是不是把全校男生的风头都压下去了？”"),
            ],
            "choices": [
                {
                    "option": "帮他戴上夸张的演出面具",
                    "dialogue_response": [
                        ("流星", "『戴上这个别人就认不出我了……不过，你一眼就能认出我吧？因为我在你心里最特别。』"),
                        ("流星", "（乖乖配合着低下头让你调整面具，眼神里满是对你的信任与依赖）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🎭 突发心动：面具下的对视",
                        "narrative": "你帮他系好面具的系带时，指尖不小心擦过他的耳后，惹得他浑身微微一颤。",
                        "dialogue": ("流星", "“别乱动……待会演完戏，你必须第一个在台下给我送花哦。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "吐槽他今天臭美了八百遍",
                    "dialogue_response": [
                        ("流星", "『舞台上的C位怎么能不精致！为了配得上站在台下的你，我可是拼了。』"),
                        ("流星", "（理直气壮地挺起胸膛，傲娇的小表情可爱得让人没脾气）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "递上一瓶矿泉水：『加油哦。』",
                    "dialogue_response": [
                        ("流星", "『收到！有了你的应援，今天的全校公演我绝对拿大满贯！』"),
                        ("流星", "（一把接过矿泉水拧开喝了一口，整个人像打了鸡血一样元气满满）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 流星·烟花树下：无法掩饰的心跳加速",
            "scene": "Location: 校园后山神社的巨大樱花树下 | Time: 20:30 | Atmosphere: 远处夜空绽放的绚丽烟花，斑驳的树影，空气中弥漫着夏夜的微凉",
            "prologue": "文化祭结束后的烟花大会上，两人不知不觉走到了后山。流星突然拉住你的手腕，呼吸有些不自然地急促起来。",
            "dialogue_intro": [
                ("流星", "“等、等一下……我的鞋带好像松了……”"),
            ],
            "choices": [
                {
                    "option": "戳戳他通红的耳尖：『真的没发烧？』",
                    "dialogue_response": [
                        ("流星", "『才不是发烧……是因为你离我太近，我的心跳快得连烟花声都听不见了。』"),
                        ("流星", "（索性破罐子破摔地抓住你的手按在他的胸口，那里正剧烈地起伏着）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🎆 突发心动：烟花下的告白预兆",
                        "narrative": "又一朵巨大的烟花腾空而起，将他眼底汹涌的爱意照得一清二楚。",
                        "dialogue": ("流星", "“从小到大一直陪在我身边的笨蛋……这次不许再装傻了！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "假装看烟花不理他",
                    "dialogue_response": [
                        ("流星", "『别看烟花啦，烟花一会就没了，但我对你的喜欢会一直亮着。』"),
                        ("流星", "（急忙伸手轻轻掰过你的脸，强迫你把视线落在他身上）"),
                    ],
                    "affection": 28,
                    "random_event": None,
                },
                {
                    "option": "温柔地握住他的手掌",
                    "dialogue_response": [
                        ("流星", "『哇，你的手好暖……从今天起，不准再做普通朋友了，做我的人吧！』"),
                        ("流星", "（反手将你的手死死包在掌心里，语气里满是势在必得的宣告）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 流星·告白终章：青梅竹马的甜心契约",
            "scene": "Location: 熟悉的那条放学路灯下 | Time: 21:30 | Atmosphere: 昏黄温暖的路灯光晕，夜风里满是少年的青涩与悸动",
            "prologue": "青梅竹马多年的终点线前，流星终于鼓起勇气停下脚步，认真地向你递出了通往未来的专属契约。",
            "dialogue_intro": [
                ("流星", "“喂……从青梅竹马升级成恋人这个提议，本大爷觉得非常可行，你觉得呢？”"),
            ],
            "choices": [
                {
                    "option": "笑着答应他的无理要求：『好啦，听你的。』",
                    "dialogue_response": [
                        ("流星", "『耶！作战成功！从今天起，你就是本少爷盖过章的专属恋人了，不准反悔！』"),
                        ("流星", "（高兴得差点原地跳起来，随后一把将你紧紧抱进怀里）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "傲娇地敲他额头一下",
                    "dialogue_response": [
                        ("流星", "『痛！……不过只要能换来你一句我愿意，挨敲也值了！』"),
                        ("流星", "（揉了揉被敲的额头，咧开嘴笑得像个拿到糖果的幼稚小孩）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "十指紧扣奔向未来",
                    "dialogue_response": [
                        ("流星", "『走吧，青梅竹马的恋爱长跑，今天终于圆满通关啦！』"),
                        ("流星", "（反手十指紧扣，牵着你大步流星地朝着属于两人的未来跑去）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,
                        "event_title": "💍 专属结局：竹马少年的终身契约",
                        "narrative": "月光拉长了并肩前行的影子，这一刻，所有的年少欢喜都变成了余生漫长的陪伴。",
                        "dialogue": ("流星", "“从小到大的青梅竹马由本大爷承包了，以后每一天都要继续多多指教咯，我的恋人！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
},
"在日留学生or打工人": {
        1: {
            "title": "🎬 流星·异国电车站：闪闪发光的偶遇",
            "scene": "Location: 东京某繁华换乘电车站 | Time: 18:15 | Atmosphere: 人潮汹涌的下班高峰期，电子指示牌闪烁着刺眼的光芒，空气中弥漫着电车的摩擦味",
            "prologue": "异国他乡的东京电车站里，你正对着错综复杂的换乘路线图发愁，一个顶着精致染发、戴着耳钉的少年轻笑着凑了过来。",
            "dialogue_intro": [
                ("流星", "“迷路的小可爱，需要本少爷大发慈悲给你指条明路吗？”"),
            ],
            "choices": [
                {
                    "option": "递给他一张东京地铁路线图",
                    "dialogue_response": [
                        ("流星", "『哇，救星降临！在东京正愁找不到路呢，你长得这么好看，一定是天使吧？』"),
                        ("流星", "（顺手接过路线图，却顺势将指尖轻轻蹭过你的手心，笑得像只偷腥的小狐狸）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🎫 突发心动：电车站的初次交集",
                        "narrative": "他极其自然地拿过你手中的路线图，用红笔在上面画出了最便捷的换乘路线。",
                        "dialogue": ("流星", "“跟着本大爷走保证不会丢，说不定还能带你发现东京隐藏的美食小店哦。”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "用关西腔开玩笑打招呼",
                    "dialogue_response": [
                        ("流星", "『哈哈，异国他乡听到这个口音太亲切了！交个朋友呗，带我去吃好吃的？』"),
                        ("流星", "（眼中闪过一丝惊艳与惊喜，随后熟络地笑了起来）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "请他喝了一罐冰镇抹茶",
                    "dialogue_response": [
                        ("流星", "『谢谢啦！今天在东京打工受的委屈，被你这罐抹茶全治愈了。』"),
                        ("流星", "（满足地拉开拉环喝了一口，看向你的眼神亮晶晶的）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 流星·深夜便利店：小恶魔的打工日记",
            "scene": "Location: 东京街角24小时便利店 | Time: 23:45 | Atmosphere: 店内明亮的荧光灯，微波炉加热便当的叮咚声，深夜独有的寂静街道",
            "prologue": "深夜兼职的便利店迎来了一天的尾声，流星穿着略显宽大的店员制服，正毫无形象地靠在货架旁揉着酸痛的肩膀。",
            "dialogue_intro": [
                ("流星", "“呼……这夜班打工简直快赶上魔鬼训练了，早知道这么累就不来体验生活了。”"),
            ],
            "choices": [
                {
                    "option": "看他整理货架累得直叹气",
                    "dialogue_response": [
                        ("流星", "『叹气会把好运赶跑的……不过，如果你的好运头衔全部分给我，我就原谅你。』"),
                        ("流星", "（立刻直起腰来冲你挑了挑眉，哪里还有半点方才疲惫的样子）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🍙 突发心动：深夜的打折饭团",
                        "narrative": "他神秘兮兮地从收银台底下拿出一个刚贴上半价标签的饭团，献宝似地递到你面前。",
                        "dialogue": ("流星", "“辛苦打工人专属的深夜加餐，不准嫌弃哦，这可是本大爷精挑细选的。”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "分给他一个打折饭团",
                    "dialogue_response": [
                        ("流星", "『虽然是打折的，但因为是你喂的，感觉比高级寿司还美味一百倍。』"),
                        ("流星", "（笑嘻嘻地咬了一口，眼睛弯成月牙般好看的弧度）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "劝他早点回宿舍休息",
                    "dialogue_response": [
                        ("流星", "『遵命！不过明天你得答应陪我一起逛涩谷，不然我今晚不走了。』"),
                        ("流星", "（双手合十摆出一副可怜兮兮的无赖表情，让人无法拒绝）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：涉谷街头的潮流漫步",
            "scene": "Location: 东京涩谷十字路口 | Time: 14:20 | Atmosphere: 汹涌的人潮交织，巨型电子屏幕播放着流行音乐，街头弥漫着青春与时尚的气息",
            "prologue": "阳光洒在热闹的涩谷街头，流星特意换上了一身潮牌私服，拉着你在川流不息的人群中肆意穿行。",
            "dialogue_intro": [
                ("流星", "（突然停下脚步转过身，指了指旁边潮牌店橱窗里的一顶鸭舌帽）"),
            ],
            "choices": [
                {
                    "option": "帮他挑了一顶超酷的鸭舌帽",
                    "dialogue_response": [
                        ("流星", "『眼光不错嘛，戴上这个走在东京街头，回头率绝对百分百……不过最想让你回头看我。』"),
                        ("流星", "（顺势把帽子扣在自己头上，冲你抛了个极其标准的电眼）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🥞 突发心动：街头的甜腻滋味",
                        "narrative": "他不由分说地拉着你走进路边的可丽饼店，买了一份加满草莓和奶油的限定甜品。",
                        "dialogue": ("流星", "“啊——张嘴。尝一口看看，是不是比东京的空气还要甜？”"),
                        "bonus_affection": 7,
                    },
                },
                {
                    "option": "吐槽他逛街比女孩子还讲究",
                    "dialogue_response": [
                        ("流星", "『这叫精致懂不懂！为了配得上站在你身边的帅气形象，我容易嘛我。』"),
                        ("流星", "（傲娇地哼了一声，随后极其自然地伸手牵住了你的衣角）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "买了两份可丽饼分食",
                    "dialogue_response": [
                        ("流星", "『甜滋滋的，就像我现在的心情一样，全都是因为你在身边。』"),
                        ("流星", "（满足地眯起眼睛，吃相像只餍足的小动物）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        4: {
            "title": "🎬 流星·暴雨突袭：东京街头的屋檐避难",
            "scene": "Location: 新宿某百年神社的古老木屋檐下 | Time: 17:00 | Atmosphere: 天空骤然下起倾盆暴雨，密集的雨幕模糊了东京的霓虹夜景",
            "prologue": "突如其来的东京暴雨打乱了行程，两人狼狈地躲进神社的屋檐下。冰凉的雨水打湿了他的发梢，平添了几分破碎感。",
            "dialogue_intro": [
                ("流星", "“哇勒，这雨也太不讲道理了吧，把本少爷精心抓的发型都毁了……”"),
            ],
            "choices": [
                {
                    "option": "把唯一的雨伞全倾斜向他",
                    "dialogue_response": [
                        ("流星", "『诶你全给我了那你自己呢……真笨。快过来，靠我近一点，这样才不会淋湿。』"),
                        ("流星", "（一把将你猛地拽进自己怀里，用单薄的外套将你严严实实地护住）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "🌧️ 突发心动：雨夜的心跳共振",
                        "narrative": "狭窄的屋檐下，四周只有哗啦啦的雨声，彼此的心跳声在寂静中显得格外清晰震耳。",
                        "dialogue": ("流星", "“听着雨声，突然觉得如果这条路没有尽头就好了，这样就能一直抱着你。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "抱怨东京的天气真让人头疼",
                    "dialogue_response": [
                        ("流星", "『管他什么暴雨，只要能和你在东京的雨夜多待一会儿，我巴不得雨下得更大点。』"),
                        ("流星", "（唇角勾起一抹坏笑，顺势把下巴搁在你的肩膀上）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "用纸巾帮他擦脸上的雨水",
                    "dialogue_response": [
                        ("流星", "『谢谢……你照顾人的样子，真的让我忍不住想赖在你身边一辈子。』"),
                        ("流星", "（乖乖地任由你擦拭，眼中闪烁着清澈而深情的微光）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 流星·东京塔下：离别前的闪光拥抱",
            "scene": "Location: 标志性的东京塔观景台下 | Time: 21:00 | Atmosphere: 东京塔亮起璀璨夺目的橘红色灯光，夜风微凉，四周游客如织",
            "prologue": "假期即将结束，明早流星就要搭乘航班返回国内。东京塔下耀眼的灯光将两人的影子拉得很长，气氛莫名有些伤感。",
            "dialogue_intro": [
                ("流星", "“可恶的假期怎么过得这么快，明天一走就不知道什么时候才能见到了……”"),
            ],
            "choices": [
                {
                    "option": "看着东京塔的灯光静静不语",
                    "dialogue_response": [
                        ("流星", "『塔再高也没有我的思念高……明天就要回去了，你会不会想我？』"),
                        ("流星", "（声音难得带上了一丝委屈和孩子气，紧紧盯着你的眼睛不放过任何一丝表情）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🗼 突发心动：东京塔下的不舍",
                        "narrative": "巨大的东京塔在夜空中静静矗立，他再也忍不住内心的不舍，张开双臂将你紧紧拥入怀中。",
                        "dialogue": ("流星", "“听好了，不准把我忘了，不然本大爷随时会从大阪飞回来抓你算账！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "拍拍他肩膀：『一路顺风。』",
                    "dialogue_response": [
                        ("流星", "『一句顺风可打发不了我……你得答应跟我天天视频，或者干脆跟我回大阪！』"),
                        ("流星", "（不满地嘟起嘴巴，双手像铁钳一样把你抱得更紧了）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "紧紧抱住他精致的身体",
                    "dialogue_response": [
                        ("流星", "『……犯规。突然这么舍不得我，那我可要考虑为了你留在东京了哦。』"),
                        ("流星", "（身体微微一僵，随后反客为主将你死死圈在怀里，眼底泛起感动的泪光）"),
                    ],
                    "affection": 28,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 流星·跨国终章：小恶魔的异国告白",
            "scene": "Location: 屏幕两端的跨国视频连线（或突如其来的现实重逢） | Time: 20:00 | Atmosphere: 跨越时差的思念，屏幕里闪烁的霓虹与现实中热烈的拥抱交织",
            "prologue": "分开后的日子里，跨国恋的思念如同野草般疯长。直到这一天，手机屏幕里的人突然话锋一转，或者带着一身风尘直接敲响了你的房门。",
            "dialogue_intro": [
                ("流星", "“喂！别看屏幕了，转过头来看看你身后的门吧，笨蛋！”"),
            ],
            "choices": [
                {
                    "option": "接通跨国视频听他深情表白",
                    "dialogue_response": [
                        ("流星", "『听好了，本少爷在日本每一秒都在想你。跨国恋什么的难不倒我，准备好做我的新娘/新郎了吗？』"),
                        ("流星", "（隔着屏幕笑得无比灿烂，眼里闪烁着星光般的笃定与深情）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "假装信号不好逗他着急",
                    "dialogue_response": [
                        ("流星", "『喂喂别挂！我信号好得很……不准开玩笑，我超级认真的喜欢你！』"),
                        ("流星", "（急得在屏幕那头直跺脚，傲娇的小少爷瞬间慌了神）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "突然出现在他面前给个惊喜",
                    "dialogue_response": [
                        ("流星", "『诶？！你怎么突然从屏幕里走到我现实里了……呜哇，太狡猾了，感动得我想哭！』"),
                        ("流星", "（话音未落便不顾一切地扑过来将你紧紧抱住，所有的异国思念在此刻化作最炽热的重逢拥抱）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,
                        "event_title": "💖 专属结局：跨越山海的异国恋契约",
                        "narrative": "东京与异国的时差在这一刻彻底失效，属于你们的恋爱长跑迎来了最甜蜜的终点。",
                        "dialogue": ("流星", "“管他什么东京还是大阪，本大爷这辈子最大的愿望，就是永远跟定你啦！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
"米七": {
        "经纪人": {
            1: {
                "title": "🎬 米七·后台初遇：长腿王子的清纯微笑",
                "scene": "Location: 影视基地艺人专属化妆间 | Time: 13:00 | Atmosphere: 环形化妆镜前亮着柔和的暖光，空气中弥漫着淡淡的定型水气味",
                "prologue": "作为专属经纪人的你推门走进休息室，身材高挑的米七正坐在椅子上翻看剧本，从镜子里看到你的身影，立刻扬起了一个清纯干净的笑容。",
                "dialogue_intro": [
                    ("米七", "“你来啦。我正在认真研究今天的拍摄桥段，随时准备开工哦。”"),
                ],
                "choices": [
                    {
                        "option": "递上剧本：『今天台词背熟了吗，大明星？』",
                        "dialogue_response": [
                            ("米七", "『有你在监督，我怎么敢偷懒呢。不过……如果能得到你的夸奖，背再多台词也值了。』"),
                            ("米七", "（微微倾过身子，清澈的眼眸一眨不眨地望着你，唇角带着温柔的笑意）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.35,
                            "event_title": "📖 突发心动：剧本的秘密",
                            "narrative": "他翻开剧本的某一页，上面竟然全是你平时叮嘱他注意身体的便签纸。",
                            "dialogue": ("米七", "“你看，这些比台词还要重要，我每天都会温习好几遍的。”"),
                            "bonus_affection": 5,
                        },
                    },
                    {
                        "option": "夸奖他身高又拔高了帅气逼人",
                        "dialogue_response": [
                            ("米七", "『谢谢……在身高上虽然赢了，但在你面前我只想做个需要被照顾的弟弟呢。』"),
                            ("米七", "（有些不好意思地揉了揉后颈，随后无辜地眨了眨眼睛）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "提醒他抓紧时间化妆做造型",
                        "dialogue_response": [
                            ("米七", "『遵命！听经纪人大人的话，我马上乖乖去坐好。』"),
                            ("米七", "（动作利索地坐直身子，配合着化妆师开始做造型，目光却一直透过镜子追随着你）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                ],
            },
            2: {
                "title": "🎬 米七·深夜片场：清纯王子的温柔独白",
                "scene": "Location: 搭建了仿古街景的影视棚 | Time: 23:00 | Atmosphere: 夜深人静的片场只剩下零星几盏工作灯，四周静悄悄的",
                "prologue": "深夜的最后一场哭戏终于顺利杀青，米七裹着厚厚的羽绒服朝你走来，额头上还带着细密的汗珠。",
                "dialogue_intro": [
                    ("米七", "（有些疲惫地揉了揉眼睛，走到你身边时自然而然地放轻了声音）"),
                ],
                "choices": [
                    {
                        "option": "看他拍戏到深夜递上热茶",
                        "dialogue_response": [
                            ("米七", "『谢谢你……每次拍戏累的时候，只要转头看到你在场边等我，我就什么疲惫都没了。』"),
                            ("米七", "（双手捧着温热的茶杯，看向你的眼神里满是化不开的柔情）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.4,
                            "event_title": "🍵 突发心动：深夜的暖意",
                            "narrative": "他接过茶杯时，温热的指尖不经意间与你的手背相触，两人同时微微一怔。",
                            "dialogue": ("米七", "“茶很甜，但好像……没有你现在看着我的眼神甜。”"),
                            "bonus_affection": 8,
                        },
                    },
                    {
                        "option": "笑 him 刚才拍哭戏眼睛都红了",
                        "dialogue_response": [
                            ("米七", "『那是因为剧情需要嘛……不过刚才那场戏，我是真的把你代入进去才哭出来的哦。』"),
                            ("米七", "（略带羞涩地抿起唇，耳根在昏暗的灯光下泛起了一抹红晕）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "陪着他一起核对明天的通告",
                        "dialogue_response": [
                            ("米七", "『有你陪在身边的深夜，连冰冷的片场都变得像家一样温暖。』"),
                            ("米七", "（顺势将头轻轻靠在你的肩膀上，安静地听着你念明天的通告安排）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                ],
            },
            3: {
                "title": "☀️ 第二天：阳光洒满的杂志拍摄",
                "scene": "Location: 落地窗采光极佳的摄影棚 | Time: 10:30 | Atmosphere: 灿烂的阳光透过玻璃倾泻而入，空气中浮动着金色的尘埃微粒",
                "prologue": "今天的时尚杂志拍摄主题是“初恋男友”，身穿白色衬衫的米七站在阳光下，长腿优势展露无遗。",
                "dialogue_intro": [
                    ("米七", "（在镜头前换了好几个姿势，突然转头隔着人群精准地锁定 了你）"),
                ],
                "choices": [
                    {
                        "option": "在镜头外挥手帮他找状态",
                        "dialogue_response": [
                            ("米七", "『看到你笑，我刚才摄影师要求的清纯眼神瞬间就到位了，不信你看成片！』"),
                            ("米七", "（摄影师抓拍下了他眼中闪烁的笑意，连连夸赞这个眼神绝了）"),
                        ],
                        "affection": 22,
                        "random_event": {
                            "trigger_rate": 0.3,
                            "event_title": "📸 突发心动：定格的视线",
                            "narrative": "拍摄间隙他快步走到你身边，借着身高优势微微俯下身子。",
                            "dialogue": ("米七", "“今天的拍摄主题虽然是初恋，但在我心里，从始至终都只有你一个人。”"),
                            "bonus_affection": 7,
                        },
                    },
                    {
                        "option": "顺手帮他整理略显凌乱的衬衫领口",
                        "dialogue_response": [
                            ("米七", "『这么近的距离……我的心跳声，你坐在旁边应该能听到吧？』"),
                            ("米七", "（身体瞬间紧绷了一瞬，随后乖乖站在原地任由你整理，呼吸却明显放轻了）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "提醒他收工后记得吃营养餐",
                        "dialogue_response": [
                            ("米七", "『遵命！不过一个人吃多没意思，今晚通告结束后，陪我一起吃好不好？』"),
                            ("米七", "（亮晶晶的眼睛里满是期待，让人完全无法狠心拒绝）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            4: {
                "title": "🎬 米七·休息室密谈：长腿王子的直球告白",
                "scene": "Location: 宽敞安静的VIP休息室 | Time: 15:45 | Atmosphere: 窗外绿树成荫，室内放着舒缓的轻音乐，私密而惬意",
                "prologue": "趁着造型师不在的间隙，米七反锁了休息室的门，迈着长腿几步走到你面前，居高临下地注视着你。",
                "dialogue_intro": [
                    ("米七", "（双手轻轻撑在你座椅两侧的扶手上，将你整个人圈在自己怀里）"),
                ],
                "choices": [
                    {
                        "option": "被他深邃清澈的眼睛盯着看",
                        "dialogue_response": [
                            ("米七", "『别移开视线嘛……我想把你的样子完完整整装进心里，一辈子也不忘。』"),
                            ("米七", "（声音低沉而温柔，磁性的嗓音像是在耳边轻轻呢喃）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.45,
                            "event_title": "💫 突发心动：逐渐靠近的呼吸",
                            "narrative": "看你有些不知所措地红了脸，他忍不住低笑了一声，眼底满是宠溺。",
                            "dialogue": ("米七", "“每次你露出这种表情，我都快要忍不住把心里藏着的话全说出来了。”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "笑问他今天怎么这么粘人",
                        "dialogue_response": [
                            ("米七", "『因为只有在没人的时候，我才敢把对你的喜欢毫无保留地表现出来呀。』"),
                            ("米七", "（有些不好意思地把头埋在你的肩窝处，像只大型犬一样轻轻蹭了蹭）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "摸摸他的头：『乖，快休息吧。』",
                        "dialogue_response": [
                            ("米七", "『被你这样摸头……我真的要被你宠坏了，以后离不开你怎么办。』"),
                            ("米七", "（享受地闭上眼睛，顺从地任由你的手掌落在他的发顶）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            5: {
                "title": "🎬 米七·突发危机：红毯前的突发暴雨",
                "scene": "Location: 户外大型颁奖典礼红毯后台入口处 | Time: 17:30 | Atmosphere: 天空乌云密布下起倾盆大雨，现场工作人员乱成一团",
                "prologue": "年度时尚盛典的红毯前夕，突如其来的暴雨打乱了入场秩序。米七刚下保姆车，就赶忙撑起大伞护在你头顶。",
                "dialogue_intro": [
                    ("米七", "“快到我伞下来！别管我的衣服了，你淋湿了怎么办？”"),
                ],
                "choices": [
                    {
                        "option": "迅速递上毛巾帮他擦拭湿发",
                        "dialogue_response": [
                            ("米七", "『谢谢你……在镜头前护着我、帮我整理狼狈样子的你，真的帅气得让我心动。』"),
                            ("米七", "（顺从地微微弯腰配合你的高度，眼神深邃得仿佛要将你吸进去）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.5,
                            "event_title": "🌧️ 突发心动：雨中的坚定守护",
                            "narrative": "闪光灯在雨幕中疯狂闪烁，他却在镜头拍不到的盲区，紧紧握住了你冰凉的手。",
                            "dialogue": ("米七", "“奖杯对我来说不重要，只要你在我身边，就是我今天拿到的最大荣誉。”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "安慰他不要担心造型受影响",
                        "dialogue_response": [
                            ("米七", "『造型无所谓，我只担心你淋雨着凉……只要你没事，今天的红毯我拿不拿奖都无所谓。』"),
                            ("米七", "（毫不犹豫地把大半个身子和伞都倾斜到你那边，自己肩膀湿了一片也浑然不觉）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "坚定地牵起他的手往会场跑",
                        "dialogue_response": [
                            ("米七", "『嗯！只要和你手牵手，哪怕暴雨再大，我也敢勇敢往前冲。』"),
                            ("米七", "（反手将你的手牢牢包裹在掌心里，迈开长腿护着你冲进灯光璀璨的会场）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            6: {
                "title": "🎬 米七·完美谢幕：长腿王子的专属契约",
                "scene": "Location: 庆功宴后的私人江景露台 | Time: 23:30 | Atmosphere: 满天繁星与城市夜景交相辉映，江风徐徐吹拂，浪漫而静谧",
                "prologue": "随着米七主演的新剧全网大爆，庆功宴也圆满落下帷幕。夜深人静的露台上，他拿着一杯果汁走到你身旁，眼神里满是化不开的炽热深情。",
                "dialogue_intro": [
                    ("米七", "“今天可以说是双喜临门呢，不过……我最想要的庆祝方式，只有一种。”"),
                ],
                "choices": [
                    {
                        "option": "微笑着祝贺他新剧大爆红",
                        "dialogue_response": [
                            ("米七", "『谢谢！但比起剧本大爆，我更想要一份跟你绑定一辈子的长期专属契约。』"),
                            ("米七", "（郑重其事地放下杯子，从口袋里掏出一个精致的小盒子，单膝半跪在你面前）"),
                        ],
                        "affection": 35,
                        "random_event": None,
                    },
                    {
                        "option": "假装嫌弃他太会说情话",
                        "dialogue_response": [
                            ("米七", "『这可不是台词哦，句句发自肺腑。不信，你听听我到现在还在为你狂跳的心。』"),
                            ("米七", "（拉起你的手轻轻按在他的左胸口处，隔着衬衫能感受到那里强烈而急促的心跳）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "温柔地靠在他宽阔的肩膀上",
                        "dialogue_response": [
                            ("米七", "『好，以后你的每一部戏，我都做你唯一的专属女主角/男主角。』"),
                            ("米七", "（眼底瞬间迸发出惊喜的光芒，随后紧紧将你拥入怀中，仿佛拥有了全世界）"),
                        ],
                        "affection": 35,
                        "random_event": {
                            "trigger_rate": 1.0,
                            "event_title": "🌟 专属结局：长腿王子的终身独家签约",
                            "narrative": "远处的江面上恰好绽放起一朵绚丽的晚间烟花，将两人的拥抱镀上一层金色的光晕。",
                            "dialogue": ("米七", "“从今以后，我的星途璀璨由你见证，而我的整颗心，永远只为你一个人独家营业！”"),
                            "bonus_affection": 15,
                        },
                    },
                ],
            },
        },
    },
"青梅竹马": {
        1: {
            "title": "🎬 米七·放学路：长腿竹马的温柔陪伴",
            "scene": "Location: 铺满夕阳余晖的放学林荫小道 | Time: 17:15 | Atmosphere: 两侧是摇曳的梧桐树叶，空气中弥漫着青草与单车铃清脆的响声",
            "prologue": "放学回家的路上，身材高挑的米七总是会特意放慢脚步，耐心地配合着你的步调，手里还拎着刚买的零食。",
            "dialogue_intro": [
                ("米七", "“今天作业有点多，累了吧？走慢一点，我陪你慢慢晃回家。”"),
            ],
            "choices": [
                {
                    "option": "抱怨他腿太长走路太快",
                    "dialogue_response": [
                        ("米七", "『那我放慢脚步等你好啦……谁叫你每次都走得慢吞吞的，真拿你没办法。』"),
                        ("米七", "（无奈又宠溺地笑了一下，脚步真的配合着放得更慢了）"),
                    ],
                    "affection": 20,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "🍦 突发心动：夏日的冰淇淋",
                        "narrative": "路过街角便利店时，他熟练地买了两支你最爱的草莓冰淇淋递过来。",
                        "dialogue": ("米七", "“呐，奖励辛苦写作业的某人，吃一口心情就会变好哦。”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "买了两支草莓冰淇淋分他一只",
                    "dialogue_response": [
                        ("米七", "『哇，最喜欢你买的冰淇淋了！从小到大，你总是这么懂我。』"),
                        ("米七", "（开心地接过来咬了一口，眼睛亮晶晶地看向你）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "拍拍他肩膀：『长高了不起哦！』",
                    "dialogue_response": [
                        ("米七", "『长高是为了能更好地保护你呀，你看，现在遮阳伞全挡在你头顶了哦。』"),
                        ("米七", "（顺势将手中的伞往你那边倾斜了大半，自己半边肩膀露在外面却浑然不觉）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 米七·秘密基地：天台上的清纯心事",
            "scene": "Location: 老旧教学楼的顶楼天台 | Time: 17:50 | Atmosphere: 橙红色的晚霞铺满天际，微风吹拂着校服衣角，安静而私密",
            "prologue": "夕阳下，两人并肩坐在天台的边缘。米七望着远处的城市天际线，向你倾诉着他对未来的青涩梦想。",
            "dialogue_intro": [
                ("米七", "（转过头认真地凝视着你，眼底闪烁着少年的坚毅与温柔）"),
            ],
            "choices": [
                {
                    "option": "听他讲对未来的种种憧憬",
                    "dialogue_response": [
                        ("米七", "『不管以后我走得多远、站得多高，我身边的那个位置永远只为你一个人留着。』"),
                        ("米七", "（语气坚定而温柔，仿佛许下了一个不会改变的少年承诺）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🍱 突发心动：便当盒里的秘密",
                        "narrative": "他突然有些不好意思地打开便当盒，里面是你最爱吃的煎蛋。",
                        "dialogue": ("米七", "“其实……今天特意跟妈妈学做的，你尝尝看味道合不合心意？”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "笑他小时候哭鼻子的糗事",
                    "dialogue_response": [
                        ("米七", "『诶！那都是陈年旧事了怎么还提！……好啦，在你面前我从来就没有秘密。』"),
                        ("米七", "（羞恼地红了耳尖，随后无奈地笑出声来，抬手轻轻揉了揉你的头发）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "把便当里的煎蛋分给他",
                    "dialogue_response": [
                        ("米七", "『真好吃！有你这个青梅竹马在，我每天都觉得自己是世界上最幸福的人。』"),
                        ("米七", "（满足地弯起眼睛，脸上露出干净清纯的笑容）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：晨光中的单车少年",
            "scene": "Location: 洒满清晨阳光的上学单车道 | Time: 07:40 | Atmosphere: 清晨微凉的晨风，单车轮毂转动的沙沙声，充满青春气息的街道",
            "prologue": "清晨的第一缕阳光洒在单车后座上，米七骑着自行车载着你穿梭在梧桐树荫下，早晨的空气里带着淡淡的青草香。",
            "dialogue_intro": [
                ("米七", "“坐稳咯！前面的路有点颠簸，抓紧我的衣角哦。”"),
            ],
            "choices": [
                {
                    "option": "坐在单车后座抓紧他的衣角",
                    "dialogue_response": [
                        ("米七", "『抓紧咯！清晨的风有点凉，把手塞进我口袋里会暖和一点哦。』"),
                        ("米七", "（单手骑着车，微微侧过身将外套口袋的方向朝向你，耳根有些微微泛红）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🚲 突发心动：单车后座的悸动",
                        "narrative": "自行车缓缓停在红绿灯路口，他回过头确认你有没有坐稳，眼神里满是掩饰不住的关切。",
                        "dialogue": ("米七", "“要是累了就靠在我背上休息一会儿，反正这条路还很长。”"),
                        "bonus_affection": 7,
                    },
                },
                {
                    "option": "抱怨他车技太稳像散步",
                    "dialogue_response": [
                        ("米七", "『安全第一嘛，我可舍不得让你在单车后座受到一点颠簸。』"),
                        ("米七", "（理直气壮地笑着回答，脚下的踩踏速度却悄悄放慢了许多）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
                {
                    "option": "安静地享受微风和他的背影",
                    "dialogue_response": [
                        ("米七", "『看着你的背影，突然希望这条上学路永远没有尽头。』"),
                        ("米七", "（似乎听到了你的低语，单薄的脊背微微一僵，随即唇角扬起了一个大大的弧度）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
            ],
        },
        4: {
            "title": "🎬 米七·文化祭后台：清纯少年的直球羞涩",
            "scene": "Location: 热闹喧嚣的校园礼堂后台化妆间 | Time: 14:30 | Atmosphere: 舞台剧道具的油漆味与服装的香气交织，空气里满是青春的躁动",
            "prologue": "校园文化祭的话剧即将开演，身穿王子礼服的米七站在镜子前反复整理着领结，看到你走进来立刻有些手足无措起来。",
            "dialogue_intro": [
                ("米七", "“你来得正好……帮我看看这个领结有没有系歪？”"),
            ],
            "choices": [
                {
                    "option": "帮他整理话剧演出的王子礼服",
                    "dialogue_response": [
                        ("米七", "『这身衣服好正式……不过，在台下看着你的我，眼里根本容不下其他任何人。』"),
                        ("米七", "（乖乖低头配合着你的动作，近得连彼此的呼吸声都能清晰听见）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "👑 突发心动：王子礼服的秘密",
                        "narrative": "你帮他整理好衣领后忍不住笑了一下，他红着脸将一束刚从道具组拿来的玫瑰花塞进你怀里。",
                        "dialogue": ("米七", "“台上的王子虽然是演的，但我对你的喜欢绝对货真价实。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "开玩笑说他演王子毫无违和感",
                    "dialogue_response": [
                        ("米七", "『那公主殿下/骑士大人，今晚的庆功宴你愿意赏脸只陪我一个人吗？』"),
                        ("米七", "（顺势弯起眼睛笑了起来，清纯帅气的模样惹得后台好几个女生频频侧目）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "递上一瓶润喉糖：『快上台了。』",
                    "dialogue_response": [
                        ("米七", "『谢谢你……有你的鼓励，我的台词绝对一个字都不会忘。』"),
                        ("米七", "（小心翼翼地剥开一颗糖塞进嘴里，看向你的眼神像装了整个星空）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 米七·烟花大会：月光下的怦然心动",
            "scene": "Location: 视野开阔的河堤边草坪 | Time: 20:30 | Atmosphere: 夜空中接连绽放的绚丽烟花，空气里满是夏夜的温热与悸动",
            "prologue": "夏日烟花大会的人潮中，米七紧紧护着你的手生怕把你走散。当第一朵巨大的烟花在夜空中炸裂时，他突然停下了脚步。",
            "dialogue_intro": [
                ("米七", "（转过身借着绚丽的烟花光芒，深深地凝视着你的双眼）"),
            ],
            "choices": [
                {
                    "option": "抬头看绚烂绽放的夏日烟火",
                    "dialogue_response": [
                        ("米七", "『烟花很美，但我的目光一刻也舍不得从你脸上移开。你比烟花还耀眼。』"),
                        ("米七", "（声音温柔得仿佛要滴出水来，借着烟花声悄悄将藏了多年的真心吐露）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "🎆 突发心动：烟火下的拥抱",
                        "narrative": "身边突然有人跑过差点撞到你，他眼疾手快地一把将你拉进怀里，心跳声震耳欲聋。",
                        "dialogue": ("米七", "“别怕，我在呢。以后每个夏天的烟花，我都陪你一起看。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "被烟花声音吓了一跳躲进他怀里",
                    "dialogue_response": [
                        ("米七", "『别怕，我在呢。以后每个夏天的烟花，我都陪你一起看。』"),
                        ("米七", "（顺势张开双手将你稳稳护在怀里，眼底满是失而复得般的温柔与坚定）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "温柔地握住他的手掌",
                    "dialogue_response": [
                        ("米七", "『手好冰……从今天起，青梅竹马的关系正式升级，做我女朋友/男朋友好不好？』"),
                        ("米七", "（反手将你的手紧紧反握在掌心里，趁着夜色鼓起勇气说出了那句告白）"),
                    ],
                    "affection": 28,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 米七·告白终章：长腿王子的完美蜕变",
            "scene": "Location: 见证两人长大的老街路口 | Time: 21:40 | Atmosphere: 昏黄温暖的路灯光晕将影子拉得很长，空气中弥漫着完美的结局气息",
            "prologue": "青梅竹马的终点线前，米七终于不再掩饰眼底汹涌的爱意。在熟悉的路灯下，他郑重地向你递出了余生的专属契约。",
            "dialogue_intro": [
                ("米七", "“从小到大陪在我身边的人一直都是你……这一次，换我来做照顾你一辈子的那个人好不好？”"),
            ],
            "choices": [
                {
                    "option": "红着脸答应他的温柔表白",
                    "dialogue_response": [
                        ("米七", "『太好了……我终于能光明正大地牵着你的手，向全世界宣布你是我的了！』"),
                        ("米七", "（高兴得像个得到全世界糖果的孩子，一把将你高高抱起转了个圈）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "靠在他肩膀上笑出声",
                    "dialogue_response": [
                        ("米七", "『笑什么？我是认真的，从青梅到恋人，余生请多多指教啦！』"),
                        ("米七", "（宠溺地捏了捏你的脸颊，随后将你拥入一个温暖坚实的怀抱中）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "十指相扣奔向幸福未来",
                    "dialogue_response": [
                        ("米七", "『走吧，我们的青春剧本，从这一秒开始正式进入最甜的篇章！』"),
                        ("米七", "（十指紧扣，牵着你大步流星地朝着属于两人的幸福未来走去）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,
                        "event_title": "💍 专属结局：青梅竹马的终身契约",
                        "narrative": "路灯将两人的影子重叠在一起，这一刻，所有的年少欢喜终于迎来了最完美的圆满。",
                        "dialogue": ("米七", "“从青梅到白头，本少爷这辈子最大的幸运，就是从小到大喜欢的人一直都是你！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
"在日留学生or打工人": {
        1: {
            "title": "🎬 米七·异国图书馆：清纯王子的安静偶遇",
            "scene": "Location: 东京某大学静谧宽敞的中央图书馆 | Time: 15:00 | Atmosphere: 窗外飘着细碎的冬雪，室内弥漫着旧书纸张的淡淡香气，四周安静得只能听见翻书声",
            "prologue": "在东京独自求学/打拼的你正埋头查阅资料，身旁突然多了一道高挑清瘦的身影。米七手里拿着一本厚厚的外语文献，略显苦恼地向你投来求助的目光。",
            "dialogue_intro": [
                ("米七", "“那个……不好意思打扰一下，请问这本馆藏的外语参考书，你知道在哪里能找到吗？”"),
            ],
            "choices": [
                {
                    "option": "递给他一本找不到的外语参考书",
                    "dialogue_response": [
                        ("米七", "『哇，太谢谢你了！在东京图书馆正发愁呢，遇到你简直像天使降临。』"),
                        ("米七", "（双手接过书本，清澈的眼眸里闪烁着惊喜与感激的光芒）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.35,
                        "event_title": "☕ 突发心动：热可可的温度",
                        "narrative": "走出图书馆时天空飘起小雪，他顺手从旁边的自动贩卖机买了两罐热可可塞进你手里。",
                        "dialogue": ("米七", "“东京的冬天虽然冷，但能在这里遇见你，突然觉得好温暖。”"),
                        "bonus_affection": 5,
                    },
                },
                {
                    "option": "用关西腔小声打招呼",
                    "dialogue_response": [
                        ("米七", "『哈哈，异国他乡听到这个口音好亲切！能陪我在东京街头走走吗？』"),
                        ("米七", "（原本紧绷的肩膀瞬间放松下来，露出了一个干净帅气的笑容）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "请他喝了一罐自动贩卖机的热可可",
                    "dialogue_response": [
                        ("米七", "『甜到心里去了，东京的冬天虽然冷，但因为有你突然觉得好温暖。』"),
                        ("米七", "（双手捧着温热的铁罐，目光柔和地注视着你）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        2: {
            "title": "🎬 米七·深夜电车站：打工人的温情守候",
            "scene": "Location: 东京深夜空旷的JR电车站台 | Time: 23:45 | Atmosphere: 末班车前的冷风呼啸而过，站台广告牌闪烁着清冷的荧光",
            "prologue": "刚结束了一整天兼职宣传海报拍摄的米七，疲惫地拖着长腿来到电车站。看到等在一旁的你，他眼底的倦意瞬间化为了温柔。",
            "dialogue_intro": [
                ("米七", "（有些疲惫地靠在站台的柱子上，朝着你无奈地笑了一下）"),
            ],
            "choices": [
                {
                    "option": "看他拍完兼职宣传海报累得靠在柱子上",
                    "dialogue_response": [
                        ("米七", "『辛苦啦，末班车快来了，靠在我肩膀上休息一会儿吧。』"),
                        ("米七", "（顺从地将头轻轻靠在你的肩膀上，贪恋着这片刻属于两人的安宁）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.4,
                        "event_title": "🍙 突发心动：深夜的家乡味",
                        "narrative": "他肚子不争气地叫了一声，你笑着从包里拿出一个还带着余温的饭团递过去。",
                        "dialogue": ("米七", "“太好吃了……在东京独自打拼的日子里，你的饭团是我吃过最美味的珍馐。”"),
                        "bonus_affection": 8,
                    },
                },
                {
                    "option": "分给他半块从家里带来的饭团",
                    "dialogue_response": [
                        ("米七", "『太好吃了……在东京独自打拼的日子里，你的饭团是我吃过最美味的珍馐。』"),
                        ("米七", "（小口小口地吃着，原本黯淡的眼神重新亮起了光彩）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "提醒他注意末班车时间",
                    "dialogue_response": [
                        ("米七", "『误了末班车也没关系，因为我想在这座城市的夜色里多待一会儿。』"),
                        ("米七", "（修长的手指轻轻勾住你的衣角，眼神里满是舍不得离开的留恋）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        3: {
            "title": "☀️ 第二天：东京塔下的晴空漫步",
            "scene": "Location: 阳光正好、微风不燥的东京塔下草坪 | Time: 13:30 | Atmosphere: 晴空万里，标志性的红色东京塔高耸入云，周围游人如织",
            "prologue": "难得的休息日，两人相约来到东京塔下散步。阳光洒在米七高挑挺拔的身影上，宛如从漫画里走出来的清纯男主角。",
            "dialogue_intro": [
                ("米七", "（转过身张开双臂，以宏伟的东京塔为背景冲你扬起灿烂的笑容）"),
            ],
            "choices": [
                {
                    "option": "帮他拍一张以东京塔为背景的照片",
                    "dialogue_response": [
                        ("米七", "『把我拍得帅一点哦……不过，这张照片以后绝对是我最珍贵的传家宝。』"),
                        ("米七", "（凑过头来看你手机里的成片，满意地弯起眼睛笑了起来）"),
                    ],
                    "affection": 22,
                    "random_event": {
                        "trigger_rate": 0.3,
                        "event_title": "🍦 突发心动：甜品店的巧合",
                        "narrative": "路过限定甜品店时，两人异口同声地买下了两份抹茶冰淇淋。",
                        "dialogue": ("米七", "“东京的甜品虽然精致，但感觉还是跟你一起吃的最有味道。”"),
                        "bonus_affection": 7,
                    },
                },
                {
                    "option": "顺路买了两份抹茶冰淇淋",
                    "dialogue_response": [
                        ("米七", "『东京的甜品虽然精致，但感觉还是跟你一起吃的最有味道。』"),
                        ("米七", "（开心地接过来尝了一口，满足得像只大型犬）"),
                    ],
                    "affection": 25,
                    "random_event": None,
                },
                {
                    "option": "提醒他看路口的红绿灯",
                    "dialogue_response": [
                        ("米七", "『遵命！只要牵着你的手，在东京再大的十字路口我也绝不会迷路。』"),
                        ("米七", "（顺势牢牢牵住你的手掌，十指紧扣着迈过人行横道）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        4: {
            "title": "🎬 米七·暴雨突袭：屋檐下的清纯心跳",
            "scene": "Location: 东京街头复古的日式木造屋檐下 | Time: 17:00 | Atmosphere: 突如其来的大雨笼罩了整个街道，四周水汽弥漫，空气冰凉而安静",
            "prologue": "一场毫无预兆的东京暴雨将两人困在街边屋檐下。看着被风吹得微微发抖的你，米七二话不说解下了自己的围巾。",
            "dialogue_intro": [
                ("米七", "（有些笨拙却极其温柔地把长长的羊毛围巾圈在你脖子上）"),
            ],
            "choices": [
                {
                    "option": "把唯一的围巾分他一半围上",
                    "dialogue_response": [
                        ("米七", "『好暖……不仅是围巾，连我的心都被你塞得满满当当的，再也不觉得冷了。』"),
                        ("米七", "（顺势微微倾身和你共用一条围巾，两人的距离近得连呼吸都交织在一起）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.45,
                        "event_title": "☂️ 突发心动：雨幕中的对视",
                        "narrative": "雨滴顺着屋檐滴落发出清脆的声响，他情不自禁地抬手帮你拨开额前湿漉漉的碎发。",
                        "dialogue": ("米七", "“那我们就是这部纯爱电影里最幸福的主角，结局必须是永远在一起。”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "开玩笑说像纯爱电影里的画面",
                    "dialogue_response": [
                        ("米七", "『那我们就是这部电影里最幸福的主角，结局必须是永远在一起。』"),
                        ("米七", "（眼底泛起认真的光芒，目光一瞬不瞬地锁在你身上）"),
                    ],
                    "affection": 22,
                    "random_event": None,
                },
                {
                    "option": "安静地听着雨声打在伞面上",
                    "dialogue_response": [
                        ("米七", "『有你在身边挡风雨，东京下多久的暴雨我都不害怕。』"),
                        ("米七", "（将伞往你那边倾斜了绝大部分，自己半边肩膀湿透也毫无察觉）"),
                    ],
                    "affection": 20,
                    "random_event": None,
                },
            ],
        },
        5: {
            "title": "🎬 米七·归国倒计时：离别前的深情拥抱",
            "scene": "Location: 可以俯瞰东京全景的高层观景台露台 | Time: 21:00 | Atmosphere: 璀璨的东京霓虹夜景在脚下蔓延，空气中弥漫着即将离别的淡淡伤感",
            "prologue": "随着米七在国内的演艺通告和出道行程敲定，他在东京的留学生/打工生涯即将画上句号。面对即将到来的异国离别，两人在观景台上久久无言。",
            "dialogue_intro": [
                ("米七", "（双手插兜遥望着远处闪烁的东京塔，声音有些沙哑和不舍）"),
            ],
            "choices": [
                {
                    "option": "看着远处的夜景依依不舍",
                    "dialogue_response": [
                        ("米七", "『明天就要回国了……真的好舍不得你。你会不会把我在东京忘了？』"),
                        ("米七", "（转过头委屈巴巴地看着你，清纯的眼眶微微泛红）"),
                    ],
                    "affection": 25,
                    "random_event": {
                        "trigger_rate": 0.5,
                        "event_title": "✈️ 突发心动：机场前的生死契约",
                        "narrative": "他突然一把将你紧紧拥入怀中，宽阔的胸膛带着滚烫的温度。",
                        "dialogue": ("米七", "“一句联系不够……你得答应我，等我成功出道，一定会第一时间回来娶你/嫁你！”"),
                        "bonus_affection": 10,
                    },
                },
                {
                    "option": "拍拍他肩膀：『放心吧，随时联系。』",
                    "dialogue_response": [
                        ("米七", "『一句联系不够……你得答应我，等我成功出道，一定会第一时间回来娶你/嫁你！』"),
                        ("米七", "（语气前所未有的认真与执着，双手紧紧握住你的肩膀）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "紧紧拥抱住他清瘦的身体",
                    "dialogue_response": [
                        ("米七", "『……犯规。被你这么一抱，我真恨不得立刻放弃行程留在东京陪你。』"),
                        ("米七", "（叹了口气反手将你揉进怀里，力道大得仿佛要把你嵌进骨血里）"),
                    ],
                    "affection": 28,
                    "random_event": None,
                },
            ],
        },
        6: {
            "title": "🎬 米七·异国终章：长腿王子的跨国告白",
            "scene": "Location: 国内璀璨灯光下的机场到达大厅 / 跨国视频连线屏幕两侧 | Time: 20:00 | Atmosphere: 闪光灯与欢呼声交织，空气中充满梦想实现与爱情圆满的喜悦",
            "prologue": "米七回国顺利出道并斩获超高人气后，在一次深夜的跨国连线（或惊喜现身）中，向一直默默支持他的你发起了最终的爱情宣告。",
            "dialogue_intro": [
                ("米七", "（对着镜头/站在你面前，眼底闪烁着星光，笑得温柔而笃定）"),
            ],
            "choices": [
                {
                    "option": "接通跨国视频听他深情表白",
                    "dialogue_response": [
                        ("米七", "『听好了，我在国内每一秒都在想你。跨国恋根本不算什么，准备好做我的新娘/新郎了吗？』"),
                        ("米七", "（隔着屏幕深情款款地单膝下跪，举起了一枚早已准备好的钻戒）"),
                    ],
                    "affection": 35,
                    "random_event": None,
                },
                {
                    "option": "假装信号不好逗他着急",
                    "dialogue_response": [
                        ("米七", "『喂喂别挂！我信号好得很……不准开玩笑，我超级认真的喜欢你！』"),
                        ("米七", "（急得差点从椅子上站起来，看你笑出声才无奈地宠溺摇头）"),
                    ],
                    "affection": 30,
                    "random_event": None,
                },
                {
                    "option": "突然提着行李箱出现在他门口",
                    "dialogue_response": [
                        ("米七", "『诶？！你怎么突然从视频里走到我现实里了……呜哇，太狡猾了，感动得我想哭！』"),
                        ("米七", "（震惊过后瞬间红了眼眶，扔下通告单大步流星地冲过来将你紧紧抱起）"),
                    ],
                    "affection": 35,
                    "random_event": {
                        "trigger_rate": 1.0,
                        "event_title": "🌟 专属结局：跨越山海的终身独家限定",
                        "narrative": "东京的雪与国内的星光在这一刻完美交融，所有的异国思念终于化作了永恒的相守。",
                        "dialogue": ("米七", "“从东京的寒冬到国内的顶峰，我这辈子最幸运的事，就是异国他乡的每一步都有你相伴，余生我们再也不分开！”"),
                        "bonus_affection": 15,
                    },
                },
            ],
        },
    },
"谦杜": {
        "经纪人": {
            1: {
                "title": "🎬 谦杜·后台初遇：时尚末子的个性开场",
                "scene": "Location: 潮流音乐节后台化妆间 | Time: 14:00 | Atmosphere: 环形镜前挂满了各类先锋潮牌衣物，空气中弥漫着淡淡的香水味",
                "prologue": "作为专属经纪人的你推门而入，顶着一头个性挑染、身穿叠穿潮服的谦杜正对着镜子整理耳饰，通过镜子斜睨了你一眼。",
                "dialogue_intro": [
                    ("谦杜", "“来啦。看看我今天的这套Look怎么样，是不是走在时尚最前沿？”"),
                ],
                "choices": [
                    {
                        "option": "夸奖他今天私服穿搭很有潮感",
                        "dialogue_response": [
                            ("谦杜", "『那当然！本少爷对时尚可是很有要求的。不过……能得到你的夸奖，说明你眼光也不赖嘛！』"),
                            ("谦杜", "（极其自信地扬了扬下巴，嘴角勾起一抹玩世不恭又带着点小得意的高傲笑容）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.35,
                            "event_title": "☕ 突发心动：冰咖啡的默契",
                            "narrative": "你顺手把刚买的冰咖啡递过去，他自然地接住，指尖不经意间与你相碰。",
                            "dialogue": ("谦杜", "“太懂我了吧！今天一整天的时尚灵感全靠你这杯冰咖啡来激活了。”"),
                            "bonus_affection": 5,
                        },
                    },
                    {
                        "option": "提醒他别把通告时间给搞混了",
                        "dialogue_response": [
                            ("谦杜", "『怎么会呢，我有认真看日程表的好不好……好啦，听你的就是了，经纪人大人！』"),
                            ("谦杜", "（略带无奈地撇了撇嘴，随后乖乖把通告单塞进口袋里）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "递上一杯冰咖啡提神",
                        "dialogue_response": [
                            ("谦杜", "『太懂我了吧！今天一整天的时尚灵感全靠你这杯冰咖啡来激活了。』"),
                            ("谦杜", "（利落地插上吸管喝了一口，眼睛亮晶晶地看向你）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                ],
            },
            2: {
                "title": "🎬 谦杜·深夜设计室：末子的时尚执着",
                "scene": "Location: 专属工作室的满墙设计手稿前 | Time: 23:30 | Atmosphere: 暖黄色的台灯光线，桌上散落着布料样品和马克笔，安静而专注",
                "prologue": "深夜的工作室里，谦杜依然趴在桌上修改下一场打歌服的服装草图。听到你的脚步声，他才懒洋洋地伸了个懒腰。",
                "dialogue_intro": [
                    ("谦杜", "（转过转椅，把手里的速写本举到你面前晃了晃）"),
                ],
                "choices": [
                    {
                        "option": "看他深夜还在设计打歌服草图",
                        "dialogue_response": [
                            ("谦杜", "『你看这个剪裁怎么样？我想把最好的舞台服呈献给大家……当然，最想看你穿上我设计的衣服。』"),
                            ("谦杜", "（眨了眨亮晶晶的眼睛，满脸写着“快夸我”的傲娇期待）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.4,
                            "event_title": "🧥 突发心动：专属定制的偏爱",
                            "narrative": "他突然起身把一件刚做好的小夹克披在你肩上，离得极近。",
                            "dialogue": ("谦杜", "“这可是全世界独一件的非卖品，只留给本少爷最在意的人。”"),
                            "bonus_affection": 8,
                        },
                    },
                    {
                        "option": "劝他别太拼快去睡觉",
                        "dialogue_response": [
                            ("谦杜", "『好啦好啦，听你的总行了吧。不过你得陪我聊会儿天，不然我可不睡。』"),
                            ("谦杜", "（顺势耍赖般地拉住你的衣角，像只寻求关注的小狮子）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "夸奖他年纪轻轻设计天赋惊人",
                        "dialogue_response": [
                            ("谦杜", "『那是，本末子可是要引领潮流的人。不过在你面前，我只想做个听话的男友/女友。』"),
                            ("谦杜", "（耳尖微微泛红，却依旧嘴硬地扬起骄傲的下巴）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                ],
            },
            3: {
                "title": "☀️ 第二天：演唱会服装间的突击",
                "scene": "Location: 巨型体育馆的后台服装间 | Time: 15:20 | Atmosphere: 密密麻麻的演出服挂在两侧，工作人员来来往往，充满紧凑的筹备感",
                "prologue": "演唱会开场前的最后一次服装检查，谦杜正站在试衣镜前，身上挂满了各种前卫的金属链条配饰。",
                "dialogue_intro": [
                    ("谦杜", "（张开双臂配合着造型调整，眼神却透过镜子直勾勾地盯着你）"),
                ],
                "choices": [
                    {
                        "option": "帮他调整外套的金属链条配饰",
                        "dialogue_response": [
                            ("谦杜", "『这么近……你身上的味道好好闻，搞得我设计灵感全变成你的名字了。』"),
                            ("谦杜", "（微微低头配合你的动作，唇角勾起一抹坏笑，心脏却在胸腔里剧烈跳动）"),
                        ],
                        "affection": 22,
                        "random_event": {
                            "trigger_rate": 0.3,
                            "event_title": "⛓️ 突发心动：金属与心跳的碰撞",
                            "narrative": "冰凉的金属链条在你指尖晃动，他反手轻轻握住了你的手腕。",
                            "dialogue": ("谦杜", "“别动，让我感受一下你手心的温度，上台前紧张的心情瞬间就被治愈了。”"),
                            "bonus_affection": 7,
                        },
                    },
                    {
                        "option": "吐槽他挂件配饰实在太多了",
                        "dialogue_response": [
                            ("谦杜", "『这叫层次感懂不懂！不过……如果你不喜欢，我马上全摘下来。』"),
                            ("谦杜", "（虽然嘴上反驳，手却真的作势要去解开那些闪闪发光的配饰）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                    {
                        "option": "递上矿泉水润喉",
                        "dialogue_response": [
                            ("谦杜", "『谢谢你……有你在后台盯着，我上台走秀的自信心直接拉满！』"),
                            ("谦杜", "（大口喝了半瓶水，眼神重新变得神采奕奕、光芒四射）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                ],
            },
            4: {
                "title": "🎬 谦杜·休息室密谈：时尚末子的直球进攻",
                "scene": "Location: 独立VIP休息室的沙发区 | Time: 18:00 | Atmosphere: 柔和的落地窗外是渐暗的暮色，室内放着轻快的R&B音乐",
                "prologue": "趁着中场休息的空档，谦杜一把拉着你坐在沙发上，将刚搜集到的全球最新时尚杂志直接拍在桌面上。",
                "dialogue_intro": [
                    ("谦杜", "“喂，别看手机了，快来看看这个季度的流行趋势，本少爷带你走在潮流尖端。”"),
                ],
                "choices": [
                    {
                        "option": "被他拉着讨论最新流行趋势",
                        "dialogue_response": [
                            ("谦杜", "『流行趋势天天变，但我对你的喜欢永远保鲜，而且只增不减哦！』"),
                            ("谦杜", "（突然毫无预兆地凑近，用那双亮晶晶的眼睛直视着你的双眼）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.45,
                            "event_title": "💫 突发心动：沙发角落的对峙",
                            "narrative": "他顺势将胳膊撑在沙发靠背上，将你整个人圈在自己和沙发之间，动弹不得。",
                            "dialogue": ("谦杜", "“没想什么呀，满脑子都是怎么才能把你变成我的专属模特……一辈子那种。”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "笑骂他小脑袋瓜整天想什么呢",
                        "dialogue_response": [
                            ("谦杜", "『没想什么呀，满脑子都是怎么才能把你变成我的专属模特。』"),
                            ("谦杜", "（有些羞恼地轻哼了一声，双手抱胸摆出一副傲娇又无赖的表情）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "轻轻敲了他额头一下",
                        "dialogue_response": [
                            ("谦杜", "『痛！……不过如果是你敲的，多敲几下也没关系。』"),
                            ("谦杜", "（立刻捂住额头装出一副可怜兮兮的样子，眼底却盛满了藏不住的笑意）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            5: {
                "title": "🎬 谦杜·突发危机：打歌服拉链突然坏了",
                "scene": "Location: 侧台狭窄的应急换衣间 | Time: 20:15 | Atmosphere: 舞台上音乐声震耳欲聋，后台工作人员乱成一团，气氛极度紧张",
                "prologue": "距离下半场登场还有不到两分钟，谦杜昂贵的先锋夹克后背拉链竟然卡住裂开了一个大口子，急得他直皱眉头。",
                "dialogue_intro": [
                    ("谦杜", "“靠，这什么破质量！马上要上台了这可怎么办……”"),
                ],
                "choices": [
                    {
                        "option": "临危不乱迅速帮他缝好拉链",
                        "dialogue_response": [
                            ("谦杜", "『哇……你简直是我的救世主！动作这么利落，帅得让我忍不住想以身相许了。』"),
                            ("谦杜", "（震惊又崇拜地看着你三两下解决危机，眼睛里简直要冒出小星星）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.5,
                            "event_title": "⚡ 突发心动：后台的紧急救援",
                            "narrative": "危机解除的瞬间，他反手一把抓住你的手腕，带着狂喜和后怕。",
                            "dialogue": ("谦杜", "“意外嘛意外！不过多亏有你在身边的安全感，不然我今天肯定出大丑。今晚庆功宴必须听我的！”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "笑他平时粗心大意关键时刻掉链子",
                        "dialogue_response": [
                            ("谦杜", "『意外嘛意外！不过多亏有你在身边的安全感，不然我今天肯定出大丑。』"),
                            ("谦杜", "（有些不好意思地摸了摸鼻子，随后感激地冲你用力点了点头）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "坚定地拍拍他肩膀：『上台加油！』",
                        "dialogue_response": [
                            ("谦杜", "『嗯！为了不辜负你的紧急救援，今天的舞台我绝对炸场！』"),
                            ("谦杜", "（重新燃起自信的火焰，帅气地转身大步迈向璀璨的舞台中央）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            6: {
                "title": "🎬 谦杜·完美谢幕：末子的终极时尚告白",
                "scene": "Location: 演唱会庆功宴后的私人天台露台 | Time: 23:45 | Atmosphere: 城市夜景如同璀璨星河，晚风微凉，空气中弥漫着完美的浪漫氛围",
                "prologue": "万众瞩目的演唱会完美落幕，谦杜换上了一身宽松舒适的私服，手里拿着两杯苏打水走到露台栏杆边，转头看向身旁的你。",
                "dialogue_intro": [
                    ("谦杜", "“今晚的舞台和服装，绝对是本少爷出道以来最完美的一次杰作……当然，除了你。”"),
                ],
                "choices": [
                    {
                        "option": "微笑着祝贺他演唱会完美收官",
                        "dialogue_response": [
                            ("谦杜", "『谢谢！但最完美的不是舞台，而是能拥有你。这份一辈子的专属恋爱契约，请你签收一下！』"),
                            ("谦杜", "（极其郑重地从口袋里掏出一个设计感十足的精致对戒盒，单膝半跪在星空下）"),
                        ],
                        "affection": 35,
                        "random_event": None,
                    },
                    {
                        "option": "假装嫌弃他套路太多",
                        "dialogue_response": [
                            ("谦杜", "『这可不是套路，句句出自真心。不信，你摸摸我到现在还在狂跳的心。』"),
                            ("谦杜", "（霸道地拉过你的手直接按在自己的左胸口，掌心下是快要跳出胸膛的心跳）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "温柔地牵起他的手",
                        "dialogue_response": [
                            ("谦杜", "『好，以后的每一季潮流由你定义，而我的心由你承包。』"),
                            ("谦杜", "（眼底瞬间迸发出耀眼的光芒，随后毫无犹豫地将你紧紧拥入怀中）"),
                        ],
                        "affection": 35,
                        "random_event": {
                            "trigger_rate": 1.0,
                            "event_title": "🌟 专属结局：时尚末子的终身独家代言",
                            "narrative": "远处的夜空中恰好升起庆祝的绚丽礼花，将两人的拥抱晕染成最动人的时尚大片。",
                            "dialogue": ("谦杜", "“听好了，本少爷这辈子所有的时尚灵感和唯一的偏爱，全权交由你一个人独家署名！”"),
                            "bonus_affection": 15,
                        },
                    },
                ],
            },
        },
    },
"谦杜": {
        "青梅竹马": {
            1: {
                "title": "🎬 谦杜·放学路：末子竹马的潮流拌嘴",
                "scene": "Location: 樱花飘落的放学林荫小道 | Time: 16:30 | Atmosphere: 斜阳将两人的影子拉得很长，书包上的挂件随步伐叮当作响",
                "prologue": "作为从小一起长大的青梅竹马，谦杜今天依旧顶着一头精心打理过的微卷发，书包上挂满了各种最新款的限定潮玩公仔，走起路来大摇大摆。",
                "dialogue_intro": [
                    ("谦杜", "（侧过头斜眼看你，满脸写着“你懂个屁”的傲娇表情）"),
                ],
                "choices": [
                    {
                        "option": "吐槽他书包上挂的玩偶太多了",
                        "dialogue_response": [
                            ("谦杜", "『这叫个性懂不懂！青梅大人一点时尚品味都没有……不过如果你喜欢，这个送你好了。』"),
                            ("谦杜", "（手忙脚乱地从书包上扯下一个最宝贝的限定公仔塞进你手里，耳根却微微发红）"),
                        ],
                        "affection": 20,
                        "random_event": {
                            "trigger_rate": 0.35,
                            "event_title": "🍈 突发心动：冰淇淋的甜味",
                            "narrative": "路过熟悉的转角小卖部时，你顺手买了两支哈密瓜冰淇淋分他一只。",
                            "dialogue": ("谦杜", "“哇！太懂我了！青梅大人万岁，今天放学后的心情简直完美！”"),
                            "bonus_affection": 5,
                        },
                    },
                    {
                        "option": "买了两支哈密瓜冰淇淋分他一只",
                        "dialogue_response": [
                            ("谦杜", "『哇！太懂我了！青梅大人万岁，今天放学后的心情简直完美！』"),
                            ("谦杜", "（开心地接过冰淇淋咬了一口，眼睛亮晶晶地冲你笑得毫无防备）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "催促他走路别总是东张西望",
                        "dialogue_response": [
                            ("谦杜", "『我在观察灵感嘛……好啦好啦，听你的，乖乖跟你一起回家总行了吧。』"),
                            ("谦杜", "（瘪了瘪嘴，但还是乖乖收回四处乱飘的目光，老老实实跟在你身旁）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                ],
            },
            2: {
                "title": "🎬 谦杜·美术室：画板前的秘密情愫",
                "scene": "Location: 放学后空无一人的美术教室 | Time: 17:15 | Atmosphere: 夕阳透过彩色玻璃窗洒落，空气中弥漫着淡淡的颜料和木头香气",
                "prologue": "你轻手轻脚地走进美术室找他，却撞见向来张扬的谦杜正对着画板聚精会神地涂抹着什么，听到动静慌忙用胳膊挡住。",
                "dialogue_intro": [
                    ("谦杜", "（猛地把速写本合上，眼神飘忽不定地试图掩饰什么）"),
                ],
                "choices": [
                    {
                        "option": "看他偷偷画自己的肖像素描",
                        "dialogue_response": [
                            ("谦杜", "『诶别看！……还没画完呢。不过，因为模特是你，我不知不觉就画得特别用心。』"),
                            ("谦杜", "（耳尖红得快要滴血，却还是硬撑着把画本一角悄悄推向你）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.4,
                            "event_title": "🎨 突发心动：画板后的独家偏爱",
                            "narrative": "你顺手拿起桌上的橡皮帮他擦掉一处多余的线条，两人的手指在画纸上轻轻交错。",
                            "dialogue": ("谦杜", "“谢啦！青梅大人的橡皮擦出来的全都是甜甜的味道呢……还有，不许笑话我的画！”"),
                            "bonus_affection": 8,
                        },
                    },
                    {
                        "option": "夸奖他画技确实挺有天赋的",
                        "dialogue_response": [
                            ("谦杜", "『那是，本天才以后可是要开个人画展的……到时候你是唯一的特邀嘉宾。』"),
                            ("谦杜", "（尾巴简直要翘到天上去了，极其骄傲地扬起下巴）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "把自己的橡皮借给他用",
                        "dialogue_response": [
                            ("谦杜", "『谢啦！青梅大人的橡皮擦出来的全都是甜甜的味道呢。』"),
                            ("谦杜", "（笑嘻嘻地接过去，握着铅笔继续低头认真修改你的肖像）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            3: {
                "title": "☀️ 第二天：晨读课的时尚涂鸦",
                "scene": "Location: 早晨洒满阳光的高中教室 | Time: 08:15 | Atmosphere: 朗朗的读书声中，邻座的某个家伙正不安分地拿笔戳你的胳膊",
                "prologue": "早读课刚过半，同桌的谦杜神神秘秘地把一本课本推到你桌上，上面画满了各种夸张又前卫的潮流穿搭涂鸦。",
                "dialogue_intro": [
                    ("谦杜", "（单手托着腮眼巴巴地望着你，用气音小声提醒）"),
                ],
                "choices": [
                    {
                        "option": "翻开课本看到满页的涂鸦笑出声",
                        "dialogue_response": [
                            ("谦杜", "『不准笑！那是艺术！……好啦，我承认我满脑子想的都是怎么引起你的注意。』"),
                            ("谦杜", "（有些恼羞成怒地想把书抢回去，结果自己反倒先忍不住笑出了声）"),
                        ],
                        "affection": 20,
                        "random_event": {
                            "trigger_rate": 0.35,
                            "event_title": "🧸 突发心动：课桌底下的约定",
                            "narrative": "你顺手拿起红笔在他的涂鸦旁边写了个“优”，他立刻顺杆往上爬，飞快地塞过来一张小纸条。",
                            "dialogue": ("谦杜", "“好耶！放学不准跑，新出的限定潮玩我请客！”"),
                            "bonus_affection": 7,
                        },
                    },
                    {
                        "option": "顺路用红笔批改他的涂鸦作业",
                        "dialogue_response": [
                            ("谦杜", "『喂！怎么还学老师批作业！……不过如果是你批的，全打勾我也认了。』"),
                            ("谦杜", "（笑嘻嘻地把脑袋凑过来，温热的呼吸几乎拂过你的耳畔）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "塞过去一张纸条约放学去买新潮玩",
                        "dialogue_response": [
                            ("谦杜", "『好耶！放学不准跑，新出的限定潮玩我请客！』"),
                            ("谦杜", "（兴奋得差点在座位上跳起来，整堂早读课都在神采飞扬地转笔）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                ],
            },
            4: {
                "title": "🎬 谦杜·文化祭服装秀：后台的贴心瞬间",
                "scene": "Location: 校文化祭后台热闹的更衣室 | Time: 14:00 | Atmosphere: 镜子前闪烁着耀眼的灯光，空气中混杂着发胶和紧张兴奋的气息",
                "prologue": "全校瞩目的文化祭服装秀即将开场，作为压轴模特的谦杜正手忙脚乱地系着外套上的复杂饰品，急得额头微微冒汗。",
                "dialogue_intro": [
                    ("谦杜", "（看到你走进来，立刻像抓住了救命稻草一样转过身求救）"),
                ],
                "choices": [
                    {
                        "option": "帮他调整走秀穿的潮牌外套",
                        "dialogue_response": [
                            ("谦杜", "『太近了……闻到你身上的味道，我走秀时差点同手同脚出洋相。』"),
                            ("谦杜", "（僵硬地站在原地一动不敢动，眼底却闪烁着藏不住的炽热光芒）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.45,
                            "event_title": "✨ 突发心动：后台的秘密暗号",
                            "narrative": "你笑着拍了拍他的肩膀递上矿泉水，他顺势把水瓶紧紧握在手里。",
                            "dialogue": ("谦杜", "“收到！等我走秀回来，有个超重要的秘密要当面告诉你……绝对不许跑！”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "鼓励他上台别紧张好好发挥",
                        "dialogue_response": [
                            ("谦杜", "『有你在台下看着，我才不紧张呢，今天绝对拿下全校最帅男模奖！』"),
                            ("谦杜", "（自信满满地打了个响指，随后帅气地冲你挑了挑眉）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "递上一瓶矿泉水：『加油哦。』",
                        "dialogue_response": [
                            ("谦杜", "『收到！等我走秀回来，有个超重要的秘密要当面告诉你。』"),
                            ("谦杜", "（郑重其事地接过水，眼神变得前所未有的坚定和认真）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            5: {
                "title": "🎬 谦杜·星空天台：末子少年的直球告白",
                "scene": "Location: 文化祭结束后的宁静学校天台 | Time: 18:30 | Atmosphere: 晚风微凉，远处的操场还隐约传来喧闹声，头顶是璀璨的星空",
                "prologue": "文化祭圆满落幕后，谦杜一把拉着气喘吁吁的你跑上天台。周围安静下来，他转过身借着月光，耳根红得彻底。",
                "dialogue_intro": [
                    ("谦杜", "（深吸了一口气，双手紧紧攥成拳头，终于下定决心开口）"),
                ],
                "choices": [
                    {
                        "option": "戳戳他通红的脸颊：『今天表现不错嘛。』",
                        "dialogue_response": [
                            ("谦杜", "『别戳脸……怪不好意思的。其实我刚才在台下一直在找你的身影，我有话对你说。』"),
                            ("谦杜", "（慌乱地捉住你恶作剧的手指，顺势将你的手掌紧紧包在他的手心里）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.5,
                            "event_title": "💫 突发心动：星空下的青梅契约",
                            "narrative": "见你想假装听不懂转身逃跑，他急忙一步跨到你面前拦住去路。",
                            "dialogue": ("谦杜", "“诶别走！今天必须给我回应……我喜欢你，从小到大只喜欢你一个，做我女朋友/男朋友好不好！”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "假装听不见想转身下楼",
                        "dialogue_response": [
                            ("谦杜", "『诶别走！今天必须给我回应……我喜欢你，做我女朋友/男朋友好不好！』"),
                            ("谦杜", "（急得声音都有些发颤，生怕你真的跑掉似的一把扯住你的衣角）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "温柔地笑着用双手回握住他",
                        "dialogue_response": [
                            ("谦杜", "『真拿你没办法……好啦，我也早就喜欢你了。』"),
                            ("谦杜", "（愣了一秒钟后瞬间爆发出巨大的狂喜，一把将你狠狠拥入怀中）"),
                        ],
                        "affection": 28,
                        "random_event": None,
                    },
                ],
            },
            6: {
                "title": "🎬 谦杜·告白终章：青梅竹马的时尚热恋",
                "scene": "Location: 曾经放学一起走过的樱花林道 | Time: 19:00 | Atmosphere: 路灯把两人的影子叠在一起，夜风温柔，空气中全是恋爱的甜味",
                "prologue": "正式确立关系后的首个晚自习放学路，两人并肩走在熟悉的街道上。身份的转变让每一个平常的动作都变得无比心动。",
                "dialogue_intro": [
                    ("谦杜", "（侧过头冲你笑得一脸灿烂，语气里满是藏不住的小骄傲）"),
                ],
                "choices": [
                    {
                        "option": "十指相扣宣布恋爱关系正式成立",
                        "dialogue_response": [
                            ("谦杜", "『太棒啦！从今天起，青梅竹马直接升级成最甜恋人，以后我的每一套穿搭秀全由你审阅！』"),
                            ("谦杜", "（把十指紧扣的手高高举起在路灯下晃了晃，笑得像个得到了全世界的大男孩）"),
                        ],
                        "affection": 35,
                        "random_event": None,
                    },
                    {
                        "option": "笑他刚才表白时结巴的样子",
                        "dialogue_response": [
                            ("谦杜", "『那是因为太紧张了好不好！面对几千人我不慌，面对你我心跳直接超速。』"),
                            ("谦杜", "（有些不好意思地用肩膀轻轻撞了撞你，随后笑意盈盈地把你护在内侧）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "靠在他肩膀上迎接美好未来",
                        "dialogue_response": [
                            ("谦杜", "『走吧，我们的青春时尚大片，从这一秒开始全糖甜到底！』"),
                            ("谦杜", "（反手极其自然地将你搂进怀里，大步流星地朝着属于两人的未来走去）"),
                        ],
                        "affection": 35,
                        "random_event": {
                            "trigger_rate": 1.0,
                            "event_title": "🌟 专属结局：青梅竹马的终身独家冠名",
                            "narrative": "路边的樱花树恰好落下一阵唯美的花瓣雨，将两人的热恋渲染成最完美的青春偶像剧大结局。",
                            "dialogue": ("谦杜", "“听好了，本少爷这辈子所有的青梅竹马情分和唯一的专属偏爱，全部无限期续签，永不解约！”"),
                            "bonus_affection": 15,
                        },
                    },
                ],
            },
        },
    },
"谦杜": {
        "在日留学生or打工人": {
            1: {
                "title": "🎬 谦杜·异国潮牌店：时尚末子的偶遇",
                "scene": "Location: 东京原宿一家人潮涌动的地下独立潮牌店 | Time: 15:00 | Atmosphere: 强烈的Hip-hop音乐回荡在店里，五光十色的霓虹灯牌将潮服衬托得格外前卫",
                "prologue": "身在东京求学/打工的你正百无聊赖地翻看着货架上的衣物，身旁突然传来一个熟悉又充满自信的声音。只见时尚末子谦杜正拿着一件设计夸张的卫衣，对着镜子苦恼地比划着。",
                "dialogue_intro": [
                    ("谦杜", "“总觉得这件衣服的剪裁差了点意思……哎，你觉得呢？”"),
                ],
                "choices": [
                    {
                        "option": "帮他挑选了一件超有品味的卫衣",
                        "dialogue_response": [
                            ("谦杜", "『哇！眼光绝了！在东京正愁找不到对胃口的衣服，你简直是我的时尚缪斯！』"),
                            ("谦杜", "（一把接过你挑中的卫衣，眼睛里闪烁着找到知己般的兴奋光芒）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.35,
                            "event_title": "☕ 突发心动：东京限定的温度",
                            "narrative": "走出潮牌店时飘起小雨，他顺手从路边贩卖机买了两罐热咖啡塞进你手里。",
                            "dialogue": ("谦杜", "“谢谢啦！今天在东京打工的疲惫，被你这杯咖啡全治愈了。”"),
                            "bonus_affection": 5,
                        },
                    },
                    {
                        "option": "用关西腔开玩笑打招呼",
                        "dialogue_response": [
                            ("谦杜", "『哈哈，异国他乡听到这个口音太亲切了！交个朋友呗，带我去逛东京小众潮店？』"),
                            ("谦杜", "（瞬间放松下来，笑嘻嘻地凑到你身旁，熟络得像认识多年的老友）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "请他喝了一杯东京限定咖啡",
                        "dialogue_response": [
                            ("谦杜", "『谢谢啦！今天在东京打工的疲惫，被你这杯咖啡全治愈了。』"),
                            ("谦杜", "（双手捧着温热的纸杯，目光柔和地冲你勾起唇角）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            2: {
                "title": "🎬 谦杜·深夜便利店：打工人的潮流畅谈",
                "scene": "Location: 东京深夜亮着白炽灯的24小时便利店 | Time: 23:45 | Atmosphere: 外面是寂静微凉的东京街道，店内回荡着单调的进门提示音",
                "prologue": "深夜兼职结束后，你在便利店遇到了同样在打工、累得直揉肩膀的谦杜。他正无精打采地整理着货架上的时尚杂志。",
                "dialogue_intro": [
                    ("谦杜", "（把最后一本杂志塞回货架，忍不住靠着货架长长地叹了一口气）"),
                ],
                "choices": [
                    {
                        "option": "看他整理货架累得直叹气安慰他",
                        "dialogue_response": [
                            ("谦杜", "『叹气会把时尚灵感赶跑的……不过，如果你的温柔分给我一点，我就立刻复活。』"),
                            ("谦杜", "（刚才还无精打采的眼神瞬间亮了起来，冲你坏笑着眨了眨眼）"),
                        ],
                        "affection": 22,
                        "random_event": {
                            "trigger_rate": 0.4,
                            "event_title": "🍞 突发心动：深夜的面包奇遇",
                            "narrative": "你笑着把一个刚打折的面包分给他一半，他感动得差点原地起立。",
                            "dialogue": ("谦杜", "“虽然是打折的，但因为是你给的，吃起来感觉比高级料理还美味。”"),
                            "bonus_affection": 8,
                        },
                    },
                    {
                        "option": "分给他一个打折面包充饥",
                        "dialogue_response": [
                            ("谦杜", "『虽然是打折的，但因为是你给的，吃起来感觉比高级料理还美味。』"),
                            ("谦杜", "（毫不客气地接过来咬了一大口，脸上写满了大大的满足）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "劝他晚上早点回公寓休息",
                        "dialogue_response": [
                            ("谦杜", "『遵命！不过明天你得答应陪我一起去原宿，不然我今晚不收工。』"),
                            ("谦杜", "（耍赖般地双手合十向你求情，语气里满是藏不住的期待）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            3: {
                "title": "☀️ 第二天：原宿街头的潮流打卡",
                "scene": "Location: 游人如织、先锋潮牌林立的原宿街头 | Time: 13:30 | Atmosphere: 阳光洒满街巷，街上随处可见打扮个性前卫的年轻人",
                "prologue": "难得的东京晴天，两人相约来到原宿街头逛街。身为时尚达人的谦杜一路上精神抖洒，对每一家潮店都两眼放光。",
                "dialogue_intro": [
                    ("谦杜", "（摆出一个极其帅气的杂志封面姿势，指了指身后的巨型潮流涂鸦墙）"),
                ],
                "choices": [
                    {
                        "option": "帮他拍一张很有杂志封面感的照片",
                        "dialogue_response": [
                            ("谦杜", "『把我拍得超帅哦……这张照片以后绝对要挂在我个人工作室的最显眼位置。』"),
                            ("谦杜", "（立刻凑过头来看手机里的成片，满意得尾巴快要翘到天上去了）"),
                        ],
                        "affection": 22,
                        "random_event": {
                            "trigger_rate": 0.3,
                            "event_title": "🍦 突发心动：街头的甜蜜可丽饼",
                            "narrative": "逛累了路过甜品店，两人分食了一份东京限定的可丽饼。",
                            "dialogue": ("谦杜", "“甜滋滋的，就像我现在的心情一样，全都是因为你在身边。”"),
                            "bonus_affection": 7,
                        },
                    },
                    {
                        "option": "吐槽他逛街比女孩子还要挑剔",
                        "dialogue_response": [
                            ("谦杜", "『这叫对审美的坚持！不过为了你，我可以放弃所有潮流，只追随你的脚步。』"),
                            ("谦杜", "（耳朵微微泛红，却还是嘴硬地轻哼了一声转过头去）"),
                        ],
                        "affection": 25,
                        "random_event": None,
                    },
                    {
                        "option": "买了两份限定可丽饼分食",
                        "dialogue_response": [
                            ("谦杜", "『甜滋滋的，就像我现在的心情一样，全都是因为你在身边。』"),
                            ("谦杜", "（笑嘻嘻地咬着奶油，眼神却一瞬不瞬地黏在你身上）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            4: {
                "title": "🎬 谦杜·暴雨突袭：东京街头的屋檐避难",
                "scene": "Location: 东京街头复古的日式建筑屋檐下 | Time: 17:15 | Atmosphere: 倾盆大雨瞬间笼罩了十字路口，水汽冰凉，周围行人行色匆匆",
                "prologue": "一场突如其来的东京暴雨把两人逼进了狭窄的屋檐下。看着你被风吹得微微发抖，手里唯一的潮牌透明伞毫不犹豫地向你倾斜。",
                "dialogue_intro": [
                    ("谦杜", "（看着自己湿透了半边肩膀的衣袖，无奈又心疼地叹了口气）"),
                ],
                "choices": [
                    {
                        "option": "把唯一的潮牌雨伞全倾斜向他",
                        "dialogue_response": [
                            ("谦杜", "『诶你全给我了那你自己呢……真笨。快过来，靠我近一点，这样才不会淋湿。』"),
                            ("谦杜", "（一把将你猛地拉进自己怀里，用宽大的外套将你整个人严严实实地护住）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.45,
                            "event_title": "🌧️ 突发心动：雨夜的心跳共振",
                            "narrative": "雨打伞面的声音格外清晰，他忍不住伸手替你擦去脸颊上的雨水。",
                            "dialogue": ("谦杜", "“管他什么暴雨，只要能和你在东京的雨夜多待一会儿，我巴不得雨下得更大点。”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "抱怨东京的天气阴晴不定",
                        "dialogue_response": [
                            ("谦杜", "『管他什么暴雨，只要能和你在东京的雨夜多待一会儿，我巴不得雨下得更大点。』"),
                            ("谦杜", "（眼底泛起认真的光芒，双手顺势环住你的肩膀抵御寒意）"),
                        ],
                        "affection": 22,
                        "random_event": None,
                    },
                    {
                        "option": "用纸巾帮他擦脸上的雨水",
                        "dialogue_response": [
                            ("谦杜", "『谢谢……你照顾人的样子，真的让我忍不住想赖在你身边一辈子。』"),
                            ("谦杜", "（乖乖站在原地任由你擦拭，嘴角扬起一抹温柔又宠溺的弧度）"),
                        ],
                        "affection": 20,
                        "random_event": None,
                    },
                ],
            },
            5: {
                "title": "🎬 谦杜·东京塔夜景：离别前的时尚告白",
                "scene": "Location: 俯瞰东京璀璨夜景的高层观景台 | Time: 21:00 | Atmosphere: 红色东京塔在夜色中分外耀眼，空气中弥漫着即将离别的伤感",
                "prologue": "随着国内演艺行程的召唤，谦杜在东京的留学生/打工生活即将画上句号。两人并肩站在观景台前，久久望着夜景无言。",
                "dialogue_intro": [
                    ("谦杜", "（双手插在外套口袋里，转过头来委屈巴巴地看着你）"),
                ],
                "choices": [
                    {
                        "option": "看着东京塔的灯光静静不语",
                        "dialogue_response": [
                            ("谦杜", "『塔再高也没有我的思念高……明天就要回国了，你会不会想我？』"),
                            ("谦杜", "（吸了吸鼻子，平日里骄傲的时尚末子此刻却像个丢了心爱玩具的大男孩）"),
                        ],
                        "affection": 25,
                        "random_event": {
                            "trigger_rate": 0.5,
                            "event_title": "✈️ 突发心动：离别前的直球契约",
                            "narrative": "他突然反手一把紧紧抱住你，宽阔的胸膛带着滚烫的温度。",
                            "dialogue": ("谦杜", "“一句加油可打发不了我……你得答应我保持联络，或者干脆跟我回大阪！”"),
                            "bonus_affection": 10,
                        },
                    },
                    {
                        "option": "拍拍他肩膀：『回国加油。』",
                        "dialogue_response": [
                            ("谦杜", "『一句加油可打发不了我……你得答应我保持联络，或者干脆跟我回大阪！』"),
                            ("谦杜", "（语气前所未有的认真与执着，双手紧紧扣住你的手腕）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "紧紧抱住他单薄的身躯",
                        "dialogue_response": [
                            ("谦杜", "『……犯规。突然这么舍不得我，那我可要考虑为了你留在东京了哦。』"),
                            ("谦杜", "（叹了口气将你整个人揉进怀里，力道大得仿佛要将这一刻永远定格）"),
                        ],
                        "affection": 28,
                        "random_event": None,
                    },
                ],
            },
            6: {
                "title": "🎬 谦杜·跨国终章：末子的时尚远距离恋爱",
                "scene": "Location: 跨国视频连线的屏幕两侧 / 国内机场到达大厅 | Time: 20:00 | Atmosphere: 闪光灯与欢呼声交织，空气中充满梦想实现与爱情圆满的喜悦",
                "prologue": "谦杜回国后凭借独特的时尚感迅速爆红出圈。在一次深夜跨国连线（或惊喜现身）中，他向一直支持他的你发起了最终的爱情宣告。",
                "dialogue_intro": [
                    ("谦杜", "（对着镜头笑得一脸灿烂，眼神里却有着让人无法忽视的坚定与深情）"),
                ],
                "choices": [
                    {
                        "option": "接通跨国视频听他深情表白",
                        "dialogue_response": [
                            ("谦杜", "『听好了，我在国内每一秒都在想你。跨国恋根本难不倒我，准备好做我的新娘/新郎了吗？』"),
                            ("谦杜", "（隔着屏幕帅气地单膝下跪，举起了一枚设计感十足的专属定制戒指）"),
                        ],
                        "affection": 35,
                        "random_event": None,
                    },
                    {
                        "option": "假装信号不好逗他着急",
                        "dialogue_response": [
                            ("谦杜", "『喂喂别挂！我信号好得很……不准开玩笑，我超级认真的喜欢你！』"),
                            ("谦杜", "（急得差点从椅子上蹦起来，看你笑出声才无奈地宠溺摇头）"),
                        ],
                        "affection": 30,
                        "random_event": None,
                    },
                    {
                        "option": "突然提着行李箱出现在他面前",
                        "dialogue_response": [
                            ("谦杜", "『诶？！你怎么突然从视频里走到我现实里了……呜哇，太狡猾了，感动得我想哭！』"),
                            ("谦杜", "（震惊过后瞬间红了眼眶，扔下通告单大步流星地冲过来将你一把紧紧抱起）"),
                        ],
                        "affection": 35,
                        "random_event": {
                            "trigger_rate": 1.0,
                            "event_title": "🌟 专属结局：跨越山海的时尚终身契约",
                            "narrative": "东京的雪与国内的霓虹在这一刻完美交融，所有的异国思念终于化作了永恒相守的浪漫大片。",
                            "dialogue": ("谦杜", "“从东京的寒冬到国内的顶峰，我这辈子所有的时尚灵感和唯一的偏爱，全权交由你一个人独家署名！”"),
                            "bonus_affection": 15,
                        },
                },
            ],
        },
    },
},
}

# -----------------------------------------------------------------------------
# 4. Session State 初始化
# -----------------------------------------------------------------------------
if "stage" not in st.session_state:
    st.session_state.stage = "menu"
if "player_role" not in st.session_state:
    st.session_state.player_role = ROLES[0]
if "target_member" not in st.session_state:
    st.session_state.target_member = "丈君"
if "current_act" not in st.session_state:
    st.session_state.current_act = 1
if "total_score" not in st.session_state:
    st.session_state.total_score = 30
if "dialogue_history" not in st.session_state:
    st.session_state.dialogue_history = []
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "active_buff" not in st.session_state:
    st.session_state.active_buff = None
if "daily_gacha_result" not in st.session_state:
    st.session_state.daily_gacha_result = None
if "random_event" not in st.session_state:
    st.session_state.random_event = None
# 新增：用于乙女游戏沉浸式互动的临时状态
if "last_dialogue_result" not in st.session_state:
    st.session_state.last_dialogue_result = None

# -----------------------------------------------------------------------------
# 5. 主界面渲染
# -----------------------------------------------------------------------------
st.markdown(
    '<p class="main-header">💖 浪花男子心动日常</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">✨ 沉浸式乙女恋爱养成企划 (全剧情流畅推进)</p>',
    unsafe_allow_html=True,
)

# 抽卡与扭蛋区域
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
                (
                    "🕵️‍♂️ 黑色鸭舌帽",
                    "低调伪装神器，免疫一次轻度偷拍危机！",
                ),
                (
                    "📜 紧急公关手稿",
                    "遭遇绯闻时自动触发，大幅度降低负面好感损失！",
                ),
                (
                    "📱 备用双卡手机",
                    "防止私生饭骚扰与紧急联络专用，增加容错率！",
                ),
                (
                    "☕ 专属应援手摇杯",
                    "满含心意的特调饮品，全选项好感度小幅额外+5!",
                ),
                (
                    "🎟️ VIP前排观演门票",
                    "近距离接触的心动暴击，好感获取效率大幅提升！",
                ),
                (
                    "🕶️ 明星同款墨镜",
                    "闪避一次记者的长焦镜头抓拍，维持神秘感与安全度！",
                ),
                (
                    "📜 绝密通告行程单",
                    "提前获知对方动向，精准制造偶遇，额外+20积分！",
                ),
                (
                    "🌹 手作永生玫瑰",
                    "浪漫值直接拉满，有机会触发隐藏甜蜜对话剧情！",
                ),
                (
                    "🍫 手工黑巧礼盒",
                    "甜而不腻的心意表达，关键时刻化解尴尬气氛！",
                ),
                (
                    "🌙 星空定制项链",
                    "专属浪漫信物，大幅提升最终结局的甜度与评级！",
                ),
                (
                    "🐾 宠物协力萌爪",
                    "利用可爱萌宠助攻，瞬间融化冰冷防备，额外+12积分！",
                ),
            ]
            item_name, item_desc = random.choice(items_pool)
            st.session_state.inventory.append(item_name)
            st.success(f"成功获得道具：{item_name}（{item_desc}）!")
        else:
            st.warning("积分不足10分,快去剧情里增加好感吧！")

if st.session_state.daily_gacha_result:
    lname, ldata = st.session_state.daily_gacha_result
    st.info(
        f"✨ 今日运势大吉！今日最强心动电波对象是：**{lname}**（特点：{ldata['trait']}）。快去选择他开启剧情吧！"
    )

# 背包与Buff道具栏
if st.session_state.inventory:
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
    st.markdown(
        f"> ⚡ **当前生效增益Buff:** `{st.session_state.active_buff}`"
    )

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. 游戏流程控制
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 6. 游戏流程控制 (优化：沉浸式乙女突发事件互动)
# -----------------------------------------------------------------------------

if st.session_state.random_event:
    ev = st.session_state.random_event
    ev_title = ev['title']
    ev_desc = ev['desc']
    m_name = st.session_state.target_member
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%); border: 2px solid #fb7185; padding: 20px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(225,29,72,0.15);">
            <h3 style="margin-top:0; color: #9f1239; font-size: 1.3rem;">⚡ 【心动危机 / 突发事件】{ev_title}</h3>
            <p style="font-size: 1.05rem; color: #44403c; line-height: 1.6;">{ev_desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 检查并处理道具自动触发（完美保留你原本的道具事件逻辑！）
    item_triggered = None
    if "文春炮" in ev_title:
        if "🕵️‍♂️ 黑色鸭舌帽" in st.session_state.inventory:
            st.success("✨ 【道具自动触发：黑色鸭舌帽】低调伪装成功！你们完美避开了文春记者的长焦长枪短炮！")
            st.session_state.inventory.remove("🕵️‍♂️ 黑色鸭舌帽")
            item_triggered = True
        elif "📜 紧急公关手稿" in st.session_state.inventory:
            st.success("✨ 【道具自动触发：紧急公关手稿】手稿发挥作用，团队迅速稳住了媒体风向！")
            st.session_state.inventory.remove("📜 紧急公关手稿")
            item_triggered = True
            
    elif "私生饭" in ev_title:
        if "📱 备用双卡手机" in st.session_state.inventory:
            st.success("✨ 【道具-备用双卡手机】及时联络到安保人员精准清场，安全脱身！")
            st.session_state.inventory.remove("📱 备用双卡手机")
            item_triggered = True

    # 根据事件类型，生成极具代入感的乙女游戏化选项
    if item_triggered:
        st.info("💡 因为你携带了正确的心动道具，顺利化解危机，额外获得 **+25 积分**！")
        if st.button("💖 携手化解危机，继续心动行程", use_container_width=True):
            st.session_state.total_score += 25
            st.session_state.random_event = None
            st.rerun()
    else:
        # 没有道具时的乙女向沉浸式抉择支线
        st.markdown(f"**{m_name} 紧紧握住你的手，低声问你：\"别怕，这种时候……你打算怎么应对？\"**")
        
        col_ev1, col_ev2 = st.columns(2)
        
        with col_ev1:
            if st.button("🛡️ 勇敢迎难而上，与他默契配合", use_container_width=True):
                st.session_state.total_score += 15
                st.session_state.last_dialogue_result = (
                    f"面对突发事件：{ev_title}", 
                    None, 
                    f"「有你在我身边，我什么都不怕。大不了……公开好了。」（宠溺又坚定地笑著看着你）", 
                    15
                )
                st.session_state.random_event = None
                st.rerun()
                
        with col_ev2:
            if st.button("🏃‍♂️ 听他的指挥，迅速寻找浪漫避难所", use_container_width=True):
                st.session_state.total_score += 10
                st.session_state.last_dialogue_result = (
                    f"面对突发事件：{ev_title}", 
                    None, 
                    f"「抓紧我！往这边跑……呼，好险，不过能和你有这种秘密经历，好像也不赖？」（无奈又宠溺地揉了揉你的头发）", 
                    10
                )
                st.session_state.random_event = None
                st.rerun()
                
        # 保留原本无道具时的数值惩罚兜底（如果玩家不想选或者直接关掉）
        if "文春炮" in ev_title or "私生饭" in ev_title:
            if st.button("⚠️ 哎呀，不小心被拍到了/被围堵了（扣除部分积分）", use_container_width=True):
                penalty = 30 if "文春炮" in ev_title else 25
                st.session_state.total_score -= penalty
                st.warning(f"危机处理略显慌乱，好感度 -{penalty} 分！快去用道具或后续剧情追回来吧！")
                st.session_state.random_event = None
                st.rerun()
        st.session_state.total_score += 20
        st.session_state.random_event = None
        st.success("随机事件圆满完成！好感度大幅上升！")
        st.rerun()

elif st.session_state.stage == "menu":
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("🛠️ 请定制你的心动企划档案")

selected_member = st.selectbox("💖 选择你的心动男主角：", MEMBERS)

    # 实时渲染人物图片
st.image(MEMBERS[selected_member]["img"], width=220)

selected_role = st.selectbox("🎭 选择你的专属身份：", ROLES)

st.markdown(f"**当前角色特色：** {MEMBERS[selected_member]['trait']}")

if st.button("🚀 开始心动企划", use_container_width=True):
        st.session_state.target_member = selected_member
        st.session_state.player_role = selected_role
        st.session_state.current_act = 1
        st.session_state.total_score = 30
        st.session_state.stage = "playing"
        st.session_state.dialogue_history = []
        st.session_state.last_dialogue_result = None
        st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 7. 动态个性化剧情数据库与核心生成函数
# -----------------------------------------------------------------------------

def get_member_story(member, role, act):
    # 1. 优先尝试从结构化数据库中读取硬编码的专属剧本
    try:
        if 'ROLE_STORY_DB' in globals():
            member_data = ROLE_STORY_DB.get(member, {})
            role_data = member_data.get(role, {})
            act_data = role_data.get(act, None)
            if act_data:
                return act_data
    except Exception:
        pass

    # 2. 智能动态生成：根据「角色特点 + 玩家身份 + 当前幕数」组合出独一无二的剧情
    member_trait = MEMBERS.get(member, {}).get("trait", "温柔贴心")
    
    # 根据幕数（Act）划分不同的剧情阶段和氛围
    prologues_by_act = {
        1: f"【初识与试探】你是{member}的{role}。初次合作的空气中带着一丝试探与新鲜感，他的性格特点（{member}：{member_trait}）在此刻展露无遗。",
        2: f"【默契升温】你是{member}的{role}。随着企划推进到第 2 幕，你们在日常相处中已经有了独特的默契，气氛开始变得微妙起来。",
        3: f"【心跳加速】你是{member}的{role}。来到了关键的第 3 幕，周围的喧嚣仿佛都消失了，只剩下彼此的心跳声。",
        4: f"【情感爆发】你是{member}的{role}。在第 4 幕的高潮中，藏在心底的情愫终于再也无法掩饰……",
        5: f"【终章抉择】你是{member}的{role}。这是决定命运的最后一幕，你们正站在心动企划的十字路口。"
    }
    
    # 为不同角色和幕数定制开场白
    intro_pool = [
        f"「呐，其实从刚才开始，我的视线就一直没办法从你身上移开呢……」",
        f"「如果是面对你的话，我好像无论什么秘密都愿意毫无保留地分享出来。」",
        f"「今天能有这么多只属于我们两个人的时间，感觉真的像做梦一样。」",
        f"「每次看你认真工作的样子，我都忍不住想离你更近一点，再近一点。」",
        f"「真狡猾啊……明明什么都没做，却总是能轻易左右我的心情。」"
    ]
    
    intro_text = intro_pool[(hash(member) + act * 3) % len(intro_pool)]

# -------------------------------------------------------------
    # 7成员 × 3身份 专属动态选项与回应生成系统
    # -------------------------------------------------------------
    
    # 7位成员的专属人设词库（自称、喜爱食物、语气风格）
    flavor_db = {
        "丈君": {"call": "本大爷", "food": "章鱼烧", "style": "热血直球"},
        "大酱": {"call": "我", "food": "黑咖啡", "style": "腹黑宠溺"},
        "大桥": {"call": "我", "food": "限定布丁", "style": "治愈天然"},
        "恭平": {"call": "本帅哥", "food": "薯片", "style": "傲娇酷盖"},
        "流星": {"call": "人家", "food": "草莓大福", "style": "精致小恶魔"},
        "米七": {"call": "我", "food": "草莓牛奶", "style": "纯情深情"},
        "谦杜": {"call": "本专家", "food": "气泡水", "style": "潮流淘气"}
    }
    
    f_info = flavor_db.get(member, {"call": "我", "food": "点心", "style": "温柔"})

  # -------------------------------------------------------------
    # 彻底告别千篇一律！为 7 位成员量身定制的完全独立选项与回应库
    # -------------------------------------------------------------
    _member_specific_pools = {
        "丈君": {
            1: [
                {"option": "吐槽他：\"台词又背错了吧，大阪来的大忙人。\"", "reply": "「呜哇，这吐槽好犀利！不过……不愧是我看中的搭档，反应真快！」", "affection": 15},
                {"option": "递过去剧本：\"好啦，快对词，别想着用搞笑梗混过去。\"", "reply": "「遵命遵命！为了不让专属大人失望，我现在立刻进入认真模式！」", "affection": 20},
                {"option": "开玩笑：\"今天表现不好，扣你的章鱼烧哦。\"", "reply": "「诶？！怎么这样！扣章鱼烧的话我今晚可就失去灵魂了！」", "affection": 10}
            ],
            2: [
                {"option": "递上一杯温水：\"辛苦了，润润喉吧。\"", "reply": "「谢谢你……每次有你在身边，心里就觉得格外踏实安心。」", "affection": 18},
                {"option": "笑着调侃：\"刚才那个包袱好像没响哦？\"", "reply": "「居然敢拆穿我！好啊，那罚你今晚陪我多对一遍台词。」", "affection": 22},
                {"option": "认真点头：\"我会做好你的专属支援的！\"", "reply": "「有你这句话，本大爷什么都不怕了，接下来的舞台一起冲吧！」", "affection": 15}
            ],
            3: [
                {"option": "轻声呢喃：\"今天发生了很多意料之外的事呢……\"", "reply": "「但对我来说，今天最棒的意外，就是遇见了你，并且离你更近了一步。」", "affection": 25},
                {"option": "直视他的眼睛：\"好啦，不许再逗我了。\"", "reply": "「我可没有在逗你，我是认真的……对你的喜欢，从来都不是开玩笑。」", "affection": 30},
                {"option": "微微避开视线：\"时间不早了，我们抓紧吧。\"", "reply": "「害羞的样子也很可爱……好啦，不逗你了，我会一直在你身边的。」", "affection": 20}
            ],
            4: [
                {"option": "坚定握住他的手：\"不管未来怎样，我都陪着你。\"", "reply": "「这句话……我可就当真了。以后无论走到哪，你都别想轻易甩掉我。」", "affection": 35},
                {"option": "打趣：\"大明星今天怎么这么黏人？\"", "reply": "「因为面对喜欢的人，谁没办法保持冷静啊……真拿你没办法。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等这一刻。\"", "reply": "「太好了……听到你这么说，悬着的心终于落下了。接下来，换我来守护你。」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，永远只为你一个人开放。\"", "reply": "「我也是……从今往后，你的每一个日常，我都想以恋人的身份全部承包。」", "affection": 50},
                {"option": "相视一笑：\"这就是我们之间最完美的结局。\"", "reply": "「不，这只是开始。属于我们的浪漫物语，才刚刚翻开序章呢。」", "affection": 45},
                {"option": "调皮眨眼：\"那接下来的行程单，可要由我来制定咯！\"", "reply": "「遵命，我的专属主策划大人。我的一切，全部听从你的指挥。」", "affection": 40}
            ]
        },
        "恭平": {
            1: [
                {"option": "敲敲桌面：\"别打游戏了，快看通告单。\"", "reply": "「啧，被抓包了……不过，有本帅哥陪着，看通告单也没那么无聊吧？」", "affection": 15},
                {"option": "调侃他：\"发型乱了哦，大明星。\"", "reply": "「诶？！真的假的？……切，明明帅得毫无死角，少诈我。」", "affection": 20},
                {"option": "无奈叹气：\"真拿你没办法，把掌机交出来。\"", "reply": "「那可不行，这局马上就赢了……除非你答应收工请我喝奶茶。」", "affection": 10}
            ],
            2: [
                {"option": "递过去一罐冰饮：\"给，降降温。\"", "reply": "「谢啦。不过……比起饮料，你一直看着我才更能让我降温吧。」", "affection": 18},
                {"option": "挑眉：\"刚才走位好像有点同手同脚哦？\"", "reply": "「那、那是战术！本帅哥才不会紧张……好啦，别笑了，过来帮我顺下动作。」", "affection": 22},
                {"option": "认真拍拍他：\"接下来的LIVE一起加油吧。\"", "reply": "「知道了啦。只要你在台下看着，本帅哥绝对会拿满分表现给你看。」", "affection": 15}
            ],
            3: [
                {"option": "轻声说：\"今天台下有很多你的应援扇呢。\"", "reply": "「嗯，看见了。不过我眼里……其实只能看见你一个人举的牌子。」", "affection": 25},
                {"option": "直视他：\"别装酷了，其实耳朵红了吧？\"", "reply": "「……哪有！才没有脸红，室内空调开太高了而已！」", "affection": 30},
                {"option": "避开视线：\"好啦，快去准备下一场。\"", "reply": "「害羞什么……不过，不准看别人，只能看我。」", "affection": 20}
            ],
            4: [
                {"option": "握住他的手：\"不管外界怎么说，我都在。\"", "reply": "「切，这种台词应该由本帅哥来说才对……不过，有你这句话, 感觉什么都不怕了。」", "affection": 35},
                {"option": "笑着打趣：\"傲娇大明星今天怎么这么诚实？\"", "reply": "「因为在你面前，那些伪装根本没用啊……真拿你没办法，被你吃得死死的。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等你这句话。\"", "reply": "「那就说定了。以后，本帅哥的专属偏爱，全部只留给你一个人。」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，从今往后只属于你。\"", "reply": "「哼，这还差不多。从今以后，你的眼里也只能有我一个男主角。」", "affection": 50},
                {"option": "相视一笑：\"这就是最完美的结局。\"", "reply": "「不，这才是我们的第一幕。接下来，由我来带你走向更耀眼的未来。」", "affection": 45},
                {"option": "调皮眨眼：\"那以后的行程安排，可得听我的咯！\"", "reply": "「遵命，我的专属大导演。本帅哥的一切，全部听从你的指挥。」", "affection": 40}
            ]
        },
        "大桥": {
            1: [
                {"option": "指着冰箱：\"不准偷吃限定布丁，那是工作后大家的！\"", "reply": "「诶——？！怎么这样！那、那我看着它不吃总行了吧……（咽口水）」", "affection": 15},
                {"option": "笑眯眯地看着他：\"排练辛苦啦，今天状态不错嘛。\"", "reply": "「嘿嘿！因为一想到等下能见到你，我跳舞的力气就直接翻倍啦！」", "affection": 20},
                {"option": "假装严肃：\"今天舞步又慢了半拍哦。\"", "reply": "「呜哇，我会好好反省的！作为惩罚，今晚请我吃拉面好不好嘛～」", "affection": 10}
            ],
            2: [
                {"option": "递过去一块毛巾：\"擦擦汗，休息一下吧。\"", "reply": "「谢谢你！每次你递的毛巾都感觉香香的……啊，我是说，有你真好！」", "affection": 18},
                {"option": "开玩笑：\"你的笑容太晃眼啦，练习室开灯了吗？\"", "reply": "「哈哈，因为看到你来了，我的开关就自动开启‘超元气模式’啦！」", "affection": 22},
                {"option": "认真说：\"接下来的声乐部分一起加油！\"", "reply": "「好！只要你在旁边听着，我一定能唱出最完美的音符！」", "affection": 15}
            ],
            3: [
                {"option": "轻声说：\"今天大家都很累，你也是。\"", "reply": "「我不累哦！只要能看到你的笑容，我的电量就永远是百分之百满格！」", "affection": 25},
                {"option": "戳戳他的脸：\"不许笑得这么傻乎乎的。\"", "reply": "「才不傻呢！这是对喜欢的人专属的、最灿烂的笑容哦。」", "affection": 30},
                {"option": "微微脸红避开：\"好啦，快把便当吃完。\"", "reply": "「遵命！把这份爱心便当全部吃光光，然后继续元气满满地陪你！」", "affection": 20}
            ],
            4: [
                {"option": "握住他的手：\"不管未来发生什么，我都支持你。\"", "reply": "「嗯！有你这句话，我的勇气直接爆棚了。以后我们要一起开开心心走下去！」", "affection": 35},
                {"option": "打趣：\"大甜心今天怎么这么温柔。\"", "reply": "「因为面对最重要的人，只想把所有的温柔和甜食全都毫无保留地给你呀。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直很喜欢你的元气。\"", "reply": "「太开心了！听到你这么说，比我吃到限定布丁还要幸福一万倍！」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，要由你来当唯一的男主角。\"", "reply": "「好耶！从今往后，我的每一天、每一餐、每一个舞台，全部都交给你承包啦！」", "affection": 50},
                {"option": "相视一笑：\"这就是最完美的结局。\"", "reply": "「不对哦，这只是我们幸福生活的甜蜜序幕，接下来还要一起吃更多好吃的呢！」", "affection": 45},
                {"option": "调皮眨眼：\"那以后的菜单，可全由我来决定咯！\"", "reply": "「遵命！我的专属主厨大人，我的一切胃口和真心，全听您的指挥！」", "affection": 40}
            ]
        },
        "大酱": {
            1: [
                {"option": "把厚厚的剧本拍在他面前：\"队长大人，别研究电影了，台词还没背完呢。\"", "reply": "「呜哇，被抓包了……不过，有你这个专业监督在，我绝对能超常发挥！」", "affection": 15},
                {"option": "调侃他：\"刚才那段眼神戏，是在对空气练习深情吗？\"", "reply": "「才不是对空气……刚才脑子里想的明明是你，不信你来检查一下？」", "affection": 20},
                {"option": "笑着拿走他的黑咖啡：\"深夜不能喝太多这个。\"", "reply": "「诶，我的精神食粮被没收了……那补偿我一个温柔的笑，我就原谅你。」", "affection": 10}
            ],
            2: [
                {"option": "递过热可可：\"喝点甜的放松一下吧，电影狂热分子。\"", "reply": "「谢谢……每次有你陪着熬夜研读剧本，心里就觉得特别踏实。」", "affection": 18},
                {"option": "开玩笑：\"刚才彩排的告白台词，好像不够真诚哦？\"", "reply": "「不够真诚吗？那换成对你专属的台词：我喜欢你，这句够真诚了吧？」", "affection": 22},
                {"option": "认真拍拍他：\"副队长辛苦啦，接下来交给我。\"", "reply": "「有你这句话，我这个队长当得可太幸福了。并肩作战吧！」", "affection": 15}
            ],
            3: [
                {"option": "轻声呢喃：\"今天片场的氛围，意外地让人心动呢。\"", "reply": "「因为我的视线自始至终都黏在你身上，外面的声音自然就听不见了。」", "affection": 25},
                {"option": "直视他的眼睛：\"好啦，不许用这种犯规的眼神看着我。\"", "reply": "「这可没办法，谁让我的灵感来源和心动对象，全都是你呢。」", "affection": 30},
                {"option": "微微脸红避开：\"导演还在那边看着呢……\"", "reply": "「没关系，让他们看好了……反正我心里眼里，全都是你。」", "affection": 20}
            ],
            4: [
                {"option": "握住他的手：\"不管电影结局如何，我们的故事才刚开始。\"", "reply": "「这句话……我可要当作一辈子的承诺收下了。以后每一幕的主角都是你。」", "affection": 35},
                {"option": "打趣：\"大电影家今天怎么这么会说情话？\"", "reply": "「因为面对真正喜欢的人，根本不需要剧本，所有的台词都是真心话。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等你这句话。\"", "reply": "「太好了……悬着的心终于落下了。接下来，换我来守护你这个专属主角。」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，永远只为你一个人上映。\"", "reply": "「我也是……从今往后，我所有的银幕故事和真实日常，全部由你承包。」", "affection": 50},
                {"option": "相视一笑：\"这就是最完美的结局。\"", "reply": "「不，这只是完美的开端。属于我们的浪漫物语，正准备翻开最甜的一页。」", "affection": 45},
                {"option": "调皮眨眼：\"那接下来的行程单，可要由我来当总导演咯！\"", "reply": "「遵命！我的一切通告和真心，全部听从专属主策划大人的指挥。」", "affection": 40}
            ]
        },
        "流星": {
            1: [
                {"option": "指着化妆镜：\"今天的妆容，好像格外精致呢。\"", "reply": "「哼哼，为了能配得上站在身边的你，我可是花了双倍心思的哦。」", "affection": 15},
                {"option": "调侃他：\"小恶魔今天又在打什么主意？\"", "reply": "「才没有打坏主意……只是在想，等下收工怎么才能顺理成章地让你陪我。」", "affection": 20},
                {"option": "递过草莓大福：\"补充一点糖分，别太累了。\"", "reply": "「哇！奖励收到了！既然你这么贴心，那接下来我也要好好‘照顾’你。」", "affection": 10}
            ],
            2: [
                {"option": "递过去湿纸巾：\"擦擦汗，偶像包袱要掉啦。\"", "reply": "「才不会掉呢！不过……在你面前稍微狼狈一点，好像也没关系。」", "affection": 18},
                {"option": "开玩笑：\"刚才的wink威力太强，后台快融化了。\"", "reply": "「那只对你一个人放电的wink，感觉还满意吗？专属特供哦。」", "affection": 22},
                {"option": "认真点头：\"我会做好你的专属美妆/时尚后盾的！\"", "reply": "「有你这句话，本制作人今天绝对是全场最耀眼的发光体！」", "affection": 15}
            ],
            3: [
                {"option": "轻声说：\"今天台下的荧光海，真的很漂亮。\"", "reply": "「再漂亮也比不过你看着我的眼神……今天最耀眼的风景，只有你一个。」", "affection": 25},
                {"option": "戳戳他的脸：\"不许用这种眼神施展小魔法。\"", "reply": "「被你看穿了呀……因为对你施展的喜欢，从来都是百分之百命中。」", "affection": 30},
                {"option": "微微脸红避开：\"好啦，快去换下一套造型。\"", "reply": "「害羞的样子最可爱了……好啦，不逗你了，等下一定要等我一起走哦。」", "affection": 20}
            ],
            4: [
                {"option": "握住他的手：\"不管走到哪，我都做你最坚定的应援。\"", "reply": "「拉钩不许变！以后无论多少闪光灯，我的视线也只锁定你一个人。」", "affection": 35},
                {"option": "打趣：\"精致的小偶像今天怎么这么粘人。\"", "reply": "「因为在喜欢的人面前，谁想保持高冷啊……真拿你没办法，被你吃得死死的。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等这一刻。\"", "reply": "「太好了……听到你这么说，我悬着的心终于落下了。接下来换我宠你。」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，永远只为你一个人定制。\"", "reply": "「我也是……从今往后，你的每一个日常和浪漫，我都以恋人的身份承包了。」", "affection": 50},
                {"option": "相视一笑：\"这就是最完美的结局。\"", "reply": "「不，这只是序章。属于我们的时尚物语，才刚刚绽放出最甜的色彩。」", "affection": 45},
                {"option": "调皮眨眼：\"那以后的造型和行程，全由我来掌控咯！\"", "reply": "「遵命，我的专属时尚主理人。我的一切，全部听从你的指挥。」", "affection": 40}
            ]
        },
        "米七": {
            1: [
                {"option": "笑着看他：\"大长腿模特，发呆的样子像在拍画报呢。\"", "reply": "「因为脑子里一直在想你……刚才导演叫我名字的时候，差点没回过神来。」", "affection": 15},
                {"option": "调侃他：\"台词又卡壳了吧，纯情的大明星。\"", "reply": "「才没有卡壳……只是面对你的时候，心跳总是会不听指挥地加速。」", "affection": 20},
                {"option": "递过草莓牛奶：\"润润喉，别太紧张。\"", "reply": "「谢谢你……只要喝到你给的牛奶，我的紧张感瞬间就全部消失了。」", "affection": 10}
            ],
            2: [
                {"option": "递过去毛巾：\"辛苦了，外景风很大吧。\"", "reply": "「风确实挺大，但只要看到你在这里等我，心里就觉得暖洋洋的。」", "affection": 18},
                {"option": "开玩笑：\"刚才那场戏的眼神，温柔得快滴出水了哦？\"", "reply": "「因为当时把你想成了心里最重要的人……结果一不小心就演得太真实了。」", "affection": 22},
                {"option": "认真点头：\"接下来的对手戏，我会好好配合你的！\"", "reply": "「有你这句话，我什么都不怕了。接下来的心动戏份，一定最完美。」", "affection": 15}
            ],
            3: [
                {"option": "轻声呢喃：\"今天的落日和微风，都温柔得不像话。\"", "reply": "「嗯，很温柔……但最温柔的，明明是一直在我身边的你。」", "affection": 25},
                {"option": "直视他的眼睛：\"好啦，不许用这种犯规的眼神看着我。\"", "reply": "「我没有犯规……只是想把对你的喜欢，全部毫无保留地通过眼神传达给你。」", "affection": 30},
                {"option": "微微脸红避开：\"时间不早了，我们抓紧背台词。\"", "reply": "「害羞的样子……真的好可爱。好啦，听你的，不过要奖励一个微笑。」", "affection": 20}
            ],
            4: [
                {"option": "坚定握住他的手：\"不管未来多远，我都陪着你。\"", "reply": "「这句话……我记下了。以后无论走到世界的哪一个角落，你都别想离开我。」", "affection": 35},
                {"option": "打趣：\"撕漫男主角今天怎么这么黏人？\"", "reply": "「因为面对喜欢的人，谁没办法保持冷静啊……真拿你没办法，谁让我眼里只有你。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等这一刻。\"", "reply": "「太好了……听到你这么说，悬着的心终于落下了。接下来，换我来守护你。」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，永远只为你一个人盛开。\"", "reply": "「我也是……从今往后，你的每一个日常和四季，我都想以恋人的身份全部承包。」", "affection": 50},
                {"option": "相视一笑：\"这就是我们之间最完美的结局。\"", "reply": "「不，这只是开始。属于我们的纯情物语，才刚刚翻开最动人的序章呢。」", "affection": 45},
                {"option": "调皮眨眼：\"那接下来的行程单，可要由我来制定咯！\"", "reply": "「遵命，我的专属主策划大人。我的一切，全部听从你的指挥。」", "affection": 40}
            ]
        },
        "谦杜": {
            1: [
                {"option": "指着他花里胡哨的卫衣：\"时尚总监今天又穿得这么吸睛。\"", "reply": "「怎么样，本专家的眼光绝对全场最潮吧！不过，最想吸引的人其实是你啦。」", "affection": 15},
                {"option": "调侃他：\"滑板又把裤子蹭破了吧，淘气鬼。\"", "reply": "「才没有！这叫街头艺术的战损风……好啦，别拆穿我嘛，求求专属大人。」", "affection": 20},
                {"option": "递过气泡水：\"快喝一口，别到处乱跑了。\"", "reply": "「谢谢！滋滋冒泡的汽水，就跟我现在看到你时激动的心情一模一样！」", "affection": 10}
            ],
            2: [
                {"option": "递过去毛巾：\"擦擦汗，潮流大佬。\"", "reply": "「谢啦！每次排练累了，只要你递东西过来，我的电量直接满格！」", "affection": 18},
                {"option": "开玩笑：\"刚才的舞蹈走位，好像有一步踩错了吧？\"", "reply": "「诶？！被抓包了……那作为惩罚，收工后陪我去吃限定抹茶芭菲吧！」", "affection": 22},
                {"option": "认真拍拍他：\"接下来的设计企划一起加油！\"", "reply": "「没问题！有你这个灵感缪斯在，我绝对能设计出最棒的舞台战袍！」", "affection": 15}
            ],
            3: [
                {"option": "轻声说：\"今天的涂鸦墙颜色真的很亮眼呢。\"", "reply": "「再亮眼也比不过你刚才对我笑的那一下……我的心都跟着亮起来了。」", "affection": 25},
                {"option": "戳戳他的脸：\"不许用颜料把我的脸弄花。\"", "reply": "「嘿嘿，这样你脸上也有我的专属标记了，我们就是绝配组合！」", "affection": 30},
                {"option": "微微脸红避开：\"好啦，快把工具收拾好。\"", "reply": "「遵命！听专属大人的话，马上收拾干净，然后带你去吃好吃的！」", "affection": 20}
            ],
            4: [
                {"option": "握住他的手：\"不管流行怎么变，我都陪着你。\"", "reply": "「拉钩上吊一百年不许变！以后我的潮流和心意，全部只为你一个人专属开放。」", "affection": 35},
                {"option": "打趣：\"元气潮男今天怎么这么认真。\"", "reply": "「因为面对喜欢的人，怎么可能不认真啊……真拿你没办法，彻底栽在你手里了。」", "affection": 30},
                {"option": "深吸一口气：\"其实，我也一直在等你这句话。\"", "reply": "「太好了……听到你这么说，悬着的心终于落下了。以后我们一起酷到底！」", "affection": 40}
            ],
            5: [
                {"option": "深情告白：\"我的心动企划，永远只为你一个人设计。\"", "reply": "「我也是……从今往后，我的每一个潮酷日常和真心，都以恋人的身份全部承包。」", "affection": 50},
                {"option": "相视一笑：\"这就是最完美的结局。\"", "reply": "「不，这只是狂欢的序幕。属于我们的潮流恋爱物语，才刚刚按下开始键呢。」", "affection": 45},
                {"option": "调皮眨眼：\"那以后的造型和行程，全由我来掌控咯！\"", "reply": "「遵命！我的专属主理人大人，我的一切全听你的指挥！」", "affection": 40}
            ]
        }
    }

    # 动态匹配当前成员的专属池（如果没写到的兜底到丈君）
    default_choices_pools = _member_specific_pools.get(member, _member_specific_pools["丈君"])
    return {
        "title": f"第 {act} 幕：{member} 与 {role} 的专属心动时刻",
        "scene": f"{member} 的专属工作空间 / 浪漫现场（Act {act}）",
        "prologue": prologues_by_act.get(act, f"你是{member}身边的{role}，在第 {act} 幕中，你们迎来了全新的心动转折。"),
        "dialogue_intro": [(member, intro_text)],
        "choices": act_choices
    }

# -----------------------------------------------------------------------------
# 8. 游戏舞台渲染 (Playing & Ending)
# -----------------------------------------------------------------------------
if st.session_state.stage == "playing":
    m = st.session_state.target_member
    r = st.session_state.player_role
    act = st.session_state.current_act
    current_story = get_member_story(m, r, act)

    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("📌 当前主角", m)
    col_s2.metric("🎭 玩家身份", r)
    col_s3.metric("💖 当前心动积分", st.session_state.total_score)

    MAX_ACT = 5
    st.progress(
        act / MAX_ACT, text=f"📖 剧情推进进度：第 {act} 幕 / 共 {MAX_ACT} 幕"
    )
    st.markdown("---")

    if current_story:
        st.markdown(f"### {current_story.get('title', '')}")
        
        if current_story.get("scene"):
            st.caption(f"📍 {current_story['scene']}")
        if current_story.get("prologue"):
            st.write(current_story["prologue"])
            
        if current_story.get("dialogue_intro"):
            for speaker, text in current_story["dialogue_intro"]:
                st.markdown(f"**{speaker}**：{text}")
                
        st.markdown("---")

        if st.session_state.last_dialogue_result:
            choice_c, resp_list, single_reply, f_score = st.session_state.last_dialogue_result
            
            dialogue_html = ""
            if resp_list:
                for speaker, text in resp_list:
                    dialogue_html += f'<p style="margin: 6px 0; color: #9f1239;"><b>{speaker}：</b>{text}</p>'
            elif single_reply:
                dialogue_html += f'<p style="margin: 6px 0; color: #9f1239;"><b>{m}：</b>{single_reply}</p>'
            else:
                dialogue_html += f'<p style="margin: 6px 0; color: #9f1239;"><b>{m}：</b>（温柔地看着你，笑而不语）</p>'

            st.markdown(
                f"""
                <div style="background-color: #fff1f2; border-left: 4px solid #e11d48; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                    <p style="margin: 0 0 8px 0; color: #881337; font-size: 0.95rem;">你的选择： {choice_c}</p>
                    <hr style="border: none; border-top: 1px dashed #fecdd3; margin: 8px 0;">
                    {dialogue_html}
                    <p style="margin: 8px 0 0 0; color: #be123c; font-size: 0.85rem; text-align: right;">✨ 好感度 +{f_score}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("💌 珍藏回忆并进入下一幕", use_container_width=True):
                    st.session_state.last_dialogue_result = None
                    if act < MAX_ACT:
                        st.session_state.current_act += 1
                    else:
                        st.session_state.stage = "ending"
                    st.rerun()
            with col_btn2:
                if st.button("🔄 重新选择当前选项", use_container_width=True):
                    st.session_state.last_dialogue_result = None
                    st.rerun()
        else:
            st.markdown("请做出你的心动回应：")

            for i, choice in enumerate(current_story.get("choices", [])):
                choice_text = choice.get("option", "")
                base_score = choice.get("affection", 0)
                resp_list = choice.get("dialogue_response", None)
                single_reply = choice.get("reply", "")
                
                if st.button(choice_text, key=f"choice_{act}_{i}"):
                    final_score = base_score
                    active_buff = getattr(st.session_state, 'active_buff', None)
                    if active_buff == "🍬 恋爱加倍糖果":
                        final_score *= 2
                        st.session_state.active_buff = None
                    elif active_buff == "🎧 读心耳机":
                        final_score += 15
                        st.session_state.active_buff = None
                    elif active_buff == "🥤 冰爽解暑饮料":
                        final_score += 10
                        st.session_state.active_buff = None
                        
                    st.session_state.total_score += final_score
                    history_reply_text = single_reply if single_reply else (resp_list[0][1] if resp_list else "...")
                    st.session_state.dialogue_history.append(
                        (current_story["title"], choice_text, history_reply_text, final_score)
                    )
                    
                    st.session_state.last_dialogue_result = (choice_text, resp_list, single_reply, final_score)
                    
                    # 随机事件触发逻辑
                    if act < MAX_ACT and random.random() < 0.4:
                        random_events_pool = [
                            {"title": "突发暴雨的屋檐避难", "desc": "两人在回家路上突然遇到倾盆大雨，被迫挤在一个小小的便利店屋檐下，肩膀紧紧贴着……"},
                            {"title": "电台直播的连线袭击", "desc": "工作间隙突然接到了一档电台连线直播，主持人现场要求他对你说一句真心话！"},
                            {"title": "猫咪咖啡厅的意外邂逅", "desc": "排练间隙去咖啡厅休息，一只可爱的布偶猫突然跳进你怀里，引得他吃醋地看着你……"},
                            {"title": "便利店最后一块布丁", "desc": "深夜去买宵夜，冰箱里只剩下最后一份他最爱的限定布丁，你们会怎么分？"},
                            {"title": "📸 文春炮的闪光灯危机", "desc": "深夜在街角散步时，暗处突然闪过一道刺眼的白光！文春记者带着长枪短炮从阴影里冲了出来，你们必须立刻做出反应！"},
                            {"title": "🚨 狂热私生饭的围堵", "desc": "刚结束录制，停车场突然冲出几个情绪激动的私生饭和私家车，死死堵住了去路，他下意识地把你护在了身后……"},
                            {"title": "🎙️ 直播未关麦的社死瞬间", "desc": "以为直播已经切断，他正凑在你耳边小声呢喃情话，结果几万名在线观众把两人的亲密私语听得清清楚楚！"},
                            {"title": "🎭 颁奖后台的擦肩而过", "desc": "在众多同行和媒体云集的颁奖典礼后台，为了避人耳目，你们俩不得不一起躲进了一个狭窄逼仄的杂物间里。"},
                            {"title": "🕶️ 机场同款引发的饭圈地震", "desc": "两人前脚刚一前一后离开机场，后脚就被火眼金睛的粉丝扒出戴了同款情侣项链，热搜瞬间爆了！"},
                        ]
                        st.session_state.random_event = random.choice(random_events_pool)

                        current_event_title = st.session_state.random_event["title"]
                        inventory = getattr(st.session_state, 'inventory', [])

                        if "文春炮" in current_event_title:
                            if "🕵️‍♂️ 黑色鸭舌帽" in inventory:
                                st.success("✨ 【触发道具：黑色鸭舌帽】低调伪装成功！成功避开了文春的镜头！")
                                inventory.remove("🕵️‍♂️ 黑色鸭舌帽")
                                st.session_state.total_score += 10
                            elif "📜 紧急公关手稿" in inventory:
                                st.success("✨ 【触发道具：紧急公关手稿】公关手稿发挥作用，稳住了媒体！")
                                inventory.remove("📜 紧急公关手稿")
                                st.session_state.total_score += 10
                            else:
                                st.session_state.total_score -= 30

                        elif "私生饭" in current_event_title:
                            if "📱 备用双卡手机" in inventory:
                                st.success("✨ 【触发道具：备用双卡手机】及时联络安保人员清场，安全脱身！")
                                inventory.remove("📱 备用双卡手机")
                                st.session_state.total_score += 10
                            else:
                                st.session_state.total_score -= 25

                    st.rerun()

    if st.session_state.dialogue_history:
        with st.expander("📜 查看本局心动回忆录"):
            for h_title, h_c, h_r, h_score in st.session_state.dialogue_history:
                st.markdown(f"**{h_title}**")
                st.markdown(f"*你的选择*：{h_c}")
                st.markdown(f"*{m}的回应*：{h_r} *(+ {h_score} 积分)*")
                st.markdown("---")

    if st.button("🔄 重新选择角色/身份", use_container_width=True):
        st.session_state.stage = "menu"
        st.session_state.last_dialogue_result = None
        st.rerun()

elif st.session_state.stage == "ending":
    m = st.session_state.target_member
    score = st.session_state.total_score

    st.markdown(
        f"""
        <div class="card-box" style="text-align: center;">
            <h2>🎉 恭喜达成完美心动结局！</h2>
            <p style="font-size: 1.1rem; color: #e11d48;">你与 {m} 的专属企划圆满落幕！</p>
            <p>最终累计心动积分：{score} 分</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if score >= 150:
        st.balloons()
        st.success(
            "🌟 **评价：传奇心动恋人**：你们的默契天衣无缝，连空气中都冒著粉红泡泡！"
        )
    elif score >= 100:
        st.success(
            "💖 **评价：甜蜜热恋中**：彼此的心意已经紧紧相连，未来每一天都是情人节！"
        )
    else:
        st.info(
            "✨ **评价：双向奔赴的起点**：虽然还有些青涩，但你们的未来充满无限可能！"
        )

    if st.button("🔄 开启新一轮心动企划", use_container_width=True):
        st.session_state.stage = "menu"
        st.session_state.current_act = 1
        st.session_state.total_score = 30
        st.session_state.dialogue_history = []
        st.session_state.last_dialogue_result = None
        st.rerun()

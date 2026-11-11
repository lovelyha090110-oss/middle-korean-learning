import streamlit as st

st.set_page_config(
    page_title="옛말에서 오늘의 말로",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 탐구용 시제품: 문헌 대조를 통해 확인한 예문만 등록해 대응 표현을 보여 줍니다.
EXAMPLES = {
    "불휘 기픈 남ᄀᆞᆫ": {
        "modern": "뿌리 깊은 나무는",
        "source": "용비어천가 제2장",
        "notes": [
            ("불휘 → 뿌리", "어휘 대응", "중세국어 어휘와 현대국어 어휘의 대응을 보여 주는 예입니다."),
            ("기픈 → 깊은", "형태·표기 비교", "용언 '깊-'이 관형어로 쓰인 형태를 비교합니다."),
            ("남ᄀᆞᆫ → 나무는", "표기·형태 비교", "체언의 표기와 보조사 결합을 비교합니다."),
        ],
    },
    "ᄇᆞᄅᆞ매 아니 뮐ᄊᆡ": {
        "modern": "바람에 아니 흔들리므로",
        "source": "용비어천가 제2장",
        "notes": [
            ("ᄇᆞᄅᆞ매 → 바람에", "표기·형태 비교", "체언의 표기와 부사격 조사 결합을 비교합니다."),
            ("아니 → 아니", "어휘 대응", "부정을 나타내는 표현이 이어지는 모습을 확인합니다."),
            ("뮐ᄊᆡ → 흔들리므로", "어휘·문법 비교", "서술어의 의미와 이유를 나타내는 연결 표현을 비교합니다."),
        ],
    },
    "곶 됴코 여름 하ᄂᆞ니": {
        "modern": "꽃 좋고 열매 많나니",
        "source": "용비어천가 제2장",
        "notes": [
            ("곶 → 꽃", "표기·음운 변화", "중세국어와 현대국어의 표기 및 소리 대응을 살펴봅니다."),
            ("됴코 → 좋고", "음운·형태 비교", "어휘 형태와 연결 어미의 대응을 비교합니다."),
            ("여름 → 열매", "의미 변화", "이 문맥의 '여름'은 계절이 아니라 열매를 뜻합니다."),
        ],
    },
    "ᄉᆡ미 기픈 므른": {
        "modern": "샘이 깊은 물은",
        "source": "용비어천가 제2장",
        "notes": [
            ("ᄉᆡ미 → 샘이", "표기·형태 비교", "체언과 주격 조사의 결합을 비교합니다."),
            ("기픈 → 깊은", "형태·표기 비교", "관형어 형태가 현대국어에서 어떻게 나타나는지 비교합니다."),
            ("므른 → 물은", "표기·형태 비교", "체언의 표기와 보조사 결합을 비교합니다."),
        ],
    },
    "ᄀᆞᄆᆞ래 아니 그츨ᄊᆡ": {
        "modern": "가뭄에 아니 그치므로",
        "source": "용비어천가 제2장",
        "notes": [
            ("ᄀᆞᄆᆞ래 → 가뭄에", "표기·형태 비교", "체언의 표기와 부사격 조사 결합을 비교합니다."),
            ("아니 → 아니", "어휘 대응", "부정을 나타내는 표현을 확인합니다."),
            ("그츨ᄊᆡ → 그치므로", "형태·문법 비교", "서술어와 이유를 나타내는 연결 표현을 비교합니다."),
        ],
    },
    "내히 이러 바ᄅᆞ래 가ᄂᆞ니": {
        "modern": "내가 되어 바다에 가나니",
        "source": "용비어천가 제2장",
        "notes": [
            ("내히 → 내(시내)가", "형태·문맥 비교", "문맥 속 명사의 의미와 주격 조사 결합을 살펴봅니다."),
            ("이러 → 되어", "어휘·형태 비교", "문맥에 따른 서술어의 현대어 대응을 확인합니다."),
            ("바ᄅᆞ래 → 바다에", "어휘·표기 비교", "중세국어 어휘와 현대국어 대응 표현을 비교합니다."),
            ("가ᄂᆞ니 → 가나니", "형태 비교", "서술어의 활용 형태를 비교합니다."),
        ],
    },
}

QUIZ = [
    {
        "q": "『용비어천가』 제2장의 문맥에서 '여름'이 뜻하는 것은?",
        "choices": ["계절인 여름", "열매", "나무"],
        "answer": "열매",
        "why": "이 구절에서 '여름'은 계절이 아니라 열매를 뜻합니다.",
    },
    {
        "q": "'불휘'에 대응하는 현대국어 표현은?",
        "choices": ["뿌리", "꽃", "바람"],
        "answer": "뿌리",
        "why": "'불휘'는 현대국어의 '뿌리'에 대응합니다.",
    },
    {
        "q": "'곶'에 대응하는 현대국어 표현은?",
        "choices": ["물", "꽃", "열매"],
        "answer": "꽃",
        "why": "'곶'은 현대국어의 '꽃'에 대응합니다.",
    },
    {
        "q": "중세국어 문장을 현대국어로 이해할 때 가장 바람직한 방법은?",
        "choices": ["글자만 일대일로 바꾼다", "문맥과 문법 기능도 함께 살핀다", "모르는 부분은 임의로 추측한다"],
        "answer": "문맥과 문법 기능도 함께 살핀다",
        "why": "문장 의미는 어휘뿐 아니라 문맥, 형태, 문법 기능을 함께 고려해야 합니다.",
    },
]

st.markdown("""
<style>
.stApp { background: #faf8f2; }
section[data-testid="stSidebar"] { background: #eee8dc; }
h1, h2, h3 { color: #493b2a; }
div.stButton > button { border-radius: 10px; }
.hero { padding: 1.4rem; border-radius: 18px; background: #eee8dc; }
.small-note { color: #756b5d; font-size: 0.88rem; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📜 학습 메뉴")
page = st.sidebar.radio(
    "학습실 선택",
    ["홈", "문장 변환실", "언어 변화 분석실", "문헌 자료실", "학습 퀴즈"],
)
st.sidebar.divider()
st.sidebar.caption("중세국어 탐구 프로젝트 · 규칙 기반 학습 시제품")

if page == "홈":
    st.title("옛말에서 오늘의 말로")
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.subheader("중세국어 문장의 변화 원리를 탐구하다")
    st.write("문헌 속 중세국어와 현대국어의 대응 표현을 비교하고, 변화 양상을 학습하는 웹 기반 학습 프로그램입니다.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")
    a, b = st.columns(2)
    with a:
        st.info("**① 문장 변환실**\n\n등록된 문헌 예문을 골라 현대국어 대응 표현을 확인합니다.")
        st.info("**② 언어 변화 분석실**\n\n예문 속 어휘와 형태의 대응 및 변화 유형을 살펴봅니다.")
    with b:
        st.info("**③ 문헌 자료실**\n\n『용비어천가』 제2장 예문을 모아 확인합니다.")
        st.info("**④ 학습 퀴즈**\n\n문맥과 언어 변화에 관한 이해도를 점검합니다.")
    st.subheader("탐구의 핵심")
    st.write("중세국어를 현대어로 단순 치환하는 데 그치지 않고, 음운·형태·어휘·문법적 차이를 분석한 뒤 그 결과를 학습 기능으로 연결하는 것이 목표입니다.")
    st.caption("현재는 등록된 예문 중심의 시제품이며, 모든 중세국어 문장을 자동 번역하는 도구는 아닙니다.")

elif page == "문장 변환실":
    st.title("문장 변환실")
    st.write("분석 자료로 등록된 문장을 선택하면 현대국어 대응 표현을 확인할 수 있습니다.")
    choice = st.selectbox("중세국어 문장 선택", list(EXAMPLES.keys()))
    st.markdown("#### 중세국어 원문")
    st.markdown(f"### {choice}")
    if st.button("현대국어 대응 표현 확인", type="primary"):
        item = EXAMPLES[choice]
        st.success(item["modern"])
        st.caption(f"자료: {item['source']} · 등록된 예문의 대응 표현")
    st.divider()
    st.markdown("#### 문장 직접 입력")
    typed = st.text_input("분석하고 싶은 문장을 입력해 보세요.", placeholder="예: 불휘 기픈 남ᄀᆞᆫ")
    if typed:
        normalized = typed.strip()
        if normalized in EXAMPLES:
            st.success(f"등록된 대응 표현: {EXAMPLES[normalized]['modern']}")
        else:
            st.warning("현재 자료실에 등록되지 않은 문장입니다. 정확한 변환을 위해 원문과 문맥을 확인한 뒤 자료를 추가해야 합니다.")

elif page == "언어 변화 분석실":
    st.title("언어 변화 분석실")
    choice = st.selectbox("분석할 문장 선택", list(EXAMPLES.keys()), key="analysis_choice")
    item = EXAMPLES[choice]
    st.markdown(f"**원문:** {choice}")
    st.markdown(f"**현대국어 대응:** {item['modern']}")
    st.caption(f"자료: {item['source']}")
    for old, category, explanation in item["notes"]:
        with st.expander(f"{old} · {category}"):
            st.write(explanation)
    st.info("분석 설명은 학습용 요약입니다. 세부적인 음운사·형태론적 판단은 원문 판본과 전문 주석을 대조해 보완해야 합니다.")

elif page == "문헌 자료실":
    st.title("문헌 자료실")
    st.write("『용비어천가』 제2장의 예문을 중심으로 중세국어와 현대국어의 대응을 살펴봅니다.")
    st.markdown("『용비어천가』는 1447년에 간행된 조선 전기의 문헌입니다.")
    for old, item in EXAMPLES.items():
        with st.expander(f"{item['source']} · {old}"):
            st.markdown(f"**중세국어:** {old}")
            st.markdown(f"**현대국어 대응:** {item['modern']}")
            st.caption("예문 및 현대어 대응은 발표·제출 전에 사용 판본의 원문과 주석을 대조해 확인하세요.")

elif page == "학습 퀴즈":
    st.title("학습 퀴즈")
    st.write("문맥과 어휘 대응에 관한 문제를 풀어 보세요.")
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    for i, q in enumerate(QUIZ):
        st.markdown(f"### 문제 {i + 1}")
        st.write(q["q"])
        st.session_state.answers[i] = st.radio(
            "답 선택",
            q["choices"],
            index=None,
            key=f"answer_{i}",
        )
    if st.button("결과 확인", type="primary"):
        score = 0
        for i, q in enumerate(QUIZ):
            answer = st.session_state.answers.get(i)
            if answer == q["answer"]:
                score += 1
        st.metric("정답 수", f"{score} / {len(QUIZ)}")
        for i, q in enumerate(QUIZ):
            answer = st.session_state.answers.get(i)
            if answer == q["answer"]:
                st.success(f"문제 {i + 1}: 정답 · {q['why']}")
            else:
                st.error(f"문제 {i + 1}: 정답은 '{q['answer']}' · {q['why']}")

st.divider()
st.caption("본 사이트는 중세국어 학습을 위한 탐구용 시제품입니다. 자료와 해설은 문헌 대조 및 전문가 주석을 통해 지속적으로 보완해야 합니다.")

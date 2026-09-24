import time
import streamlit as st

st.title("💄 เกมเติมคำศัพท์หมวดเครื่องสำอาง")

# =====================================================
# 1. กำหนดค่าเริ่มต้นใน session_state
# =====================================================

for i in range(1, 6):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# =====================================================
# 📌 ฟังก์ชันเริ่มเกมใหม่
# =====================================================

def reset_game():
    for i in range(1, 6):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# =====================================================
# 📌 ฟังก์ชันตรวจคำตอบ + แสดงผล
# =====================================================

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):

    st.balloons()

    score = 0

    # ตรวจคำตอบทั้ง 5 ข้อ
    correct_answers = [
        "lipstick",
        "mascara",
        "foundation",
        "blush",
        "perfume"
    ]

    for i in range(5):

        user_answer = answers[i].strip().lower()

        if user_answer == correct_answers[i]:
            st.success(f"✅ ข้อ {i+1}: ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {i+1}: ยังไม่ถูกต้อง "
                f"(คุณตอบ '{answers[i]}')"
            )

    st.info(f"🏆 ได้คะแนนรวม: {score}/5 คะแนน")

    if score == 5:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")

    if st.button("ปิดผลลัพธ์"):
        st.rerun()


# =====================================================
# 2. ปุ่มเริ่มเกม
# =====================================================

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# =====================================================
# 3. แสดงเวลานับถอยหลัง
# =====================================================

if st.session_state.start is not None and not st.session_state.is_ended:

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:

        st.warning(f"⏳ เหลือเวลา: {time_left} วินาที")

    else:

        st.session_state.is_ended = True
        st.rerun()


st.divider()


# =====================================================
# 4. ช่องรับคำตอบ
# =====================================================

ans1 = st.text_input(
    "ข้อ 1: A product used to color your lips. 💄",
    value=st.session_state.ans1_val,
    placeholder="Hint: It starts with L..."
)

ans2 = st.text_input(
    "ข้อ 2: A product used to make your eyelashes look longer and darker. 👁️",
    value=st.session_state.ans2_val,
    placeholder="Hint: It starts with M..."
)

ans3 = st.text_input(
    "ข้อ 3: A product used to make your skin look even and smooth. 🧴",
    value=st.session_state.ans3_val,
    placeholder="Hint: It starts with F..."
)

ans4 = st.text_input(
    "ข้อ 4: A product used to add color to your cheeks. 🌸",
    value=st.session_state.ans4_val,
    placeholder="Hint: It starts with B..."
)

ans5 = st.text_input(
    "ข้อ 5: A liquid with a pleasant smell that you put on your body. 🌷",
    value=st.session_state.ans5_val,
    placeholder="Hint: It starts with P..."
)


# =====================================================
# อัปเดตคำตอบล่าสุดเข้า session_state
# =====================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# =====================================================
# 5. ปุ่มส่งคำตอบ
# =====================================================

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📤 ส่งคำตอบ"):

        st.session_state.is_ended = True

        answers = [
            ans1,
            ans2,
            ans3,
            ans4,
            ans5
        ]

        show_result_dialog(answers)

        st.rerun()


# =====================================================
# 6. แสดง Dialog ผลลัพธ์เมื่อหมดเวลา
# =====================================================

if st.session_state.is_ended:

    answers = [
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
        st.session_state.ans5_val
    ]

    show_result_dialog(answers)


st.divider()

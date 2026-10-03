import streamlit as st

from resume_parser import extract_resume

from resume_analyzer import (
    detect_skills,
    detect_projects,
    detect_experience,
    detect_education,
    detect_certifications,
    detect_achievements
)

from question_engine import (
    generate_full_question_pool,
    get_adaptive_question
)

from answer_evaluator import evaluate_answer


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="IntelliInterview",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "interview_started": False,
    "current_question": None,
    "question_pool": [],
    "used_questions": [],
    "answers": [],
    "last_evaluation": None,
    "current_difficulty": "medium",
    "question_number": 0,
    "total_questions": 10,
    "resume_analyzed": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HEADER
# =========================================================

st.title("🎯 IntelliInterview")

st.markdown(
    """
    ### AI-Powered Resume-Aware Interview Simulator

    Upload your resume and practice a personalized technical interview.
    IntelliInterview analyzes your resume, generates relevant questions,
    evaluates your answers, and adapts the difficulty based on your performance.
    """
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🎯 IntelliInterview")

    st.write("Your interview assistant")

    st.divider()

    st.subheader("How it works")

    st.write("1. 📄 Upload resume")
    st.write("2. 🔍 Analyze resume")
    st.write("3. 🎤 Start interview")
    st.write("4. 💬 Answer questions")
    st.write("5. 📊 Get evaluated")
    st.write("6. 🔄 Difficulty adapts")
    st.write("7. 🏆 View final report")

    st.divider()

    st.caption(
        "IntelliInterview is designed for interview practice "
        "and educational purposes."
    )


# =========================================================
# RESUME UPLOAD
# =========================================================

st.header("📄 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"],
    help="Upload a PDF or DOCX resume."
)


if uploaded_file:

    try:

        # -------------------------------------------------
        # EXTRACT RESUME
        # -------------------------------------------------

        resume_text = extract_resume(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        # -------------------------------------------------
        # ANALYZE RESUME
        # -------------------------------------------------

        skills = detect_skills(resume_text)
        projects = detect_projects(resume_text)
        experience = detect_experience(resume_text)
        education = detect_education(resume_text)
        certifications = detect_certifications(resume_text)
        achievements = detect_achievements(resume_text)

        st.session_state.resume_analyzed = True

        # =================================================
        # RESUME ANALYSIS
        # =================================================

        st.header("🔍 Resume Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.subheader("🛠 Skills")

            if skills:

                for skill in skills:
                    st.write(f"• {skill}")

            else:

                st.write("No specific skills detected.")

        with col2:

            st.subheader("🚀 Projects")

            if projects:

                for project in projects:
                    st.write(f"• {project}")

            else:

                st.write("No projects detected.")

        with col3:

            st.subheader("🎓 Education")

            if education:

                for item in education:
                    st.write(f"• {item}")

            else:

                st.write("No education details detected.")

        col4, col5, col6 = st.columns(3)

        with col4:

            st.subheader("💼 Experience")

            if experience:

                for item in experience:
                    st.write(f"• {item}")

            else:

                st.write("No experience detected.")

        with col5:

            st.subheader("📜 Certifications")

            if certifications:

                for item in certifications:
                    st.write(f"• {item}")

            else:

                st.write("No certifications detected.")

        with col6:

            st.subheader("🏆 Achievements")

            if achievements:

                for item in achievements:
                    st.write(f"• {item}")

            else:

                st.write("No achievements detected.")

        st.divider()

        # =================================================
        # INTERVIEW SETTINGS
        # =================================================

        if not st.session_state.interview_started:

            st.header("🎤 Interview Settings")

            col1, col2 = st.columns(2)

            with col1:

                difficulty = st.selectbox(
                    "Starting difficulty",
                    ["easy", "medium", "hard"],
                    index=1
                )

            with col2:

                number_of_questions = st.slider(
                    "Number of questions",
                    5,
                    15,
                    10
                )

            st.write("")

            if st.button(
                "🚀 Start Interview",
                use_container_width=True
            ):

                question_pool = generate_full_question_pool(
                    skills,
                    projects
                )

                first_question = get_adaptive_question(
                    question_pool,
                    difficulty,
                    []
                )

                if first_question is None:

                    st.error(
                        "Could not generate interview questions."
                    )

                else:

                    st.session_state.interview_started = True

                    st.session_state.question_pool = (
                        question_pool
                    )

                    st.session_state.used_questions = [
                        first_question["question"]
                    ]

                    st.session_state.current_question = (
                        first_question
                    )

                    st.session_state.answers = []

                    st.session_state.last_evaluation = None

                    st.session_state.current_difficulty = (
                        difficulty
                    )

                    st.session_state.question_number = 1

                    st.session_state.total_questions = (
                        number_of_questions
                    )

                    st.rerun()

        # =================================================
        # INTERVIEW
        # =================================================

        if st.session_state.interview_started:

            st.divider()

            st.header("🎤 Interview in Progress")

            current_question = (
                st.session_state.current_question
            )

            question_number = (
                st.session_state.question_number
            )

            total_questions = (
                st.session_state.total_questions
            )

            current_difficulty = (
                st.session_state.current_difficulty
            )

            # ------------------------------------------------
            # PROGRESS
            # ------------------------------------------------

            progress = (
                question_number / total_questions
            )

            st.progress(
                min(progress, 1.0)
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Question",
                    f"{question_number}/{total_questions}"
                )

            with col2:

                st.metric(
                    "Topic",
                    current_question["skill"]
                )

            with col3:

                st.metric(
                    "Difficulty",
                    current_difficulty.upper()
                )

            st.divider()

            # ------------------------------------------------
            # QUESTION
            # ------------------------------------------------

            st.subheader(
                f"Question {question_number}"
            )

            st.info(
                current_question["question"]
            )

            answer = st.text_area(
                "Your Answer",
                height=180,
                placeholder=(
                    "Explain your answer clearly. "
                    "You can include examples where appropriate."
                )
            )

            if st.button(
                "Submit Answer",
                use_container_width=True
            ):

                if not answer.strip():

                    st.warning(
                        "Please enter an answer before submitting."
                    )

                else:

                    # -----------------------------------------
                    # EVALUATION
                    # -----------------------------------------

                    evaluation = evaluate_answer(
                        answer,
                        current_question["keywords"]
                    )

                    st.session_state.last_evaluation = (
                        evaluation
                    )

                    # -----------------------------------------
                    # SAVE ANSWER
                    # -----------------------------------------

                    st.session_state.answers.append(
                        {
                            "question": (
                                current_question["question"]
                            ),
                            "answer": answer,
                            "skill": current_question["skill"],
                            "difficulty": current_difficulty,
                            "score": evaluation["score"]
                        }
                    )

                    score = evaluation["score"]

                    # -----------------------------------------
                    # ADAPT DIFFICULTY
                    # -----------------------------------------

                    levels = [
                        "easy",
                        "medium",
                        "hard"
                    ]

                    current_index = levels.index(
                        current_difficulty
                    )

                    if score >= 80:

                        next_index = min(
                            current_index + 1,
                            2
                        )

                        next_difficulty = levels[
                            next_index
                        ]

                    elif score < 50:

                        next_index = max(
                            current_index - 1,
                            0
                        )

                        next_difficulty = levels[
                            next_index
                        ]

                    else:

                        next_difficulty = (
                            current_difficulty
                        )

                    # -----------------------------------------
                    # NEXT QUESTION
                    # -----------------------------------------

                    next_question = get_adaptive_question(
                        st.session_state.question_pool,
                        next_difficulty,
                        st.session_state.used_questions
                    )

                    # -----------------------------------------
                    # FINISH INTERVIEW
                    # -----------------------------------------

                    if (
                        question_number
                        >= total_questions
                        or next_question is None
                    ):

                        st.session_state.interview_started = False

                        st.rerun()

                    else:

                        st.session_state.current_difficulty = (
                            next_difficulty
                        )

                        st.session_state.current_question = (
                            next_question
                        )

                        st.session_state.used_questions.append(
                            next_question["question"]
                        )

                        st.session_state.question_number += 1

                        st.rerun()

        # =================================================
        # LAST ANSWER FEEDBACK
        # =================================================

        if (
            st.session_state.interview_started
            and st.session_state.last_evaluation
        ):

            evaluation = (
                st.session_state.last_evaluation
            )

            st.divider()

            st.subheader(
                "📊 Previous Answer Evaluation"
            )

            score = evaluation["score"]

            if score >= 80:

                st.success(
                    f"Score: {score}/100 — Excellent answer!"
                )

            elif score >= 50:

                st.info(
                    f"Score: {score}/100 — Good effort!"
                )

            else:

                st.warning(
                    f"Score: {score}/100 — "
                    "There are some concepts to improve."
                )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Concept Score",
                    evaluation["concept_score"]
                )

            with col2:

                st.metric(
                    "Answer Length Score",
                    evaluation["length_score"]
                )

            if evaluation["matched_keywords"]:

                st.write(
                    "✅ **Concepts detected:** "
                    + ", ".join(
                        evaluation["matched_keywords"]
                    )
                )

            if evaluation["missing_keywords"]:

                st.write(
                    "💡 **Concepts to improve:** "
                    + ", ".join(
                        evaluation["missing_keywords"]
                    )
                )

            st.write(
                "**Feedback:**",
                evaluation["feedback"]
            )

        # =================================================
        # FINAL REPORT
        # =================================================

        if (
            not st.session_state.interview_started
            and st.session_state.answers
        ):

            st.divider()

            st.header("🏆 Final Interview Report")

            answers = st.session_state.answers

            scores = [
                item["score"]
                for item in answers
            ]

            overall_score = (
                sum(scores) / len(scores)
            )

            # ------------------------------------------------
            # MAIN SCORE
            # ------------------------------------------------

            st.subheader("Overall Performance")

            score_col1, score_col2, score_col3 = st.columns(3)

            with score_col1:

                st.metric(
                    "Overall Score",
                    f"{overall_score:.1f}/100"
                )

            with score_col2:

                st.metric(
                    "Questions Answered",
                    len(answers)
                )

            with score_col3:

                strongest_score = max(scores)

                st.metric(
                    "Highest Score",
                    f"{strongest_score}/100"
                )

            # ------------------------------------------------
            # PERFORMANCE MESSAGE
            # ------------------------------------------------

            if overall_score >= 80:

                st.success(
                    "Strong interview performance. "
                    "Your answers demonstrated good understanding "
                    "of the concepts covered."
                )

            elif overall_score >= 60:

                st.info(
                    "Good interview performance. "
                    "You demonstrated a useful foundation, "
                    "with some concepts that could be strengthened."
                )

            else:

                st.warning(
                    "This interview highlighted several areas "
                    "that would benefit from additional practice."
                )

            # ------------------------------------------------
            # SCORE PROGRESS
            # ------------------------------------------------

            st.subheader("📈 Score Progression")

            for index, item in enumerate(
                answers,
                start=1
            ):

                st.write(
                    f"Question {index}: "
                    f"{item['score']}/100"
                )

                st.progress(
                    item["score"] / 100
                )

            # ------------------------------------------------
            # TOPIC PERFORMANCE
            # ------------------------------------------------

            st.subheader("📚 Topic Performance")

            topic_scores = {}

            for item in answers:

                topic = item["skill"]

                if topic not in topic_scores:
                    topic_scores[topic] = []

                topic_scores[topic].append(
                    item["score"]
                )

            for topic, topic_score_list in (
                topic_scores.items()
            ):

                average = (
                    sum(topic_score_list)
                    / len(topic_score_list)
                )

                st.write(
                    f"**{topic}** — "
                    f"{average:.1f}/100"
                )

                st.progress(
                    average / 100
                )

            # ------------------------------------------------
            # STRENGTHS
            # ------------------------------------------------

            st.subheader("💪 Strong Areas")

            strong_answers = [
                item for item in answers
                if item["score"] >= 80
            ]

            if strong_answers:

                for item in strong_answers:

                    st.write(
                        f"• {item['skill']} — "
                        f"{item['score']}/100"
                    )

            else:

                st.write(
                    "No answers reached the strong-performance "
                    "threshold yet. Keep practicing!"
                )

            # ------------------------------------------------
            # AREAS TO IMPROVE
            # -
            st.subheader("📌 Areas to Improve")

            weak_answers = [
                item for item in answers
                if item["score"] < 50
            ]

            if weak_answers:

                for item in weak_answers:

                    st.write(
                        f"• {item['skill']} — "
                        f"{item['score']}/100"
                    )

            else:

                st.write(
                    "No answers fell below the improvement "
                    "threshold."
                )

            # ------------------------------------------------
            # QUESTION HISTORY
            # ------------------------------------------------

            st.subheader("📋 Question History")

            for index, item in enumerate(
                answers,
                start=1
            ):

                with st.expander(
                    f"Question {index} — "
                    f"{item['score']}/100"
                ):

                    st.write(
                        "**Question:**",
                        item["question"]
                    )

                    st.write(
                        "**Topic:**",
                        item["skill"]
                    )

                    st.write(
                        "**Difficulty:**",
                        item["difficulty"]
                    )

                    st.write(
                        "**Your Answer:**",
                        item["answer"]
                    )

                    st.write(
                        "**Score:**",
                        f"{item['score']}/100"
                    )

            # ------------------------------------------------
            # RESTART
            # ------------------------------------------------

            st.divider()

            if st.button(
                "🔄 Start New Interview",
                use_container_width=True
            ):

                st.session_state.interview_started = False
                st.session_state.current_question = None
                st.session_state.question_pool = []
                st.session_state.used_questions = []
                st.session_state.answers = []
                st.session_state.last_evaluation = None
                st.session_state.current_difficulty = "medium"
                st.session_state.question_number = 0

                st.rerun()


    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )
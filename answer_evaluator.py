import re


# --------------------------------------------------
# TEXT NORMALIZATION
# --------------------------------------------------

def normalize_text(text):
    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# --------------------------------------------------
# CHECK WHETHER CONCEPT IS PRESENT
# --------------------------------------------------

def concept_present(answer, keyword):

    answer = normalize_text(answer)
    keyword = normalize_text(keyword)

    # Direct match
    if keyword in answer:
        return True

    # Simple synonym/concept matching
    synonyms = {

        "mutable": [
            "can be changed",
            "can change",
            "modifiable",
            "modified"
        ],

        "immutable": [
            "cannot be changed",
            "cannot change",
            "unchangeable"
        ],

        "programming language": [
            "language",
            "coding language"
        ],

        "database": [
            "data storage",
            "data management"
        ],

        "prediction": [
            "predict",
            "forecast"
        ],

        "project": [
            "application",
            "system",
            "implementation"
        ],

        "solution": [
            "solved",
            "fix",
            "approach"
        ],

        "experience": [
            "worked",
            "used",
            "developed"
        ]
    }

    if keyword in synonyms:

        for synonym in synonyms[keyword]:

            if synonym in answer:
                return True

    return False


# --------------------------------------------------
# ANSWER LENGTH SCORE
# --------------------------------------------------

def calculate_length_score(answer):

    words = answer.split()

    word_count = len(words)

    if word_count < 5:
        return 20

    elif word_count < 15:
        return 50

    elif word_count < 30:
        return 80

    else:
        return 100


# --------------------------------------------------
# MAIN EVALUATION FUNCTION
# --------------------------------------------------

def evaluate_answer(answer, expected_keywords):

    if not answer or not answer.strip():

        return {
            "score": 0,
            "concept_score": 0,
            "length_score": 0,
            "matched_keywords": [],
            "missing_keywords": expected_keywords,
            "feedback": "No answer was provided."
        }


    # Normalize answer
    answer_clean = normalize_text(answer)


    # --------------------------------------------------
    # CHECK CONCEPTS
    # --------------------------------------------------

    matched_keywords = []

    missing_keywords = []


    for keyword in expected_keywords:

        if concept_present(
            answer_clean,
            keyword
        ):

            matched_keywords.append(
                keyword
            )

        else:

            missing_keywords.append(
                keyword
            )


    # --------------------------------------------------
    # CONCEPT SCORE
    # --------------------------------------------------

    if expected_keywords:

        concept_score = int(
            (
                len(matched_keywords)
                /
                len(expected_keywords)
            )
            * 100
        )

    else:

        concept_score = 50


    # --------------------------------------------------
    # LENGTH SCORE
    # --------------------------------------------------

    length_score = calculate_length_score(
        answer
    )


    # --------------------------------------------------
    # FINAL SCORE
    # --------------------------------------------------

    final_score = int(
        (
            concept_score * 0.75
            +
            length_score * 0.25
        )
    )


    # --------------------------------------------------
    # FEEDBACK
    # --------------------------------------------------

    if final_score >= 85:

        feedback = (
            "Excellent answer. You demonstrated "
            "a strong understanding of the topic "
            "and covered the important concepts."
        )

    elif final_score >= 70:

        feedback = (
            "Good answer. You demonstrated "
            "a reasonable understanding of the topic. "
            "Adding more technical detail would make "
            "your answer stronger."
        )

    elif final_score >= 50:

        feedback = (
            "Your answer shows some understanding, "
            "but several important concepts are missing. "
            "Try to explain the topic more clearly."
        )

    else:

        feedback = (
            "Your answer needs improvement. "
            "Review the basic concepts and try to "
            "give a more complete explanation."
        )


    # --------------------------------------------------
    # ADD MISSING CONCEPTS
    # --------------------------------------------------

    if missing_keywords:

        feedback += (
            "\n\nConcepts to improve: "
            +
            ", ".join(
                missing_keywords
            )
        )


    # --------------------------------------------------
    # ADD STRENGTHS
    # --------------------------------------------------

    if matched_keywords:

        strengths = (
            "\n\nConcepts covered: "
            +
            ", ".join(
                matched_keywords
            )
        )

        feedback += strengths


    return {

        "score": final_score,

        "concept_score": concept_score,

        "length_score": length_score,

        "matched_keywords": matched_keywords,

        "missing_keywords": missing_keywords,

        "feedback": feedback
    }
# question_engine.py

QUESTION_DATABASE = {

    "Python": {
        "easy": [
            {
                "question": "What is Python and where is it commonly used?",
                "keywords": ["programming language", "general purpose", "web", "data", "automation"]
            },
            {
                "question": "What are variables in Python?",
                "keywords": ["variable", "store", "value", "data"]
            }
        ],

        "medium": [
            {
                "question": "What is the difference between a list and a tuple in Python?",
                "keywords": ["list", "tuple", "mutable", "immutable"]
            },
            {
                "question": "What are Python dictionaries and how are they used?",
                "keywords": ["dictionary", "key", "value", "mapping"]
            }
        ],

        "hard": [
            {
                "question": "Explain how exception handling works in Python.",
                "keywords": ["try", "except", "finally", "error", "exception"]
            },
            {
                "question": "Explain the difference between shallow copy and deep copy in Python.",
                "keywords": ["shallow", "deep", "copy", "reference", "object"]
            }
        ]
    },

    "SQL": {
        "easy": [
            {
                "question": "What is SQL?",
                "keywords": ["structured query language", "database", "query"]
            },
            {
                "question": "What is a table in a database?",
                "keywords": ["table", "rows", "columns", "data"]
            }
        ],

        "medium": [
            {
                "question": "What is the difference between WHERE and HAVING in SQL?",
                "keywords": ["where", "having", "filter", "group", "aggregate"]
            },
            {
                "question": "Explain the difference between INNER JOIN and LEFT JOIN.",
                "keywords": ["inner join", "left join", "matching", "rows"]
            }
        ],

        "hard": [
            {
                "question": "What is database normalization and why is it useful?",
                "keywords": ["normalization", "redundancy", "database", "tables"]
            },
            {
                "question": "How would you optimize a slow SQL query?",
                "keywords": ["index", "query", "execution", "optimization", "database"]
            }
        ]
    },

    "Machine Learning": {
        "easy": [
            {
                "question": "What is Machine Learning?",
                "keywords": ["machine learning", "data", "model", "prediction"]
            },
            {
                "question": "What is the difference between supervised and unsupervised learning?",
                "keywords": ["supervised", "unsupervised", "label", "data"]
            }
        ],

        "medium": [
            {
                "question": "What is overfitting in Machine Learning?",
                "keywords": ["overfitting", "training", "test", "generalization"]
            },
            {
                "question": "What is the purpose of splitting data into training and testing sets?",
                "keywords": ["training", "testing", "model", "evaluation"]
            }
        ],

        "hard": [
            {
                "question": "Explain the bias-variance tradeoff.",
                "keywords": ["bias", "variance", "model", "overfitting", "underfitting"]
            },
            {
                "question": "How would you handle an imbalanced classification dataset?",
                "keywords": ["imbalanced", "class", "sampling", "smote", "weight"]
            }
        ]
    },

    "R": {
        "easy": [
            {
                "question": "What is R programming mainly used for?",
                "keywords": ["r", "statistics", "data", "analysis"]
            }
        ],

        "medium": [
            {
                "question": "What are data frames in R?",
                "keywords": ["data frame", "rows", "columns", "data"]
            }
        ],

        "hard": [
            {
                "question": "Explain how R can be used for statistical modeling.",
                "keywords": ["r", "statistical", "model", "analysis"]
            }
        ]
    },

    "HTML": {
        "easy": [
            {
                "question": "What is HTML?",
                "keywords": ["html", "markup", "web", "structure"]
            }
        ],

        "medium": [
            {
                "question": "What is the difference between div and semantic HTML elements?",
                "keywords": ["div", "semantic", "structure", "header", "section"]
            }
        ],

        "hard": [
            {
                "question": "How would you improve the accessibility of an HTML page?",
                "keywords": ["accessibility", "semantic", "aria", "screen reader"]
            }
        ]
    },

    "CSS": {
        "easy": [
            {
                "question": "What is CSS used for?",
                "keywords": ["css", "style", "design", "web"]
            }
        ],

        "medium": [
            {
                "question": "Explain the CSS box model.",
                "keywords": ["box model", "margin", "border", "padding", "content"]
            }
        ],

        "hard": [
            {
                "question": "What is CSS specificity and how does it affect styling?",
                "keywords": ["specificity", "selector", "style", "priority"]
            }
        ]
    },

    "JavaScript": {
        "easy": [
            {
                "question": "What is JavaScript?",
                "keywords": ["javascript", "programming", "web", "browser"]
            }
        ],

        "medium": [
            {
                "question": "What is the difference between let, const and var?",
                "keywords": ["let", "const", "var", "variable", "scope"]
            }
        ],

        "hard": [
            {
                "question": "Explain asynchronous programming in JavaScript.",
                "keywords": ["asynchronous", "promise", "async", "await", "callback"]
            }
        ]
    }
}


def get_questions_for_skill(skill, difficulty):
    """
    Return questions for a known skill and difficulty.
    """

    if skill in QUESTION_DATABASE:
        questions = QUESTION_DATABASE[skill].get(difficulty, [])

        result = []

        for question in questions:
            result.append({
                "question": question["question"],
                "keywords": question["keywords"],
                "skill": skill,
                "type": "skill",
                "difficulty": difficulty
            })

        return result

    return []


def generate_generic_skill_questions(skill, difficulty):
    """
    Generate questions for skills that are not in our database.
    """

    questions = {

        "easy": [
            {
                "question": f"What is {skill}, and where is it commonly used?",
                "keywords": [skill.lower(), "used", "purpose"]
            },
            {
                "question": f"Why did you learn or use {skill}?",
                "keywords": [skill.lower(), "learn", "use", "purpose"]
            }
        ],

        "medium": [
            {
                "question": f"Explain how you have used {skill} in a practical situation.",
                "keywords": [skill.lower(), "used", "project", "application"]
            },
            {
                "question": f"What are some important features or concepts of {skill}?",
                "keywords": [skill.lower(), "features", "concepts"]
            }
        ],

        "hard": [
            {
                "question": f"What challenges can occur when using {skill}, and how would you solve them?",
                "keywords": [skill.lower(), "challenge", "problem", "solution"]
            },
            {
                "question": f"Describe an advanced use case of {skill} and explain your approach.",
                "keywords": [skill.lower(), "advanced", "approach", "solution"]
            }
        ]
    }

    result = []

    for question in questions.get(difficulty, []):
        result.append({
            "question": question["question"],
            "keywords": question["keywords"],
            "skill": skill,
            "type": "skill",
            "difficulty": difficulty
        })

    return result


def generate_skill_questions(skills, difficulty):
    """
    Generate questions for all detected skills.
    """

    questions = []

    for skill in skills:

        known_questions = get_questions_for_skill(skill, difficulty)

        if known_questions:
            questions.extend(known_questions)
        else:
            questions.extend(
                generate_generic_skill_questions(skill, difficulty)
            )

    return questions


def generate_project_questions(projects, difficulty):
    """
    Generate questions based on projects from the resume.
    """

    questions = []

    for project in projects:

        if difficulty == "easy":
            question = f"What was the main objective of your project '{project}'?"
            keywords = [
                "project",
                "objective",
                "goal",
                "purpose"
            ]

        elif difficulty == "medium":
            question = f"What technologies did you use in '{project}' and why did you choose them?"
            keywords = [
                "project",
                "technology",
                "technologies",
                "used",
                "reason"
            ]

        else:
            question = f"What was the most challenging part of '{project}', and how did you solve it?"
            keywords = [
                "project",
                "challenge",
                "problem",
                "solution",
                "solved"
            ]

        questions.append({
            "question": question,
            "keywords": keywords,
            "skill": "Project",
            "type": "project",
            "difficulty": difficulty
        })

    return questions


def generate_hr_questions(difficulty):

    if difficulty == "easy":
        return [
            {
                "question": "Tell me about yourself.",
                "keywords": ["education", "skills", "experience", "project"],
                "skill": "HR",
                "type": "hr",
                "difficulty": "easy"
            }
        ]

    elif difficulty == "medium":
        return [
            {
                "question": "Why are you interested in this role?",
                "keywords": ["interest", "skills", "career", "role"],
                "skill": "HR",
                "type": "hr",
                "difficulty": "medium"
            }
        ]

    else:
        return [
            {
                "question": "Describe a difficult problem you faced and how you handled it.",
                "keywords": ["problem", "challenge", "solution", "result"],
                "skill": "HR",
                "type": "hr",
                "difficulty": "hard"
            }
        ]


def generate_interview_questions(
    skills,
    projects,
    difficulty="medium",
    number_of_questions=10
):
    """
    Generate the initial interview question list.
    """

    questions = []

    questions.extend(
        generate_skill_questions(skills, difficulty)
    )

    questions.extend(
        generate_project_questions(projects, difficulty)
    )

    questions.extend(
        generate_hr_questions(difficulty)
    )

    return questions[:number_of_questions]


def generate_full_question_pool(skills, projects):
    """
    Generate questions at all difficulty levels.
    This is used by the adaptive interview.
    """

    pool = []

    for difficulty in ["easy", "medium", "hard"]:

        pool.extend(
            generate_skill_questions(
                skills,
                difficulty
            )
        )

        pool.extend(
            generate_project_questions(
                projects,
                difficulty
            )
        )

        pool.extend(
            generate_hr_questions(
                difficulty
            )
        )

    return pool


def get_adaptive_question(
    question_pool,
    target_difficulty,
    used_questions
):
    """
    Select an unused question matching the requested difficulty.
    """

    matching_questions = [
        q for q in question_pool
        if q["difficulty"] == target_difficulty
        and q["question"] not in used_questions
    ]

    if matching_questions:
        return matching_questions[0]

    # If no question exists at the requested difficulty,
    # use any unused question.
    remaining_questions = [
        q for q in question_pool
        if q["question"] not in used_questions
    ]

    if remaining_questions:
        return remaining_questions[0]

    return None
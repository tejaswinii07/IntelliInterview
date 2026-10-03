import re


# --------------------------------------------------
# SECTION NAMES
# --------------------------------------------------

SECTION_ALIASES = {

    "skills": [
        "skills",
        "technical skills",
        "technical skill",
        "core skills",
        "key skills",
        "professional skills",
        "competencies",
        "areas of expertise",
        "expertise",
        "technologies",
        "technical competencies"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
        "major projects",
        "project experience"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "work history",
        "internship",
        "internships"
    ],

    "education": [
        "education",
        "academic background",
        "educational qualification",
        "qualifications",
        "academic qualifications"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses",
        "training",
        "courses"
    ],

    "achievements": [
        "achievements",
        "awards",
        "honors",
        "accomplishments"
    ]
}


# --------------------------------------------------
# NORMALIZE TEXT
# --------------------------------------------------

def normalize_text(text):

    text = text.replace("\r", "\n")

    # Replace multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# --------------------------------------------------
# IDENTIFY SECTION
# --------------------------------------------------

def identify_section(line):

    clean_line = line.strip().lower()

    # Remove common symbols
    clean_line = re.sub(r"[^a-zA-Z ]", "", clean_line)

    clean_line = clean_line.strip()

    for section, aliases in SECTION_ALIASES.items():

        for alias in aliases:

            if clean_line == alias.lower():

                return section

    return None


# --------------------------------------------------
# EXTRACT SECTIONS
# --------------------------------------------------

def extract_sections(text):

    text = normalize_text(text)

    lines = text.split("\n")

    sections = {

        "skills": [],
        "projects": [],
        "experience": [],
        "education": [],
        "certifications": [],
        "achievements": []

    }

    current_section = None

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        detected_section = identify_section(clean_line)

        if detected_section:

            current_section = detected_section
            continue

        if current_section:

            sections[current_section].append(clean_line)

    return sections


# --------------------------------------------------
# CLEAN SKILL ITEMS
# --------------------------------------------------

def clean_skill_item(item):

    item = item.strip()

    # Remove bullets
    item = re.sub(
        r"^[•●▪◦\-–—*]+",
        "",
        item
    )

    # Remove numbering
    item = re.sub(
        r"^\d+[\.\)]\s*",
        "",
        item
    )

    item = item.strip()

    return item


# --------------------------------------------------
# EXTRACT SKILLS
# --------------------------------------------------

def detect_skills(text):

    sections = extract_sections(text)

    skill_lines = sections["skills"]

    skills = []

    for line in skill_lines:

        # Many resumes use commas, | or semicolons
        items = re.split(
            r"[,;|]",
            line
        )

        for item in items:

            skill = clean_skill_item(item)

            if len(skill) >= 2:

                if skill.lower() not in [
                    s.lower() for s in skills
                ]:

                    skills.append(skill)

    return skills


# --------------------------------------------------
# EXTRACT PROJECTS
# --------------------------------------------------

def detect_projects(text):

    sections = extract_sections(text)

    project_lines = sections["projects"]

    projects = []

    for line in project_lines:

        line = clean_skill_item(line)

        if len(line) >= 3:

            if line.lower() not in [
                p.lower() for p in projects
            ]:

                projects.append(line)

    return projects


# --------------------------------------------------
# EXTRACT EXPERIENCE
# --------------------------------------------------

def detect_experience(text):

    sections = extract_sections(text)

    experience = []

    for line in sections["experience"]:

        line = clean_skill_item(line)

        if len(line) >= 3:

            experience.append(line)

    return experience


# --------------------------------------------------
# EXTRACT EDUCATION
# --------------------------------------------------

def detect_education(text):

    sections = extract_sections(text)

    education = []

    for line in sections["education"]:

        line = clean_skill_item(line)

        if len(line) >= 3:

            education.append(line)

    return education


# --------------------------------------------------
# EXTRACT CERTIFICATIONS
# --------------------------------------------------

def detect_certifications(text):

    sections = extract_sections(text)

    certifications = []

    for line in sections["certifications"]:

        line = clean_skill_item(line)

        if len(line) >= 3:

            certifications.append(line)

    return certifications


# --------------------------------------------------
# EXTRACT ACHIEVEMENTS
# --------------------------------------------------

def detect_achievements(text):

    sections = extract_sections(text)

    achievements = []

    for line in sections["achievements"]:

        line = clean_skill_item(line)

        if len(line) >= 3:

            achievements.append(line)

    return achievements
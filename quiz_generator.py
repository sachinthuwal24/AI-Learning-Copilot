from roadmap_generator import model

def generate_quiz(topic):

    prompt = f"""
    Create a quiz on {topic}

    Give 5 MCQs.

    Format:

    Question:
    A)
    B)
    C)
    D)

    Correct Answer:
    """

    response = model.generate_content(prompt)

    return response.text
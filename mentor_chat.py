from roadmap_generator import model

def ask_mentor(question):

    prompt = f"""
    You are an expert teacher.

    Explain in a simple way.

    Question:
    {question}

    Give:
    1. Explanation
    2. Example
    3. Real World Use Case
    """

    response = model.generate_content(prompt)

    return response.text
def recommend_topics(topic):

    recommendations = {

        "python": [
            "NumPy",
            "Pandas",
            "OOP",
            "Data Structures"
        ],

        "cpp": [
            "Pointers",
            "STL",
            "OOP",
            "Competitive Programming"
        ],

        "machine learning": [
            "Scikit-learn",
            "Deep Learning",
            "TensorFlow",
            "PyTorch"
        ],

        "web development": [
            "JavaScript",
            "React",
            "Node.js",
            "MongoDB"
        ]
    }

    return recommendations.get(
        topic.lower(),
        ["AI", "Data Science", "Cloud Computing"]
    )
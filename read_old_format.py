import json


def get_qa(path):
    questions = []
    answers = []
    with open(path, 'r', encoding='utf-8') as file:
        # Read each line in the file
        for line in file:
            # Process the line (e.g., print it)
            item = json.loads(line)
            questions.append(item["content"])
            answers.append(item["summary"])
    return questions, answers
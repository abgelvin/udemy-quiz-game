from data import question_data
from question_model import Question


question_list = [
    Question(question['text'], question['answer']) for question in question_data
]


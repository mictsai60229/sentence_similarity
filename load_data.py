import os

directory = "answers"

def load_answer(idx):
    return [line for line in open(os.path.join(directory, "%s.txt" %(idx)))]
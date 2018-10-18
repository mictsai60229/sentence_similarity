import operator
import math
# flask
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# my model
import predictor
import splitter
import load_data

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)



'''
request json

{"response" : doc}

'''
@app.route('/', methods=['POST'])
def answer():
    data = request.get_json()
    
    if not data: return jsonify({'status': 'wrong'})
    
    answers = main_process(data)
    
    
    return jsonify(answers)


answer = load_data.load_answer("2")
answer = [splitter.character_splitter(line) for line in answer]
answer = [line for line in answer if line]


def compute_doc(correct, unscored):
    
    doc_similarity = []
    for line1 in unscored:
        len1 = len(line1)
        similarity = []
        for line2 in correct:
            len2 = len(line2)
            predict_json = predictor.predictor.predict(
                hypothesis=line1,
                premise=line2
            )
            similarity.append(predict_json['label_probs'][0])
        
        max_index, max_value = max(enumerate(similarity), key=operator.itemgetter(1))
        doc_similarity.append((line1, correct[max_index], max_value))
    
    return doc_similarity
            
        

def main_process(data):
    
    response = data['response']
    response = splitter.line_splitter(response)
    response = [splitter.character_splitter(line) for line in response]
    response = [line for line in response if line]
    
    
    doc_similarity = compute_doc(answer, response)
    
    return doc_similarity
    



if __name__ == "__main__":
    
    
    app.run(host='0.0.0.0', port=1315)
    
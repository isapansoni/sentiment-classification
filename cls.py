from transformers import pipeline


classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
#classifier = pipeline("text-classification",model='bin/distilbert-base-uncased-emotion')



def prediction_return(input_string):

    prediction = classifier(input_string)
    return prediction


op = prediction_return('I am very happy today')

print(op)
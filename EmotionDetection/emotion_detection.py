import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)

    STATUS_CODE = response.status_code

    
    if STATUS_CODE is 400:
        return {
        'anger' : None,
        'disgust' : None,
        'fear' : None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    output = {
        'anger' : emotions['anger'],
        'disgust' : emotions['disgust'],
        'fear' : emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }

    return output
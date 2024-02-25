import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header,timeout=10)
    if(response.status_code == 400):
        return  {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)
    anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear= formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy= formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness= formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    score_array = formatted_response["emotionPredictions"][0]["emotion"]
    score_list = list(score_array.values())
    max_index=0
    
    for index,value in enumerate(score_list):
        if value > score_list[max_index]:
            max_index=index
    
    max_emotion = list(score_array.keys())[max_index]
    dominant_emotion = max_emotion

    finalObj = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }
    return finalObj

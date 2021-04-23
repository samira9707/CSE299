package com.example.protisruti30.interfaces;

import com.google.cloud.dialogflow.v2.DetectIntentResponse;
//response detection to chat bot
public interface BotReply {

    void callback(DetectIntentResponse returnResponse);
}

package com.example.aot_offical;


import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.*;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class GarbageClassification extends AppCompatActivity {
    MQTTHelper mqttHelper;
    TextView organic, inorganic;
    Button back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_garbage_classification);
        startMQTT();
        organic = findViewById(R.id.organicRubbishPercentageText);
        inorganic = findViewById(R.id.inorganicRubbishPercentageText);
        back = findViewById(R.id.backGarbageClassification);
        back.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent iBackGarbageClassification = new Intent();
                iBackGarbageClassification.setClass(GarbageClassification.this,Main.class);
                startActivity(iBackGarbageClassification);
            }
        });
    }

    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        // Lambda instruction or Asynchronous instruction
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + " * " + message.toString());

                if (topic.contains("organix"))
                {
                    organic.setText(message.toString());
                }
                if (topic.contains("inorganz"))
                {
                    inorganic.setText(message.toString());
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }

    public void sendDataMQTT(String topic, String value){
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){

        }

    }



}

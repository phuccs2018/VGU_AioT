package bku.iot.application123;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;


import java.nio.charset.Charset;



public class Main extends AppCompatActivity {

    ImageButton calendar,result,faq,turnOff;
    Button test;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        calendar = findViewById(R.id.calendarMain);
        result = findViewById(R.id.resultMain);
        faq = findViewById(R.id.FAQMain);
        turnOff = findViewById(R.id.turnOffMain);

        calendar.setOnClickListener(mListener);
        result.setOnClickListener(mListener);
        faq.setOnClickListener(mListener);
        turnOff.setOnClickListener(mListener);

    }

    View.OnClickListener mListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            int id = v.getId();
            switch (id)
            {
                case R.id.calendarMain:
                    //code
                    Intent iCalendar = new Intent();
                    iCalendar.setClass(Main.this,Calendar.class);
                    startActivity(iCalendar);
                    break;
                case R.id.resultMain:
                    //code
                    Intent iResult = new Intent();
                    iResult.setClass(Main.this,GarbageClassification.class);
                    startActivity(iResult);
                    break;
                case R.id.FAQMain:
                    //code
                    Intent iFAQ = new Intent();
                    iFAQ.setClass(Main.this,FAQ.class);
                    startActivity(iFAQ);
                    break;

                case R.id.turnOffMain:
                    //code
                    Intent intent = new Intent(getApplicationContext(), Main.class);
                    startActivity(intent);
                    // Tao su kien ket thuc app
                    Intent startMain = new Intent(Intent.ACTION_MAIN);
                    startMain.addCategory(Intent.CATEGORY_HOME);
                    startActivity(startMain);
                    finish();
                    break;

                default:
                    break;
            }
        }
    };



}
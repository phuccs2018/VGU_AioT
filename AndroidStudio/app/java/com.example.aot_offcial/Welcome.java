package com.example.aot_offical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

public class Welcome extends AppCompatActivity {

    ImageButton welcome;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome);

        welcome = findViewById(R.id.welcomeImage);

        welcome.setOnClickListener(mListener);
    }

    View.OnClickListener mListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            int id = v.getId();
            switch (id) {
                case R.id.welcomeImage:
                    //code
                    Intent iWelcomeImage= new Intent();
                    iWelcomeImage.setClass(Welcome.this, Main.class);
                    startActivity(iWelcomeImage);
                    break;
            }
        }


    };
}

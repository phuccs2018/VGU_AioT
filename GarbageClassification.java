package bku.iot.application123;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

public class GarbageClassification extends AppCompatActivity {

    Button back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_garbage_classification);
//       back = findViewById(R.id.backGarbageClassification);
//       back.setOnClickListener(new View.OnClickListener()
//       {
//           @Override
//           public void onClick(View view)
//           {
//               Intent iBackGarbageClassification = new Intent();
//               iBackGarbageClassification.setClass(GarbageClassification.this,Main.class);
//               startActivity(iBackGarbageClassification);
//           }
//       });
    }

}

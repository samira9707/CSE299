package com.example.protisruti;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private Button button,button1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getSupportActionBar().hide();
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = (Button) findViewById(R.id.button_view);
        button1 = (Button) findViewById(R.id.view_last);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openViewData();
            }
        });
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                LastData();

            }
        });


    }
    public void openViewData(){
       Intent intent = new Intent(this,ViewData.class);
       startActivity(intent);
    }
    public void LastData(){
        Intent intent = new Intent(this,Hpage.class);
        startActivity(intent);
    }
}
package com.example.protisruti;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.WindowManager;

public class splash_screen extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //hide action bar and stutas bar
        getSupportActionBar().hide();
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);
        Handler hd = new Handler();
        final boolean hb = hd.postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent i = new Intent(splash_screen.this, MainActivity.class);
                startActivity(i);
                finish();
            }
        },1000);


    }
}
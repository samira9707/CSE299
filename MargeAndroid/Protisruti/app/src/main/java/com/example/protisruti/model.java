package com.example.protisruti;

public class model {
    String Moisture,Time,ldr,temp;

    public model() {
    }

    public model(String moisture, String time, String ldr, String temp) {
        Moisture = moisture;
        Time = time;
        this.ldr = ldr;
        this.temp = temp;
    }

    public String getMoisture() {
        return Moisture;
    }

    public void setMoisture(String moisture) {
        Moisture = moisture;
    }

    public String getTime() {
        return Time;
    }

    public void setTime(String time) {
        Time = time;
    }

    public String getLdr() {
        return ldr;
    }

    public void setLdr(String ldr) {
        this.ldr = ldr;
    }

    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
}


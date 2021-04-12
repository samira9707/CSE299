package com.example.protisruti;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;

public class secondadapter extends FirebaseRecyclerAdapter<model,secondadapter.myviewholder> {

    public secondadapter(@NonNull FirebaseRecyclerOptions<model> options) {
        super(options);
    }

    @Override
    protected void onBindViewHolder(@NonNull myviewholder holder, int position, @NonNull model model) {

        holder.time.setText(model.getTime());


    }

    @NonNull
    @Override
    public myviewholder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.activity_hpage,parent,false);
        return new myviewholder(view);
    }

    class myviewholder extends RecyclerView.ViewHolder{
        TextView moisture,time,ldr,temp;
        public myviewholder(@NonNull View itemView) {
            super(itemView);

            time = (TextView)itemView.findViewById(R.id.textView1);
            /*ldr = (TextView)itemView.findViewById(R.id.Idr);
            temp = (TextView) itemView.findViewById(R.id.temp);*/


        }
    }
}

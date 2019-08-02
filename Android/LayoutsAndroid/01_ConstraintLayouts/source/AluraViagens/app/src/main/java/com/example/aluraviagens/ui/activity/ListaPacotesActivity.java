package com.example.aluraviagens.ui.activity;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import com.alura.aluraviagens.dao.PacoteDAO;
import com.example.aluraviagens.R;
import com.example.aluraviagens.ui.adapter.ListaPacoteAdapter;

import java.util.List;

import br.com.alura.aluraviagens.model.Pacote;

public class ListaPacotesActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lista_pacotes);
        ListView listaDePacotes = findViewById(R.id.lista_pacotes_listView);

        List<Pacote> pacotes = new PacoteDAO().lista();

        listaDePacotes.setAdapter(new ListaPacoteAdapter(pacotes, this));
    }
}

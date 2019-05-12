package br.com.alura.agenda.services;

import br.com.alura.agenda.modelo.Aluno;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface AlunoService {

    @POST("aluno")
    Call<Void> insere(@Body Aluno aluno);
}

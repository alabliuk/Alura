var frase = $(".frase").text();
var numPalavras = frase.split(" ").length;
var tamanhoFrase = $("#tamanho-frase");
tamanhoFrase.text(numPalavras);

var campo = $(".campo-digitacao");
campo.on("input", function() {
    var conteudo = campo.val();

    //Retira os espaço da String (Corrigindo o Bug do espaço sendo contado como caractere)
    var conteudoSemEspaco = conteudo.replace(/\s+/g,'');

    var qtdPalavras = conteudo.split(/\s+/).length - 1;
    $("#contador-palavras").text(qtdPalavras);

    var qtdCaracteres = conteudoSemEspaco.length;
    $('#contador-caracteres').text(qtdCaracteres);
});



/*

Ambas as funções .val() e .text() podem manipular os valores de texto dos elementos, mas a .val() funciona em elementos de <input> que são campos aonde o usuário do site insere dados , como os campos de <input>(todos os tipos), <textarea> e <select>.

Já a função .text() pega o conteúdo de texto de tags HTML que tem texto dentro, como as <h1>, <span> e <p>

Ambas as funções podem atribuir novos valores a determinados elementos, ou apenas pegar os valores deles.

*/
using ByteBank.Funcionarios;
using System;

namespace ByteBank
{
    class Program
    {
        static void Main(string[] args)
        {
            GerenciadorBonificacao gerenciador = new GerenciadorBonificacao();

            Funcionario carlos = new Funcionario(2000, "546.879.157-20");
            carlos.Nome = "Carlos";

            gerenciador.Registrar(carlos);

            Console.WriteLine(Funcionario.TotalDeFuncionarios);
            Console.WriteLine(carlos.Nome);
            Console.WriteLine(carlos.GetBonificacao());

            carlos.AumentarSalario();
            Console.WriteLine("Novo salário do carlos " + carlos.Salario);

            Diretor roberta = new Diretor("454.658.148-3");
            roberta.Nome = "Roberta";

            gerenciador.Registrar(roberta);

            Console.WriteLine(Funcionario.TotalDeFuncionarios);
            Console.WriteLine(roberta.Nome);
            Console.WriteLine(roberta.GetBonificacao());

            roberta.AumentarSalario();
            Console.WriteLine("Novo salário de Roberta " + roberta.Salario);

            Console.WriteLine($"Total de bonificações: { gerenciador.GetTotalBonificacao() }");
        }
    }
}

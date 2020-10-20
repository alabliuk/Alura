using System;

namespace ByteBank.Funcionarios
{
    public class Funcionario
    {
        public static int TotalDeFuncionarios { get; private set; }

        public string Nome { get; set; }
        public string CPF { get; private set; }
        public double Salario { get; set; }

        public Funcionario(string cpf)
        {
            // *** cpf minúsculo é o argumento e CPF maiúsculo é a propriedade <<<

            Console.WriteLine("Criando FUNCIONARIO");
            CPF = cpf;
            TotalDeFuncionarios++;
        }

        // virtual = permite a modificação de comportamento pela classe filha
        public virtual double GetBonificacao()
        {
            return Salario * 0.10;
        }
    }
}

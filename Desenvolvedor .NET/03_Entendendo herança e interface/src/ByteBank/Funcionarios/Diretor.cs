using System;

namespace ByteBank.Funcionarios
{
    public class Diretor : Funcionario
    {
        public Diretor(string cpf) : base(cpf)
        {
            Console.WriteLine("Criando DIRETOR");
        }

        // override = modifica o comportamento do metodo da classe mae
        public override double GetBonificacao()
        {
            return Salario + base.GetBonificacao();
        }
    }
}

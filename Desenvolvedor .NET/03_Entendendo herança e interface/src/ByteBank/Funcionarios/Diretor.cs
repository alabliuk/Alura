using System;

namespace ByteBank.Funcionarios
{
    public class Diretor : Funcionario
    {
        public Diretor(string cpf) : base(5000, cpf)
        {
            Console.WriteLine("Criando DIRETOR");
        }

        public override void AumentarSalario()
        {
            Salario *= 1.15;
        }

        // override = modifica o comportamento do metodo da classe mae
        public override double GetBonificacao()
        {
            return Salario + base.GetBonificacao();
        }
    }
}

namespace ByteBank.Funcionarios
{
    public class Diretor : Funcionario
    {
        // override = modifica o comportamento do metodo da classe mae
        public override double GetBonificacao()
        {
            return Salario;
        }
    }
}

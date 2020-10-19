namespace ByteBank.Funcionarios
{
    public class Funcionario
    {
        public string Nome { get; set; }
        public string CPF { get; set; }
        public double Salario { get; set; }
        
        // virtual = permite a modificação de comportamento pela classe filha
        public virtual double GetBonificacao()
        {
            return Salario * 0.10;
        }
    }
}

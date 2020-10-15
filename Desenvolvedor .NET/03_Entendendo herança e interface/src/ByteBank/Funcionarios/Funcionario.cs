namespace ByteBank.Funcionarios
{
    public class Funcionario
    {
        // 0 - funcionário
        // 1 - diretor
        // 2 - designer
        // N - ...
        private readonly int _tipo;

        public string Nome { get; set; }
        public string CPF { get; set; }
        public double Salario { get; set; }
        
        // construtor
        public Funcionario(int tipo)
        {
            _tipo = tipo;
        }

        public double GetBonificacao()
        {
            if (_tipo == 1)
                return Salario;

            return Salario * 0.10;
        }
    }
}

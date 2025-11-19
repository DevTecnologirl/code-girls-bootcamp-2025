object ReceitaFederal {
    fun calcularImposto(salario: Double): Double {
        val aliquota = when {
            salario <= 1100.0 -> 0.05
            salario <= 2500.0 -> 0.10
            else -> 0.15
        }
        return aliquota * salario
    }
}

fun main() {
    val valorSalario = readLine()!!.toDouble()
    val valorBeneficio = readLine()!!.toDouble()

    val imposto = ReceitaFederal.calcularImposto(valorSalario)
    val saida = valorSalario - imposto + valorBeneficio

    println(String.format("%.2f", saida))
}

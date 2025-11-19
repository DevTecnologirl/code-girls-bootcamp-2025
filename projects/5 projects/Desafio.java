import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {
        Scanner leitorEntrada = new Scanner(System.in);

        float valorSalario = leitorEntrada.nextFloat();
        float valorBeneficio = leitorEntrada.nextFloat();

        float valorImposto = 0f;

        if (valorSalario <= 1100f) {
            valorImposto = 0.05f * valorSalario;
        } else if (valorSalario <= 2500f) {
            valorImposto = 0.10f * valorSalario;
        } else {
            valorImposto = 0.15f * valorSalario;
        }

        float saida = valorSalario - valorImposto + valorBeneficio;

        System.out.println(String.format("%.2f", saida));

        leitorEntrada.close(); // boa prática
    }
}

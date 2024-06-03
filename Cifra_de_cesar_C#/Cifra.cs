using System;
using System.Linq;
public class program
{
    //Armazenamento do alfabeto.
    static string[] maiuscula = {"A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"};
    static string[] minuscula = maiuscula.Select(letra => letra.ToLower()).ToArray();

    public static void Main()
    {
        //leitura e armazenamento da entrada.
        Console.WriteLine("Digite a mensagem que será criptografada :");
        string texto = Console.ReadLine();

        //processamento
        string textoCriptografado = "";

        foreach (char x in texto)
        {
            textoCriptografado += criptografando(x.ToString());
        }

         // Exibir a mensagem criptografada
        Console.WriteLine("Texto criptografado: " + textoCriptografado);
    }


        //função para criptografar.
    public static string criptografando(string letra)
    {
        // Verifica se a letra está no array de maiúsculas
        if (maiuscula.Contains(letra)){
            int index = (Array.IndexOf(maiuscula, letra) + 3) % maiuscula.Length;
            return maiuscula[index];
        }
        // Verifica se a letra está no array de minúsculas
        else if (minuscula.Contains(letra)){
            int index = (Array.IndexOf(minuscula, letra) + 3) % minuscula.Length;
            return minuscula[index];
        }
        else{
            return letra;
        }
    }
}

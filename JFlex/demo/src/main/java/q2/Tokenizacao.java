package q2;

import java.util.HashMap;
import java.util.Map;

import q1.Token;

import java.io.FileWriter;  // Import necessário para gravar em arquivo
import java.io.IOException; // Import necessário para tratamento de exceções

public class Tokenizacao {
    private HashMap<String, Token> tabelaSimbolos;

    public Tokenizacao() {
        this.tabelaSimbolos = new HashMap<>();
    }

    public void add(String token, String lexema) {
        for (Token t : tabelaSimbolos.values()) {
            if (t.getToken().equals(token) && t.getLexema().equals(lexema)) {
                return; // Não adicionar duplicado
            }
        }
        Token novoToken = new Token(token, lexema);
        tabelaSimbolos.put(novoToken.getId(), novoToken);
    }

    public void print() {
        for (Map.Entry<String, Token> entry : tabelaSimbolos.entrySet()) {
            System.out.println("ID: " + entry.getKey() + ", Token: " + entry.getValue().getToken() + ", Lexema: " + entry.getValue().getLexema());
        }
    }

    // Método para salvar a tabela de símbolos em um arquivo
    public void saveToFile(String filename) {
        try (FileWriter writer = new FileWriter(filename)) {
            for (Token token : tabelaSimbolos.values()) {
                writer.write(token.getToken() + " " + token.getLexema() + "\n");
            }
            System.out.println("Arquivo gerado com sucesso: " + filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


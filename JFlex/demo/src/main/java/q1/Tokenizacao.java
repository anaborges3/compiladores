package q1;

import java.util.HashMap;
import java.util.Map;

public class Tokenizacao {
    private HashMap<String, Token> tabelaSimbolos = new HashMap<>();

    public void add(String token, String lexema) {
        for (Token t : tabelaSimbolos.values()) {
            if (t.getToken().equals(token) && t.getLexema().equals(lexema)) {
                return; // Não adicionar duplicado
            }
        }
        Token newToken = new Token(token, lexema);
        tabelaSimbolos.put(newToken.getId(), newToken);
    }

    public void print() {
        for (Map.Entry<String, Token> entry : tabelaSimbolos.entrySet()) {
            System.out.println("ID: " + entry.getKey() + ", Token: " + entry.getValue().getToken() + ", Lexema: " + entry.getValue().getLexema());
        }
    }
}


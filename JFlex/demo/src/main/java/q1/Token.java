package q1;

public class Token {
    private String id;
    private String token;
    private String lexema;

    public Token(String token, String lexema) {
        this.id = generateId();
        this.token = token;
        this.lexema = lexema;
    }

    public String getId() { return id; }
    public String getToken() { return token; }
    public String getLexema() { return lexema; }

    public static String generateId() {
        return Long.toHexString(Double.doubleToLongBits(Math.random()));
    }
}


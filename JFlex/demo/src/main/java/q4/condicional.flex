%{
    System.out.println("Analisador de Estruturas Condicionais");
%}

ifkw = "if"
elsekw = "else"
switchkw = "switch"
ternary = [?:]
oprel = [><=!]=?

%%

{ifkw}     { System.out.println("IF: " + yytext()); }
{elsekw}   { System.out.println("ELSE: " + yytext()); }
{switchkw} { System.out.println("SWITCH: " + yytext()); }
{ternary}  { System.out.println("TERNÁRIO: " + yytext()); }
{oprel}    { System.out.println("OP_REL: " + yytext()); }

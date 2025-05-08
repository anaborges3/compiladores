%{
    int resultado = 0;
%}

digit = [0-9]+
op = [+-*/]

%%

{digit}   { resultado += Integer.parseInt(yytext()); }
{op}      { System.out.println("Operador: " + yytext()); }
<<EOF>>   { System.out.println("Resultado: " + resultado); return 0; }

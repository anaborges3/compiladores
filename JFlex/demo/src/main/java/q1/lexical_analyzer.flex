%{
    Tokenizacao listToken = new Tokenizacao();
%}

%%

[a-zA-Z_]+   { listToken.add("KW_ID", yytext()); }
[0-9]+       { listToken.add("KW_NUMBER", yytext()); }
[-+*/=]      { listToken.add("KW_OP", yytext()); }
";"          { listToken.add("KW_END", yytext()); }
"(" | ")"    { listToken.add("KW_PAR", yytext()); }
<<EOF>>      { listToken.print(); return 0; }

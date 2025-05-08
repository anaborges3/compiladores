%{
    Stack<String> stack = new Stack<>();
%}

digit = [0-9]+
op = [*/+-]

%%

{digit}   { System.out.print(yytext() + " "); }
{op}      { stack.push(yytext()); }
<<EOF>>   { 
    while (!stack.isEmpty()) 
        System.out.print(stack.pop() + " ");
    return 0; 
}

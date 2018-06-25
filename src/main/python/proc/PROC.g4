grammar PROC;

// Parser Rules

program         : expression ;
expression      : constant_expression
                | difference_expression
                | zero_expression
                | if_expression
                | variable_expression
                | let_expression
                | procedure_expression
                | call_expression
                ;

constant_expression     : NUMBER ;

difference_expression   : '-' '(' expression ',' expression ')' ;

zero_expression         : 'zero?' '(' expression ')' ;

if_expression           : 'if' expression 'then' expression 'else' expression ;

variable_expression     : IDENTIFIER ;

let_expression          : 'let' IDENTIFIER '=' expression 'in' expression ;

procedure_expression    : 'proc' '(' IDENTIFIER ')' expression ;

call_expression         : '(' expression expression ')' ;



// Lexer Rules

NUMBER          : [0-9]+ ;
IDENTIFIER      : [a-zA-Z][a-zA-Z0-9]* ;
WS              : [ \t\r\n]+ -> skip ;
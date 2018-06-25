grammar Array;

init_exp    :   '{' value (',' value)* '}' ;

value   :   init_exp
        |   INT
        ;

INT     :   [0-9]+ ;
WS      :   [ \t\r\n]+ -> skip ;
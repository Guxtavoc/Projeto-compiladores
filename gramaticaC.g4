grammar gramaticaC;

programa
    : biblioteca 'int' 'main' '(' ')' bloco EOF
    ;

biblioteca
    : '#include' '<' ID '.' ID '>'
    ;

bloco
    : '{' (declaracao | comando)* '}'
    ;

declaracao
    : tipo ID ('=' expressao)? (',' ID ('=' expressao)?)* ';'
    ;

tipo
    : 'int'
    | 'float'
    ;

comando
    : escrita
    | leitura
    | atribuicao ';'
    | enquanto
    | condicional
    | repita
    ;

escrita
    : 'printf' '(' (STRING | expressao) (',' expressao)* ')' ';'
    ;

leitura
    : 'scanf' '(' STRING (',' '&'? ID)* ')' ';'
    ;

atribuicao
    : ID '=' expressao
    ;
    
enquanto
    : 'while' '(' expressao ')' bloco
    ;

condicional
    : 'if' '(' expressao ')' bloco ('else' bloco)?
    ;

repita
    : 'do' bloco 'while' '(' expressao ')' ';'
    ;
    
expressao
    : expressao ('||' | '&&') expressao
    | expressao ('==' | '!=' | '<' | '<=' | '>' | '>=') expressao
    | expressao ('+' | '-') expressao
    | expressao ('*' | '/') expressao
    | ('+' | '-')? atomo
    ;

atomo
    : NUMERO
    | REAL
    | STRING
    | ID
    | '(' expressao ')'
    ;

ID      : [a-zA-Z_][a-zA-Z_0-9]*;
NUMERO  : [0-9]+;
REAL    : [0-9]+ '.' [0-9]*;
STRING  : '"' (~["\\] | '\\' .)* '"';
WS      : [ \t\r\n]+ -> skip;
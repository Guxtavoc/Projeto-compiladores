grammar MicroLang;
programa
    : biblioteca 'int' 'main''(' ')' bloco EOF
    ;

biblioteca
    : '#include' '<' ID '.' ID'>'
    ;
bloco
    : '{' (declaracao | comando)* '}'
    ;

declaracao
    : tipo lista_variaveis ';'
    ;

tipo
    : 'int'
    | 'float'
    ;

lista_variaveis
    : lista_variaveis ',' var_decl_item
    | var_decl_item
    ;

var_decl_item
    : ID ( '=' (NUMERO | REAL | STRING | ID) )?
    ;
    
comando
    : escrita
    | leitura
    | atribuicao ';'
    | enquanto
    ;

escrita
    : 'printf' '(' ( expressao | STRING ) ')' ';'
    ;

leitura
    : 'scanf' '(' STRING (',' '&'? ID)* ')' ';'
    ;

lista_identificador
    : lista_identificador ',' identificador
    | identificador
    ;

identificador
    : ID
    ;

atribuicao
    : ID '=' expressao
    ;
    
enquanto
    : 'while' '(' expr_bool ')' bloco
    ;

expressao
    : expr_bool
    ;

expr_bool
    : expr_relacao ('||' expr_relacao)*
    ;

expr_relacao
    : expr_comparacao (('==' | '!=' | '<' | '<=' | '>' | '>=') expr_comparacao)?
    ;

expr_comparacao
    : termo (('+' | '-') termo)*
    ;

termo
    : fator (('*' | '/') fator)*
    ;

fator
    : ('+' | '-') fator
    | NUMERO
    | REAL
    | STRING
    | ID
    | '(' expressao ')'
    ;

primary
    : NUMERO
    | REAL
    | STRING
    | ID
    | '(' expr_bool ')'
    ;

ID
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

NUMERO
    : ('0'..'9')+
    ;

REAL
    :
    (NUMERO)+ '.' (NUMERO)*
    ;

STRING
    : '"' ( ~["\\] | '\\' . )* '"'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
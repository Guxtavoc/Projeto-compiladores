grammar MicroLang;
programa
    : 'programa' ID bloco EOF
    ;

bloco
    : '{' (declaracao | comando)* '}'
    ;

declaracao
    : tipo lista_variaveis ';'
    ;

tipo
    : 'inteiro'
    | 'real'
    | 'texto'
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
    | repita
    | laco_para
    | loop_infinito
    ;

escrita
    : 'printf' ( expressao | STRING ) ';'
    ;

leitura
    : 'scan' lista_identificador ';'
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

repita
    : 'do' bloco 'ate' '(' expr_bool ')' ';'?   // opcional o ponto-e-vírgula final
    ;

laco_para
    : 'fator' '(' atribuicao ';' expr_bool? ';' incremento ')' bloco
    ;

incremento
    : ID ( '++' | '--' | '+=' expressao | '-=' expressao )
    ;

loop_infinito
    : 'loop' bloco
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
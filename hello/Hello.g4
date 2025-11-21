grammar Hello;
r : 'hola' ID ;
ID : [a-z]+ ;
WS : [ \t\r\n]+ -> skip;
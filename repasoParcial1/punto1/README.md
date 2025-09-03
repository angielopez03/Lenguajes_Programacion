En C

```
gcc punto1 -o enc
./enc archivo.txt
```
En flex

```
flex punto1.l
gcc lex.yy.c -o flex -lfl
./flex archivo.txt
```

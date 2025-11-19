from antlr4 import *
from matricesVisitor import matricesVisitor as BaseVisitor
from matricesLexer import matricesLexer
from matricesParser import matricesParser
import numpy as np
import sys

class EvaluadorMatrices(BaseVisitor):
    def __init__(self):
        self.variables = {}  # Almacén de matrices
    
    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            resultado = self.visit(sentencia)
            if resultado is None:
                continue  # Ignorar sentencias vacías o incorrectas
        return None
    
    def visitSentencia(self, ctx):
        if ctx.expresion() is None:
            return None  # No hay nada que evaluar

        nombre_var = ctx.identificador().getText()
        valor_matriz = self.visit(ctx.expresion())
        if valor_matriz is None:
            return None

        self.variables[nombre_var] = valor_matriz
        
        print(f"Variable '{nombre_var}' asignada:")
        print(f"Dimensiones: {valor_matriz.shape}")
        print(valor_matriz)
        print()
        
        return valor_matriz
    
    def visitExpresion(self, ctx):
        if ctx.matriz():
            return self.visit(ctx.matriz())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expresion(0))
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '·':
            return self.visitExpresionProducto(ctx)
        elif ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '.punto':
            return self.visitExpresionProductoFuncion(ctx)
        elif ctx.identificador():
            return self.visitIdentificador(ctx.identificador())
        else:
            return None  # Expresión no válida
    
    def visitExpresionProducto(self, ctx):
        matriz_izq = self.visit(ctx.expresion(0))
        matriz_der = self.visit(ctx.expresion(1))
        
        if matriz_izq.shape[1] != matriz_der.shape[0]:
            raise ValueError(
                f"Dimensiones incompatibles para producto punto:\n"
                f"Matriz izquierda: {matriz_izq.shape}\n"
                f"Matriz derecha: {matriz_der.shape}\n"
                f"Las columnas de la primera ({matriz_izq.shape[1]}) deben "
                f"igualar las filas de la segunda ({matriz_der.shape[0]})"
            )
        
        resultado = np.dot(matriz_izq, matriz_der)
        print(f"Producto punto: {matriz_izq.shape} · {matriz_der.shape} = {resultado.shape}")
        return resultado
    
    def visitExpresionProductoFuncion(self, ctx):
        matriz_izq = self.visit(ctx.expresion(0))
        matriz_der = self.visit(ctx.expresion(1))
        
        if matriz_izq.shape[1] != matriz_der.shape[0]:
            raise ValueError(
                f"Dimensiones incompatibles para producto punto:\n"
                f"Matriz izquierda: {matriz_izq.shape}\n"
                f"Matriz derecha: {matriz_der.shape}\n"
                f"Las columnas de la primera ({matriz_izq.shape[1]}) deben "
                f"igualar las filas de la segunda ({matriz_der.shape[0]})"
            )
        
        resultado = np.dot(matriz_izq, matriz_der)
        print(f"Producto punto: {matriz_izq.shape} · {matriz_der.shape} = {resultado.shape}")
        return resultado
    
    def visitMatriz(self, ctx):
        filas_ctx = ctx.filas()
        matriz_lista = []
        
        for fila_ctx in filas_ctx.fila():
            fila = self.visit(fila_ctx)
            matriz_lista.append(fila)
        
        return np.array(matriz_lista)
    
    def visitFila(self, ctx):
        numeros = [self.visit(numero_ctx) for numero_ctx in ctx.numero()]
        return numeros
    
    def visitNumero(self, ctx):
        texto = ctx.getText()
        try:
            return int(texto)
        except ValueError:
            return float(texto)
    
    def visitIdentificador(self, ctx):
        nombre = ctx.getText()
        if nombre not in self.variables:
            raise NameError(f"Variable '{nombre}' no definida")
        return self.variables[nombre]

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.txt")
        return

    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')

    lexer = matricesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = matricesParser(stream)

    tree = parser.programa()  # Regla inicial de la gramática
    visitor = EvaluadorMatrices()
    visitor.visit(tree)

if __name__ == '__main__':
    main()


from matricesVisitor import matricesVisitor as BaseVisitor
from matricesParser import matricesParser as Parser
import numpy as np

class EvaluadorMatrices(BaseVisitor):
    def __init__(self):
        self.variables = {}  # Almacén de matrices
    
    def visitPrograma(self, ctx):
        resultados = []
        for sentencia in ctx.sentencia():
            resultado = self.visit(sentencia)
            resultados.append(resultado)
        return resultados
    
    def visitSentencia(self, ctx):
        nombre_var = ctx.identificador().getText()
        valor_matriz = self.visit(ctx.expresion())
        
        self.variables[nombre_var] = valor_matriz
        
        print(f"Variable '{nombre_var}' asignada:")
        print(f"Dimensiones: {valor_matriz.shape}")
        print(valor_matriz)
        print()
        
        return {
            'variable': nombre_var,
            'valor': valor_matriz,
            'dimensiones': valor_matriz.shape
        }
    
    def visitExpresionMatriz(self, ctx):
        return self.visit(ctx.matriz())
    
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
    
    def visitExpresionParentesis(self, ctx):
        return self.visit(ctx.expresion())
    
    def visitMatriz(self, ctx):
        filas_ctx = ctx.filas()
        matriz_lista = []
        
        for fila_ctx in filas_ctx.fila():
            fila = self.visit(fila_ctx)
            matriz_lista.append(fila)
        
        return np.array(matriz_lista)
    
    def visitFila(self, ctx):
        numeros = []
        for numero_ctx in ctx.numero():
            valor = self.visit(numero_ctx)
            numeros.append(valor)
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

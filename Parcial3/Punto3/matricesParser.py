# Generated from matrices.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,5,4,59,8,4,10,4,12,4,62,9,4,1,5,1,5,1,5,1,5,5,5,68,8,5,10,5,
        12,5,71,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,1,4,8,0,2,4,6,8,10,12,
        14,0,0,77,0,17,1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,51,1,0,0,0,8,
        55,1,0,0,0,10,63,1,0,0,0,12,74,1,0,0,0,14,76,1,0,0,0,16,18,3,2,1,
        0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,
        1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,3,14,7,0,24,25,5,1,0,0,
        25,26,3,4,2,0,26,27,5,2,0,0,27,3,1,0,0,0,28,29,6,2,-1,0,29,36,3,
        6,3,0,30,31,5,3,0,0,31,32,3,4,2,0,32,33,5,4,0,0,33,36,1,0,0,0,34,
        36,3,14,7,0,35,28,1,0,0,0,35,30,1,0,0,0,35,34,1,0,0,0,36,48,1,0,
        0,0,37,38,10,3,0,0,38,39,5,9,0,0,39,47,3,4,2,4,40,41,10,2,0,0,41,
        42,5,10,0,0,42,43,5,3,0,0,43,44,3,4,2,0,44,45,5,4,0,0,45,47,1,0,
        0,0,46,37,1,0,0,0,46,40,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,5,1,0,0,0,50,48,1,0,0,0,51,52,5,5,0,0,52,53,3,8,4,0,53,
        54,5,6,0,0,54,7,1,0,0,0,55,60,3,10,5,0,56,57,5,13,0,0,57,59,3,10,
        5,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,9,
        1,0,0,0,62,60,1,0,0,0,63,64,5,5,0,0,64,69,3,12,6,0,65,66,5,13,0,
        0,66,68,3,12,6,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,
        1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,6,0,0,73,11,1,0,0,0,
        74,75,5,7,0,0,75,13,1,0,0,0,76,77,5,8,0,0,77,15,1,0,0,0,6,19,35,
        46,48,60,69
    ]

class matricesParser ( Parser ):

    grammarFileName = "matrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "'\\u00B7'", "'.punto'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMERO", "IDENTIFICADOR", 
                      "PUNTO_OP", "PUNTO_FUNC", "COMENTARIO", "ESPACIO", 
                      "SEP" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_expresion = 2
    RULE_matriz = 3
    RULE_filas = 4
    RULE_fila = 5
    RULE_numero = 6
    RULE_identificador = 7

    ruleNames =  [ "programa", "sentencia", "expresion", "matriz", "filas", 
                   "fila", "numero", "identificador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMERO=7
    IDENTIFICADOR=8
    PUNTO_OP=9
    PUNTO_FUNC=10
    COMENTARIO=11
    ESPACIO=12
    SEP=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(matricesParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(matricesParser.SentenciaContext,i)


        def getRuleIndex(self):
            return matricesParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = matricesParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sentencia()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 21
            self.match(matricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(matricesParser.IdentificadorContext,0)


        def expresion(self):
            return self.getTypedRuleContext(matricesParser.ExpresionContext,0)


        def getRuleIndex(self):
            return matricesParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = matricesParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.identificador()
            self.state = 24
            self.match(matricesParser.T__0)
            self.state = 25
            self.expresion(0)
            self.state = 26
            self.match(matricesParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matriz(self):
            return self.getTypedRuleContext(matricesParser.MatrizContext,0)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(matricesParser.ExpresionContext,i)


        def identificador(self):
            return self.getTypedRuleContext(matricesParser.IdentificadorContext,0)


        def PUNTO_OP(self):
            return self.getToken(matricesParser.PUNTO_OP, 0)

        def PUNTO_FUNC(self):
            return self.getToken(matricesParser.PUNTO_FUNC, 0)

        def getRuleIndex(self):
            return matricesParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matricesParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 29
                self.matriz()
                pass
            elif token in [3]:
                self.state = 30
                self.match(matricesParser.T__2)
                self.state = 31
                self.expresion(0)
                self.state = 32
                self.match(matricesParser.T__3)
                pass
            elif token in [8]:
                self.state = 34
                self.identificador()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = matricesParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 37
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 38
                        self.match(matricesParser.PUNTO_OP)
                        self.state = 39
                        self.expresion(4)
                        pass

                    elif la_ == 2:
                        localctx = matricesParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 40
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 41
                        self.match(matricesParser.PUNTO_FUNC)
                        self.state = 42
                        self.match(matricesParser.T__2)
                        self.state = 43
                        self.expresion(0)
                        self.state = 44
                        self.match(matricesParser.T__3)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filas(self):
            return self.getTypedRuleContext(matricesParser.FilasContext,0)


        def getRuleIndex(self):
            return matricesParser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = matricesParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_matriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(matricesParser.T__4)
            self.state = 52
            self.filas()
            self.state = 53
            self.match(matricesParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.FilaContext)
            else:
                return self.getTypedRuleContext(matricesParser.FilaContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(matricesParser.SEP)
            else:
                return self.getToken(matricesParser.SEP, i)

        def getRuleIndex(self):
            return matricesParser.RULE_filas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilas" ):
                listener.enterFilas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilas" ):
                listener.exitFilas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilas" ):
                return visitor.visitFilas(self)
            else:
                return visitor.visitChildren(self)




    def filas(self):

        localctx = matricesParser.FilasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.fila()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 56
                self.match(matricesParser.SEP)
                self.state = 57
                self.fila()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.NumeroContext)
            else:
                return self.getTypedRuleContext(matricesParser.NumeroContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(matricesParser.SEP)
            else:
                return self.getToken(matricesParser.SEP, i)

        def getRuleIndex(self):
            return matricesParser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = matricesParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fila)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(matricesParser.T__4)
            self.state = 64
            self.numero()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 65
                self.match(matricesParser.SEP)
                self.state = 66
                self.numero()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(matricesParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(matricesParser.NUMERO, 0)

        def getRuleIndex(self):
            return matricesParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = matricesParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numero)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(matricesParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(matricesParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return matricesParser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)




    def identificador(self):

        localctx = matricesParser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identificador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(matricesParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         





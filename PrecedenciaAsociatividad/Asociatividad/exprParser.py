# Generated from expr.g4 by ANTLR 4.13.2
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
        4,1,11,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,
        2,1,3,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,3,1,3,1,3,3,
        3,55,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,4,0,0,5,0,2,4,6,8,
        0,0,70,0,11,1,0,0,0,2,24,1,0,0,0,4,39,1,0,0,0,6,54,1,0,0,0,8,62,
        1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,
        13,14,1,0,0,0,14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,10,0,0,17,25,1,
        0,0,0,18,19,5,8,0,0,19,20,5,1,0,0,20,21,3,4,2,0,21,22,5,10,0,0,22,
        25,1,0,0,0,23,25,5,10,0,0,24,15,1,0,0,0,24,18,1,0,0,0,24,23,1,0,
        0,0,25,3,1,0,0,0,26,31,3,6,3,0,27,28,5,6,0,0,28,30,3,6,3,0,29,27,
        1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,40,1,0,0,0,
        33,31,1,0,0,0,34,35,3,6,3,0,35,36,5,7,0,0,36,37,3,4,2,0,37,40,1,
        0,0,0,38,40,3,6,3,0,39,26,1,0,0,0,39,34,1,0,0,0,39,38,1,0,0,0,40,
        5,1,0,0,0,41,46,3,8,4,0,42,43,5,4,0,0,43,45,3,8,4,0,44,42,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,55,1,0,0,0,48,46,
        1,0,0,0,49,50,3,8,4,0,50,51,5,5,0,0,51,52,3,6,3,0,52,55,1,0,0,0,
        53,55,3,8,4,0,54,41,1,0,0,0,54,49,1,0,0,0,54,53,1,0,0,0,55,7,1,0,
        0,0,56,63,5,9,0,0,57,63,5,8,0,0,58,59,5,2,0,0,59,60,3,4,2,0,60,61,
        5,3,0,0,61,63,1,0,0,0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,
        63,9,1,0,0,0,7,13,24,31,39,46,54,62
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4

    ruleNames =  [ "prog", "stat", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    ID=8
    INT=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.StatContext)
            else:
                return self.getTypedRuleContext(exprParser.StatContext,i)


        def getRuleIndex(self):
            return exprParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = exprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1796) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = exprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = exprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(exprParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = exprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(exprParser.ID)
                self.state = 19
                self.match(exprParser.T__0)
                self.state = 20
                self.expr()
                self.state = 21
                self.match(exprParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = exprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(exprParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddLeftContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.TermContext)
            else:
                return self.getTypedRuleContext(exprParser.TermContext,i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.ADD)
            else:
                return self.getToken(exprParser.ADD, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddLeft" ):
                return visitor.visitAddLeft(self)
            else:
                return visitor.visitChildren(self)


    class SubRightContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(exprParser.TermContext,0)

        def SUB(self):
            return self.getToken(exprParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubRight" ):
                return visitor.visitSubRight(self)
            else:
                return visitor.visitChildren(self)


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(exprParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = exprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = exprParser.AddLeftContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.term()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 27
                    self.match(exprParser.ADD)
                    self.state = 28
                    self.term()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = exprParser.SubRightContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.term()
                self.state = 35
                self.match(exprParser.SUB)
                self.state = 36
                self.expr()
                pass

            elif la_ == 3:
                localctx = exprParser.ToTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivRightContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(exprParser.FactorContext,0)

        def DIV(self):
            return self.getToken(exprParser.DIV, 0)
        def term(self):
            return self.getTypedRuleContext(exprParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivRight" ):
                return visitor.visitDivRight(self)
            else:
                return visitor.visitChildren(self)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(exprParser.FactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulLeftContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.FactorContext)
            else:
                return self.getTypedRuleContext(exprParser.FactorContext,i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.MUL)
            else:
                return self.getToken(exprParser.MUL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulLeft" ):
                return visitor.visitMulLeft(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = exprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = exprParser.MulLeftContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.factor()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 42
                    self.match(exprParser.MUL)
                    self.state = 43
                    self.factor()
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = exprParser.DivRightContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.factor()
                self.state = 50
                self.match(exprParser.DIV)
                self.state = 51
                self.term()
                pass

            elif la_ == 3:
                localctx = exprParser.ToFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(exprParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = exprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = exprParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(exprParser.INT)
                pass
            elif token in [8]:
                localctx = exprParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(exprParser.ID)
                pass
            elif token in [2]:
                localctx = exprParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(exprParser.T__1)
                self.state = 59
                self.expr()
                self.state = 60
                self.match(exprParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






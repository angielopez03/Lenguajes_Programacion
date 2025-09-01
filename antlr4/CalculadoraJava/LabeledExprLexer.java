// Generated from LabeledExpr.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class LabeledExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, FUNC=5, MUL=6, DIV=7, ADD=8, SUB=9, ID=10, 
		INT=11, NEWLINE=12, WS=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "FUNC", "MUL", "DIV", "ADD", "SUB", "ID", 
			"INT", "NEWLINE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'!'", "'('", "')'", null, "'*'", "'/'", "'+'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "FUNC", "MUL", "DIV", "ADD", "SUB", "ID", 
			"INT", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public LabeledExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LabeledExpr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\rU\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u00046\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\t\u0004\tA\b\t\u000b\t\f\tB\u0001\n\u0004"+
		"\nF\b\n\u000b\n\f\nG\u0001\u000b\u0003\u000bK\b\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0004\fP\b\f\u000b\f\f\fQ\u0001\f\u0001\f\u0000\u0000\r"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u0001\u0000"+
		"\u0003\u0002\u0000AZaz\u0001\u000009\u0002\u0000\t\t  ]\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0001\u001b\u0001\u0000\u0000\u0000\u0003\u001d\u0001\u0000\u0000"+
		"\u0000\u0005\u001f\u0001\u0000\u0000\u0000\u0007!\u0001\u0000\u0000\u0000"+
		"\t5\u0001\u0000\u0000\u0000\u000b7\u0001\u0000\u0000\u0000\r9\u0001\u0000"+
		"\u0000\u0000\u000f;\u0001\u0000\u0000\u0000\u0011=\u0001\u0000\u0000\u0000"+
		"\u0013@\u0001\u0000\u0000\u0000\u0015E\u0001\u0000\u0000\u0000\u0017J"+
		"\u0001\u0000\u0000\u0000\u0019O\u0001\u0000\u0000\u0000\u001b\u001c\u0005"+
		"=\u0000\u0000\u001c\u0002\u0001\u0000\u0000\u0000\u001d\u001e\u0005!\u0000"+
		"\u0000\u001e\u0004\u0001\u0000\u0000\u0000\u001f \u0005(\u0000\u0000 "+
		"\u0006\u0001\u0000\u0000\u0000!\"\u0005)\u0000\u0000\"\b\u0001\u0000\u0000"+
		"\u0000#$\u0005s\u0000\u0000$%\u0005i\u0000\u0000%6\u0005n\u0000\u0000"+
		"&\'\u0005c\u0000\u0000\'(\u0005o\u0000\u0000(6\u0005s\u0000\u0000)*\u0005"+
		"t\u0000\u0000*+\u0005a\u0000\u0000+6\u0005n\u0000\u0000,-\u0005s\u0000"+
		"\u0000-.\u0005q\u0000\u0000./\u0005r\u0000\u0000/6\u0005t\u0000\u0000"+
		"01\u0005l\u0000\u000016\u0005n\u0000\u000023\u0005l\u0000\u000034\u0005"+
		"o\u0000\u000046\u0005g\u0000\u00005#\u0001\u0000\u0000\u00005&\u0001\u0000"+
		"\u0000\u00005)\u0001\u0000\u0000\u00005,\u0001\u0000\u0000\u000050\u0001"+
		"\u0000\u0000\u000052\u0001\u0000\u0000\u00006\n\u0001\u0000\u0000\u0000"+
		"78\u0005*\u0000\u00008\f\u0001\u0000\u0000\u00009:\u0005/\u0000\u0000"+
		":\u000e\u0001\u0000\u0000\u0000;<\u0005+\u0000\u0000<\u0010\u0001\u0000"+
		"\u0000\u0000=>\u0005-\u0000\u0000>\u0012\u0001\u0000\u0000\u0000?A\u0007"+
		"\u0000\u0000\u0000@?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000"+
		"B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0014\u0001\u0000"+
		"\u0000\u0000DF\u0007\u0001\u0000\u0000ED\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000"+
		"H\u0016\u0001\u0000\u0000\u0000IK\u0005\r\u0000\u0000JI\u0001\u0000\u0000"+
		"\u0000JK\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0005\n\u0000"+
		"\u0000M\u0018\u0001\u0000\u0000\u0000NP\u0007\u0002\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0006\f\u0000\u0000"+
		"T\u001a\u0001\u0000\u0000\u0000\u0006\u00005BGJQ\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
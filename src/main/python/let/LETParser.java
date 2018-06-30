// Generated from LET.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LETParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, NUMBER=12, IDENTIFIER=13, WS=14;
	public static final int
		RULE_program = 0, RULE_expression = 1, RULE_constant_expression = 2, RULE_difference_expression = 3, 
		RULE_zero_expression = 4, RULE_if_expression = 5, RULE_variable_expression = 6, 
		RULE_let_expression = 7;
	public static final String[] ruleNames = {
		"program", "expression", "constant_expression", "difference_expression", 
		"zero_expression", "if_expression", "variable_expression", "let_expression"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'-'", "'('", "','", "')'", "'zero?'", "'if'", "'then'", "'else'", 
		"'let'", "'='", "'in'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		"NUMBER", "IDENTIFIER", "WS"
	};
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

	@Override
	public String getGrammarFileName() { return "LET.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LETParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Constant_expressionContext constant_expression() {
			return getRuleContext(Constant_expressionContext.class,0);
		}
		public Difference_expressionContext difference_expression() {
			return getRuleContext(Difference_expressionContext.class,0);
		}
		public Zero_expressionContext zero_expression() {
			return getRuleContext(Zero_expressionContext.class,0);
		}
		public If_expressionContext if_expression() {
			return getRuleContext(If_expressionContext.class,0);
		}
		public Variable_expressionContext variable_expression() {
			return getRuleContext(Variable_expressionContext.class,0);
		}
		public Let_expressionContext let_expression() {
			return getRuleContext(Let_expressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expression);
		try {
			setState(24);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				constant_expression();
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				difference_expression();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 3);
				{
				setState(20);
				zero_expression();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 4);
				{
				setState(21);
				if_expression();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 5);
				{
				setState(22);
				variable_expression();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 6);
				{
				setState(23);
				let_expression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Constant_expressionContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LETParser.NUMBER, 0); }
		public Constant_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitConstant_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Constant_expressionContext constant_expression() throws RecognitionException {
		Constant_expressionContext _localctx = new Constant_expressionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_constant_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Difference_expressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Difference_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_difference_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitDifference_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Difference_expressionContext difference_expression() throws RecognitionException {
		Difference_expressionContext _localctx = new Difference_expressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_difference_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(T__0);
			setState(29);
			match(T__1);
			setState(30);
			expression();
			setState(31);
			match(T__2);
			setState(32);
			expression();
			setState(33);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Zero_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Zero_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_zero_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitZero_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Zero_expressionContext zero_expression() throws RecognitionException {
		Zero_expressionContext _localctx = new Zero_expressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_zero_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(T__4);
			setState(36);
			match(T__1);
			setState(37);
			expression();
			setState(38);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_expressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public If_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitIf_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_expressionContext if_expression() throws RecognitionException {
		If_expressionContext _localctx = new If_expressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_if_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(T__5);
			setState(41);
			expression();
			setState(42);
			match(T__6);
			setState(43);
			expression();
			setState(44);
			match(T__7);
			setState(45);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_expressionContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LETParser.IDENTIFIER, 0); }
		public Variable_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitVariable_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Variable_expressionContext variable_expression() throws RecognitionException {
		Variable_expressionContext _localctx = new Variable_expressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variable_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Let_expressionContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LETParser.IDENTIFIER, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Let_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LETVisitor ) return ((LETVisitor<? extends T>)visitor).visitLet_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Let_expressionContext let_expression() throws RecognitionException {
		Let_expressionContext _localctx = new Let_expressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_let_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(T__8);
			setState(50);
			match(IDENTIFIER);
			setState(51);
			match(T__9);
			setState(52);
			expression();
			setState(53);
			match(T__10);
			setState(54);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20;\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\5\3\33\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2\67\2\22\3\2\2\2\4\32\3\2\2\2\6"+
		"\34\3\2\2\2\b\36\3\2\2\2\n%\3\2\2\2\f*\3\2\2\2\16\61\3\2\2\2\20\63\3\2"+
		"\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\33\5\6\4\2\25\33\5\b\5\2\26\33\5\n"+
		"\6\2\27\33\5\f\7\2\30\33\5\16\b\2\31\33\5\20\t\2\32\24\3\2\2\2\32\25\3"+
		"\2\2\2\32\26\3\2\2\2\32\27\3\2\2\2\32\30\3\2\2\2\32\31\3\2\2\2\33\5\3"+
		"\2\2\2\34\35\7\16\2\2\35\7\3\2\2\2\36\37\7\3\2\2\37 \7\4\2\2 !\5\4\3\2"+
		"!\"\7\5\2\2\"#\5\4\3\2#$\7\6\2\2$\t\3\2\2\2%&\7\7\2\2&\'\7\4\2\2\'(\5"+
		"\4\3\2()\7\6\2\2)\13\3\2\2\2*+\7\b\2\2+,\5\4\3\2,-\7\t\2\2-.\5\4\3\2."+
		"/\7\n\2\2/\60\5\4\3\2\60\r\3\2\2\2\61\62\7\17\2\2\62\17\3\2\2\2\63\64"+
		"\7\13\2\2\64\65\7\17\2\2\65\66\7\f\2\2\66\67\5\4\3\2\678\7\r\2\289\5\4"+
		"\3\29\21\3\2\2\2\3\32";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
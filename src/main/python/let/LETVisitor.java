// Generated from LET.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LETParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LETVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LETParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(LETParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(LETParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#constant_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstant_expression(LETParser.Constant_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#difference_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDifference_expression(LETParser.Difference_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#zero_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitZero_expression(LETParser.Zero_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#if_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_expression(LETParser.If_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#variable_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_expression(LETParser.Variable_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LETParser#let_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLet_expression(LETParser.Let_expressionContext ctx);
}
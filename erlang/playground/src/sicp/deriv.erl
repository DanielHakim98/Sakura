-module(deriv).

-export([is_variable/1, is_same_variable/2, make_sum/2, is_sum/1, addend/1, augend/1,
         make_product/2, is_product/1, multiplier/1, multiplicand/1, make_exponent/2,
         is_exponent/1, base/1, exponent/1, derivative/2]).

%% Check if input is a variable (string)
%% is_variable/1
is_variable(Expression) -> io_lib:latin1_char_list(Expression).

%% Check if both inputs are the same variable
%% is_same_variable/2
is_same_variable(V1, V2) ->
    case {is_variable(V1), is_variable(V2)} of
        {true, true} -> V1 =:= V2;
        _ -> false
    end.

%% Sum constructor
make_sum(V1, 0) -> V1;
make_sum(0, V2) -> V2;
make_sum(V1, V2) when is_number(V1), is_number(V2) -> V1 + V2;
make_sum(V1, V2) -> ['+', V1, V2].

%% Check is list is a sum expression
is_sum([H | _]) when H =:= '+' -> true;
is_sum(_) -> false.

%% Extract first sum term
addend(Expression) -> first_term(Expression).

%% Extract second sum term
augend(Expression) -> second_term(Expression).

%% Product constructor
make_product(V1, V2) when V1 =:= 0; V2 =:= 0 -> 0;
make_product(V1, 1) -> V1;
make_product(1, V2) -> V2;
make_product(V1, V2) when is_number(V1), is_number(V2) -> V1 * V2;
make_product(V1, V2) -> ['*', V1, V2].

%% Check is list is a product expression
is_product([H | _]) when H =:= '*' -> true;
is_product(_) -> false.

%% Extract first product term
multiplier(Expression) -> first_term(Expression).

%% Extract second product term
multiplicand(Expression) -> second_term(Expression).

%% Exponent constructor
make_exponent(_, 0) -> 1;
make_exponent(V1, 1) -> V1;
make_exponent(V1, V2) when is_number(V1), is_number(V2) -> math:pow(V1, V2);
make_exponent(V1, V2) -> ['^', V1, V2].

%% Check is list is a exponent expression
is_exponent([H | _]) when H =:= '^' -> true;
is_exponent(_) -> false.

%% Extract base
base(Expression) -> first_term(Expression).

%% Extract exponent
exponent(Expression) -> second_term(Expression).

%% Extract first term
first_term([_ | Tail]) ->
    case Tail of
        [Head | _] -> Head;
        _ -> {error, "could not extract head(tail(Input))"}
    end;
first_term(_) -> {error, "invalid input format. must be a list"}.

%% Extract the second term
second_term([Operator, _ | Tail]) ->
    case Tail of
        [Head] -> Head;
        _ -> [Operator | Tail]
    end;
second_term(_) -> {error, "invalid input format. must be a list"}.

derivative(Expr, _) when is_number(Expr) -> 0;
derivative(Expr, Var) ->
    case is_variable(Expr) of
        true ->
            case is_same_variable(Expr, Var) of
                true -> 1;
                false -> 0
            end;
        false ->
            case Expr of
                ['+' | _] -> make_sum(derivative(addend(Expr), Var), derivative(augend(Expr), Var));
                ['*' | _] ->
                    make_sum(make_product(multiplier(Expr), derivative(multiplicand(Expr), Var)),
                             make_product(derivative(multiplier(Expr), Var), multiplicand(Expr)));
                [_ | _] -> {error, "not implemented"}
            end
    end.

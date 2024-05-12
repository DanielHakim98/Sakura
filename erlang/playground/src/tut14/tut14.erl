-module(tut14).
-export([start/0, say_something/2]).

say_something(_, 0) ->
    done;
say_something(What, Times) ->
    io:format("~p #~p~n", [What, Times]),
    say_something(What, Times -1).

start()->
    P1 = spawn(tut14, say_something, [hello, 3]),
    P2 = spawn(tut14, say_something, [goodbye, 5]),
    io:format("~p~n", [{P1,P2}]).
    % io:format("waiting for both processes to finish").

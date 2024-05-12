-module(functions).
-export([head/1, tail/1, second/1, same/2, valid_time/1]).

head([H|_]) -> H.
tail([_|T])-> T.
second([_,X|_]) -> X.


same(X,X) ->
    true;
same(_,_) ->
    false.


valid_time({Date = {Y,M,D}, Time={H,Min,S}}) when H >= 0,  H < 24 ->
    io:format("The Date tuple(~p) says today is : ~p/~p/~p, ~n", [Date, Y, M,D]),
    io:format("The time tuple(~p) indicates: ~p:~p:~p.~n", [Time, H, Min, S]);
valid_time(_) ->
    io:format("Stop feeding me wrong data!~n").


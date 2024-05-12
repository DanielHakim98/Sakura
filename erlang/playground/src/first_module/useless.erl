-module(useless).
-export([add/2, greet_and_add_two/1]).

%% Add two numbers and return the total.
%% useless:add/1 is showing an example of exporting function in a module.
add(X,Y) ->
    X + Y.

%% Show greetings.
%% io:format/1 is the standard function used to output text.
hello() ->
    io:format("Hello, World!~n").


greet_and_add_two(X)->
    hello(),
    add(X, 2).
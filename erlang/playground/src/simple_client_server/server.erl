-module(server).
-export([start/0, loop/0]).

start()->
    spawn(server, loop, []).

loop() ->
    receive
        Client ->
            io:format("Received message from ~p~n", [Client]),
            Client !{self(), "message from server"}
    end,
    loop().

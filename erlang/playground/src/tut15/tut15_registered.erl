-module(tut15_registered).
-export[ping/1, pong/0, start/0].

ping(0)->
    Ping_PID = self(),
    pong_server ! {finished, Ping_PID},
    io:format("Ping ~p finished playing with Pong ~p~n", [Ping_PID, pong_server]);
ping(N)->
    Ping_PID = self(),
    pong_server ! {ping, Ping_PID},
    receive
        pong ->
            io:format("Ping ~p received Pong ~p~n", [Ping_PID, pong_server])
    end,
    ping(N-1).

pong() ->
    receive
        {finished, Ping_PID} ->
            io:format("Pong has finished playing Ping ~p~n", [Ping_PID]);
        {ping, Ping_PID} ->
            io:format("Pong received Ping from Ping ~p~n", [Ping_PID]),
            Ping_PID ! pong,
            pong()
    end.

start() ->
    register(pong_server, spawn(tut15_registered, pong, [])),
    spawn(tut15_registered, ping, [3]).
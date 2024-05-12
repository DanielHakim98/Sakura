-module(tut15).
-export([start/0, ping/2, pong/0]).

ping(0, Pong_PID) ->
    SelfID = self(),
    Pong_PID ! {finished, SelfID},
    io:format("Ping ~p:  finished~n", [SelfID]);
ping(N, Pong_PID) ->
    SelfID = self(),
    Pong_PID ! {ping, SelfID},
    receive
        {pong, Pong_PID} ->
            io:format("Ping ~p: received pong ~p ~n", [SelfID, Pong_PID])
    end,
    ping(N-1, Pong_PID).

pong() ->
    receive
        {finished, Ping_PID} ->
            io:format("Pong finished for ping ~p~n", [Ping_PID]);
        {ping, Ping_PID} ->
            io:format("Pong received ping ~p ~n", [Ping_PID]),
            Ping_PID ! {pong, self()},
            pong()
    end.

start() ->
    % Start server 'Pong'
    Pong_PID = spawn(tut15, pong, []),

    % Start client 'Ping'
    spawn(tut15, ping, [3, Pong_PID]),
    start.
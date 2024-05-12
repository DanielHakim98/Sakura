-module(client).
-export([ping/1]).

ping(Server) ->
    Server !self(),
    receive
        Data-> io:format("~p~n",[Data] )
    end.
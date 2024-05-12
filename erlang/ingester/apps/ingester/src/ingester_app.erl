%%%-------------------------------------------------------------------
%% @doc ingester public API
%% @end
%%%-------------------------------------------------------------------

-module(ingester_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    ingester_sup:start_link().

stop(_State) ->
    ok.

%% internal functions

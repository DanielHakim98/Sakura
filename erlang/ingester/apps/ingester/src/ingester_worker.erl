-module(ingester_worker).
-export([start_link/0, init/1]).


start_link() ->
    gen_server:start_link(?MODULE, [], []).

init([]) ->
    call_api().

call_api() ->
    {ok, {{_, 200, _}, _, Body}}
        = httpc:request(get, {"https://www.erlang.org", []}, [{ssl, httpc:ssl_verify_host_options(true)}], []),
    io:format("~s", [Body]).
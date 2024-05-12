-module(powers).

-export([raise/2, raise_tail/2]).

raise(_, 0) -> 1;
raise(Base, 1) -> Base;
raise(Base, N) when N > 0 -> Base * raise(Base, N - 1);
raise(Base, N) when N < 0 -> 1.0 / raise(Base, -1 * N).

raise_tail(_, 0) -> 1;
raise_tail(Base, 1) -> Base;
raise_tail(Base, N) -> loop_raise(Base, N, 1).

loop_raise(_, 0, Accumulator) -> Accumulator;
loop_raise(Base, N, Accumulator) when N > 0 ->
    loop_raise(Base, N - 1, Accumulator * Base);
loop_raise(Base, N, Accumulator) when N < 0 ->
    1.0 / loop_raise(Base, -1 * N, Accumulator).

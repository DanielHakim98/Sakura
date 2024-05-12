-module(caesar_cipher).
-export([run/2]).
-define(UPPER_A, 65).
-define(UPPER_Z, 90).
-define(LOWER_A, 97).
-define(LOWER_Z, 122).
-define(TOTAL_CHARS, 26).

run(Sentence, 0) -> {ok, Sentence};
run(_, N) when is_integer(N) =:=  false ->{error, "shifter must be a number"};
run(Sentence, N) ->
    shift_sentence(Sentence, N, []).

shift_sentence([], _, Shifted) ->{ok, Shifted};
shift_sentence(Sentence, N, PrevShifted) ->
    [Head | Tail] = Sentence,
    Shifted = case Head of
        Head when Head >= ?UPPER_A, Head =< ?UPPER_Z ->
            PrevShifted ++ [shift_char(Head, normalize_shifter(N), ?UPPER_A)];
        Head when Head >= ?LOWER_A, Head =< ?LOWER_Z ->
            PrevShifted ++ [shift_char(Head, normalize_shifter(N), ?LOWER_A)];
        _ -> PrevShifted ++ [Head]
    end,
    shift_sentence(Tail, N, Shifted).

%% Shortcut way to normalize the shifter.
%% Previously, the way I did it by adding the char with the shifter,
%% and then check the result is out of range 65-90 or 97-122.
%% if yes, then do while loop substracting/adding 26 to shifted char until it the value is within
%% ascii character decimals.

%% let say if Shifter is negative (Ex: -100), we need to add 26 four times to the value
%% until it becomes positive integer and less or equal 26.
%% 4 = -100 + 26 + 26 + 26 + 26.,
normalize_shifter(Shifter) when Shifter < 0 -> (Shifter rem ?TOTAL_CHARS )+ ?TOTAL_CHARS;

%% if Shifter is positive (Ex: 100), we need to substract 26 2 times from the value
%% until it become less or equal 26.
%% 21 = 73 - 26 - 26.
normalize_shifter(Shifter) -> Shifter rem ?TOTAL_CHARS.


%% StartChar: can be either UPPER_A (65) or LOWER_A (97)
%% DistanceFromStartChar:
%%      the difference between StartChar and Char, if Char is B (66),
%%      then the value would be 66 - 65 = 1
%% DistanceToShifted:
%%      if 'DistanceFromStartChar' + 'Shifter' is less than total alphabets (26),
%%          then the total is taken as it is
%%      else,
%%          it calculates the remainder when divided by total alphabets (26),
%%
shift_char(Char, Shifter, StartChar) ->
    DistanceFromStartChar = Char - StartChar,
    DistanceToShifted = (DistanceFromStartChar + Shifter) rem ?TOTAL_CHARS,
    StartChar + DistanceToShifted.
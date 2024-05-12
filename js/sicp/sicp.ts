export const sicp = (function () {
  //-----Base implementation------
  //Primitive procedure
  let cons = (x, y) => [x, y];
  let car = (pair: any[]) => pair[0];
  let cdr = (pair: any[]) => pair[1];
  //Nil definition
  let nil = [];
  let isNil = (obj: any) =>
    obj == null || (Array.isArray(obj) && obj.length == 0);
  //Helper procedure to build, extract, compare and print list
  let cadr = (pair) => car(cdr(pair));
  let list = (...args) => {
    if (args.length > 1) return cons(args[0], list(...args.slice(1)));
    else if (args.length == 0) return nil;
    else return cons(args[0], nil);
  };
  let isEqual = (seq1, seq2) => JSON.stringify(seq1) === JSON.stringify(seq2);
  let print = (seq) => JSON.stringify(seq);
  //List operations
  let listRef = (seq, n) => {
    if (n == 0) return car(seq);
    else return listRef(cdr(seq), n - 1);
  };
  let length = (seq) => {
    let lengthIter = (s, count) => {
      if (isNil(s)) return count;
      else return lengthIter(cdr(s), count + 1);
    };
    return lengthIter(seq, 0);
  };
  let append = (list1, list2) => {
    if (isNil(list1)) return list2;
    else return cons(car(list1), append(cdr(list1), list2));
  };

  //------Solutions of ex2.17------
  let lastPair = (seq) => {
    if (isNil(seq)) return nil;
    let rest = cdr(seq);
    if (isNil(rest) && isNil(car(rest))) return car(seq);
    else return lastPair(rest);
  };
  //------Solutions of ex2.18------
  let reverse = (seq) => {
    let reverseIter = (ret, s) => {
      if (isNil(s)) return ret;
      let first = car(s);
      let rest = cdr(s);
      return reverseIter(cons(first, ret), rest);
    };
    return reverseIter(nil, seq);
  };

  //------Tree------
  let isPair = (seq) => Array.isArray(seq) && seq.length == 2;
  let countLeaves = (seq) => {
    if (isNil(seq)) return 0;
    else if (!isPair(seq)) return 1;
    else return countLeaves(car(seq)) + countLeaves(cdr(seq));
  };

  //Export object in case not to pollute global enviroment
  return {
    //Base
    cons: cons,
    car: car,
    cdr: cdr,
    nil: nil,
    isNil: isNil,
    //List
    cadr: cadr,
    list: list,
    isEqual: isEqual,
    print: print,
    listRef: listRef,
    length: length,
    append: append,
    //Other
    lastPair: lastPair,
    reverse: reverse,
    //Tree
    isPair: isPair,
    countLeaves: countLeaves,
  };
})();

function pair(head: any, tail: any) {
  return (idx: number): number => {
    if (idx > 1 || idx < 0) {
      throw Error("idx must be 0 or 1");
    }
    return idx == 0 ? head : tail;
  };
}

function head(pair: (i: number) => number) {
  return pair(0);
}

function tail(pair: (i: number) => number) {
  return pair(1);
}

// coordinate is just an abstraction of pair
const coord = pair;
const x_coord = head;
const y_coord = tail;

const point = coord(-12, 5);
console.log("x_coor(point) = ", x_coord(point));
console.log("y_coord(point) = ", y_coord(point));

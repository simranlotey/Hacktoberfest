function multiplyMatrices(matrixA: number[][], matrixB: number[][]): number[][] {
  const rowsA = matrixA.length;
  const colsA = matrixA[0].length;
  const rowsB = matrixB.length;
  const colsB = matrixB[0].length;

  if (colsA !== rowsB) {
    throw new Error("Incompatible matrices for multiplication");
  }

  const result: number[][] = new Array(rowsA);
  for (let i = 0; i < rowsA; i++) {
    result[i] = new Array(colsB).fill(0);
  }

  for (let i = 0; i < rowsA; i++) {
    for (let j = 0; j < colsB; j++) {
      for (let k = 0; k < colsA; k++) {
        result[i][j] += matrixA[i][k] * matrixB[k][j];
      }
    }
  }

  return result;
}

/* Testcase:
const matrixA: number[][] = [[2, 3], [4, 1]];
const matrixB: number[][] = [[5, 6], [7, 8]];

try {
  const result = multiplyMatrices(matrixA, matrixB);
  console.log("Matrix A * Matrix B:");
  for (let row of result) {
    console.log(row.join(" "));
  }
} catch (error) {
  console.error(error.message);
}
*/

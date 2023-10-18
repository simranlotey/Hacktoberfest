function multiplyMatrices(matrixA: number[][], matrixB: number[][]): number[][] | null {
    const rowsA = matrixA.length;
    const colsA = matrixA[0].length;
    const rowsB = matrixB.length;
    const colsB = matrixB[0].length;

    if (colsA !== rowsB) {
        console.error("Matrix dimensions are not compatible for multiplication.");
        return null;
    }

    const result: number[][] = [];

    for (let i = 0; i < rowsA; i++) {
        result[i] = [];

        for (let j = 0; j < colsB; j++) {
            let sum = 0;

            for (let k = 0; k < colsA; k++) {
                sum += matrixA[i][k] * matrixB[k][j];
            }

            result[i][j] = sum;
        }
    }

    return result;
}

// Example usage
const matrixA = [
    [2, 3],
    [4, 5],
];

const matrixB = [
    [6, 7],
    [8, 9],
];

const product = multiplyMatrices(matrixA, matrixB);

if (product) {
    console.log("Matrix A * Matrix B:");
    for (const row of product) {
        console.log(row);
    }
}

function solveSudoku(board: number[][]): boolean {
  const emptyCell = findEmptyCell(board);
  
  if (!emptyCell) {
    // No empty cells left, the Sudoku puzzle is solved
    return true;
  }

  const [row, col] = emptyCell;
  
  for (let num = 1; num <= 9; num++) {
    if (isValidMove(board, row, col, num)) {
      board[row][col] = num;

      if (solveSudoku(board)) {
        return true; // Recursion succeeded
      }

      board[row][col] = 0; // Backtrack
    }
  }

  return false; // No valid solution found
}

function findEmptyCell(board: number[][]): [number, number] | null {
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      if (board[row][col] === 0) {
        return [row, col];
      }
    }
  }
  return null; // No empty cell found
}

function isValidMove(board: number[][], row: number, col: number, num: number): boolean {
  // Check row
  for (let i = 0; i < 9; i++) {
    if (board[row][i] === num) {
      return false;
    }
  }

  // Check column
  for (let i = 0; i < 9; i++) {
    if (board[i][col] === num) {
      return false;
    }
  }

  // Check 3x3 grid
  const gridStartRow = Math.floor(row / 3) * 3;
  const gridStartCol = Math.floor(col / 3) * 3;
  for (let i = gridStartRow; i < gridStartRow + 3; i++) {
    for (let j = gridStartCol; j < gridStartCol + 3; j++) {
      if (board[i][j] === num) {
        return false;
      }
    }
  }

  return true;
}

/* Testcase
const sudokuBoard: number[][] = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9],
];

if (solveSudoku(sudokuBoard)) {
  console.log("Solved Sudoku:");
  for (let row of sudokuBoard) {
    console.log(row.join(" "));
  }
} else {
  console.log("No solution exists.");
}*/

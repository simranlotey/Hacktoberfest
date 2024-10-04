public class NKnightsSolver {
    public static void main(String[] args) {
        int n = 2;
        boolean[][] board = new boolean[n][n];
        knight(board, 0, 0, n);
    }
    static void knight(boolean[][] board, int row, int col, int knights) {
        if(knights==0) {
            display1(board);
            System.out.println();
            return;
        }
        if(row == board.length-1 && col == board.length-1) {
            return;
        }
        if(col == board.length) {
            knight(board, row+1, 0, knights);
            return;
        }
        if(isSafe1(board, row, col)) {
            board[row][col] = true;
            knight(board, row, col+1, knights-1);
            board[row][col] = false;
        }
        knight(board, row, col+1, knights);
    }
    static boolean isSafe1(boolean[][] board, int row, int col) {
        if(isValid(board, row-2, col-1)) {
            if(board[row-2][col-1]) {
                return false;
            }
        }
        if(isValid(board, row-1, col-2)) {
            if(board[row-1][col-2]) {
                return false;
            }
        }
        if(isValid(board, row-2, col+1)) {
            if(board[row-2][col+1]) {
                return false;
            }
        }
        if(isValid(board, row-1, col+2)) {
            if(board[row-1][col+2]) {
                return false;
            }
        }
        return true;
    }
    //do not repeat yourself, hence created this function
    static boolean isValid(boolean[][] board, int row, int col) {
        if(row>=0 && col>=0 && row<board.length && col<board.length && !board[row][col]) {
            return true;
        }
        return false;
    }
    static void display1(boolean[][] board) {
        for(boolean[] row: board) {
            for(boolean element: row) {
                if(element) {
                    System.out.print("K ");
                } else {
                    System.out.print(".");
                }
            }
            System.out.println();
        }
    }
}
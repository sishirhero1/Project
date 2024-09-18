public class SudokuSolver {
    public static boolean solveSudoku(int[][] board) {
        // Checking if it's a 9x9 Sudoku puzzle
        int N = board.length;
        if (N != 9)
            return false;

        int row = -1;
        int col = -1;
        boolean isEmpty = true;

        // Finding an empty cell
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    row = i;
                    col = j;
                    isEmpty = false;
                    break;
                }
            }
            if (!isEmpty)
                break;
        }

        // If no empty cell is found, the puzzle is solved
        if (isEmpty)
            return true;

        // Try filling the empty cell with numbers from 1 to 9
        for (int num = 1; num <= 9; num++) {
            if (isSafe(board, row, col, num)) {
                board[row][col] = num;

                if (solveSudoku(board))
                    return true;

                // If the current configuration doesn't lead to a solution, reset the cell and backtrack it.
                board[row][col] = 0;
            }
        }
        return false;
    }

    public static boolean isSafe(int[][] board, int row, int col, int num) {
        // Check if 'num' is not already present in the current row, current column, and current 3x3 subgrid
        return !usedInRow(board, row, num) && !usedInColumn(board, col, num) && !usedInSubgrid(board, row - row % 3, col - col % 3, num);
    }

    public static boolean usedInRow(int[][] board, int row, int num) {
        for (int col = 0; col < 9; col++) {
            if (board[row][col] == num)
                return true;
        }
        return false;
    }

    public static boolean usedInColumn(int[][] board, int col, int num) {
        for (int row = 0; row < 9; row++) {
            if (board[row][col] == num)
                return true;
        }
        return false;
    }

    public static boolean usedInSubgrid(int[][] board, int startRow, int startCol, int num) {
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                if (board[row + startRow][col + startCol] == num)
                    return true;
            }
        }
        return false;
    }

    public static void printBoard(int[][] board) {
        int N = board.length;
        for (int r = 0; r < N; r++) {
            for (int d = 0; d < N; d++) {
                System.out.print(board[r][d]);
                System.out.print(" ");
            }
            System.out.print("\n");

            if ((r + 1) % 3 == 0)
                System.out.print("");
        }
    }

    public static void main(String[] args) {
        int[][] board = new int[][] {
            {5, 3, 0, 0, 7, 0, 0, 0, 0},
            {6, 0, 0, 1, 9, 5, 0, 0, 0},
            {0, 9, 8, 0, 0, 0, 0, 6, 0},
            {8, 0, 0, 0, 6, 0, 0, 0, 3},
            {4, 0, 0, 8, 0, 3, 0, 0, 1},
            {7, 0, 0, 0, 2, 0, 0, 0, 6},
            {0, 6, 0, 0, 0, 0, 2, 8, 0},
            {0, 0, 0, 4, 1, 9, 0, 0, 5},
            {0, 0, 0, 0, 8, 0, 0, 7, 9}
        };

        if (solveSudoku(board))
            printBoard(board);
        else
            System.out.println("No solution exists.");
    }
}

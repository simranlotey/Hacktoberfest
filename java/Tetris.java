import javax.swing.*;

import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.util.Timer;

// this is class for all the shapes and their rotations
class Shape {
    Tetrominoe pieceShape; // the shape of the piece
    int coords[][]; // the coordinates of the piece
    int[][][] coordsTable; // the coordinates of the piece in all its rotations


    public Shape() {
        
        initShape(); // initialize the shape
    }
    
    void initShape() {

        coords = new int[4][2]; // initialize the size of the piece
        setShape(Tetrominoe.NoShape); // set the shape to NoShape
    }

    // set the shape of the piece to the given shape and set the coordinates of the piece to the coordinates of the given shape
    protected void setShape(Tetrominoe shape) {

         coordsTable = new int[][][] { 
            { { 0, 0 },   { 0, 0 },   { 0, 0 },   { 0, 0 } },
            { { 0, -1 },  { 0, 0 },   { -1, 0 },  { -1, 1 } },
            { { 0, -1 },  { 0, 0 },   { 1, 0 },   { 1, 1 } },
            { { 0, -1 },  { 0, 0 },   { 0, 1 },   { 0, 2 } },
            { { -1, 0 },  { 0, 0 },   { 1, 0 },   { 0, 1 } },
            { { 0, 0 },   { 1, 0 },   { 0, 1 },   { 1, 1 } },
            { { -1, -1 }, { 0, -1 },  { 0, 0 },   { 0, 1 } },
            { { 1, -1 },  { 0, -1 },  { 0, 0 },   { 0, 1 } }
        };

        for (int i = 0; i < 4 ; i++) { // for the no of rows in the shape
            
            for (int j = 0; j < 2; ++j) { // for the no of columns in the shape
                
                coords[i][j] = coordsTable[shape.ordinal()][i][j]; // set the coordinates of the piece to the coordinates of the given shape
            }
        }
        
        pieceShape = shape; 
    }

    void setX(int index, int x) { coords[index][0] = x; } // set the x coordinate of the piece
    void setY(int index, int y) { coords[index][1] = y; } // set the y coordinate of the piece
    public int x(int index) { return coords[index][0]; } // get the x coordinate of the piece
    public int y(int index) { return coords[index][1]; } // get the y coordinate of the piece
    public Tetrominoe getShape()  { return pieceShape; } // get the shape of the piece

    // set the shape of the piece to a random shape everytime a new piece is created
    public void setRandomShape() {
        
        Random r = new Random(); // create a random object
        int x = Math.abs(r.nextInt()) % 7 + 1; // get a random number between 1 and 7
        Tetrominoe[] values = Tetrominoe.values();  // get all the shapes
        setShape(values[x]); // set the shape of the piece to a random shape
    }

    // get the minimum x coordinate of the piece
    public int minX() {
        
      int m = coords[0][0];
      
      for (int i=0; i < 4; i++) { // for the no of rows in the shape
          
          m = Math.min(m, coords[i][0]); // get the minimum x coordinate of the piece
      }
      
      return m; // return the minimum x coordinate of the piece
    }


    // get the minimum y coordinate of the piece
    public int minY() { 
        
      int m = coords[0][1]; 
      
      for (int i=0; i < 4; i++) { // for the no of rows in the shape
          
          m = Math.min(m, coords[i][1]); // get the minimum y coordinate of the piece
      }
      
      return m; // return the minimum y coordinate of the piece
    }

    // rotate the piece to the left
    public Shape rotateLeft() {
        
        if (pieceShape == Tetrominoe.SquareShape) // if the shape is a square shape
            return this; // return the shape without rotation

        Shape result = new Shape(); // create a new shape
        result.pieceShape = pieceShape; // set the shape of the new shape to the shape of the piece

        for (int i = 0; i < 4; ++i) { // for the no of rows in the shape
            
            result.setX(i, y(i)); // set the x coordinate of the new shape to the y coordinate of the piece
            result.setY(i, -x(i)); // set the y coordinate of the new shape to the negative x coordinate of the piece
        }
        
        return result; // return the new shape
    }

    // rotate the piece to the right
    public Shape rotateRight() {
        
        if (pieceShape == Tetrominoe.SquareShape) // if the shape is a square shape
            return this; // return the shape without rotation

        Shape result = new Shape(); // create a new shape
        result.pieceShape = pieceShape; // set the shape of the new shape to the shape of the piece

        for (int i = 0; i < 4; ++i) { // for the no of rows in the shape

            result.setX(i, -y(i)); // set the x coordinate of the new shape to the negative y coordinate of the piece
            result.setY(i, x(i)); // set the y coordinate of the new shape to the x coordinate of the piece
        }
        
        return result; // return the new shape
    }
}

enum Tetrominoe { NoShape, ZShape, SShape, LineShape, 
    TShape, SquareShape, LShape, MirroredLShape };

// this is the class for the board
class Board extends JPanel {

	static final long serialVersionUID = 1L;
	final int BOARD_WIDTH = 10; // the width of the board
    final int BOARD_HEIGHT = 22; // the height of the board
    final int INITIAL_DELAY = 100; // the initial delay of the timer
    final int PERIOD_INTERVAL = 300; // the period interval of the timer

    Timer timer; 
    boolean isFallingFinished = false; // check if the piece has finished falling
    boolean isStarted = false; // check if the game has started
    boolean isPaused = false; // check if the game is paused
    int numLinesRemoved = 0; // the number of lines removed
    int curX = 0; // the current x coordinate of the piece
    int curY = 0; // the current y coordinate of the piece
    JLabel statusbar;
    Shape curPiece;
    Tetrominoe[] board;

    public Board(Tetris parent) {

        initBoard(parent);
    }

    // initialize the board
    void initBoard(Tetris parent) {

        setFocusable(true);
        setBorder(BorderFactory.createLineBorder(Color.pink, 4));
        timer = new Timer();
        timer.scheduleAtFixedRate(new ScheduleTask(),
                INITIAL_DELAY, PERIOD_INTERVAL);

        curPiece = new Shape();

        statusbar = parent.getStatusBar();
        board = new Tetrominoe[BOARD_WIDTH * BOARD_HEIGHT];
        addKeyListener(new TAdapter());
        clearBoard();
    }

    int squareWidth() {
        return (int) getSize().getWidth() / BOARD_WIDTH;
    }

    int squareHeight() {
        return (int) getSize().getHeight() / BOARD_HEIGHT;
    }

    Tetrominoe shapeAt(int x, int y) {
        return board[(y * BOARD_WIDTH) + x];
    }

    public void start() {

        isStarted = true;
        clearBoard();
        newPiece();
    }

    void pause() {

        if (!isStarted) {
            return;
        }

        isPaused = !isPaused;

        if (isPaused) {

            statusbar.setText("Paused");
        } else {

            statusbar.setText(String.valueOf(numLinesRemoved));
        }
    }

    // draw the board
    void doDrawing(Graphics g) {

        Dimension size = getSize();
        int boardTop = (int) size.getHeight() - BOARD_HEIGHT * squareHeight();

        for (int i = 0; i < BOARD_HEIGHT; ++i) {

            for (int j = 0; j < BOARD_WIDTH; ++j) {

                Tetrominoe shape = shapeAt(j, BOARD_HEIGHT - i - 1);

                if (shape != Tetrominoe.NoShape) {
                    
                    drawSquare(g, 0 + j * squareWidth(),
                            boardTop + i * squareHeight(), shape);
                }
            }
        }

        if (curPiece.getShape() != Tetrominoe.NoShape) { // if the shape of the piece is not a no shape

            for (int i = 0; i < 4; ++i) { // for the no of rows in the shape

                int x = curX + curPiece.x(i); // get the x coordinate of the piece
                int y = curY - curPiece.y(i); // get the y coordinate of the piece
                drawSquare(g, 0 + x * squareWidth(),
                        boardTop + (BOARD_HEIGHT - y - 1) * squareHeight(),
                        curPiece.getShape()); // draw the piece on the board
            }
        }
    }

    // draw the square on the board
    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        doDrawing(g);
    }

    // draw the new coordinates of the piece while falling down
    void dropDown() {

        int newY = curY; // set the new y coordinate to the current y coordinate

        while (newY > 0) { // while the new y coordinate is greater than 0

            if (!tryMove(curPiece, curX, newY - 1)) { // if the piece cannot move to the new coordinates
                
                break; // break the loop
            }
            
            --newY; // decrement the new y coordinate
        }

        pieceDropped(); // call the piece dropped method
    }

    // draw the new coordinates of the piece while moving
    void oneLineDown() {

        if (!tryMove(curPiece, curX, curY - 1)) {
            
            pieceDropped();
        }
    }

    void clearBoard() {

        for (int i = 0; i < BOARD_HEIGHT * BOARD_WIDTH; ++i) {
            board[i] = Tetrominoe.NoShape;
        }
    }

    void pieceDropped() {

        for (int i = 0; i < 4; ++i) { 

            int x = curX + curPiece.x(i);
            int y = curY - curPiece.y(i);
            board[(y * BOARD_WIDTH) + x] = curPiece.getShape();
        }

        removeFullLines(); // remove the full lines

        if (!isFallingFinished) { // if the piece has not finished falling
            newPiece(); // create a new piece
        }
    }

    // create a new piece
    void newPiece() {

        curPiece.setRandomShape(); // set the shape of the piece to a random shape
        curX = BOARD_WIDTH / 2 + 1; // set the x coordinate of the piece to the middle of the board
        curY = BOARD_HEIGHT - 1 + curPiece.minY();

        if (!tryMove(curPiece, curX, curY)) { // if the piece cannot move to the new coordinates
            curPiece.setShape(Tetrominoe.NoShape); // set the shape of the piece to a no shape
            timer.cancel(); 
            isStarted = false;
            statusbar.setText("GAME OVER!");
        }
    }

    // check if the piece can move to the new coordinates
    boolean tryMove(Shape newPiece, int newX, int newY) {

        for (int i = 0; i < 4; ++i) {

            int x = newX + newPiece.x(i);
            int y = newY - newPiece.y(i);

            if (x < 0 || x >= BOARD_WIDTH || y < 0 || y >= BOARD_HEIGHT) { // if the new coordinates are out of the board
                return false; // return false
            }

            if (shapeAt(x, y) != Tetrominoe.NoShape) { // if the new coordinates are not a no shape
                return false; // return false
            }
        }

        curPiece = newPiece; // set the current piece to the new piece
        curX = newX;     // set the current x coordinate to the new x coordinate
        curY = newY;    // set the current y coordinate to the new y coordinate

        repaint(); // repaint the board with the new coordinates of the piece

        return true; // return true
    }

    // remove the full line from the board
    void removeFullLines() {

        int numFullLines = 0; // set the number of full lines to 0

        for (int i = BOARD_HEIGHT - 1; i >= 0; --i) { // for the no of rows in the board
            boolean lineIsFull = true; // set the line is full to true

            for (int j = 0; j < BOARD_WIDTH; ++j) { // for the no of columns in the board
                
                if (shapeAt(j, i) == Tetrominoe.NoShape) { // if the shape at the coordinates is a no shape
                    
                    lineIsFull = false; // set the line is full to false
                    break; // break the loop
                }
            }

            if (lineIsFull) { // if the line is full
                
                ++numFullLines; // increment the number of full lines
                
                for (int k = i; k < BOARD_HEIGHT - 1; ++k) { // for the no of rows in the board
                    for (int j = 0; j < BOARD_WIDTH; ++j) { // for the no of columns in the board
                        
                        board[(k * BOARD_WIDTH) + j] = shapeAt(j, k + 1); // set the shape at the coordinates to the shape at the coordinates below
                    }
                }
            }
        }

        if (numFullLines > 0) { // if the number of full lines is greater than 0

            numLinesRemoved += numFullLines; // increment the number of lines removed by the number of full lines
            statusbar.setText("Score: "+String.valueOf(numLinesRemoved)); // set the text of the score to the number of lines removed
            isFallingFinished = true; // set the piece has finished falling to true
            curPiece.setShape(Tetrominoe.NoShape); // set the shape of the piece to a no shape
            repaint();
        }
    }

    // draw the square on the board
    void drawSquare(Graphics g, int x, int y, 
            Tetrominoe shape) {

        Color colors[] = {
            new Color(0, 0, 0), new Color(204, 102, 102),
            new Color(102, 204, 102), new Color(102, 102, 204),
            new Color(204, 204, 102), new Color(204, 102, 204),
            new Color(102, 204, 204), new Color(218, 170, 0),
            
        };

        Color color = colors[shape.ordinal()];

        g.setColor(color);
        g.fillRect(x + 1, y + 1, squareWidth() - 2, squareHeight() - 2);

        g.setColor(color.brighter());
        g.drawLine(x, y + squareHeight() - 1, x, y);
        g.drawLine(x, y, x + squareWidth() - 1, y);

        g.setColor(color.darker());
        g.drawLine(x + 1, y + squareHeight() - 1,
                x + squareWidth() - 1, y + squareHeight() - 1);
        g.drawLine(x + squareWidth() - 1, y + squareHeight() - 1,
                x + squareWidth() - 1, y + 1);

    }

    void doGameCycle() {

        update();
        repaint();
    }

    void update() {
        
        if (isPaused) { // if the game is paused
            return; // return
        }

        if (isFallingFinished) { // if the piece has finished falling

            isFallingFinished = false; // set the piece has finished falling to false
            newPiece(); // create a new piece
        } else {

            oneLineDown(); // move the piece down one line
        }
    }

    // used to check the pressed keys
    class TAdapter extends KeyAdapter {

        @Override
        public void keyPressed(KeyEvent e) {
            
            if (!isStarted || curPiece.getShape() == Tetrominoe.NoShape) { // if the game has not started or the shape of the piece is a no shape
                return; // return
            }

            int keycode = e.getKeyCode(); // get the key code of the pressed key

            if (keycode == KeyEvent.VK_ENTER) { // if the pressed key is the enter key
                pause(); // pause the game
                return; // return
            }

            if (isPaused) { 
                return;
            }

            switch (keycode) { // switch the key code of the pressed key

                case KeyEvent.VK_LEFT: // if the pressed key is the left arrow
                    tryMove(curPiece, curX - 1, curY); // try to move the piece to the left
                    break;

                case KeyEvent.VK_RIGHT: // if the pressed key is the right arrow
                    tryMove(curPiece, curX + 1, curY); // try to move the piece to the right
                    break;

                case KeyEvent.VK_DOWN: // if the pressed key is the down arrow
                    tryMove(curPiece.rotateRight(), curX, curY); // try to rotate the piece to the right
                    break;

                case KeyEvent.VK_UP: // if the pressed key is the up arrow
                    tryMove(curPiece.rotateLeft(), curX, curY); // try to rotate the piece to the left
                    break;

                case KeyEvent.VK_SPACE: // if the pressed key is the space bar
                    dropDown(); // drop the piece down
                    break;

                case KeyEvent.VK_D: // if the pressed key is the d key
                    oneLineDown(); // move the piece down one line
                    break;
            }
        }
    }

    class ScheduleTask extends TimerTask {

        @Override
        public void run() {

            doGameCycle();
        }
    }
}

// main class of the game
class Tetris extends JFrame {

	static final long serialVersionUID = 1L;
	JLabel statusbar;

    public Tetris() {

        initUI();
    }

    void initUI() {
        
        JPanel panel = new JPanel();
        panel.setBackground(new Color(0XF5EBE0));

        statusbar = new JLabel("Score: 0");
        statusbar.setFont(new Font("MV Boli", Font.BOLD, 30));
        panel.add(statusbar, BorderLayout.NORTH);
    
        Board board = new Board(this);
        add(panel, BorderLayout.NORTH);
        add(board);
        board.setBackground(new Color(0Xf0e2d3));
        board.start();
        
        setTitle("Tetris");
        setSize(400, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null);
    }

    public JLabel getStatusBar() {

        return statusbar;
    }

    // run the game from here
    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {

            Tetris game = new Tetris();
            game.setVisible(true);
        });
    }
}

package com.IntelligentSystems.nitish;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Random;

public class HillClimbing {
	static int heuristic = 0;
    static int neighbours = 0;
    static int resetTime = 0;
    static int states = 0;
    static int n=0;
    
    public static void main(String[]args) throws NumberFormatException, IOException{
    	QueenObject[] chessBoard;
        int temporaryHeuristic=0, numberOfNeighbors = 0, bestHeuristic=0, currentHeuristic = 0;
        
        System.out.println("Enter the size of the Chess Board");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());
        QueenObject[] bestOfAllBoards = new QueenObject[n];
        QueenObject[] temporaryBoards = new QueenObject[n];
        
        QueenObject[] initialBoard = createChessBoard(n);
        chessBoard = Arrays.copyOf(initialBoard,n);
         
        currentHeuristic = checkHeuristics(initialBoard);

        //Test other states
        while (currentHeuristic != 0) {
            bestHeuristic = currentHeuristic;
            numberOfNeighbors = 0;
            for (int i=0; i<n; i++) {   //  To copy the board pieces
                //bestOfAllBoards[i] = new QueenObject(chessBoard[i].getRow(), chessBoard[i].getCol());
            	temporaryBoards[i] = new QueenObject(chessBoard[i].getRow(), chessBoard[i].getCol());
                //temporaryBoards[i] = new QueenObject(bestOfAllBoards[i].getRow(), bestOfAllBoards[i].getCol());
            }

            for (int i=0; i<n; i++) {
            	//Resetting the boards
                if (i>0)    
                    temporaryBoards[i-1] = new QueenObject (chessBoard[i-1].getRow(), chessBoard[i-1].getCol());
                temporaryBoards[i] = new QueenObject (0, temporaryBoards[i].getCol());
                for (int j=0; j<n; j++) {
                	//Check the Heuristic and get a temporary one
                    temporaryHeuristic = checkHeuristics(temporaryBoards);  
                    //Check if there is one with a lower heuristic
                    if (temporaryHeuristic < bestHeuristic) {    
                    	//Reset the number with that heuristic to 1
                        numberOfNeighbors++;   
                        bestHeuristic = temporaryHeuristic;

                        //Copy over the board with the best heuristic
                        for (int k=0; k<n; k++)   
                            bestOfAllBoards[k] = new QueenObject(temporaryBoards[k].getRow(), temporaryBoards[k].getCol());
                    }
                    //Moves the queen down
                    if (temporaryBoards[i].getRow()!=n-1)   
                        temporaryBoards[i].down();
                }
            }
            System.out.println();
            //Print the state
            printChessBoard(chessBoard, n, currentHeuristic, numberOfNeighbors);   
            System.out.println("Go to a new next state");

            if (bestHeuristic == currentHeuristic) {
                System.out.println("There are no better states. So resetting");
                bestOfAllBoards = createChessBoard(n);
                heuristic = checkHeuristics(bestOfAllBoards);
                resetTime++;
            } else
                heuristic = bestHeuristic;

            states++;
            chessBoard=bestOfAllBoards;
            currentHeuristic = heuristic;
        }
        System.out.println();
        //Print the last one
        printChessBoard(chessBoard, n, currentHeuristic, neighbours);  
        System.out.println("\nTotal Changes: " + states);
        System.out.println("Resets Done: " + resetTime);
    }

    //The function to check heuristics for each of the state
    public static int checkHeuristics (QueenObject[] chessBoard) {
        int heuristic = 0;

        for (int i = 0; i< chessBoard.length; i++) {
            for (int j=i+1; j<chessBoard.length; j++ ) {
                if (chessBoard[i].inConflicting(chessBoard[j])) {
                    heuristic++;
                }
            }
        }
        return heuristic;
    }

    //Create a new Chess board with queens. Queens are denoted as 1
    public static QueenObject[] createChessBoard(int n) {
    	Random random = new Random();
        QueenObject[] start = new QueenObject[n];
        for(int i=0; i<n; i++){
            start[i] = new QueenObject(random.nextInt(n), i);
        }
        return start;
    }

    // Prints the chess board 
    private static void printChessBoard (QueenObject[] actualState, int n, int heuristic, int neighbours) {
        int[][] newBoard = new int[n][n];

        //Define it to 0
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                newBoard[i][j]=0;
            }
        }
        for (int i=0; i<n; i++) {
            newBoard[actualState[i].getRow()][actualState[i].getCol()]=1;
        }

        System.out.println("The heuristic value is " + heuristic);
        System.out.println("The current state");
        for (int i=0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(newBoard[i][j] + " ");
            }
            System.out.print("\n");
        }
        System.out.println("Neighbour that had the lowest heuristic value " + neighbours);
    }
    
}

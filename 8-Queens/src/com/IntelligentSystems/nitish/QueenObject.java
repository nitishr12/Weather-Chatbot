package com.IntelligentSystems.nitish;
public class QueenObject {
    int row;
    int column;

    QueenObject(int row, int column) {
        this.row = row;
        this.column = column;
    }

    public boolean inConflicting(QueenObject q){
        //  Check horizontally and vertically
        if(row == q.getRow() || column == q.getCol())
            return true;
        //  Check diagonally
        else if(Math.abs(column-q.getCol()) == Math.abs(row-q.getRow()))
            return true;
        else
        	return false;
    }

    int getRow() {
        return row;
    }

    int getCol() {
        return column;
    }


    void down () {
        row++;
    }
}
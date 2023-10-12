class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COL = len(matrix), len(matrix[0])
        #creating a matrix with extra row and col
        self.sumMat = [[0]*(COL+1) for _ in range(ROWS+1)]
        
        #assigning prefix sum to the new matrix sum
        for r in range(ROWS):
            prefix =0 
            for c in range(COL):
                #calculating col prefix sum from original matrix
                prefix += matrix[r][c]
                #calculating above sum from newly created matrix
                above = self.sumMat[r][c+1]
                #assigning prefic sum to the newly created matric (sum)
                self.sumMat[r+1][c+1]=prefix+above
                   
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #msimplifying the variables since our original matrix is row+1 and col+1 size
        r1,r2,c1,c2 = row1+1, row2+1, col1+1,col2+1
        bottomright = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topleft = self.sumMat[r1-1][c1-1]
        
        return bottomright - above - left + topleft
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        mat_r = len(mat)
        mat_c = len(mat[0])
        if mat_r*mat_c != r*c:
            return mat
        one_d = [0]*(r*c)
        for i in range(mat_r):
            for j in range(mat_c):
                one_d[mat_c*i+j] = mat[i][j]

        res = [[0]*c for i in range(r)]
       
        for i in range(r*c):
            res[i//c][i%c] = one_d[i]
            
        return res

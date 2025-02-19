class Algorithms:
    @staticmethod
    def fibonacci (n): #Argument of the function is indicated in ordinal numbers
        if n > 0:
            var = {f'F{1}': 0}    
            a, b, c = 0, 1, 0
            if n > 1:
                for i in range(2, n + 1):
                    a = b + c
                    var[f'F{i}'] = a
                    b, c = c, a
            return var
        else:
            raise TypeError("Invalid option")
        
    @staticmethod
    def factorial (n):
        if n > 0:
            var = 0
            for i in range (n - 1, 1,-1):
                n *= i
                var = n
            return var
        else:
            raise TypeError("Invalid option")

         
print(Algorithms.factorial())


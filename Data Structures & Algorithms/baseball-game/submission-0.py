class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum:int = 0
        if(len(operations) == 0): return 0
        record=[] #Treat it like a record so we can pop,peek, and push.
         #First we convert all of the string numbers to int numbers
         #record = [int(x) if x.lstrip('-').isdigit() else x for x in ops]
        for i in range(len(operations)):
            if(operations[i] == "+"):
                prevTwoNumSum = record[-1] + record[-2]
                record.append(prevTwoNumSum)
            elif(operations[i] == "C"):
                record.pop()
            elif(operations[i] == "D"):
                prevTwoNumProduct = record[-1] * 2
                record.append(prevTwoNumProduct)
            else:
                record.append(int(operations[i]))

        #Now sum the values
        for l in range(len(record)):
            sum+=record[l]
        return sum;
        


        
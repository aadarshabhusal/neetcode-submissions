class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):

            if operations[i] != "C" and operations[i] != "D" and operations[i] != "+":
                record.append(int(operations[i]))

            if operations[i] == "+":
                record.append(record[-1] + record[-2])

            if operations[i] == "C":
                del record[-1]
            
            if operations[i] == "D":
                record.append (record[-1] * 2)

        return sum(record)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #Easy

        res = [] #хранение букв

        while columnNumber:
            columnNumber, ch = divmod(columnNumber - 1, 26) #Получаем результат деления число и остаток
            res.append(chr(ch + ord("A"))) #добавляем букву
        return "".join(reversed(res))
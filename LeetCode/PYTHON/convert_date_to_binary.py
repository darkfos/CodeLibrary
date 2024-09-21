class Solution:
    """
        Easy

        Description:
        You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
        date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.
        Return the binary representation of date.
    """
    
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([self.convert_number_to_binary(int(str_number)) for str_number in date.split("-")])

    def convert_number_to_binary(self, number: int) -> str:
        result_string: str = ""
        
        while number:
            result_string += str(number % 2)
            number //= 2

        return result_string[::-1]
        

result = Solution().convertDateToBinary("2080-02-29")
print(result)
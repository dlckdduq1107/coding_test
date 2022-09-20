def plusOne(self, digits):
        result = ''
        for i in digits:
            result += str(i)
        return list(str(int(result)+1))
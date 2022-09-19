def divide(dividend, divisor):
        res = str(dividend/divisor)
        print(res)
        result = res.split('.')[0]
        print(result)
        return int(result)

print(divide(-2147483648,-1))
#bai 1: tinh so fibonacci thu n
def fib(n):
    if (n <= 1 or n == 2):
        if (n < 1):
            return 0
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
#bai 2: tinh so n cua day so pell
#p0 = 1
#p1 = 1
#pn = 2p(n - 1) + p(n - 2)
def pell(n):
    if (n <= 1 or n == 2):
        if (n < 1):
            return 0
        return 1
    else:
        return 2*pell(n - 1) + pell(n - 2)

#bai 3: chuyen doi tu so thap phan sang so nhi phan
#vi du: 13 = 1101
def dec_2_bin(n):
    if (n//2 == 0):
        return n%2
    else:
        print(n%2, end = '')
        return dec_2_bin(n//2)
   
if __name__ == '__main__':
    print(dec_2_bin(13))
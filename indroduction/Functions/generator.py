#yeild keyword
def count_down(num):
    while num > 0:
        yield num #yield values one at a line 
        num -=1

#using the generstor
for number in count_down(5):
    print(number)


### Convex Example.
### Author: Levi C Nicklas
###
###
### Notes: This is a convex optimization example.


## Objective Fucntion ##
def obj_func(x,y):
    value =  4*x^2 + 10*y^2
    print(value)
    return value

def grad_obj_func(x,y):
    valueX = 8*x + 10*y^2
    valueY = 4*x^2 + 20*y

    value = [valueX,valueY]
    print(value)
    return(value)


# Output Test
obj_func(2,2)
grad_obj_func(2,2)







    



    



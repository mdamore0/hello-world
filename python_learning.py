"""
Kick off the best practice class
"""

def hello_world():
    str_beg_script = "Hello world"
    print(str_beg_script)

def loop_numbers():
    lst_rand_numbers = [1,2,3,5]
    for num in lst_rand_numbers:
        print(num*10)

def operators():
    """
    +	Add two operands or unary plus
    -	Subtract right operand from the left or unary minus
    *	Multiply two operands
    /	Divide left operand by the right one (always results into float)
    %	Modulus - remainder of the division of left operand by the right
    //	Floor division - division that results into whole number adjusted to the left in the number line
    **	Exponent - left operand raised to the power of right

    """
    dict_operator = { "+":"Add two operands or unary plus" ,
                      "-" : "Subtract right operand from the left or unary minus",
                      "*" : "Multiply two operands",
                      "/" : "Divide(returns float)" ,
                      "%" : "Modulus - remainder of the division of left operand by the right",
                      "//" : "Floor division - division results into whole number",
                      "**" : "Exponent"
                      }
    print(dict_operator["+"])

def comp_operator():
    """
    >	Greater that - True if left operand is greater than the right	x > y
    <	Less that - True if left operand is less than the right	x < y
    ==	Equal to - True if both operands are equal	x == y
    !=	Not equal to - True if operands are not equal	x != y
    >=	Greater than or equal to - True if left operand is greater than or equal to the right	x >= y
    <=	Less than or equal to - True if left operand is less than or equal to the right	x <= y
    """

    dict_comp_operator = {
         ">" : "Greater that - True if left operand is greater than the right	x > y",
         "<" : "Less that - True if left operand is less than the right	x < y",
         "==" : "Equal to - True if both operands are equal	x == y",
         "!=" :  "Not equal to - True if operands are not equal	x != y",
         ">=" : "Greater than or equal to - True if left operand is greater than or equal to the right	x >= y",
         "<=" :	"Less than or equal to - True if left operand is less than or equal to the right	x <= y"
        }
    print(dict_comp_operator["=="])

def assignment_operators():
    """
    =	x = 5	x = 5
    +=	x += 5	x = x + 5
    -=	x -= 5	x = x - 5
    *=	x *= 5	x = x * 5
    /=	x /= 5	x = x / 5
    %=	x %= 5	x = x % 5
    //=	x //= 5	x = x // 5
    **=	x **= 5	x = x ** 5
    &=	x &= 5	x = x & 5
    |=	x |= 5	x = x | 5
    ^=	x ^= 5	x = x ^ 5
    >>=	x >>= 5	x = x >> 5
    <<=	x <<= 5	x = x << 5
    """

    dict_assign_operators = {
    "=" : "x = 5",
    "+=" : "x = x + 5",
    "-=" : "x = x - 5",
    "*=	x" :	"x = x * 5",
    "/=	x" : "x = x / 5",
    "%=" : "x = x % 5",
    "//=" :	"x = x // 5",
    "**=" : "x = x ** 5",
    "&=" : "x = x & 5",
    "|=" : "x = x | 5",
    "^=" : "x = x ^ 5",
    ">>=" : "x = x >> 5",
    "<<=" : "x = x << 5"
     }
    if "=" in dict_assign_operators:
        print("= is an assign operator and its value is" + " {value}".format(value=dict_assign_operators["="]))
    elif True:
        print("//= is an assign operator and its value is" + " {value2}".format(value2=dict_assign_operators["//="]))
    else:
        print("Value no within assign operators")

def conditional_exp():
    x = 100
    if x > 24:
        print("true")
        if x == 100:
            print("true")
    else:
        print("not true")

def loop_exp():
    # List of numbers
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
    # variable to store the sum
    sum = 0
    # iterate over the list
    for val in numbers:
        sum = sum + val
    # Output: The sum is 48
    print("The sum is", sum)

    genre = ['pop', 'rock', 'jazz']

    # iterate over the list using index
    for i in range(len(genre)):
        print("I like", genre[i])
    else:
        print("No items left")


loop_exp()
conditional_exp()
assignment_operators()
# comp_operator()
# operators()
# hello_world()
# loop_numbers()
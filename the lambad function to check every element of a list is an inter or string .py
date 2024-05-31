#sample list
my_list = (1, "jake", 2, "peter",3.5 , "parker")

# Lambda function to check if element is integer or string
check_list = lambda x: isinstance(x,str) or isinstance(x,int)

# Check if every element satisfies the condition
result = all(check_list(x) for x in my_list)

# Print the result
if result:
    print("The all elements are intergers and string")

else:
    print("Not all elements are intergers and string")
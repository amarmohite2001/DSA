# method that needs to be implemented
import time
st = time.time()   
def hasVowels(strArray, queries):
    # initialise an empty list
    result = []
    # traverse query by query
    for query in queries:
        
        values = query.split("-")
        l = int(values[0])
        r = int(values[1])
        
        # initialise count to 0
        count = 0
        
        # from index l to r, find string count that start and end with vowels
        for i in range(l-1, min([r, len(strArray)]), 1):
            # if condition passes, increment count by 1 
            if strArray[i][0] in "aeiouAEIOU" and strArray[i][-1] in "aeiouAEIOU":
                count += 1
            
        # for every iteration, add count into result
        result.append(count)
        
    # atlast return result list
    return result
et = time.time()          
# testing code
print(hasVowels(['yy','u','oe'], ['1-2', '2-3']))
print(et-st,'seconds')
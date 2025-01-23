def raindrops(number):
    result = ""
    
    if result % 3 == 0:
    result += "Pling"
    if result % 5 == 0:
    result += "Plang"
    if number % 7 == 0:
        result += "Plong"
        
    return result if result else str(number)
    
    print(raindrops(28)) 
    print(raindrops(30))
    print(raindrops(34))

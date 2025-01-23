def decoder(coded_list): # First we define a decoder function
    if not coded_list:  # If the coded element is empty an empty list should be returned
        return []
    
    else:  # Otherwise it should return the first element repeated n times, where n is the number that follows the first element, 
        return [coded_list[0]] * coded_list[1] + decoder(coded_list[2:])  # then concatenating the recursion of the same function
        

if __name__ == "__main__":
    compressed_list = ["A",12,"B",4,"A",6,"B",1]
    print(decoder(compressed_list))
def rotational_ordering(head, requests):
    # Sort the list of requests
    requests = sorted(requests)
    #print(requests)

    # Split the list of requests into two halves
    mid = len(requests) // 2
    first_half = requests[:mid]
    second_half = requests[mid:]

    # Create two new lists by interleaving the requests
    # from the first half and second half
    # interleaved1 = [first_half[i//2] for i in range(len(first_half)*2)]
    # interleaved2 = [second_half[i//2] for i in range(len(second_half)*2)]

    # # Calculate the distance from the head position to the
    # # nearest end of each interleaved list
    # dist1 = abs(interleaved1[-1] - head)
    # dist2 = abs(interleaved2[-1] - head)

    # #Choose the list with the shorter distance and return it
    # if dist1 < dist2:
    #    return interleaved1
    # else:   
    #    return interleaved2
    
    
    interleaved1 = []
    
    for i in range(len(first_half)):
        print(head)

        interleaved = []
        for i in range(len(first_half)):
            interleaved.append(abs(first_half[i]-head))
        #print(interleaved)
        min_index = interleaved.index(min(interleaved))
        #print(min_index)
        if interleaved[min_index] == 0:
            interleaved1.append(first_half[min_index-1])
            head = interleaved1[-1]
        else:
            interleaved1.append(first_half[min_index])
            head = interleaved1[-1]
    for i in range(len(second_half)):
        print(head)
        interleaved = []
        for i in range(len(second_half)):
            interleaved.append(abs(second_half[i]-head))
            #print(head)
        #print(interleaved)
        min_index = interleaved.index(min(interleaved))
        #print(min_index)
        if interleaved[min_index] == 0:
            interleaved1.append(second_half[min_index+1])
            head = interleaved1[-1]
        else:
            interleaved1.append(second_half[min_index])
            head = interleaved1[-1]        
        
    return interleaved1
        
    #min_index = interleavedindex(min(interleaved))        

    
    
head = 50
requests = [82, 170, 43, 140, 24, 16, 190, 5]

print("Initial position of head:", head)
    
print(rotational_ordering(head,requests))
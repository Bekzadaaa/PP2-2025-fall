with open("text.txt", "r") as f:  
    print(sum(1 for _ in f))  

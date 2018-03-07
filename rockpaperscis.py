import random

def rockPaperScis(p1, p2, mr):
    p1score = 0
    p2score = 0
    scores = [p1score, p2score]

    for x in range(1, mr):
              
        gd = random.randint(1, 9)

        if(gd == 3 or gd == 4 or gd == 8): #Player 1 Wins
            
            p1score+=1
            
            print("%s Wins!\n" % p1)
        
        elif(gd == 2 or gd == 6 or gd == 7):
            
            p2score+=1
        
            print("%s Wins!\n" % p2)
            
        else:
            
            print("Draw")
            pass


        #Winner Decision is Made

    if(p1score > p2score):
        winner = p1
    elif(p2score > p1score):
        winner = p2
    else:
        winner = "No One"

        #Release Scores to Players

    print("End Score:\n\t%s on %s\n\t%s on %s\n%s Wins!" % (p1, p1score, p2, p2score, winner))

        #   r p s p2
        #r  1 2 3
        #p  4 5 6
        #s  7 8 9
        #p1

        #check to see who won the round

rockPaperScis("Alex", "James", 3)
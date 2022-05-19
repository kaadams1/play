"""Restaurant rating lister."""

def restaurant_rating(filename):

    file = open(filename)

    while True:

        try:
    
            user_rest = input("Enter a restaurant name: ")
            user_rate = int(input("Rate that restaurant on a scale of 1 to 5: "))

        except ValueError:
            print("Not a valid input. Please enter a whole number between 1 and 5. ")
            continue

        if user_rate > 5 or user_rate < 1:
            print("Not a valid input. Please enter a whole number between 1 and 5. ")
            continue
    
        ratings_dic = {}

        for line in file:

            line = line.rstrip()
            info = line.split(':')

            rest_name = info[0]        
            rest_rating = info[1]
                
            ratings_dic[rest_name] = rest_rating
            
        ratings_dic[user_rest] = user_rate
            
        for restaurant, rating in sorted(ratings_dic.items()):
            print(f"{restaurant} is rated at {rating}.")

                
        file.close()

restaurant_rating('scores.txt')
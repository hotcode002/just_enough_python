##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program we will learn about
# 1. sets Data Structure
# 2. set operations
#    - union
#    - intersection
#    - difference

midwest_states = {"North Dakota", "South Dakota", "Nebraska", "Minnesota", \
                  "Iowa", "Missouri", "Wisconsin", "Illinois", "Kansas",   \
                  "Michigan", "Indiana", "Ohio"}

northeast_states = { "Maine", "New York", "New Jersey", "Vermont", "Massachusetts",  \
                     "Rhode Island", "Connecticut", "New Hampshire", "Pennsylvania"}

southwest_states = { "Arizona", "Colorado", "Kansas", "New Mexico", "Oklahoma",\
                     "Texas", "Utah"}

northwest_states = { "Oregon", "Washington" "Idaho"}

greatplains_states = { "Kansas", "Nebraska", "North Dakota","South Dakota", \
                       "Colorado", "Iowa", "Minnesota", "Montana", "New Mexico", "Oklahoma", \
                       "Texas", "Wyoming"}

dustbowl_states = { "Texas", "Oklahoma", "Kansas", "Colorado" , "New Mexico"}

us_states_dem = { "California",	"Colorado",	"Connecticut",	"Delaware",	"Hawaii", \
               "Illinois",	"Maine",	"Maryland",	"Massachusetts",	"Minnesota",\
               "Nevada",	"New Hampshire",	"New Jersey",	"New Mexico", \
               "New York",	"Oregon",	"Rhode Island",	"Vermont",	"Virginia", \
               "Washington"}

us_states_rep = { "Alabama",	"Alaska",	"Arizona",	"Arkansas",	"Florida", \
               "Georgia",	"Idaho",	"Indiana",	"Iowa",	"Kansas",	"Kentucky", \
               "Louisiana",	"Michigan",	"Mississippi",	"Missouri",	"Montana",	\
               "Nebraska",	"North Carolina",	"North Dakota",	"Ohio",	"Oklahoma", \
               "Pennsylvania",	"South Carolina",	"South Dakota",	"Tennessee",	\
               "Texas",	"Utah",	"West Virginia",	"Wisconsin",	"Wyoming" }


print ( " Pick any combination ")
choices = {"1" : "us_states_dem", 
           "2" : "us_states_rep",
           "3" : "midwest_states",
           "4" : "northeast_states",
           "5" : "northwest_states",
           "6" : "southwest_states",
           "7" : "greatplains_states",
           "8" : "dustbowl_states"}

while ( True ) : 
    for item in choices.items() :
        print ( item [0] , item [1]) 

    user_choice = input ( "enter your choice - type exit() to leave - ")
    if user_choice == "exit" : 
        break    

    tokens = str.split ( user_choice)
    for tok in tokens : 
        if tok != "|" and tok != "&" and tok != "+" and tok != "-" :
            user_choice = str.replace ( user_choice, tok,choices[tok] )

    print ( eval( user_choice))
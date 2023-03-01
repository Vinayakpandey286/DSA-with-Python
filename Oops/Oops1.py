class movies:
    '''This is class developed by me'''
    def __init__(self,title,hero,heroine) -> None: # constructor
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print("movie name:", self.title)
        print("hero name:", self.hero)
        print("heroine name:", self.heroine)

# print(movies.__doc__)
#there is no method/constructor overloading concepts in python.
#you can create any no. and constructor python will consider only the last one.

list_of_movies=[]
while True:
    title=input("enter movie name: ")
    hero=input("enter hero name: ")
    heroine=input("enter heroine name: ")

    m=movies(title,hero,heroine)
    list_of_movies.append(m)
    print("movie added succesfully")

    option=input("Do you want to add another movie?[yes|no]: ")
    if option.lower=="no":
        break
    print("All movies Information")

    for movie in list_of_movies:
        movie.info()
        print()
        

# def more_about_self (func) :
#     def wrapper() :
#         print(f"I like football as my favorite sport")
#         func()
#     return wrapper
# @more_about_self    
# def say_hi () :
#     print(f"Hi there its me!")
# say_hi()  


def get_sprinkles (func,type = "green-sprinkles") :
    def wrapper(*args,**kwargs) :
        print(f"take this {type}...")
        func(*args,**kwargs)
    return wrapper
@get_sprinkles
def ice_cream(flavor) :
    print(f"I love {flavor}")
ice_cream("chocolate")    


def coding_rn (func):
    def wrapper(*args,**kwargs):
        print(f"But i am drinking water")
        func(*args,**kwargs)
    return wrapper
@coding_rn    
def watch_foot (team):
    print(f"I am watching {team} right now!")
watch_foot("Inter Milan")    
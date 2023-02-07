""" Example Problem when to use factory desing pattern """

# Suppose we have created an app whose main purpose is to translate one language into another and currently our app 
# works with 10 languages only. Now our app has become widely popular among people but the demand has grown suddenly 
# to include 5 more languages. It’s a piece of great news! only for the owner not for the developers. They have to 
# change the whole code because now most part of the code is coupled with the existing languages only and that’s why 
# developers have to make changes to the entire codebase which is really a difficult task to do.Let’s look at the code 
# for the problem which we may face without using the factory method.

""" Solution """

# Its solution is to replace the straightforward object construction calls with calls to the special factory method.
# Actually, there will be no difference in the object creation but they are being called within the factory method.

class Frenchlocalizer:
    def __init__(self) -> None:
        self.translate = {"car": "voiture", "bike": "bicyclette","cycle":"cyclette"}

    def localize(self,word) -> str:
        mgs = "Sorry! We've no translations for your word."
        return self.translate.get(word,mgs)

class Spanishlocalizer:
    def __init__(self):
        self.translate = {"car": "coche", "bike": "bicicleta","cycle":"ciclo"}

    def localize(self,word) -> str:
        mgs = "Sorry! We've no translations for your word."
        return self.translate.get(word,mgs)

def factory_localizer(language):
    localizers = {"French" :Frenchlocalizer,"Spanish":Spanishlocalizer}
    # If we want to add more lanuages create the loacalizer class and put it in above dict
    
    return localizers[language]()


if __name__ == '__main__':
    f = factory_localizer('French')
    s = factory_localizer('Spanish')

    print(f.localize("car"))
    print(s.localize("car"))


# Pros

# 1. We can easily add new types of products without disturbing the existing client code.
# 2. Generally, tight coupling is being avoided between the products and the creator classes and objects.
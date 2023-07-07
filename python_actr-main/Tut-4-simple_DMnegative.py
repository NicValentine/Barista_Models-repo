from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer)
    
    focus.set('goal:sandwich object:bread_bottom')

    DM.add('condiment:mustard')
    DM.add('condiment:peanutbutter')

    def bread_bottom(focus='goal:sandwich object:bread_bottom'):
        print("I have a piece of bread")                 
        focus.set('goal:sandwich object:cheese')                

    def cheese(focus='goal:sandwich object:cheese'):            
        print("I have put cheese on the bread")          
        focus.set('goal:sandwich object:ham')

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich action:recall_condiment')

    def recall_condiment(focus='goal:sandwich action:recall_condiment'):
        print("recalling the order")
        DM.request('condiment:?x!peanutbutter')                
        focus.set('goal:sandwich recall:condiment')         

    def condiment(focus='goal:sandwich recall:condiment', DMbuffer='condiment:?condiment'):  
        print("I recall they wanted.......")
        print (condiment)             
        print("i have put the condiment on the sandwich")
        focus.set('goal:sandwich object:bread_top')

    def bread_top(focus='goal:sandwich object:bread_top'):
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('goal:stop')   

tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
subway.run()                               # run the environment

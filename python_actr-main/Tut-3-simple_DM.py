from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer)
    
    focus.set('goal:sandwich object:bread_bottom')

    DM.add('condiment:mustard')

    def bread_bottom(focus='goal:sandwich object:bread_bottom'):# if focus buffer has this chunk then....
        print("I have a piece of bread")                 # print the action
        focus.set('goal:sandwich object:cheese')                # change chunk in focus buffer

    def cheese(focus='goal:sandwich object:cheese'):            # the rest of the productions are the same
        print("I have put cheese on the bread")          # but carry out different actions
        focus.set('goal:sandwich object:ham')

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich action:recall_condiment')

    def recall_condiment(focus='goal:sandwich action:recall_condiment'):
        print("recalling the order")
        DM.request('condiment:?x')                # retrieve a chunk from DM into the DM buffer
        focus.set('goal:sandwich recall:condiment')         # ? means that slot can match any content

    def condiment(focus='goal:sandwich recall:condiment', DMbuffer='condiment:?condiment'):  # match to DMbuffer as well
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

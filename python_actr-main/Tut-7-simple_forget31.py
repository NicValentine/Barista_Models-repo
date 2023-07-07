from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer,latency=0.05,threshold=0,finst_size=10,finst_time=30.0)

    dm_n=DMNoise(DM,noise=0.0)            # set activation noise level
    dm_bl=DMBaseLevel(DM,decay=0.5)       # set activation decay

    focus.set('goal:sandwich object:bread_bottom')

    DM.add('condiment:mustard')
    DM.add('condiment:ketchup',baselevel=1)  # set the baselevel
                                             # used mainly for debugging, can also represent a stronger memory
                                             # baselevel will be explained more in subsequent assignments

    def bread_bottom(focus='goal:sandwich object:bread_bottom'):
        print("I have a piece of bread")                
        focus.set('goal:sandwich object:cheese')

    def cheese(focus='goal:sandwich object:cheese'):    
        print("I have put cheese on the bread")     
        focus.set('goal:sandwich object:ham')

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich action:recall_condiment')
        DMbuffer.set('something')

    def recall_condiment(focus='goal:sandwich action:recall_condiment'):
        print("recalling the order")
        DM.request('condiment:?')
        focus.set('goal:sandwich object:condiment')

    def forgot(focus='goal:sandwich object:condiment', DM='error:True', DMbuffer=None):
                                           # DMbuffer=None means the buffer is empty
                                           # DM='error:True' means the search was unsucessful
                                           # note - when a DM.request is made it clears the buffer
                                           #      - and keeps it clear until the request is delviered or fails
        print('I recall they wanted.......')
        print("I forgot")
        focus.set('goal:stop')
        
    def condiment(focus='goal:sandwich object:condiment', DMbuffer='condiment:?condiment'):  # match to DMbuffer as well
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
log_everything(subway)
subway.run()                               # run the environment

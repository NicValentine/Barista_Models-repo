from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    focus.set('action:yay')

    def bread_bottom(focus='action:yay'):     # if focus buffer has this chunk then....
        print("Yay!!!! it works")           # print
        focus.set('action:stop')              # change chunk in focus buffer


tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
subway.run()                               # run the environment

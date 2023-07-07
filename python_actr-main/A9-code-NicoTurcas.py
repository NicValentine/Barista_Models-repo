from python_actr import *  

# Assignment 9 - simple forgetting with subsymbolic parameters

# We have taken the former barsita model and added subsymbolic parameters 
# to simulate the agent forgetting the order. 

class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer,latency=0.05,threshold=0.3,finst_size=4,finst_time=5) 
    dm_n=DMNoise(DM,noise=0.0)            # set activation noise level
    dm_bl=DMBaseLevel(DM,decay=0.05)       # set activation decay

    focus.set('task:espresso operation:lift_portafilter')

    DM.add('garnish:cinnamon')
    DM.add('garnish:pumpkin_spice')
    DM.add('garnish:nutmeg') 


    def production_lift_portafilter(focus='task:espresso operation:lift_portafilter'):
        print("Barista: To make our latte we first need to make an espresso, grab the portafilter off the counter")                 
        focus.set('task:espresso operation:insert_portafilter_into_grinder')                

    def production_insert_portafilter_into_grinder(focus='task:espresso operation:insert_portafilter_into_grinder'):
        print("Barista: Place the portafilter into the grinder group head")          
        focus.set('task:espresso operation:grind_beans')

    def production_grind_beans(focus='task:espresso operation:grind_beans'):
        print("Barista: We will now grind the espresso beans.")
        focus.set('task:espresso operation:remove_portafilter_from_grinder')

    def production_remove_portafilter_from_grinder(focus='task:espresso operation:remove_portafilter_from_grinder'):
        print("Barista: Remove the portafilter from the grinder.")
        focus.set('task:espresso operation:insert_portafilter_into_grouphead')   
    
    def production_insert_portafilter_into_grouphead(focus='task:espresso operation:insert_portafilter_into_grouphead'):
        print('Barista: Place the portafilter into the grouphead.')
        focus.set('task:espresso operation:grab_cup')
    
    def production_grab_cup(focus='task:espresso operation:grab_cup'):
        print('Barista: Pick up the cup off the counter.')
        focus.set('task:espresso operation:place_cup_on_tray')

    def production_place_cup_on_tray(focus='task:espresso operation:place_cup_on_tray'):
        print('Barista:Place a cup under the grouphead to catch the espresso shot.')
        focus.set('task:espresso operation:pull_espresso')
    
    def production_pull_espresso(focus='task:espresso operation:pull_espresso'):
        print('Barista: Pull the espresso shot')
        focus.set('task:latte operation:pick_up_pitcher') # task changed from espresso to latte now
    
    def production_pick_up_pitcher(focus='task:latte operation:pick_up_pitcher'):
        print('Barista: Pick up the pitcher with milk in it.')
        focus.set('task:latte operation:steam_milk')
    
    def production_steam_milk(focus='task:latte operation:steam_milk'):
        print('Barista: Lets steam this milk')
        focus.set('task:latte operation:pick_up_cup')

    def production_pick_up_cup(focus='task:latte operation:pick_up_cup'):
        print('Barista: Pick up the cup with the espresso in it.')
        focus.set('task:latte operation:make_latte')

    def production_make_latte_mix_steamed_milk_and_espresso(focus='task:latte operation:make_latte'):
        print('Barista: Mix the steamed milk with the espresso to make a latte')
        focus.set('task:latte operation:recall_garnish')

        # Garnish request
    def production_recall_garnish(focus='task:latte operation:recall_garnish'):
        print('Recalling garnish....')
        DM.request('garnish:?garnish',require_new=True) 
        focus.set('task:latte operation:garnish_latte')
    
        # Garnish Forgotten
    def production_garnish_forgotten(focus='task:latte operation:garnish_latte', DM='error:True', DMbuffer=None):
        print('I recall they wanted....')
        print("I forgot")
        focus.set('goal:stop')

        # Garnish Remebered
    def production_garnish_latte(focus='task:latte operation:garnish_latte', DMbuffer='garnish:?garnish'):
        print('I recall they wanted....')
        print(garnish)
        focus.set('task:latte operation:serve')

    def production_serve(focus='task:latte operation:serve'):
        print('Barista: Latte order, pick up!')
        focus.set('task:wait')



nico=MyAgent()                              # name the agent
cafe=MyEnvironment()                     # name the environment
cafe.agent=nico                           # put the agent in the environment
cafe.run()                               # run the environment

from python_actr import *  

### Order it all and figure out how to get grinder to run



class Cafe_Environment(Model):        
    espresso_machine = Model(isa='espresso_machine', grouphead='grouphead_unoccupied', grinder='grinder_unoccupied', grinder_button='off', steamwand='off', tray='unoccupied')
    portafilter = Model(isa='portafilter', state='empty', location='on_counter')
    cup = Model(isa='cup', state='empty', location='on_counter')
    pitcher = Model(isa='pitcher', milk='unsteamed', location='on_counter')
    spoon=Model(isa='spoon', location='on_counter')

# the barista and the espresso machine are both conducted by the same action module, they should be different as they are the actions of different agents. 
class BaristaActionModule(Model):     
    
    # 2) lift portafilter off counter
    # 'portafilter', 'location', 'in_hand'
    def barista_action_lift_portafilter(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'portafilter', 'location', 'in_grinder'
    def barista_action_insert_portafilter_into_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'espresso_machine', 'grinder_button', 'on'
    def barista_action_turn_on_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 5
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value) ### how to trigger espresso machine action module from prodcution of barista action module? by having a prodct ready for in java jolt
     
class EspressoMachineActionModule(Model):     

    # 'espresso_machine','grinder','grinder_occupied'
    def espresso_machine_action_occupied_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)


    def espresso_machine_action_grinding(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
        
class Barista(ACTR):
    focus=Buffer()
    focus.set('task:espresso operation:lift_portafilter')
    action=BaristaActionModule()

        # 1) lift portafilter off counter
    def production_lift_portafilter(focus='task:espresso operation:lift_portafilter'):
        print('Barista Babe: Hey there newbie, welcome to the team, lemme teach you how to make an espresso.')
        print('Barista Babe: First you want to place the portafilter into the grinder.')
        print('Barista Babe: So first, we grab the portafilter.')
        action.barista_action_lift_portafilter('portafilter', 'location', 'in_hand')
        focus.set('task:espresso operation:insert_portafilter_into_grinder')

        # 3) place portafilter into grinder....this needs to result in the portafilter and espresso machine being updated
    def production_insert_portafilter_into_grinder(focus='task:espresso operation:insert_portafilter_into_grinder'):
        print('Barista: Place the portafilter into the grinder group head.')
        action.barista_action_insert_portafilter_into_grinder('portafilter', 'location', 'in_grinder') ###GRINDER NEEDS TO BE UPDATED HERE!!! #first thing
        focus.set('task:espresso operation:grind_beans') ## add grinder conditional here

        # grind beans production will turn on the grind_button on the espresso machine which will trigger it to grind and fill the portafilter with grounds. 
    def production_grind_beans(focus='task:espresso operation:grind_beans'):
        print('Barista: Alright, now we gonna grrrinnndd dem beans!')
        action.barista_action_turn_on_grinder('espresso_machine', 'grinder_button', 'on')
        focus.set('state:wait')
    
class Espresso_Machine(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:on')
    action=EspressoMachineActionModule()
 
    # A result of 
    def occupied_grinder(focus='state:on', portafilter='location:in_grinder'):
        print('Espresso Machine: Grinder grouphead is occupied')
        action.espresso_machine_action_occupied_grinder('espresso_machine','grinder','grinder_occupied')
        focus.set('state:on') #### it's looping here!!!
    
    def grinding(focus='state:on', espresso_machine='grinder_button:on'): #NEED TO GET THIS TO RUN!
        print('Java Jolt: grinding dem beans')
        action.espresso_machine_action_grinding('portafilter', 'state', 'full') # grinding dem beans fills up the portafilter
        focus.set('state:wait',)





nico=Barista()
machine1=Espresso_Machine()
env=Cafe_Environment()
env.agent=nico
env.agent=machine1 

log_everything(env)

env.run()



'''
    def remove_portafilter_from_grinder():
    def insert_portafilter_into_grouphead():
    def place_cup_on_tray():
    def pull_shot():
    def serve():
    def steam_milk():
    def pour_milk():
'''
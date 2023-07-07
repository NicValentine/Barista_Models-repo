from python_actr import *  


class MyEnvironment(Model):
    plane=Model(isa='plane', controller='off', foot_pedal='off', yoke='off', gear='off', flaps='on') # flaps are initially on


class ActionModule(Model):

    def pilot_action_thrust_controller(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def pilot_action_press_foot_pedal(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def pilot_action_pull_yoke(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def pilot_action_retract_gear(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def pilot_action_retract_flaps(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)



class MyAgent(ACTR):
    
    focus=Buffer()
    action=ActionModule()
    focus.set('task:thrust_controller')

    def production_thrust_controller(focus='task:thrust_controller'):
        print("THRUST!!!!")
        action.pilot_action_thrust_controller('plane','controller','on')                 
        focus.set('task:press_foot_pedal')

    def production_press_foot_pedal(focus='task:press_foot_pedal'):
        print('Press down foot pedal')
        action.pilot_action_press_foot_pedal('plane','foot_pedal','on')
        focus.set('task:pull_yoke')                

    def production_pull_yoke(focus='task:pull_yoke'):
        print('Pull yoke')
        action.pilot_action_pull_yoke('plane','yoke','on')
        focus.set('task:retract_gear_flaps')   

    def production_retract_gear_flaps(focus='task:retract_gear_flaps'):
        print('WE FLYING!!!! ^__^')
        action.pilot_action_retract_gear('plane','gear','on')
        action.pilot_action_retract_flaps('plane','flaps','off')
        focus.set('task:wait')   


class cockpit(ACTR): 
    production_time=0.0
    focus=Buffer()
    focus.set('state:on')
    action=ActionModule()


####################################################################    

captain_shelly=MyAgent()                              # name the agent
machine=cockpit()
airplane=MyEnvironment()                     # name the environment
airplane.agent=captain_shelly 
airplane.agent=machine
log_everything(airplane)                         # put the agent in the environment
airplane.run()                               # run the environment

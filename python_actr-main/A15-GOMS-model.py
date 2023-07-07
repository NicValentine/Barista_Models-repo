from python_actr import *  

# ASSIGNMENT: GOMS MODEL

# This is a GOMS model of a barista training a new hire. 
# The barista makes a cappuccino and in doing so, teaches the new hire how to make three drinks: 
# drink 1: espresso shot
# drink 2: latte
# drink 3: cappuccino

class Cafe_Environment(Model):        
    espresso_machine = Model(isa='espresso_machine', grouphead='unoccupied', shot_button='off', grinder='unoccupied', grinder_button='off', steamwand='off', tray='unoccupied')
    portafilter = Model(isa='portafilter', state='empty', location='on_counter')
    cup = Model(isa='cup', state='empty', location='on_counter')
    pitcher = Model(isa='pitcher', milk='unsteamed', location='on_counter')
    spoon=Model(isa='spoon', location='on_counter')

# the barista and the espresso machine are both conducted by the same action module, 
# future iterations should be different as they are the actions of different agents, 
# but I ran into some issues when I tried to do this such as how a production from one 
# action module fires a production from another action module...this can be fixed

class ActionModule(Model):     

    # 2) 'portafilter', 'location', 'in_hand'
    def barista_action_lift_portafilter(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 3i) 'portafilter', 'location', 'in_grinder'
    def barista_action_insert_portafilter_into_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 3ii) 'espresso_machine','grinder','grinder_occupied'
    def espresso_machine_action_occupied_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 5) 'espresso_machine', 'grinder_button', 'on'
    # this triggers the espresso machine
    def barista_action_turn_on_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 5
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value) 


    # 7i) 'portafilter', 'state', 'full'
    def espresso_machine_action_grinding(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 7ii) 'espresso_machine','grinder_button','off' 
    # grinding ends once portafilter is full
    def espresso_machine_grinder_button_off(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)


    #9i) 'portafilter', 'location', 'in_hand'
    def barista_action_remove_portafilter_from_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    #9ii) 'espresso_machine', 'grinder', 'unoccupied'
    def espresso_machine_action_unoccupied_grinder (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 11i) 'portafilter', 'location', 'grouphead'
    def barista_action_insert_portafilter_into_grouphead (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
    
    # 11ii) 'espresso_machine', 'grouphead', 'occupied'
    def espresso_machine_action_occupied_grouphead (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 13) action.barista_action_grab_cup('cup', 'location', 'in_hand')
    def barista_action_grab_cup (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

   
    # 15i) 'portafilter', 'location', 'grouphead'
    def barista_action_grab_cup (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
    
    # 15ii) 'espresso_machine', 'grouphead', 'occupied'
    def espresso_machine_occupied_tray (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 17) 'espresso_machine', 'shot_button', 'on'
    def espresso_machine_press_shot_button (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 19i) 'cup', 'state', 'espresso'
    def espresso_machine_pull_espresso (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)


    # 19ii) 'espresso_machine', 'shot_button', 'off'
    def espresso_machine_shot_button_off (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 21) 'pitcher', 'location', 'in_hand'
    def barista_action_place_pitcher_under_steamwand(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 23) 'espresso_machine', 'steamwand', 'on'
    def barista_action_steam_milk(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 26) 'cup','location','in_hand'
    def barista_action_pick_up_espresso_cup_for_latte(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 28) 'cup','state','latte'
    def barista_action_mix_latte(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 30) 'cup','location','on_counter'
    def barista_cup_down_for_cappuccino_foam(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 32) 'spoon','location','in_hand'
    def barista_action_pick_up_spoon(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 34) 'cup','state','cappuccino'
    def barista_action_scoop_foam(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 36) 'cup','location','in_hand'
    def barista_action_pick_up_cup_of_cappuccino(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 38) 'cup','location','service_station'
    def barista_action_serve_drink(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

#################################################


class Barista(ACTR):
    focus=Buffer()
    focus.set('task:espresso operation:lift_portafilter')
    action=ActionModule()

        # 1) lift portafilter off counter
    def production_lift_portafilter(focus='task:espresso operation:lift_portafilter'):
        print('Barista Babe: Hey there newbie, welcome to the team, lemme teach you how to make an espresso.')
        print('Barista Babe: So first, grab the portafilter off the counter.')
        action.barista_action_lift_portafilter('portafilter', 'location', 'in_hand')
        focus.set('task:espresso operation:insert_portafilter_into_grinder')

        # 3) place portafilter into grinder....this results in the portafilter and espresso machine being updated
    def production_insert_portafilter_into_grinder(focus='task:espresso operation:insert_portafilter_into_grinder'):
        print('Barista Babe: Place the portafilter into the grinder group head.')
        action.barista_action_insert_portafilter_into_grinder('portafilter', 'location', 'in_grinder') 
        action.espresso_machine_action_occupied_grinder('espresso_machine', 'grinder', 'occupied')
        focus.set('task:espresso operation:grind_beans')
   
        # 4) grind beans production will turn on the grind_button on the espresso machine which will trigger it to grind and fill the portafilter with grounds. 
    def production_grind_beans(focus='task:espresso operation:grind_beans'):
        print('Barista Babe: Alright, turn on the grinder and grrrinnndd dem beans!')
        action.barista_action_turn_on_grinder('espresso_machine', 'grinder_button', 'on')
        focus.set('task:espresso operation:remove_portafilter_from_grinder')


        # 8) remove and hold portafilter 
    def production_remove_portafilter_from_grinder(focus='task:espresso operation:remove_portafilter_from_grinder'):
        print('Barista Babe: Okay, now we take out the portafilter from the grinder.')
        action.barista_action_remove_portafilter_from_grinder('portafilter', 'location', 'in_hand') # need two actions one that updates the location of portafilter the other to update state of espresso machine
        action.espresso_machine_action_unoccupied_grinder('espresso_machine', 'grinder', 'unoccupied')
        focus.set('task:espresso operation:insert_portafilter_into_grouphead')

        # 10) insert portafilter into grouphead
    def production_insert_portafilter_into_grouphead(focus='task:espresso operation:insert_portafilter_into_grouphead'):
        print('Barista Babe: Place the portafilter from the into the espresso steamer group head.')
        action.barista_action_insert_portafilter_into_grouphead('portafilter', 'location', 'grouphead')
        action.espresso_machine_action_occupied_grouphead('espresso_machine', 'grouphead', 'occupied')
        focus.set('task:espresso operation:grab_cup')

        # 12) Grab cup
    def production_grab_cup(focus='task:espresso operation:grab_cup'):
        print('Barista Babe: Alright, lets just pick up the cup on the counter.')
        action.barista_action_grab_cup('cup', 'location', 'in_hand')
        focus.set('task:espresso operation:place_cup_on_tray')

        # 14) Place cup under grouphead on tray to catch espresso
    def production_place_cup_on_tray(focus='task:espresso operation:place_cup_on_tray'):
        print('Barista Babe: Place the cup on the espresso machine tray, under the group head to catch the espresso.')
        action.barista_action_grab_cup('cup', 'location', 'tray')
        action.espresso_machine_occupied_tray('espresso_machine', 'tray', 'occupied')
        focus.set('task:espresso operation:press_shot_button')

        # 16) Pull espresso
    def production_press_shot_button(focus='task:espresso operation:press_shot_button'):
        print('Barista Babe: Now, press the shot button to pull the espresso shot.')
        action.espresso_machine_press_shot_button('espresso_machine', 'shot_button', 'on')
        focus.set('task:latte operation:pick_up_pitcher') # the task has changed to a latte now

        # 20) Pick up pitcher 
    def production_pick_up_pitcher(focus='task:latte operation:pick_up_pitcher'):
        print('Barista Babe: Now that the espresso shot has been pulled, if that is what the guest ordered, it would be ready to serve.')
        print('Barista Babe: However, I will show you how to turn this into a latte, so lets steam some milk!')
        print('Barista Babe: Pick up the pitcher that has some milk in it off the counter and hold it under the steamwand.')
        action.barista_action_place_pitcher_under_steamwand('pitcher', 'location', 'in_hand') 
        focus.set('task:latte operation:steam_milk')

        # 22) Steam Milk
    def production_steam_milk(focus='task:latte operation:steam_milk'):
        print('Barista Babe: Now it is time to steam the milk!')
        action.barista_action_steam_milk('espresso_machine', 'steamwand', 'on') 
        focus.set('task:latte operation:pick_up_espresso_cup_for_latte')

        # 25) Pick up espresso cup
    def production_pick_up_espresso_cup_for_latte(focus='task:latte operation:pick_up_espresso_cup_for_latte'):
        print('Barista Babe: So now that our milk is steamed pick up the cup with espresso in it.') # pitcher is still in_hand
        action.barista_action_pick_up_espresso_cup_for_latte('cup','location','in_hand')
        focus.set('task:latte operation:mix_latte')


        # 27) Mix espresso and steamed milk to make latte 
    def production_make_latte(focus='task:latte operation:mix_latte'):
        print('Barista Babe: So now we pour the steamed milk onto the espresso to make a latte.') 
        action.barista_action_mix_latte('cup','state','latte')
        focus.set('task:cappuccino operation:place_cup_down_cappuccino')

        # 29) place cup down 
        # note : a real cappuccino has a different ratio of milk to espresso compared to a latte
    def production_place_cup_down_for_cappuccino(focus='task:cappuccino operation:place_cup_down_cappuccino'):
        print('Barista Babe: To make the cappuccino we take our latte and add foamed milk, so place the cup down on the counter.') 
        action.barista_cup_down_for_cappuccino_foam('cup','location','on_counter')
        focus.set('task:cappuccino operation:pick_up_spoon')

        # 31) pick up spoon
    def production_pick_up_spoon(focus='task:cappuccino operation:pick_up_spoon'):
        print('Barista Babe: To finish the cappiccino grab a spoon to scoop some of the frothy milk foam.') 
        action.barista_action_pick_up_spoon('spoon','location','in_hand')
        focus.set('task:cappuccino operation:spoon_milk_foam')

        # 33) spoon milk foam
    def production_spoon_milk_foam(focus='task:cappuccino operation:spoon_milk_foam'):
        print('Barista Babe: Scoop the foam from the pitcher.') 
        action.barista_action_scoop_foam('cup','state','cappuccino')
        focus.set('task:cappuccino operation:pick_up_cup_to_serve')

        # 35) pick up cup
    def production_pick_up_cup_to_serve(focus='task:cappuccino operation:pick_up_cup_to_serve'):
        print('Barista Babe: Alright, we have completed the cappuccino! ^__^ ') 
        action.barista_action_pick_up_cup_of_cappuccino('cup','location','in_hand')
        focus.set('task:cappuccino operation:serve_drink')

        # 37) place cup on pick up station and call service
    def production_serve_drink(focus='task:cappuccino operation:serve_drink'):
        print('Barista Babe: Okay, that is it, just bring the espresso to the pick area to serve to the guest. PICK UP!!!')
        action.barista_action_serve_drink('cup', 'location', 'service_station')
        focus.set('task:end')

class Espresso_Machine(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:on')
    action=ActionModule()

    # 6) Grinding beans function of the Java Jolt Espresso Machinne
    def grinding(focus='state:on', espresso_machine='grinder_button:on'):
        print('Java Jolt: grinding dem beans')
        action.espresso_machine_action_grinding('portafilter', 'state', 'full') # grinding dem beans fills up the portafilter
        action.espresso_machine_grinder_button_off('espresso_machine','grinder_button','off') # grinding ends once portafilter is full
        focus.set('state:on')

    # 18) Pull espresso function of the Java Jolt Espresso Machine
    def pull_espresso (focus='state:on', espresso_machine='shot_button:on'):
        print('Java Jolt: pulling espresso brrrrzzzzzzzz')
        action.espresso_machine_pull_espresso('cup', 'state', 'espresso')
        action.espresso_machine_shot_button_off('espresso_machine', 'shot_button', 'off')
        focus.set('state:on')
    
    # 24) Steam milk with steamwand of the Java Jolt Espresso Machine
    def steamwand (focus='state:on', espresso_machine='steamwand:on'):
        print('Java Jolt: steaming the milk hiiiisssssss')
        action.espresso_machine_pull_espresso('pitcher', 'milk', 'steamed')
        action.espresso_machine_shot_button_off('espresso_machine', 'steamwand', 'off')
        focus.set('state:on')

nico=Barista()
machine1=Espresso_Machine()
env=Cafe_Environment()
env.agent=nico
env.agent=machine1 
log_everything(env)
env.run()



from python_actr import *  

#############################################################################################################
#####                                    FINAL ASSIGNMENT                                               #####
#############################################################################################################

# In this assignment we present a cognitive model of how an agent can multi-task in a cafe environment. 
# The barista model is now expanded with the incorporation of the imaginal module. 
# This addition will allow us to model interuptions which may occur during the cappuccino making process. 
# In this model, a customer requesting the bathroom key interupts the barista.
#
# The barista agent can deal with this interuption in two ways: 
# i) through the use of the imaginal module by holding the current stage of the cappuccino. 
# ii) A DM memory chunk is added to the DM module which is then recalled after the key has been passed to the guest. 
#
# The barista then goes on to complete the cappucino, but then must remember what side biscut the customer ordered.
# This biscut needs to be remembered, so the barista must recall the side (biscotti (correct), cannoli (wrong), savoiardi lady fingers (wrong)). 
# The barista either:
#   a) correctly remembers
#   b) forgets and asks the customer to remind them
#   c) incorrectly recalls the side with a previous customers order. 
#
# This ACT-R model demonstrates how interuptions in a SGOMS task can be handled when multi-tasking is required.
# Our model demonstrates that due to a serial bottleneck of cognitive processing, rapid task switching is required for certain proceedures in order to multitask. 
# In the future this model can be expanded to simulate concurrent multitasking via threaded cognition (Salvucci & Taatgen, 2008)
#
#
#############################################################################################################
#####                                     CAFE ENVIRONMENT                                              #####
#############################################################################################################

class Cafe_Environment(Model):        
    espresso_machine = Model(isa='espresso_machine', grouphead='unoccupied', shot_button='off', grinder='unoccupied', grinder_button='off', steamwand='off', tray='unoccupied')
    portafilter = Model(isa='portafilter', state='empty', location='on_counter')
    cup = Model(isa='cup', state='empty', location='on_counter')
    pitcher = Model(isa='pitcher', milk='unsteamed', location='on_counter')
    spoon=Model(isa='spoon', location='on_counter')
    bathroom_key= Model(isa='key', location='on_counter')

#############################################################################################################
#####                                     ACTION MODULE                                                 #####
#############################################################################################################

class ActionModule(Model):     

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

    # 'espresso_machine', 'grinder_button', 'on'
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


    # 'portafilter', 'state', 'full'
    def espresso_machine_action_grinding(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'espresso_machine','grinder_button','off' 
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


    # 'portafilter', 'location', 'in_hand'
    def barista_action_remove_portafilter_from_grinder(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'espresso_machine', 'grinder', 'unoccupied'
    def espresso_machine_action_unoccupied_grinder (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'portafilter', 'location', 'grouphead'
    def barista_action_insert_portafilter_into_grouphead (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
    
    # 'espresso_machine', 'grouphead', 'occupied'
    def espresso_machine_action_occupied_grouphead (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup', 'location', 'in_hand'
    def barista_action_grab_cup (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

   
    # 'portafilter', 'location', 'grouphead'
    def barista_action_grab_cup (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
    
    # 'espresso_machine', 'grouphead', 'occupied'
    def espresso_machine_occupied_tray (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'bathroom_key', 'location', 'guest'
    def barista_action_give_key_to_guest (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'espresso_machine', 'shot_button', 'on'
    def espresso_machine_press_shot_button (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup', 'state', 'espresso'
    def espresso_machine_pull_espresso (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)


    # 'espresso_machine', 'shot_button', 'off'
    def espresso_machine_shot_button_off (self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'pitcher', 'location', 'in_hand'
    def barista_action_place_pitcher_under_steamwand(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'espresso_machine', 'steamwand', 'on'
    def barista_action_steam_milk(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','location','in_hand'
    def barista_action_pick_up_espresso_cup_for_latte(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','state','latte'
    def barista_action_mix_latte(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','location','on_counter'
    def barista_cup_down_for_cappuccino_foam(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'spoon','location','in_hand'
    def barista_action_pick_up_spoon(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','state','cappuccino'
    def barista_action_scoop_foam(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','location','in_hand'
    def barista_action_pick_up_cup_of_cappuccino(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    # 'cup','location','service_station'
    def barista_action_serve_drink(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

#############################################################################################################
#####                                     BARISTA                                                       #####
#############################################################################################################

class Barista(ACTR):
    focus=Buffer()
    imaginal=Buffer()
    imaginal.set('task:null operation:null')
    action=ActionModule()
    DMbuffer=Buffer() ##added
    DM=Memory(DMbuffer,latency=0.05,threshold=0.03,finst_size=4,finst_time=5) 
    dm_n=DMNoise(DM,noise=0.05)            # set activation noise level
    dm_bl=DMBaseLevel(DM,decay=0.05)       # set activation decay
    partial=Partial(DM,strength=1.0,limit=-1.0) 

    partial.similarity('current','previous1', 0.0)   
    partial.similarity('current','previous2', 0.0)   
    partial.similarity('previous1','previous2', 0.0)   

    DM.add('customer:current side:biscotti')
    DM.add('customer:previous1 side:cannoli')
    DM.add('customer:previous2 side:savoiardi_lady_fingers') 

    focus.set('task:espresso operation:lift_portafilter')


        # lift portafilter off counter
    def production_lift_portafilter(focus='task:espresso operation:lift_portafilter', imaginal='task:null operation:null'):
        print('Barista: Alright, one cappucino with a biscotti coming up!.')
        print('Barista: First I need to make the espresso, so I will grab the portafilter off the counter.')
        action.barista_action_lift_portafilter('portafilter', 'location', 'in_hand')
        focus.set('task:espresso operation:insert_portafilter_into_grinder')

        # place portafilter into grinder....this results in the portafilter and espresso machine being updated
    def production_insert_portafilter_into_grinder(focus='task:espresso operation:insert_portafilter_into_grinder', imaginal='task:null operation:null'):
        print('Barista: Now I will place the portafilter into the grinder group head.')
        action.barista_action_insert_portafilter_into_grinder('portafilter', 'location', 'in_grinder') 
        action.espresso_machine_action_occupied_grinder('espresso_machine', 'grinder', 'occupied')
        focus.set('task:espresso operation:grind_beans')
   
        # grind beans production will turn on the grind_button on the espresso machine which will trigger it to grind and fill the portafilter with grounds. 
    def production_grind_beans(focus='task:espresso operation:grind_beans', imaginal='task:null operation:null'):
        print('Barista: Alright, the next step is to turn on the grinder and grind the espresso beans!')
        action.barista_action_turn_on_grinder('espresso_machine', 'grinder_button', 'on')
        focus.set('task:espresso operation:remove_portafilter_from_grinder')

        # remove and hold portafilter 
    def production_remove_portafilter_from_grinder(focus='task:espresso operation:remove_portafilter_from_grinder', imaginal='task:null operation:null'):
        print('Barista: Okay, now we take out the portafilter from the grinder.')
        action.barista_action_remove_portafilter_from_grinder('portafilter', 'location', 'in_hand') # need two actions one that updates the location of portafilter the other to update state of espresso machine
        action.espresso_machine_action_unoccupied_grinder('espresso_machine', 'grinder', 'unoccupied')
        focus.set('task:espresso operation:insert_portafilter_into_grouphead')

        # insert portafilter into grouphead
    def production_insert_portafilter_into_grouphead(focus='task:espresso operation:insert_portafilter_into_grouphead', imaginal='task:null operation:null'):
        print('Barista: Place the portafilter from the into the espresso steamer group head.')
        action.barista_action_insert_portafilter_into_grouphead('portafilter', 'location', 'grouphead')
        action.espresso_machine_action_occupied_grouphead('espresso_machine', 'grouphead', 'occupied')
        focus.set('task:espresso operation:grab_cup')

        # Grab cup
    def production_grab_cup(focus='task:espresso operation:grab_cup', imaginal='task:null operation:null'):
        print('Barista: Alright, lets pick up the cup on the counter.')
        action.barista_action_grab_cup('cup', 'location', 'in_hand')
        focus.set('task:espresso operation:place_cup_on_tray')

#####--------------------------------------------------------------------------------------------#####
#####                                                                                            #####
#####                               INTERUPTION HAPPENS HERE                                     #####
#####                                                                                            #####
#####--------------------------------------------------------------------------------------------#####

        # Place cup under grouphead on tray to catch espresso
    def production_place_cup_on_tray(focus='task:espresso operation:place_cup_on_tray', imaginal='task:null operation:null'):
        print('Barista: Next, I will place the cup on the espresso machine tray, under the group head to catch the espresso.')
        print('GUEST: EXCUSE ME CAN I HAVE THE KEY TO THE BATHROOM!?!?!?!?!?!?!?!?') ####### HERE IS WHERE INTERUPTION HAPPENS
        action.barista_action_grab_cup('cup', 'location', 'tray')
        action.espresso_machine_occupied_tray('espresso_machine', 'tray', 'occupied')
        imaginal.set('task:espresso operation:press_shot_button')
        focus.set('task:bathroom_key operation:get_key')

        # Bathroom Key
        # Imaginal buffer is used to remember what task and operation the barista is at
    def bathroom_key(focus='task:bathroom_key operation:get_key', imaginal='task:espresso operation:press_shot_button'):
        print('Barista:Here is the key.')
        action.barista_action_give_key_to_guest('bathroom_key', 'location', 'guest')
        print('Barista: So where were we?')
        focus.set('task:espresso operation:press_shot_button')
        imaginal.set('task:null operation:null')

#####--------------------------------------------------------------------------------------------#####
#####                                                                                            #####
#####       IF YOU WANTED TO COMPLETE THIS WITH A DM REQUEST INSTEAD OF IMAGINAL MODULE          #####
#####                                                                                            #####     
#####--------------------------------------------------------------------------------------------#####


#        Place cup under grouphead on tray to catch espresso
#    def production_place_cup_on_tray(focus='task:espresso operation:place_cup_on_tray', imaginal='task:null operation:null'):
#        print('Barista: Place the cup on the espresso machine tray, under the group head to catch the espresso.')
#        print('GUEST: EXCUSE ME CAN I HAVE THE KEY TO THE BATHROOM!?!?!?!?!?!?!?!?') ####### HERE IS WHERE INTERUPTION HAPPENS
#        action.barista_action_grab_cup('cup', 'location', 'tray')
#        action.espresso_machine_occupied_tray('espresso_machine', 'tray', 'occupied')
#        DM.add('task:espresso operation:press_shot_button')    # ADD TO DECLARATIVE MEMORY
#        focus.set('task:bathroom_key operation:get_key')

#        Bathroom Key 
#    def bathroom_key(focus='task:bathroom_key operation:get_key'):
#        print('Barista:Here is the key.')
#        action.barista_action_give_key_to_guest('bathroom_key', 'location', 'guest')
#        print('Barista: So where were we?....') ### DM REQUEST HERE
#        DM.request('task:?task operation:?operation')
#        focus.set('task:recall_step')
#        imaginal.set('task:null operation:null')
#
#        Forgot Step
#    def production_garnish_forgotten(focus='task:recall_step', DM='error:True', DMbuffer=None):
#        print("Barista: I forgot at what step I was at .... awkward.")
#        focus.set('task:stop')

#        Remebered Step
#    def production_garnish_latte(focus='task:recall_step', DMbuffer='task:espresso operation:press_shot_button'):
#        print('Barista: Ah yes I was making an...',task,'...and currently doing....',operation)
#        print('Barista: Now, press the shot button to pull the espresso shot.')
#        action.espresso_machine_press_shot_button('espresso_machine', 'shot_button', 'on')
#        focus.set('task:latte operation:pick_up_pitcher') # the task has changed to a latte now


#############################################################################################################
#############################################################################################################
#############################################################################################################

        # Pull espresso 
    def production_press_shot_button(focus='task:espresso operation:press_shot_button', imaginal='task:null operation:null'):
        print('Barista:....Oh Right!...I have to press the shot button to pull the espresso shot.')
        action.espresso_machine_press_shot_button('espresso_machine', 'shot_button', 'on')
        focus.set('task:latte operation:pick_up_pitcher') # the task has changed to a latte now

        # Pick up pitcher 
    def production_pick_up_pitcher(focus='task:latte operation:pick_up_pitcher', imaginal='task:null operation:null'):
        print('Barista: Now that the espresso shot has been pulled, if that is what the guest ordered, it would be ready to serve.')
        print('Barista: However, I will show you how to turn this into a latte, so lets steam some milk!')
        print('Barista: Pick up the pitcher that has some milk in it off the counter and hold it under the steamwand.')
        action.barista_action_place_pitcher_under_steamwand('pitcher', 'location', 'in_hand') 
        focus.set('task:latte operation:steam_milk')

        # Steam Milk
    def production_steam_milk(focus='task:latte operation:steam_milk', imaginal='task:null operation:null'):
        print('Barista: Now it is time to steam the milk!')
        action.barista_action_steam_milk('espresso_machine', 'steamwand', 'on') 
        focus.set('task:latte operation:pick_up_espresso_cup_for_latte')

        # Pick up espresso cup
    def production_pick_up_espresso_cup_for_latte(focus='task:latte operation:pick_up_espresso_cup_for_latte', imaginal='task:null operation:null'):
        print('Barista: So now that our milk is steamed pick up the cup with espresso in it.') # pitcher is still in_hand
        action.barista_action_pick_up_espresso_cup_for_latte('cup','location','in_hand')
        focus.set('task:latte operation:mix_latte')


        # Mix espresso and steamed milk to make latte 
    def production_make_latte(focus='task:latte operation:mix_latte', imaginal='task:null operation:null'):
        print('Barista: So now we pour the steamed milk onto the espresso to make a latte.') 
        action.barista_action_mix_latte('cup','state','latte')
        focus.set('task:cappuccino operation:place_cup_down_cappuccino')

        # place cup down 
        # note : a real cappuccino has a different ratio of milk to espresso compared to a latte
    def production_place_cup_down_for_cappuccino(focus='task:cappuccino operation:place_cup_down_cappuccino', imaginal='task:null operation:null'):
        print('Barista: To make the cappuccino we take our latte and add foamed milk, so place the cup down on the counter.') 
        action.barista_cup_down_for_cappuccino_foam('cup','location','on_counter')
        focus.set('task:cappuccino operation:pick_up_spoon')

        # pick up spoon
    def production_pick_up_spoon(focus='task:cappuccino operation:pick_up_spoon', imaginal='task:null operation:null'):
        print('Barista: To finish the cappiccino grab a spoon to scoop some of the frothy milk foam.') 
        action.barista_action_pick_up_spoon('spoon','location','in_hand')
        focus.set('task:cappuccino operation:spoon_milk_foam')

        # spoon milk foam
    def production_spoon_milk_foam(focus='task:cappuccino operation:spoon_milk_foam', imaginal='task:null operation:null'):
        print('Barista: Scoop the foam from the pitcher.') 
        action.barista_action_scoop_foam('cup','state','cappuccino')
        focus.set('task:cappuccino operation:pick_up_cup_to_serve')

        # pick up cup
    def production_pick_up_cup_to_serve(focus='task:cappuccino operation:pick_up_cup_to_serve', imaginal='task:null operation:null'):
        print('Barista: Alright, we have completed the cappuccino!') 
        action.barista_action_pick_up_cup_of_cappuccino('cup','location','in_hand')
        focus.set('task:cappuccino operation:serve_drink')

        # place cup on pick up station and call service
    def production_serve_drink(focus='task:cappuccino operation:serve_drink', imaginal='task:null operation:null'):
        print('Barista: Okay, here is your cappucino, let me just grab your side....')
        action.barista_action_serve_drink('cup', 'location', 'service_station')
        focus.set('task:side operation:side_biscut_recall customer:current')

        # Recall side biscut 
    def production_recall_side(focus='task:side operation:side_biscut_recall customer:current'):
        print('Barista: They ordered a side with their cappuccino, what was it?......')
        DM.request('customer:current side:?side', require_new=True) 
        focus.set('task:side operation:side_biscut')

        # Garnish Remebered
    def production_garnish_latte(focus='task:side operation:side_biscut', DMbuffer='side:?side'): #side:?side
        print('Barista: I recall they wanted....a',side,'...Enjoy! ^__^')
        focus.set('task:stop')

        # Garnish Forgotten
    def production_garnish_forgotten(focus='task:side operation:side_biscut', DM='error:True', DMbuffer=None):
        print('Barista: I recall they wanted....')
        print("Barista: I forgot, what was the side you wanted again?")
        print("Barista: Oh right, a biscotti, here you are, enjoy! ^__^")
        focus.set('task:stop')


#############################################################################################################
#####                                    ESPRESSO MACHINE                                               #####
#############################################################################################################

class Espresso_Machine(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:on')
    action=ActionModule()

    # Grinding beans function of the Java Jolt Espresso Machinne
    def grinding(focus='state:on', espresso_machine='grinder_button:on'):
        print('Java Jolt: grinding dem beans')
        action.espresso_machine_action_grinding('portafilter', 'state', 'full') # grinding dem beans fills up the portafilter
        action.espresso_machine_grinder_button_off('espresso_machine','grinder_button','off') # grinding ends once portafilter is full
        focus.set('state:on')

    # Pull espresso function of the Java Jolt Espresso Machine
    def pull_espresso (focus='state:on', espresso_machine='shot_button:on'):
        print('Java Jolt: pulling espresso brrrrzzzzzzzz')
        action.espresso_machine_pull_espresso('cup', 'state', 'espresso')
        action.espresso_machine_shot_button_off('espresso_machine', 'shot_button', 'off')
        focus.set('state:on')
    
    # Steam milk with steamwand of the Java Jolt Espresso Machine
    def steamwand (focus='state:on', espresso_machine='steamwand:on'):
        print('Java Jolt: steaming the milk hiiiisssssss')
        action.espresso_machine_pull_espresso('pitcher', 'milk', 'steamed')
        action.espresso_machine_shot_button_off('espresso_machine', 'steamwand', 'off')
        focus.set('state:on')

#############################################################################################################
#############################################################################################################
#############################################################################################################

nico=Barista()
machine1=Espresso_Machine()
env=Cafe_Environment()
env.agent=nico
env.agent=machine1 
log_everything(env)
env.run()



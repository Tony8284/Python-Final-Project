
import time
import sys

wound = 0
def print_slow(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)  # print_slow character without newline
        time.sleep(delay)
    print()  # print_slow newline after the text is print_slowed slowly

def print_slow_extra_slow(text, delay=0.5):
    for char in text:
        print(char, end='', flush=True)  # print_slow character without newline
        time.sleep(delay)
    print()  # print_slow newline after the text is print_slowed slowly

print_slow ("You approach a giant steel door with a Demon's Face grafted on to it.")
print_slow ("The Demon speaks.")
print_slow ("Welcome to the Dungeon.")
print_slow ("Your goal is to survive each floor and defeat the boss on the Fifth Floor.")
print_slow ("Are you ready?")
ready = input () 

def die():
    print_slow ("You Died!!")
    print_slow ("Hit Enter to Leave This Plane of Existence.")
    sys.exit()
    #note proper punctuation dumbass
def first_floor():
    print_slow("The Doors Swing Open.")
    print_slow("You feel an adrenaline rush from the fear of death and the unexpected riches.")
    print_slow("The first enemy approaches.")
    print_slow("A Goblin!!")
    print_slow("What will you do now Adventurer?")
    print_slow("Pick up your weapon and FIGHT or RUN past him.")

def second_floor():
    print_slow("The rocky and mountainous area you were once in suddenly changes.")
    print_slow("A cold wind shocks your body.")
    print_slow("An entirely new biome, Ice Spikes and Snow everywhere.")
    print_slow("You explore the floor trying to find the stairs as fast as possible before you freeze.")
    print_slow("Just as your extremeties begin to numb you see the entrance to the third floor.")
    print_slow("when suddenly a pack of wild dire wolves surround you from behind.")
    print_slow("What will you do?")
#implement a three strike system
#three wrong choices in a row will eventually lead to a death unless its not a very stupid one
def third_floor():
    print_slow("You walk the down the stairs and immediatley feel the heat, making you forget about the cold.")
    print_slow("A beautiful lava lake. At the end, you see a door leading to the next floor.")
    print_slow("You notice each rock and boulder protruding from the lava lake is within reach.")
    print_slow("Will you jump?")





def goblin_fight():
    print_slow("Your swords clash and after a hard faught battle you emerge victorious.")
    print_slow("You take the time to loot the goblin and safely make your way down the stairs leading to the next floor.")

    #what happens if player decides to fight goblin

def goblin_run():
    print_slow("You try running around the goblin.")
    print_slow("The goblin swings its sword at you and you succesfully dodge it.")
    print_slow("Thankfully nothing wrong happened this time.")
    print_slow("You approach the stairs leading down and on to the second floor you go.")
    #what happens if player decides to run past goblin
    
def second_floor_function_first_choice(second_floor_choice):
    global wound
    if(second_floor_choice == "A") or (second_floor_choice == "a"):
      
      print_slow("you remember the price of dire wolf pelt in the store.")
      print_slow("Just like with the goblin you want them dead, just surviving and getting to the other floor isn't enough anymore.")
      print_slow("Shivering and numb, you raise your sword and strike first.")
      print_slow("The first wolf goes down without any trouble but the other 3 had other plans.")
      print_slow("you take a couple of slashes to the back and arm.")
      print_slow("With each attack of the wolf you counterattack and manage to kill the other three.")
      print_slow_extra_slow("At a price.")
      print_slow("Your leg is heavily wounded.")
      print_slow("Barely standing you loot the wolf pelts and continue onwards to the next floor.")
      
      wound = 2
       
          #Goblin Attack,Wolf Attack --Major wounded both loot
    elif(second_floor_choice == "B") or (second_floor_choice == "b"):
      
      print_slow("You decide that the goblin gave you enough trouble and that the extra money from wolf pelts wasn't worth the risk.")
      print_slow("You turn away from the group and with all your might you dash towards the stairs.")
      print_slow("One of the wolves manages to catch up to you as you are heading down the stairs.")
      print_slow("You take a deep bite wound in your leg as you fall down the stairs into the next floor.")
      print_slow("The fire and heat coming from the next floor manages to scare the wolves back to their home floors.")
      wound = 1    
          #Goblin Attack, Wolf Dash --- minor wound
    elif(second_floor_choice == "C") or (second_floor_choice == "c"):
      print_slow("Remembering the loot you obtained from the goblin.")
      print_slow("You decide to throw the goblin ears you collected as proof of kill to distract and stall the wolves.")
      print_slow("The coins for killing a goblin i'snt worth the risk.")
      print_slow("You almost lose all sensation in your extremeties as the warmth and heat from the lower floor revitalizes them.")
      wound = 0
          #Goblin Attack, Wolf Goblin Loot, No Wounds
    else:
      print_slow("it was a multiple choice of a,b, and c bro.")
      print_slow("it could be a mistake or it could not, regardless start over.")
      die()


def second_floor_function_second_choice(second_floor_choice_2):
      global wound 
    
      if second_floor_choice_2 == "A" or second_floor_choice_2 == "a":
        print_slow("You ran past the goblin but decided that the coin from the wolf pelts would outweigh the risk.")
        print_slow("Invigorated with energy you slash at the first wolf and quickly kill the second one.")
        print_slow("The last two wolves hesitate but jump in nevertheless.")
        print_slow("You overpower the two wolves, one latched on to your leg and the other your armor.")
        print_slow("Victory is yours and so are the wolf pelts.")
        print_slow("You make your way to the warm entrance of the next floor.")
        
        wound = 1
          #third floor function
          #Goblin Dash,Wolf Fight Wolf Loot ---- Minor Wound
      elif second_floor_choice_2 == "B" or second_floor_choice_2 == "b":
        print_slow("You ran past the first goblin, surely you can run past these wolves as well.")
        print_slow("You turn away from the group and with all your might you dash towards the stairs.")
        print_slow("One of the wolves manages to catch up to you as you are heading down the stairs.")
        print_slow("You take a deep bite wound in your leg as you fall down the stairs into the next floor.")
        print_slow("The fire and heat coming from the next floor manages to scare the wolves back to their home floors.")
        
        wound = 1 
       #third floor function
          #goblin dash, Wolf Dash, no loot
      else :
        print_slow("it was a multiple choice of a and b bro")
        print_slow("it could be a mistake or it could not, regardless start over")
        die()


def third_floor_scene(third_floor_input):
    global wound 
    if third_floor_input.lower () in ["yes", "yep", "sure","ok","let's go","lets go","ready as i'll ever be","ye","yeah"]:
        if wound == 0:
          print_slow("You gracefully jump from one boulder, on to the next.")
          print_slow("Without any major incidents you arrive safely at the other end of the lava lake.")
          print_slow("On to the next floor!")


         #no wound chat third floor get across

        elif wound == 1:
          print_slow("As you jump from boulder to boulder.")
          print_slow("The sharp pain in your leg causes you to lose your footing.")
          print_slow("You scrape your elbows and dislocate your shoulder but manage to hang on by a thread.")
          print_slow("Bloodied and tattered, but you made it across.")
          print_slow("To the next floor.")
          wound = 2

          # 1 wound chat third floor get across
          #wound update to 2
        elif wound == 2:
          print_slow("Heavily wounded from the wolves you attempt to get across the perilous lava lake.")
          print_slow("On the third jump your leg gives out.")
          print_slow("You fall short of the boulder and slowly slide down into your doom.")
          die()
          
        else:
          print_slow("uh what?")
          die()# 2 wound chat third floor get across
           
        
        #what happens in third floor when jumping across



def fourth_floor_scene1():
    print_slow("As you ready your weapon and raise your gaurd, you realize that the fourth floor is just....")
    print_slow("A town?")
    print_slow("Completely unexpected you are greeted in a friendly manner.")
    print_slow("Exhausted from your previous endeavours you come across two choices before fighting the final boss.")
    print_slow("[A] Rest at Inn         [B] Train ")




def fourth_floor_scene(fourth_floor_input):
    global wound
    if fourth_floor_input == "A" or fourth_floor_input == "a":
        if wound == 0:
            print_slow("You arrive healthy into the towns bustling inn")
            print_slow("Most adventurers there question you on how you made it this far without any injuries.")
            print_slow("flooded with questions, you take your time telling of your stories and finish the night partying away.")
            print_slow("You wake up the next day well rested and ready to take on the Boss.")
            wound = 0
        elif wound == 2:
            print_slow("You arrive at the inn and some healers quickly tend to your wounds.")
            print_slow("The other adventurers surround you and ask questions of your travels. Curios how you got those injuries.")
            print_slow("You wake up the next day well rested and healthy. Ready to fight the Boss.")
            wound = 0
        else:
            print_slow("HOW!!!!!")
    elif fourth_floor_input == "B" or fourth_floor_input == "b":
        if wound == 0:
            print_slow("You arrive at the city, but decide i'ts never too late to train.")
            print_slow("As you are healthy and in top notch condition you head over to the training grounds and hack away at the dummies.")
            print_slow("You stay for a week training in solitude until you steel your resolve and make your way to the next floor.")
            wound = 1
            #there really isnt a wound here just to differentiate in fifth floor scene
        elif wound == 2:
            print_slow ("Heavily wounded and barely able to walk straight you decide that these wounds are nothing and go to the training grounds.")
            print_slow("Some onlookers praise you for your tenacity while others worry and pity you.")
            print_slow("What could drive someone to this maddened state.")
            print_slow("Your wounds didn't get better, but you are much better with your weapon than you were at the start of this adventure.")
            wound = 3
            #this isnt really making it more severe
        else:
            print_slow("HOW!!!!!")
    else:
        print_slow("its a multiple choice question bro")
        print_slow("Try again")

    #give the player a city
    # The choice of an Inn to rest. Heal all wounds
    #the choice to train. Increase any wound 



def fifth_floor_scene():
    global wound

    print_slow("Finally the moment you have been waiting for.")
    if wound == 0:
        print_slow("Well rested and healed you venture forth into the fifth floor.")
        print_slow("You grab your weapon and enter what seems to be a dimly lit cavern.")
        print_slow("Suddenly a Dragon peeks its head from one of the cave openings.")
        print_slow("Remembering your objective, you dash forward weapon in hand and fight the foul beast.")
        print_slow("Victory is yours.")
        print_slow("Not a perfect victory; you are burnt and bloodied from a couple parts of your body.")
        print_slow("You get teleported back to the begining of the dungeon. No recollection of a town, but deep down you know you defeated the dragon.")
        print_slow("The demon face in the door starts laughing.")
        print_slow("Are you ready to reach the tenth floor?")
        print()
        print()
        print_slow("To Be Continued!!!!")
        print_slow("Neutral Ending 1/3")


    elif wound == 1:
        print_slow("You never got complacent.")
        print_slow("You knew better than to relax.")
        print_slow("As you arrive in front of the dimly lit cavern.")
        print_slow("A dragon springs from one of the caves entrances.")
        print_slow("Effortlessly.")
        print_slow("Would be the only way to describe the battle that took place.")
        print_slow("With your weapon and expert skills, the dragon falls and is beheaded in three strikes.")
        print_slow("You are teleported back to the front entrance of the dungeon.")
        print_slow("The demon in the wall laughs and congratulates you.")
        print_slow("You are not fit for these early floors.")
        print_slow("Are you ready to reach the 50th floor?")
        print()
        print()
        print_slow("To Be Continued!!!!")
        print_slow("True Ending 3/3")





    elif wound == 3:
        print_slow("Your skill with your weapon has improved drastically.")
        print_slow("As you enter the dimly lit cavern,")
        print_slow("a dragon appears from one of the cavern openings.")
        print_slow("Fear and excitement fill you as you trade blows with the dragon.")
        print_slow("Evenly matched.")
        print_slow("With each blow you and the dragon take one step closer to death.")
        print_slow("Eventually the final blow, one last attack from each of you.")
        print_slow("Both of you fall flat on the ground unmoving.")
        print_slow("You took each other out.")
        print_slow("Valiantly Fought.")
        print()
        print()
        print_slow("You Died in the process but you still beat the fifth floor boss.")
        print_slow("Bad Ending 2/3")
        
    else:
        print_slow("SOMETHING WENT WRONG IF THIS SHOWS UP")




def the_game_itself(choice_1):
    if choice_1.lower() in ["fight","attack","kill","engage"]:
        goblin_fight()
        print()
        second_floor()
        print_slow("[A] Fight         [B] Dash         [C] Use Goblin's Loot")
        second_floor_choice_1 = input()
        second_floor_function_first_choice(second_floor_choice_1)
        print()
        third_floor()
        third_floor_input = input()
        third_floor_scene(third_floor_input)
        print()
        fourth_floor_scene1()

        while True:
            fourth_floor_input = input()
            fourth_floor_input_lower = fourth_floor_input.lower()
            if fourth_floor_input_lower == 'a' or fourth_floor_input_lower == 'b':
                fourth_floor_scene(fourth_floor_input)
                break
            else:
                print_slow("bro its a multiple choice question")
                print_slow("TRY AGAIN, you dont have a choice in the matter")
        
        print()
        print()
        
        fifth_floor_scene()

        #once code is done, focus on visual for user
        #fourth Floor
        #fourth floor will have a Resting place and a Training Place
        #Resting will remove any wounds leading to a hard fought victory
        #Training without removing wounds will lead to death at final boss
        #Training at 0 wounds will lead to an easy and stylish Victory aka the TRUE ENDING





    elif choice_1.lower() in ["run","dash","dodge","avoid"] :
       goblin_run()
       second_floor()
       print_slow("[A] Fight         [B] Dash")
       print()
       second_floor_choice_2 = input()
       second_floor_function_second_choice(second_floor_choice_2)
       print()
       third_floor()
       third_floor_input = input()
       third_floor_scene(third_floor_input)
       print()
       fourth_floor_scene1()

       while True:
            fourth_floor_input = input()
            fourth_floor_input_lower = fourth_floor_input.lower()
            if fourth_floor_input_lower == 'a' or fourth_floor_input_lower == 'b':
                fourth_floor_scene(fourth_floor_input)
                break
            else:
                print_slow("bro its a multiple choice question")
                print_slow("TRY AGAIN, you dont have a choice in the matter")
        

       print()
       print()
       fifth_floor_scene()



    else :
        print_slow("so you are going to" + choice_1 )
        print_slow("I'm sure this will end well")
        die()












if ready.lower() in ["yes", "yep", "sure","ok","let's go","lets go","ready as i'll ever be","ye","yeah"]: 
      print_slow ("Good Luck Adventurer")
      first_floor()
      choice_1 = input()
      the_game_itself(choice_1)
elif ready.lower() in ["no","nah","im ok"]: 
      print_slow ("Bruh")
      die()
else :
      print_slow ("Huh?, its a yes or no question dude.")
      print_slow ("you know what? just restart")
      die()



  













    

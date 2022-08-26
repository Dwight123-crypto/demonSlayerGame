class Demon:
    
    def __init__(self, name, rank, demonArt, life):
        self.name = name
        self.rank = rank
        self.demonArt = demonArt
        self.life = life
        
    def getName(self):
        return self.name
        
    def getRank(self):
        return self.rank
        
    def getArt(self):
        return self.demonArt
        
    def getLife(self):
        return self.life
        
    def attack(self, Hashira):
        print(self.name + " attacks "+ Hashira.getName())
        Hashira.life = Hashira.life - 50
        
Lower5 = Demon("Rui", "Lower Demon Moon 5", "Cutting Thread Rotation", 100)
Lower1 = Demon("Enmu", "Lower Demon Moon 1", "Whispers of Forced Unconscious Hypnosis", 100)
Upper6_1 = Demon("Daki", "Upper Demon Moon 6", "Eight Layered Obi Slash", 100)
Upper6_2 = Demon("Gyutaro", "Upper Demon Moon 6", "Flying Blood Sickles", 100)
        

class Hashira:
    
    def __init__(self, name, breathing, form, life):
        self.name = name
        self.breathing = breathing
        self.form = form
        self.life = life
        
    def getName(self):
        return self.name
        
    def getBreathe(self):
        return self.breathing
        
    def getForm(self):
        return self.form
        
    def getLife(self):
        return self.life
        
    def attack(self, Demon):
        print(self.name + " attacks "+ Demon.getName())
        Demon.life = Demon.life - 50
        
Water_hashira = Hashira("Giyu Tomioka", "Water breathing", "Eleventh Form: Dead Calm, Tidal Waves", 100)
Insect_hashira = Hashira("Shinobu Kocho", "Insect breathing", "Butterfly Dance: Caprice, Illusory Light", 100)
Fire_hashira = Hashira("Kyojuro Rengoko", "Fire breathing", "Fourth Form: Blooming Flame Undulation", 100)
Sound_hashira = Hashira("Tengen Uzui", "Sound Breathing", "Fifth Form: String Performance", 100)


name = input("Enter ur name to start: ")
print("")
print("Konnichiwa! "+name+ "-kun!")
print("")
print("Please pick ur Hashira!")
print("")
print("[1] Water hashira")
print("[2] Insect hashira")
print("[3] Fire hashira")
print("[4] Sound hashira")
print("")

hashira = int(input("Enter Hashira: "))

if hashira == 1:
    hashira_name = Water_hashira.getName()
    print("")
    print("You have picked...")
    print("")
    print("---------------------------------------------")
    print("Water Hashira: "+Water_hashira.getName())
    print("Type of Breathing: "+Water_hashira.getBreathe())
    print("Skill: "+Water_hashira.getForm())
    print("Life: "+str(Water_hashira.getLife()))
    print("---------------------------------------------")
elif hashira == 2:
    hashira_name = Insect_hashira.getName()
    print("")
    print("You have picked...")
    print("")
    print("-----------------------------------------------")
    print("Insect Hashira: "+Insect_hashira.getName())
    print("Type of Breathing: "+Insect_hashira.getBreathe())
    print("Skill: "+Insect_hashira.getForm())
    print("Life: "+str(Insect_hashira.getLife()))
    print("-----------------------------------------------")
elif hashira == 3:
    hashira_name = Fire_hashira.getName()
    print("")
    print("You have picked...")
    print("")
    print("---------------------------------------------")
    print("Fire Hashira: "+Fire_hashira.getName())
    print("Type of Breathing: "+Fire_hashira.getBreathe())
    print("Skill: "+Fire_hashira.getForm())
    print("Life: "+str(Fire_hashira.getLife()))
    print("---------------------------------------------")
elif hashira == 4:
    hashira_name =  Sound_hashira.getName()
    print("")
    print("You have picked...")
    print("")
    print("-------------------------------------")
    print("Sound Hashira: "+Sound_hashira.getName())
    print("Type of Breathing: "+Sound_hashira.getBreathe())
    print("Skill: "+Sound_hashira.getForm())
    print("Life: "+str(Sound_hashira.getLife()))
    print("-------------------------------------")
    
input()
    
print("Please pick Demon Lare...")
print("")
print("[1] Natagumo Mountain")
print("[2] Mugen")
print("[3] Red Light District")
print("")
lare = int(input("Enter Demon Lare: "))

if lare == 1:
    print("")
    print("You have picked Natagumo Mountain!")
elif lare == 2:
    print("")
    print("You have picked Mugen!")
elif lare == 3:
    print("")
    print("You have picked Red light District!")

input()
print("Demon approaching...")
input()
print("GET READY TO FIGHT!!!")
input()

if lare == 1:
    print(Lower5.getName()+": What are you doing here human?")
    input()
    print(Lower5.getName()+": I will slice you into pieces!")
    input()
    print("----------------------------------")
    print("Demon: "+Lower5.getName())
    print("Rank: "+Lower5.getRank())
    print("Demon Art: "+Lower5.getArt())
    print("Life: "+str(Lower5.getLife()))
    print("----------------------------------")
    input()
    print(hashira_name+": A Lower 5 Demon Moon!")
    input()
    print(Lower5.getName()+": My name is Rui")
    input()
    print(Lower5.getName()+": I will kill anyone who dare interfere on my family's bond!")
    input()
    print(hashira_name+": I will not let that happen!")
    input()
    print(Lower5.getName()+": We'll see about that...")
    input()
    print(Lower5.getName()+": Prepare to die!")
    input()
    if hashira == 1:
        Lower5.attack(Water_hashira);
        input()
        print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
        input()
        print("Giyu's Life: "+str(Water_hashira.getLife()))
        input()
        while Lower5.getLife() >=1 and Water_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Water_hashira.attack(Lower5);
                input()
                print(Water_hashira.getName()+": "+Water_hashira.getForm())
                input()
                print("Rui's Life: "+str(Lower5.getLife()))
                print("")
                
            elif x == 1:
                Lower5.attack(Water_hashira);
                input()
                print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
                input()
                print("Giyu's Life: "+str(Water_hashira.getLife()))
                print("")
                
                break 
            
        if Lower5.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Water_hashira.getLife() == 0:
            print("YOU LOSE!!!")
    
    elif hashira == 2:
        Lower5.attack(Insect_hashira);
        input()
        print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
        input()
        print("Shinobu's Life: "+str(Insect_hashira.getLife()))
        input()
        while Lower5.getLife() >=1 and Insect_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Insect_hashira.attack(Lower5);
                input()
                print(Insect_hashira.getName()+": "+Insect_hashira.getForm())
                input()
                print("Rui's Life: "+str(Lower5.getLife()))
                print("")
                
            elif x == 1:
                Lower5.attack(Insect_hashira);
                input()
                print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
                input()
                print("Shinobu's Life: "+str(Insect_hashira.getLife()))
                print("")
                
                break 
            
        if Lower5.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Insect_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 3:
        Lower5.attack(Fire_hashira);
        input()
        print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
        input()
        print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
        input()
        while Lower5.getLife() >=1 and Fire_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Fire_hashira.attack(Lower5);
                input()
                print(Fire_hashira.getName()+": "+Fire_hashira.getForm())
                input()
                print("Rui's Life: "+str(Lower5.getLife()))
                print("")
                
            elif x == 1:
                Lower5.attack(Fire_hashira);
                input()
                print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
                input()
                print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
                print("")
                
                break 
            
        if Lower5.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Fire_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 4:
        Lower5.attack(Sound_hashira);
        input()
        print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
        input()
        print("Tengen's Life: "+str(Sound_hashira.getLife()))
        input()
        while Lower5.getLife() >=1 and Sound_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Sound_hashira.attack(Lower5);
                input()
                print(Sound_hashira.getName()+": "+Sound_hashira.getForm())
                input()
                print("Rui's Life: "+str(Lower5.getLife()))
                print("")
                
            elif x == 1:
                Lower5.attack(Sound_hashira);
                input()
                print(Lower5.getName()+": Blood Demon Art: "+Lower5.getArt())
                input()
                print("Tengen's Life: "+str(Sound_hashira.getLife()))
                print("")
                
                break 
            
        if Lower5.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Sound_hashira.getLife() == 0:
            print("YOU LOSE!!!")

elif lare == 2:
    print(Lower1.getName()+": Ohayo!")
    input()
    print(Lower1.getName()+": Do u want to experience a sweet dream?")
    input()
    print("--------------------------------------------------")
    print("Demon: "+Lower1.getName())
    print("Rank: "+Lower1.getRank())
    print("Demon Art: "+Lower1.getArt())
    print("Life: "+str(Lower1.getLife()))
    print("--------------------------------------------------")
    input()
    print(hashira_name+": A Lower 1 Demon Moon!")
    input()
    print(Lower1.getName()+": I'm Enmu")
    input()
    print(Lower1.getName()+": Once I kill u Muzan-sama will share more of his blood on me!")
    input()
    print(hashira_name+": I will not let that happen!")
    input()
    print(Lower1.getName()+": We'll see about that...")
    input()
    print(Lower1.getName()+": Prepare to die!")
    input()
    if hashira == 1:
        Lower1.attack(Water_hashira);
        input()
        print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
        input()
        print("Giyu's Life: "+str(Water_hashira.getLife()))
        input()
        while Lower1.getLife() >=1 and Water_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Water_hashira.attack(Lower1);
                input()
                print(Water_hashira.getName()+": "+Water_hashira.getForm())
                input()
                print("Enmu's Life: "+str(Lower1.getLife()))
                print("")
                
            elif x == 1:
                Lower1.attack(Water_hashira);
                input()
                print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
                input()
                print("Giyu's Life: "+str(Water_hashira.getLife()))
                print("")
                
                break 
            
        if Lower1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Water_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 2:
        Lower1.attack(Insect_hashira);
        input()
        print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
        input()
        print("Shinobu's Life: "+str(Insect_hashira.getLife()))
        input()
        while Lower1.getLife() >=1 and Insect_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Insect_hashira.attack(Lower1);
                input()
                print(Insect_hashira.getName()+": "+Insect_hashira.getForm())
                input()
                print("Enmu's Life: "+str(Lower1.getLife()))
                print("")
                
            elif x == 1:
                Lower1.attack(Insect_hashira);
                input()
                print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
                input()
                print("Shinobu's Life: "+str(Insect_hashira.getLife()))
                print("")
                
                break 
            
        if Lower1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Insect_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 3:
        Lower1.attack(Fire_hashira);
        input()
        print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
        input()
        print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
        input()
        while Lower1.getLife() >=1 and Fire_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Fire_hashira.attack(Lower1);
                input()
                print(Fire_hashira.getName()+": "+Fire_hashira.getForm())
                input()
                print("Enmu's Life: "+str(Lower1.getLife()))
                print("")
                
            elif x == 1:
                Lower1.attack(Fire_hashira);
                input()
                print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
                input()
                print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
                print("")
                
                break 
            
        if Lower1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Fire_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 4:
        Lower1.attack(Sound_hashira);
        input()
        print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
        input()
        print("Tengen's Life: "+str(Sound_hashira.getLife()))
        input()
        while Lower1.getLife() >=1 and Sound_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Sound_hashira.attack(Lower1);
                input()
                print(Sound_hashira.getName()+": "+Sound_hashira.getForm())
                input()
                print("Enmu's Life: "+str(Lower1.getLife()))
                print("")
                
            elif x == 1:
                Lower1.attack(Sound_hashira);
                input()
                print(Lower1.getName()+": Blood Demon Art: "+Lower1.getArt())
                input()
                print("Tengen's Life: "+str(Sound_hashira.getLife()))
                print("")
                
                break 
            
        if Lower1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Sound_hashira.getLife() == 0:
            print("YOU LOSE!!!")
    
elif lare == 3:
    print(Upper6_1.getName()+": What's an ugly human doing here?")
    input()
    print(Upper6_1.getName()+": An ugly human like you doesn't have the right to live!")
    input()
    print(Upper6_1.getName()+": Only those that are beautiful & strong has the right!")
    input()
    print("----------------------------------")
    print("Demon: "+Upper6_1.getName())
    print("Rank: "+Upper6_1.getRank())
    print("Demon Art: "+Upper6_1.getArt())
    print("Life: "+str(Upper6_1.getLife()))
    print("----------------------------------")
    input()
    print(hashira_name+": A Upper 6 Demon Moon!")
    input()
    print(Upper6_1.getName()+": I'm Daki")
    input()
    print(Upper6_1.getName()+": I have already devoured 7 hashira's & you will be next!")
    input()
    print(hashira_name+": I will not let that happen!")
    input()
    print(Upper6_1.getName()+": We'll see about that...")
    input()
    print(Upper6_1.getName()+": Prepare to die!")
    input()
    if hashira == 1:
        Upper6_1.attack(Water_hashira);
        input()
        print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
        input()
        print("Giyu's Life: "+str(Water_hashira.getLife()))
        input()
        while Upper6_1.getLife() >=1 and Water_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Water_hashira.attack(Upper6_1);
                input()
                print(Water_hashira.getName()+": "+Water_hashira.getForm())
                input()
                print("Daki's Life: "+str(Upper6_1.getLife()))
                print("")
                
            elif x == 1:
                Upper6_1.attack(Water_hashira);
                input()
                print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
                input()
                print("Giyu's Life: "+str(Water_hashira.getLife()))
                print("")
                
                break 
            
        if Upper6_1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Water_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 2:
        Upper6_1.attack(Insect_hashira);
        input()
        print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
        input()
        print("Shinobu's Life: "+str(Insect_hashira.getLife()))
        input()
        while Upper6_1.getLife() >=1 and Insect_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Insect_hashira.attack(Upper6_1);
                input()
                print(Insect_hashira.getName()+": "+Insect_hashira.getForm())
                input()
                print("Daki's Life: "+str(Upper6_1.getLife()))
                print("")
                
            elif x == 1:
                Upper6_1.attack(Insect_hashira);
                input()
                print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
                input()
                print("Shinobu's Life: "+str(Insect_hashira.getLife()))
                print("")
                
                break 
            
        if Upper6_1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Insect_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 3:
        Upper6_1.attack(Fire_hashira);
        input()
        print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
        input()
        print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
        input()
        while Upper6_1.getLife() >=1 and Fire_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Fire_hashira.attack(Upper6_1);
                input()
                print(Fire_hashira.getName()+": "+Fire_hashira.getForm())
                input()
                print("Daki's Life: "+str(Upper6_1.getLife()))
                print("")
                
            elif x == 1:
                Upper6_1.attack(Fire_hashira);
                input()
                print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
                input()
                print("Kyojuro's Life: "+str(Fire_hashira.getLife()))
                print("")
                
                break 
            
        if Upper6_1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Fire_hashira.getLife() == 0:
            print("YOU LOSE!!!")
            
    elif hashira == 4:
        Upper6_1.attack(Sound_hashira);
        input()
        print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
        input()
        print("Tengen's Life: "+str(Sound_hashira.getLife()))
        input()
        while Upper6_1.getLife() >=1 and Sound_hashira.getLife() >=1:
            print("[0] Attack!!!")
            print("[1] Not attack")
            print("")
            x = int(input("Enter move: "))
            print("")
            if x == 0:
                Sound_hashira.attack(Upper6_1);
                input()
                print(Sound_hashira.getName()+": "+Sound_hashira.getForm())
                input()
                print("Daki's Life: "+str(Upper6_1.getLife()))
                print("")
                
            elif x == 1:
                Upper6_1.attack(Sound_hashira);
                input()
                print(Upper6_1.getName()+": Blood Demon Art: "+Upper6_1.getArt())
                input()
                print("Tengen's Life: "+str(Sound_hashira.getLife()))
                print("")
                
                break 
            
        if Upper6_1.getLife() == 0:
            print("YOU WIN!!!")
            
        elif Sound_hashira.getLife() == 0:
            print("YOU LOSE!!!")
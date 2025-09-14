import pyttsx3
print(dir(pyttsx3))
from datetime import datetime
class speak:
    def __init__(self):
        self.eng=pyttsx3.init()
        self.voice=self.eng.getProperty("voices")
        self.eng.setProperty("rate",195)
        self.eng.setProperty("voice",self.voice[1].id)#initilize zira's voice(id 1 for zira and o for david)
    
    def talk(self,*args):
        text=" ".join(args)
        text = text.replace(",", ",  ")
        text = text.replace(".", ".    ")
        self.eng.say(text)
        self.eng.runAndWait()
    
    def GreetUser(self):
        hr=datetime.now().time().hour
        if(hr>=4 and hr<12):
            self.talk("good morning,have a great day")
        elif(hr>=12 and hr<17):
            self.talk("good afternoon, hope your day is going well")
        elif(hr>=17 and hr<22):
            self.talk("good evening,time to relax and recharge")
        elif(hr>=22 or hr<4):
            self.talk("good night,see ya later")

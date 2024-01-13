"""
Author: Gaurav Shukla and on scrath Gtl123  Data Finished: 13-01-2024 
Please do not edit the convert function as it has a lot of hard coded generators expressions so editing one will lead to eteranal doom ;)
Also this code is roughly 40% smaller than v1.0 and so is quite unreadable so don't try :/ """
import math , os
class ConvertMIDItoTuneShare:
    def __init__(self,filename,tempo = 110, quality=1, outputname=""):
        try:
            with open("Assets/OSD2SD.txt", "r") as f:
                self.OSD2SD = [(int(item) if item.isnumeric() else None) for item in f.read().split(",")]
            with open("Assets/OSI.txt", "r") as f:
                self.OSI = [(int(item.split(",")[0]) if item.find(",") != -1 else None) for item in f.read().split("\n")]
            with open("Assets/SBI.txt", "r") as f:
                self.SBI = f.read().split(",")
            with open(f"Input/{filename}", "r") as f:
                self.Data = f.read().rsplit(":")[2].rsplit(";") 
        except Exception as FatalError:
            Exception(f"Error Loading Files : {FatalError}")
        self.filename, self.tempo, self.quality, self.outputname , self.lastVolume,self.missedNotes = filename,tempo,quality,outputname,100,0
        self.convert()
    def convert(self):
        try:
            notes = []
            [(notes.append(self.fetchvalues(note)) if "slot" in self.fetchvalues(note) else None ) for note in self.Data]
            self.maxSlots, self.minSlots= 0 ,notes[0]["slot"]
            def setminmax(case,i):
                if case == "X":
                    i["slot"] = round(i["slot"]-self.minSlots)
                if i["slot"] > self.maxSlots and case != "X":
                    self.maxSlots = i["slot"]
                if i["slot"] < self.minSlots and case != "X":
                    self.minSlots = i["slot"]
            [(setminmax("null",i)) for i in notes]
            self.maxSlots = math.ceil(self.maxSlots - self.minSlots)
            [ (setminmax("X",i) if "slot" in i else None ) for i in notes]
            slots = [ [] for _ in range(self.maxSlots+1)]
            [ (slots[i["slot"]].append({"note": i["note"],"length": min(max(1, i["length"]), 36)-1,"instrument": int(i["instrument"]),"volume": i["volume"]})) for i in notes]
            code =  f"{round(self.tempo*self.quality)}!" + ''.join(list([f"{''.join(list(((((str(self.__code__(data=data))) if self.getNote(self.SBI[self.OSI.index(data['instrument'])], data['note']) else '') if data['instrument'] in self.OSI else '') for data in slot)))}!" for slot in slots]))
            outputname = self.outputname if self.outputname != "" else f"Output/{self.filename.split(sep = '.')[0]}_converted.txt"
            with open(outputname, "w") as f:
                f.write(code)
                print(f"Converstion was successful and is saved as {outputname} is the Output folder." if self.missedNotes == 0 else f"Converstion was partially successful with {self.missedNotes} missed notes and is saved as {outputname} is the Output folder.")
        except Exception as commonError:
            Exception(f"Fatal Error {commonError}")
    def fetchvalues(self,i):
        t = str(i).rsplit(" ")
        self.lastVolume  = min(max(0, round(float(t[4]) * 36 * self.quality)), 35) if len(t) > 4 else self.lastVolume       
        return (({"note": t[1],"slot": float(t[0]) * self.quality,"length": math.ceil(float(t[2]) * self.quality),"instrument": t[3],"volume":self.lastVolume,})) if len(t) > 2 else {}        
    def getNote(self,instr, n):
        li = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        note , transpose = n[:-1] , int(n[-1]) - 2
        ret = transpose * len(li) + li.index(note) + 10
        return ([0] if self.OSD2SD[ret-10] is None else [1, str(self.OSD2SD[ret-10])]) if instr == "l" else ([1, str(ret)] if len(str(ret)) < 3 else [0])
    def __code__(self,data):
        try:
            return (self.getNote(self.SBI[self.OSI.index(data["instrument"])], data["note"])[1] + self.SBI[self.OSI.index(data["instrument"])] + "0123456789abcdefghijklmnopqrstuvwxyz"[data["length"]] + "0123456789abcdefghijklmnopqrstuvwxyz"[data["volume"]])
        except Exception:
            self.missedNotes += 1
            return ("")      
[(ConvertMIDItoTuneShare(filename=filename, tempo=110, quality=1.5) if os.path.isfile(os.path.join("Input", filename)) else None ) for filename in os.listdir("Input")]

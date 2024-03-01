import decimal
from math import pi
from os import system
from datetime import datetime
class Program:

    def __init__(self) -> None:
        self.cInput = "" 
        self.PI = decimal.Decimal(str(pi))
        self.bwklist = {}

    def ParseInput(self) -> None:
        userInput = self.cInput.split(" ", -1)
        command = userInput[0]
        queTest = decimal.Decimal("0")
        qSave = 0
        nonMax = 0
        valList = []
        finalAns = ""
        if "-s" in userInput: qSave = 1
        
        if command == "cl": self.ClearScreen()

        elif command == "ql":
            print(self.Q_Look(userInput[1]))
        elif command == "qs":
            self.Q_Save(userInput[1], userInput[2])
            print("Question saved.\n")
        elif command == "h":
            self.help()
        elif command == "qdel":
            self.bwklist.pop(userInput[1])
            print(f"{userInput[1]} deleted.\n")
        elif command == "+":
            
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
            
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            
            ans = decimal.Decimal(str(0))
            for i, _ in enumerate(valList):
                    if len(valList) != 2:
                        if i == len(valList):
                            ans, finalAns = self.Add(que, ans, valList[i], qS=qSave)

                        else: ans, _ = self.Add(que, ans, valList[i], qS=0)
                    else: ans, finalAns = self.Add(que, valList[0], valList[1], qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
        #Subtracting
        elif command == "-":
            
            if "-nm" in userInput: nonMax = 1
            
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
            
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str or userInput[i] == "-s" or userInput[i] == "-nm":
                    pass
                else: valList.append(decimal.Decimal(userInput[i]))
            
            ans = decimal.Decimal(str(0))
            if nonMax == 0:    
                
                ans, finalAns = self.Sub(que, tuple(valList), qs=qSave)
                
                if que != "":
                    print(finalAns)
                else: print(ans)
            
            else:
                
                for i, _ in enumerate(valList):
                        if len(valList) != 2:
                            if i == 0: ans, _ = self.SubNonMax(que, valList[i], valList[i+1])
                            elif i == len(valList):
                                ans, finalAns = self.SubNonMax(que, ans, valList[i], qS=qSave)
                            elif i+1 < len(valList): ans, _ = self.SubNonMax(que, ans, valList[i+1], qS=0)
                        else: ans, finalAns = self.SubNonMax(que, valList[0], valList[1], qS=qSave)
                
                if que != "":
                    print(finalAns)
                else: print(ans)
        #Multiplying
        elif command == "*":
            
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
            
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            
            ans = decimal.Decimal(str(0))
            if len(valList) != 2:
                for i, _ in enumerate(valList):

                        if i == len(valList):
                            ans, finalAns = self.Mult(que, ans, valList[i], qS=qSave)

                        else: ans, _ = self.Mult(que, ans, valList[i], qS=0)

            else: ans, finalAns = self.Mult(que, valList[0], valList[1], qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
        #Dividing
        elif command == "/":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))

            ans = decimal.Decimal(str(0))
            if len(valList) != 2:
                for i, _ in enumerate(valList):

                        if i == len(valList):
                            ans, finalAns = self.Div(que, ans, valList[i], qS=qSave)

                        else: ans, _ = self.Div(que, ans, valList[i], qS=0)

            else: ans, finalAns = self.Div(que, valList[0], valList[1], qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
        #Midpoint
        elif command == "mp":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            
            ans = self.MidP(que, valList[0], valList[1], valList[2], valList[3], qS=qSave)
            if que != "":
                print(ans)
            else: print(ans)
        #Nth term
        elif command == "nt":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            
            ans = self.NthT(que, valList[0], valList[1])
            if que != "":
                print(ans)
            else: print(ans)
        #Circumference
        elif command == "cir":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            valList[1] = int(str(valList[1]))
            ans, finalAns = self.FindCirc(valList[0], valList[1], qNum=que, qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
        #Circle area
        elif command == "car":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            valList[1] = int(str(valList[1]))
            ans, finalAns = self.FindC_Area(valList[0], valList[1], qNum=que, qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
        #Sector area
        elif command == "sar":
            try: queTest = decimal.Decimal(userInput[1])
            except decimal.DecimalException: que = userInput[1]
            else: que = ""
        
            for i, _ in enumerate(userInput):
                
                try: num = decimal.Decimal(userInput[i])
                except decimal.DecimalException: num = userInput[i] 
                
                if i == 0 or type(num) == str:
                    pass
                elif userInput[i] == "-s": qSave = 1
                else: valList.append(decimal.Decimal(userInput[i]))
            valList[2] = int(str(valList[2]))
            ans, finalAns = self.FindSectArea(valList[0], valList[1], valList[2], qNum=que, qS=qSave)
            if que != "":
                print(finalAns)
            else: print(ans)
    
    #Question lookup and save
    def Q_Save(self, qNum: str, ans) -> None:
        ansD = self.bwklist
        if qNum == "": print("ERROR: Arg 'qNum' = Null\n")
        else: ansD[qNum] = ans
    def Q_Look(self, qNum: str):
        try:
            return f"{qNum}: {self.bwklist[qNum]}"
        except KeyError:
            print("ERROR: '1B' not found.\n")

    
    #Basic arithmetic - can pass as many values to add
    def Add(self, qNum="", *values: decimal.Decimal, qS=0):
        n = decimal.Decimal(str(0))
        
        for _, value in enumerate(values):
            n+=value
        
        if qS == 1: self.Q_Save(qNum, n)
        
        if qNum == "": return n, f"{qNum}: {n}"
        else: return n, f"{qNum}: {n}"
    
    def Sub(self, qNum="", *values: tuple, qS=0):
        n = max(values)
        v = list(values)
        v = [x for x in v if x != max(v)]
        values = tuple(v)
        
        for _, value in enumerate(values):
            n-=value

        if qS == 1: self.Q_Save(qNum, n)
        
        if qNum == "": return n, f"{qNum}: {n}"
        else: return n, f"{qNum}: {n}"
    
    def SubNonMax(self, qNum="", *values: decimal.Decimal, qS=0):
        n = values[0]
        n-=values[1]
        if qS == 1: self.Q_Save(qNum, n)
        if qNum=="": return n, f"{qNum}: {n}"
        else: return n, f"{qNum}: {n}"
    
    def Mult(self, qNum="", *values: decimal.Decimal, qS=0):
        n = values[0]
        n*=values[1]
        if qS == 1: self.Q_Save(qNum, n)
        
        if qNum == "": return n, f"{qNum}: {n}"
        return n, f"{qNum}: {n}"
    
    def Div(self, qNum="", *values: decimal.Decimal, qS=0):
        n = values[0]
        n/=values[1]
        
        if qS == 1: self.Q_Save(qNum, n)
        
        if qNum == "": return n, f"{qNum}: {n}"
        else: return n, f"{qNum}: {n}"

    
    #EXTRA STUFF: Midpoint and nth term
    def MidP(self, qNum="", *values: decimal.Decimal, qS=0):
        if len(values) > 4: return "ERROR: Args 'values' exceeded 4."
        
        x1, y1, x2, y2 = values
        x, _ = self.Add("", x1, x2)
        y, _ = self.Add("", y1, y2)
        avgX, _ = self.Div("", x, decimal.Decimal(2))
        avgY, _ = self.Div("", y, decimal.Decimal(2))
        
        if qS == 1: self.Q_Save(qNum, f"{avgX}, {avgY}")
        
        if qNum == "": return f"{avgX}, {avgY}"
        else: return f"{qNum}: {avgX}, {avgY}"

    def NthT(self, qNum="", *values: decimal.Decimal, qS=0):
        diff, _ = self.Sub("", values[0], values[1])
        secondDiff = diff-values[0]
        ans1 = f"{diff}n + {secondDiff}"
        ans2 = f"{diff}n - {secondDiff}"
        ans3 = f"{diff}n"
        if secondDiff < 0: 
            if qS == 1: self.Q_Save(qNum, ans1)
            return ans1
        elif secondDiff > 0: 
            if qS == 1: self.Q_Save(qNum, ans3)
            return ans2
        else:
            if qS == 1: self.Q_Save(qNum)
            return ans3
    
    
    #EXTRA STUFF: Circle related things
    def FindCirc(self, diameter: decimal.Decimal, dp: int, qNum="", qS=0):
        PI = self.PI
        circ = PI*diameter
        circ = round(circ, dp)
        if qS == 1: self.Q_Save(qNum, circ)
        if qNum == "": return circ, f"{qNum}: {circ}"
        else: return circ, f"{qNum}: {circ}"
    
    def FindC_Area(self, radius: decimal.Decimal, dp: int, qNum="", qS=0):
        area = round(self.PI*radius**2, dp)
        if qS == 1: self.Q_Save(qNum, area)
        if qNum == "": return area, f"{qNum}: {area}"
        else: return area, f"{qNum}: {area}"
    
    def FindSectArea(self, angle: decimal.Decimal, area: decimal.Decimal, dp: int, qNum="", qS=0):
        sectArea = round(angle/360*area, dp)
        if qS == 1: self.Q_Save(qNum, sectArea)
        if qNum == "": return sectArea, f"{qNum}: {sectArea}"
        else: return sectArea, f"{qNum}: {sectArea}"
    
    
    #UTILITIES: Help and clear-screen
    def ClearScreen(self):
        system("cls")
    
    def help(self):
        print("Available commands:\n+ <questionnumber>* <numbers>sep <savequestion>* - add\n- <questionnumber>* <numbers>sep <nonmaxflag>* <savequestion>* - subtract\n* <questionnumber>* <numbers>sep <savequestion>* - multiply\n/ <questionnumber>* <numbers>sep <savequestion>* - divide\nmp <questionnumber>* <x1, y1, x2, y2>sep <savequestion>* - midpoint\nnt <questionnumber>* <sequence>sep <savequestion>* - nth term\ncir <questionnumber>* <diameter> <dp> <savequestion>* - circumference\ncar <questionnumber>* <radius> <dp> <savequestion>* - area of a circle\nsar <questionnumber>* <angle> <area> <dp> <savequestion>* - area of a sector of a circle\ncl - clear screen\nql <questionnumber> - find the answer of a previous question\nqs <questionnumber> <questionanswer> - saves a question you can't save with the other functions\nqdel <questionnumber> - deletes a question you accidently saved\n\nIf you see a * after > means optional. If you see a 'sep' after > means separate numbers with a space.")


sKiller = Program()
print("| | sKiller vCLI5.0 Alpha | |")
print("Type 'h' for commands.")
#Main loop
while True:
    sKiller.cInput = input(">")
    sKiller.ParseInput()

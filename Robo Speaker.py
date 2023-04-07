import os
if __name__ =='__main__':

 print("Welcome to Robo Speaker")
 while(True):
  txt = input("Enter anything to pronounce it: ")
  if txt == "exit":
    os.system("Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye friend take care')")    
    break
  cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{txt}')"
  os.system(cmd)
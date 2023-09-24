import time
class tvs():

          def __init__(self, sit="OFF", volume= 0, channel_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50], current_channel="Parasonic"):
                    self.sit = sit
                    self.volume = volume
                    self.channel_list = channel_list
                    self.current_channel = current_channel

          def open(self):
                    if(self.sit == "ON"):
                              print("TV is already ON.")
                    else:
                              self.sit = "ON"
                              print("TV will be open.")

          def close(self):
                    if(self.sit == "OFF"):
                              print("TV is already OFF.")
                    else:
		self.sit = "OFF"
		print("TV will be close.")

          def change_volume(self):
                    while(True):
                              ans = input("Volume off '<'\nVolume on '>'\nExit 'exit'\nChoose: ")
                              if(ans == "exit"):
                                        break
                              if(ans == "<"):
                                        if(self.volume <= 0):
                                                  print("You cannot volume off any more.")
                                        else:
                                                  self.volume -= 1
                                                  print("Current volume: ",self.volume)
                              elif(ans == ">"):
                                        if(self.volume >= 100):
                                                  print("You canot volume on any more.")
                                        else:
                                                  self.volume += 1
                                                  print("Current volume: ",self.volume)
                              else:
                                        print("Unknown command!")
                                        print("\n----------------\n")

          def total_channel(self):
                    print("total channel is ",self.n)

          def channel_change(self,o):
                    v=self.channel_list[o]+1
                    print("Channel was changed.\nCurrent channel name: ",self.current_channel)

          def __len__(self):
                    return len(self.channel_list)

          def __str__(self):
                    return "---All the information---\nTV Current Situation: {}\nTV Current Volume: {}\nTV Channel List: {}\nTV Current Channel: {}".format(self.sit, self.volume, self.channel_list, self.current_channel)
	
def main():

          tv1 = tvs()
          print("""
                              -----------TV System-----------
		1. ON
		2. OFF
		3. Change Volume
		4. Total Channel
		5. Learn Channel Num
		6. Change Channel
		7. TV Info
		8. Exit
		""")

          while(True):

                    command = input("Please, enter your command: ")
                    if(command == "8"):
                              print("The system will shut down now.")
                              time.sleep(1)
                              break
                    elif(command == "1"):
                              tv1.open()
                    elif(command == "2"):
		tv1.close()
                    elif(command == "3"):
		tv1.change_volume()
                    elif(command == "4"):
		tv1.total_channel()
                    elif(command == "5"):
                              print("The number of channels: ", len(tv1))
                    elif(command == "6"):
                              m=int(input("enter channel number =")
                              tv1.channel_change(m)
                    elif(command == "7"):
		print(tv1)

                    else:
                              print("Unknown Command!")




if __name__ == "__main__":
	main()	

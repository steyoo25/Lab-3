import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        #
        # TO DO
        #
        self.attackButton = tkinter.Button(self,text='Attack',fg='red',bg='black',command=self.attack_clicked)
        self.attackButton.grid(row=0,column=0)

        self.youToComputer = tkinter.Label(self)
        self.youToComputer.grid(row=0,column=1)

        self.computerToYou = tkinter.Label(self)
        self.computerToYou.grid(row=1,column=1)

        self.winMsg = tkinter.Label(self, fg='red')
        self.winMsg.grid(row=2,column=1)

        tkinter.Label(self, text='You').grid(row=3,column=0)
        tkinter.Label(self, text='Computer').grid(row=3,column=1)
        
        player1Large = tkinter.PhotoImage(file='images/'+self.player1.large_image)
        w1=tkinter.Label(self, image=player1Large)
        w1.photo = player1Large
        w1.grid(row=4,column=0)
        
        player2Large = tkinter.PhotoImage(file='images/'+self.player2.large_image)
        w2=tkinter.Label(self, image=player2Large)
        w2.photo = player2Large
        w2.grid(row=4,column=1)

        self.player1HitPoints = tkinter.Label(self, text=str(self.player1.hit_points) + '/' + str(self.player1_max_hp) + ' HP')
        self.player2HitPoints = tkinter.Label(self, text=str(self.player2.hit_points) + '/' + str(self.player2_max_hp) + ' HP')
        self.player1HitPoints.grid(row=5,column=0)
        self.player2HitPoints.grid(row=5,column=1)

        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        #
        # TO DO
        #
        r1 = self.player1.attack(self.player2)
        r2 = self.player2.attack(self.player1)
        self.player1HitPoints['text'] = str(self.player1.hit_points) + '/' + str(self.player1_max_hp) + ' HP'
        self.player2HitPoints['text'] = str(self.player2.hit_points) + '/' + str(self.player2_max_hp) + ' HP'
        self.youToComputer['text'] = r1
        self.computerToYou['text'] = r2
        if self.player1.hit_points > 0 and self.player2.hit_points <= 0:
            self.winMsg['text'] = f'{self.player1.name} is victorious!'
            self.attackButton.destroy()
            self.exitButton = tkinter.Button(self, text='Exit!', fg='red', bg='black',padx=20, font='15')
            self.exitButton['command'] = self.exit_clicked 
            self.exitButton.grid(row=6,column=1,sticky=tkinter.E)

        elif self.player2.hit_points > 0 and self.player1.hit_points <= 0:
            self.winMsg['text'] = f'{self.player2.name} is victorious!'
            self.attackButton.destroy()
            self.exitButton = tkinter.Button(self, text='Exit!', fg='red', bg='black',padx=20, font='15')
            self.exitButton['command'] = self.exit_clicked 
            self.exitButton.grid(row=6,column=1,sticky=tkinter.E)
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
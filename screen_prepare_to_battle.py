import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        #
        # TO DO
        #
        tkinter.Label(self, text='You').grid(row=0,column=0)
        tkinter.Label(self, text='Computer').grid(row=0,column=1)
        
        player1Large = tkinter.PhotoImage(file='images/'+self.player1.large_image)
        w1=tkinter.Label(self, image=player1Large)
        w1.photo = player1Large
        w1.grid(row=1,column=0)
        
        player2Large = tkinter.PhotoImage(file='images/'+self.player2.large_image)
        w2=tkinter.Label(self, image=player2Large)
        w2.photo = player2Large
        w2.grid(row=1,column=1)

        r1=2
        player1List = [
            (self.player1.hit_points,'HP'), 
            (self.player1.dexterity,'Dexterity'),
            (self.player1.strength,'Strength')
        ]
        for x in player1List:
            tkinter.Label(self, text=str(x[0])+' '+x[1], font='14').grid(row=r1,column=0)
            r1+=1

        r1=2
        player2List = [
            (self.player2.hit_points,'HP'), 
            (self.player2.dexterity,'Dexterity'),
            (self.player2.strength,'Strength')
        ]        
        for x in player2List:
            tkinter.Label(self, text=str(x[0])+' '+x[1], font='14').grid(row=r1,column=1)
            r1+=1

        tkinter.Button(self, text='Commence Battle!', fg='red', bg='black',command=self.commence_battle_clicked).grid(row=5,column=1,sticky=tkinter.E)
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
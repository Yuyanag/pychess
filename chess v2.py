class piece: 
    def __init__(self,icon,pos,colour):
        self.Icon = icon
        self.currentlocation = pos #string value that shows the current position
        self.moveable = [] #stores the places which the pieces are able to move to
        self.checking = []
        self.colour = colour #determines if the piece is black or white

    def updatemove(self):
        self.moveable = []

    def filter(self):
        self.checking = [] #used ONLY for checks

class pawn(piece): #note 2: the moves are mirrored to cater coding
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)
        self.FM = True #checks that the pawn hasnt move yet to move 2 steps
        self.en = False
    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        #reverse = 
        if self.colour == "black":
            if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(int(self.currentlocation[0]) + 1))
            if cb.board[int(self.currentlocation[0]) + 2][colom.index(self.currentlocation[1])] == "." and self.FM == True:
                self.moveable.append(self.currentlocation[1] + str(int(self.currentlocation[0]) + 2))
            
            if colom.index(self.currentlocation[1]) + 1 <= 7:
                if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) + 1] != ".":
                    if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) + 1].colour == "white":
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) + 1))
                
                if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1] != ".":
                    if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].colour == "white" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].Icon.upper() == "P" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].en == True:
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) + 1))
            
            if colom.index(self.currentlocation[1]) - 1 >= 0:
                if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) - 1] != ".":
                    if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) - 1].colour == "white":
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) + 1))

                if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1] != ".":
                    if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].colour == "white" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].Icon.upper() == "P" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].en == True:
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) + 1))
            

        elif self.colour == "white":
            if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(int(self.currentlocation[0]) - 1))
            if cb.board[int(self.currentlocation[0]) - 2][colom.index(self.currentlocation[1])] == "." and self.FM == True:
                self.moveable.append(self.currentlocation[1] + str(int(self.currentlocation[0]) - 2))
            
            if colom.index(self.currentlocation[1]) + 1 <= 7:
                if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) + 1] != ".":
                    if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) + 1].colour == "black":
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) - 1))

                if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1] != ".":
                    if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].colour == "black" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].Icon.upper() == "P" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) + 1].en == True:
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) - 1))
            
            if colom.index(self.currentlocation[1]) - 1 >= 0:
                if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) - 1] != ".":
                    if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) - 1].colour == "black":
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) - 1))

                if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1] != ".":
                    if cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].colour == "black" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].Icon.upper() == "P" and cb.board[int(self.currentlocation[0])][colom.index(self.currentlocation[1]) - 1].en == True:
                        self.moveable.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) - 1))
        
        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1]

        def filter(self): #note: the pieces moves are 1 index behind, please amend from input
            self.checking = []
    
            temp = []
            if self.colour == "black":
                
                
                if colom.index(self.currentlocation[1]) + 1 <= 7:
                    if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) + 1] != ".":
                        if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) + 1].colour == "white" and cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) + 1].Icon.upper() == "K":
                            temp.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) + 1))
                
                if colom.index(self.currentlocation[1]) - 1 >= 0:
                    if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) - 1] != ".":
                        if cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) - 1].colour == "white" and cb.board[int(self.currentlocation[0]) + 1][colom.index(self.currentlocation[1]) - 1].Icon.upper() == "K":
                            temp.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) + 1))
                
    
            elif self.colour == "white":
                
                
                if colom.index(self.currentlocation[1]) + 1 <= 7:
                    if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) + 1] != ".":
                        if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) + 1].colour == "black" and cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) + 1].Icon.upper() == "K":
                            temp.append(colom[colom.index(self.currentlocation[1]) + 1] + str(int(self.currentlocation[0]) - 1))
                
                if colom.index(self.currentlocation[1]) - 1 >= 0:
                    if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) - 1] != ".":
                        if cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) - 1].colour == "black" and cb.board[int(self.currentlocation[0]) - 1][colom.index(self.currentlocation[1]) - 1].Icon.upper() == "K":
                            temp.append(colom[colom.index(self.currentlocation[1]) - 1] + str(int(self.currentlocation[0]) - 1))

            for i in range(len(temp)):
                temp[i] =temp[i][::-1] 

            for item in temp:
                for i in range(len(cb.board)):
                    for items in cb.board[i]:
                        if items != ".":
                            if items.Icon.upper() == "K" and items.colour != self.colour and items.currentlocation == item:
                                self.checking += item
                
        
        
                
        

class rook(piece):
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)
        self.castle = True
    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        reverse = "76543210"
        i = int(int(self.currentlocation[0]) - 1)
        #print(i)
        while i >= 0:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i))
                i -= 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i))
                break
            else:
                break
                                    

        i = int(int(self.currentlocation[0]) + 1)
        while i <= 7:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i))
                i += 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i))
                break
            
            else:
                break
                
            
        i = colom.index(self.currentlocation[1]) - 1
        while i >= 0:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                self.moveable.append(colom[i] + self.currentlocation[0])
                i -= 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                self.moveable.append(colom[i] + self.currentlocation[0])
                break
            else:
                break

        
                

        i = colom.index(self.currentlocation[1]) + 1
        while i <= 7:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                self.moveable.append(colom[i] + self.currentlocation[0])
                i += 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                self.moveable.append(colom[i] + self.currentlocation[0])
                break
            else:
                break

        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1] 
                
    def filter(self): #note: the pieces moves are 1 index behind, please amend from input
        self.checking = []
        temp = []
        reverse = "76543210"
        i = int(int(self.currentlocation[0]) - 1)
        #print(i)
        while i >= 0:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                temp.append(self.currentlocation[1] + str(i))
                i -= 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                temp.append(self.currentlocation[1] + str(i))
                break
            else:
                break
        
        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp
                                    
        temp = []
        i = int(int(self.currentlocation[0]) + 1)
        while i <= 7:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                temp.append(self.currentlocation[1] + str(i))
                i += 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                temp.append(self.currentlocation[1] + str(i))
                break
            
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp
        temp = []    
        i = colom.index(self.currentlocation[1]) - 1
        while i >= 0:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                temp.append(colom[i] + self.currentlocation[0])
                i -= 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                temp.append(colom[i] + self.currentlocation[0])
                break
            else:
                break
       

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 
                
        temp = []
        i = colom.index(self.currentlocation[1]) + 1
        while i <= 7:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                temp.append(colom[i] + self.currentlocation[0])
                i += 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                temp.append(colom[i] + self.currentlocation[0])
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp

        
                

class knight(piece):
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)

    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        
        i = int(self.currentlocation[0])
        j = colom.index(self.currentlocation[1])


        if (i+2 <= 7 and j+1 <= 7):
            if cb.board[i + 2][j + 1] == ".":
                self.moveable.append(colom[j + 1] + str(i + 2))
            elif capturehelp(cb.board[i + 2][j + 1],self.colour) == True:
                self.moveable.append(colom[j + 1] + str(i + 2))
        
        if (i+2 <= 7 and j-1 >= 0):
            if cb.board[i + 2][j - 1] == ".":
                self.moveable.append(colom[j - 1] + str(i + 2))
            elif capturehelp(cb.board[i + 2][j - 1],self.colour) == True:
                self.moveable.append(colom[j - 1] + str(i + 2))
        
        if (i-2 >= 0 and j+1 <= 7):
            if cb.board[i - 2][j + 1] == ".":
                self.moveable.append(colom[j + 1] + str(i - 2))
            elif capturehelp(cb.board[i - 2][j + 1],self.colour) == True:
                self.moveable.append(colom[j + 1] + str(i - 2))
        
        if (i-2 >= 0 and j-1 >= 0):
            if cb.board[i - 2][j - 1] == ".":
                self.moveable.append(colom[j - 1] + str(i - 2))
            elif capturehelp(cb.board[i - 2][j - 1],self.colour) == True:
                self.moveable.append(colom[j - 1] + str(i - 2))
        
        if (i+1 <= 7 and j+2 <= 7):
            if cb.board[i + 1][j + 2] == ".":
                self.moveable.append(colom[j + 2] + str(i + 1))
            elif capturehelp(cb.board[i + 1][j + 2],self.colour) == True:
                self.moveable.append(colom[j + 2] + str(i + 1))
        
        if (i+1 <= 7 and j-2 >= 0):
            if cb.board[i + 1][j - 2] == ".":
                self.moveable.append(colom[j - 2] + str(i + 1))
            elif capturehelp(cb.board[i + 1][j - 2],self.colour) == True:
                self.moveable.append(colom[j - 2] + str(i + 1))
        
        if (i-1 >= 0 and j+2 <= 7):
            if cb.board[i - 1][j + 2] == ".":
                self.moveable.append(colom[j + 2] + str(i - 1))
            elif capturehelp(cb.board[i - 1][j + 2],self.colour) == True:
                self.moveable.append(colom[j + 2] + str(i - 1))
        
        if (i-1 >= 0 and j-2 >= 0):
            if cb.board[i - 1][j - 2] == ".":
                self.moveable.append(colom[j - 2] + str(i - 1))
            elif capturehelp(cb.board[i - 1][j - 2],self.colour) == True:
                self.moveable.append(colom[j - 2] + str(i - 1))

        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1] 
        
        
        

class bishop(piece):
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)

    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        reverse = "76543210"
        i = int(self.currentlocation[0]) - 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i >= 0 and j>= 0):
            if cb.board[i][j] == ".": # RUCD
                self.moveable.append(colom[j] + str(i))
                i -= 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break

        i = int(self.currentlocation[0]) -1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i >= 0 and j <= 7):
            if cb.board[i][j] == ".": # RUCU
                self.moveable.append(colom[j] + str(i))
                i -= 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break

        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i <= 7 and j >= 0):
            if cb.board[i][j] == ".": # RDCD
                self.moveable.append(colom[j] + str(i))
                i += 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break
                
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i <= 7 and j <= 7):
            if cb.board[i][j] == ".": # RDCU
                self.moveable.append(colom[j] + str(i))
                i += 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1] 

    def filter(self): #note: the pieces moves are 1 index behind, please amend from input
        self.checking = []
        reverse = "76543210"

        temp = []
        i = int(self.currentlocation[0]) - 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i >= 0 and j>= 0):
            if cb.board[i][j] == ".": # RUCD
                temp.append(colom[j] + str(i))
                i -= 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 


        temp = []
        i = int(self.currentlocation[0]) -1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i >= 0 and j <= 7):
            if cb.board[i][j] == ".": # RUCU
                temp.append(colom[j] + str(i))
                i -= 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 

        temp = []
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i <= 7 and j >= 0):
            if cb.board[i][j] == ".": # RDCD
                temp.append(colom[j] + str(i))
                i += 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 

        temp = []
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i <= 7 and j <= 7):
            if cb.board[i][j] == ".": # RDCU
                temp.append(colom[j] + str(i))
                i += 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp


        
class queen(piece):
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)

    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        
        i = int(self.currentlocation[0]) - 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i >= 0 and j>= 0):
            if cb.board[i][j] == ".": # RUCD
                self.moveable.append(colom[j] + str(i))
                i -= 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break

        i = int(self.currentlocation[0]) -1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i >= 0 and j <= 7):
            if cb.board[i][j] == ".": # RUCU
                self.moveable.append(colom[j] + str(i))
                i -= 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break

        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i <= 7 and j >= 0):
            if cb.board[i][j] == ".": # RDCD
                self.moveable.append(colom[j] + str(i))
                i += 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break
                
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i <= 7 and j <= 7):
            if cb.board[i][j] == ".": # RDCU
                self.moveable.append(colom[j] + str(i))
                i += 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                self.moveable.append(colom[j] + str(i))
                break
            else:
                break


        i = int(int(self.currentlocation[0]) - 1)
        #print(i)
        while i >= 0:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i))
                i -= 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i))
                break
            else:
                break
                                    

        i = int(int(self.currentlocation[0]) + 1)
        while i <= 7:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i))
                i += 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i))
                break
            
            else:
                break
                
            
        i = colom.index(self.currentlocation[1]) - 1
        while i >= 0:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                self.moveable.append(colom[i] + self.currentlocation[0])
                i -= 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                self.moveable.append(colom[i] + self.currentlocation[0])
                break
            else:
                break
                

        i = colom.index(self.currentlocation[1]) + 1
        while i <= 7:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                self.moveable.append(colom[i] + self.currentlocation[0])
                i += 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                self.moveable.append(colom[i] + self.currentlocation[0])
                break
            else:
                break


        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1] 

    def filter(self):
        self.checking = []
        temp = []
        reverse = "76543210"
        i = int(int(self.currentlocation[0]) - 1)
        #print(i)
        while i >= 0:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                temp.append(self.currentlocation[1] + str(i))
                i -= 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                temp.append(self.currentlocation[1] + str(i))
                break
            else:
                break
        
        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp
                                    
        temp = []
        i = int(int(self.currentlocation[0]) + 1)
        while i <= 7:
            if cb.board[i][colom.index(self.currentlocation[1])] == ".":
                temp.append(self.currentlocation[1] + str(i))
                i += 1
            elif capturehelp(cb.board[i][colom.index(self.currentlocation[1])],self.colour):
                temp.append(self.currentlocation[1] + str(i))
                break
            
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp
        temp = []    
        i = colom.index(self.currentlocation[1]) - 1
        while i >= 0:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                temp.append(colom[i] + self.currentlocation[0])
                i -= 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                temp.append(colom[i] + self.currentlocation[0])
                break
            else:
                break
       

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 
                
        temp = []
        i = colom.index(self.currentlocation[1]) + 1
        while i <= 7:
            if cb.board[int(self.currentlocation[0])][i] == ".":
                temp.append(colom[i] + self.currentlocation[0])
                i += 1
            elif capturehelp(cb.board[int(self.currentlocation[0])][i],self.colour):
                temp.append(colom[i] + self.currentlocation[0])
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp

        temp = []
        i = int(self.currentlocation[0]) - 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i >= 0 and j>= 0):
            if cb.board[i][j] == ".": # RUCD
                temp.append(colom[j] + str(i))
                i -= 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 


        temp = []
        i = int(self.currentlocation[0]) -1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i >= 0 and j <= 7):
            if cb.board[i][j] == ".": # RUCU
                temp.append(colom[j] + str(i))
                i -= 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 

        temp = []
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) - 1
        
        while (i <= 7 and j >= 0):
            if cb.board[i][j] == ".": # RDCD
                temp.append(colom[j] + str(i))
                i += 1
                j -= 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 

        temp = []
        i = int(self.currentlocation[0]) + 1
        j = colom.index(self.currentlocation[1]) + 1
        
        while (i <= 7 and j <= 7):
            if cb.board[i][j] == ".": # RDCU
                temp.append(colom[j] + str(i))
                i += 1
                j += 1
            elif capturehelp(cb.board[i][j],self.colour):
                temp.append(colom[j] + str(i))
                break
            else:
                break

        for i in range(len(temp)):
            temp[i] =temp[i][::-1] 
        
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.Icon.upper() == "K" and item.colour != self.colour:
                        self.checking = self.checking + temp 



class king(piece):
    def __init__(self,icon,pos,colour):
        super().__init__(icon,pos,colour)
        self.check = False
        self.castle = True

    def kingcheck2(self):
        defend = False
        attacking = []
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.colour != self.colour:
                        for pos in item.moveable:
                            if pos == self.currentlocation:
                                return True
        return False
    
    def kingcheck(self):
        self.check = False
        defend = False
        attacking = []
        for i in range(len(cb.board)):
            for item in cb.board[i]:
                if item != ".":
                    if item.colour != self.colour:
                        for pos in item.moveable:
                            if pos == self.currentlocation:
                                self.check = True
                                attacking.append(item)
                                break
            
        if self.check == True:
            #print("Original",self.moveable)
            for move in self.moveable:      
                for i in range(len(cb.board)):
                    for item in cb.board[i]:
                        if item != ".":
                            if item.colour != self.colour:
                                #print(self.moveable)
                                for pos2 in item.moveable:
                                    if pos2 == move:
                                        #print(item)
                                        self.moveable = self.moveable[:self.moveable.index(pos2)] + self.moveable[self.moveable.index(pos2) + 1:]
                                        #print(self.moveable)
            #print(self.moveable)
            for pieces in attacking:
                pieces.filter()
                #print("yo",pieces.checking)
                defend == False
                for i in range(len(cb.board)):
                    for item in cb.board[i]:
                        if item != ".":
                            if item.colour == self.colour:
                                j = 0
                                while j < len(item.moveable):
                                    if len(item.moveable) >= j:
                                        break
                                    if item.moveable[j] not in pieces.checking and item.moveable[j] != pieces.currentlocation:
                                        item.moveable = item.moveable[:j] + item.moveable[j+1:]
                                    else:
                                        defend = True
                                        j += 1
                if defend == False and len(self.moveable) == 0:
                    return False
        return True

                                             
                
                        


        
    def updatemove(self): #note: the pieces moves are 1 index behind, please amend from input
        self.moveable = []
        castle = True

        #castling long
        if self.castle == True:
            if cb.board[int(self.currentlocation[0])][0] != ".":
                if cb.board[int(self.currentlocation[0])][0].Icon.upper() == "R" and cb.board[int(self.currentlocation[0])][0].colour == self.colour and cb.board[int(self.currentlocation[0])][0].castle == True:
                    for i in range(1,4):
                        if cb.board[int(self.currentlocation[0])][i] != ".":
                            castle = False
                    if self.kingcheck2() == True:
                        castle = False
                    for i in range(1,4):
                        pos = str(self.currentlocation[0]) + colom[i]
                        for j in range(len(cb.board)):
                            for items in cb.board[j]:
                                if items != ".":
                                    if items.colour != self.colour:
                                        if pos in items.moveable:
                                            castle = False
                    if castle == True:
                        self.moveable.append("OOO")
            
            elif cb.board[int(self.currentlocation[0])][7] != ".":
                if cb.board[int(self.currentlocation[0])][7].Icon.upper() == "R" and cb.board[int(self.currentlocation[0])][7].colour == self.colour and cb.board[int(self.currentlocation[0])][7].castle == True:
                    for i in range(5,8):
                        if cb.board[int(self.currentlocation[0])][i] != ".":
                            castle = False
                    if self.kingcheck2() == True:
                        castle = False
                    for i in range(5,7):
                        pos = str(self.currentlocation[0]) + colom[i]
                        for j in range(len(cb.board)):
                            for items in cb.board[j]:
                                if items != ".":
                                    if items.colour != self.colour:
                                        if pos in items.moveable:
                                            castle = False
                    if castle == True:
                        self.moveable.append("OO")

                        
                
                
        
        
        i = int(self.currentlocation[0])
        j = colom.index(self.currentlocation[1])
        
        if (i-1 >= 0 and j-1 >= 0):
            if cb.board[i-1][j-1] == ".": # RUCD
                self.moveable.append(colom[j-1] + str(i-1))
            elif capturehelp(cb.board[i-1][j-1],self.colour):
                self.moveable.append(colom[j-1] + str(i-1))

        i = int(self.currentlocation[0])
        j = colom.index(self.currentlocation[1])
        
        if (i-1 >= 0 and j+1 <= 7):
            if cb.board[i-1][j+1] == ".": # RUCU
                self.moveable.append(colom[j+1] + str(i-1))
            elif capturehelp(cb.board[i-1][j+1],self.colour):
                self.moveable.append(colom[j+1] + str(i-1))
        
        i = int(self.currentlocation[0])
        j = colom.index(self.currentlocation[1])
        
        if (i+1 <= 7 and j-1 >= 0):
            if cb.board[i+1][j-1] == ".": # RDCD
                self.moveable.append(colom[j-1] + str(i+1))
            elif capturehelp(cb.board[i+1][j-1],self.colour):
                self.moveable.append(colom[j-1] + str(i+1))


        i = int(self.currentlocation[0])
        j = colom.index(self.currentlocation[1])
        
        if (i+1 <= 7 and j+1 <= 7):
            if cb.board[i+1][j+1] == ".": # RDCU
                self.moveable.append(colom[j+1] + str(i+1))
            elif capturehelp(cb.board[i+1][j+1],self.colour):
                self.moveable.append(colom[j+1] + str(i+1))
     

        i = int(self.currentlocation[0])
        if i-1 >= 0:
            if cb.board[i-1][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i-1))
            elif capturehelp(cb.board[i-1][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i-1))
            
                                

        i = int(self.currentlocation[0])
        if i+1 <= 7:
            if cb.board[i+1][colom.index(self.currentlocation[1])] == ".":
                self.moveable.append(self.currentlocation[1] + str(i+1))
            elif capturehelp(cb.board[i+1][colom.index(self.currentlocation[1])],self.colour):
                self.moveable.append(self.currentlocation[1] + str(i+1))
            
            

        i = colom.index(self.currentlocation[1])
        if i-1 >= 0:
            if cb.board[int(self.currentlocation[0])][i-1] == ".":
                self.moveable.append(colom[i-1] + self.currentlocation[0])
            elif capturehelp(cb.board[int(self.currentlocation[0])][i-1],self.colour):
                self.moveable.append(colom[i-1] + self.currentlocation[0])

        i = colom.index(self.currentlocation[1])
        if i+1 <= 7:
            if cb.board[int(self.currentlocation[0])][i+1] == ".":
                self.moveable.append(colom[i+1] + self.currentlocation[0])
            elif capturehelp(cb.board[int(self.currentlocation[0])][i+1],self.colour):
                self.moveable.append(colom[i+1] + self.currentlocation[0])

        for i in range(len(self.moveable)):
            self.moveable[i] =self.moveable[i][::-1] 
        


bp = "rhbqkbhr"
wp = "RHBQKBHR"
colom = "ABCDEFGH"

class board:
    def __init__(self):
        self.board = [["."] * 8] * 8
        for i in range(len(self.board)):
            self.board[i] = ["."] * 8
            
    def setup(self):
        column = "ABCDEFGH"
        for i in range(len(self.board[1])):
            location = "1" + column[i]
            pwn = pawn("p",location,"black")
            self.board[1][i] = pwn
            #print(location)
        for i in range(len(self.board[6])):
            location = "6" + column[i]
            pwn = pawn("P",location,"white")
            self.board[6][i] = pwn
            #print(location)

        for i in range(len(self.board[0])):
            location = "0" + column[i]
            if i == 0 or i == 7:
                pi = rook(bp[i],location,"black")
            elif i == 1 or i == 6:
                pi = knight(bp[i],location,"black")
            elif i == 2 or i == 5:
                pi = bishop(bp[i],location,"black")
            elif i == 3:
                pi = queen(bp[i],location,"black")
            else:
                pi = king(bp[i],location,"black")
            self.board[0][i] = pi     

        for i in range(len(self.board[7])):
            location = "7" + column[i]
            if i == 0 or i == 7:
                pi = rook(wp[i],location,"white")
            elif i == 1 or i == 6:
                pi = knight(wp[i],location,"white")
            elif i == 2 or i == 5:
                pi = bishop(wp[i],location,"white")
            elif i == 3:
                pi = queen(wp[i],location,"white")
            else:
                pi = king(wp[i],location,"white")
            self.board[7][i] = pi

    
    def display(self): #displays the board
        i = 8
        for item in self.board:
            string = ""
            for stuff in item:
                if stuff == ".":
                    string += " ."
                else:
                    string = string + " " + stuff.Icon
                
            print(str(i) + " |" + string)
            i -=1
        print("   -----------------")
        print("    " + "A B C D E F G H")

def capturehelp(point,colour):
    if point != ".":
        if colour == "black":
            if point.colour == "white":
                return True
        elif colour == "white":
            if point.colour == "black":
                return True


#-------------------main program-----------------
cb = board()
cb.setup()
#cb.display()
turn = "W"
print("Welcome to chess on python! White pieces are uppercase while black pieces are lowercase" + "\n" + "To avoid confusion, knights are represented as H or h ")
print()

while True:
    mate = False
    check = False
    for i in range(len(cb.board)):
        for item in cb.board[i]:
            if item != ".":
                item.updatemove()
            
                #print(item.moveable)
    for i in range(len(cb.board)):
        for item in cb.board[i]:
            if item != ".":
                if item.Icon.upper() == "K":
                    if item.kingcheck() == False:
                        mate = True 
                    elif item.check == True:
                        check = True
                    
                        
                        
    cb.display()
    if mate == True:
        print()
        print("GGWP, a checkmate occurred")
        break
        
    target = None
    moveflag = False
    print()
    if turn == "W":
        print("white to move \n")
    else:
        print("black to move \n")
    if check == True:
        move = input("Warning: Your king is in check, your moves are limited(eg. A2): ")
    else:
        move = input("enter the position of the piece you wanna move (eg. A2). To castle, select your king: ")
        while True:
            checks = "ABCDEFGH"
            checks2 = "12345678"
            if len(move) == 2 and move[0].upper() in checks and move[1] in checks2:
                break
            else:
                move = input("enter a valid position of the piece you wanna move (eg. A2): ")

                
    reverse = "76543210"
    row = "ABCDEFGH"
    pos1 = move[0].upper() + reverse[int(move[1]) - 1]
    pos1 = pos1[::-1]
    current = pos1[0] + str(row.index(pos1[1]))
    
    for item in cb.board:
        for stuff in item:
            if stuff != "." and ((stuff.colour == "white" and turn == "W") or (stuff.colour == "black" and turn == "B")):
                if stuff.currentlocation == pos1:
                    moveflag = True
                    target = stuff
                    #print(stuff.moveable)
                    #print(stuff.Icon)
                    break
    
    if moveflag == True:
        #print(target.moveable)
        move2 = input("Enter where you wanna move to " +"\n" + "(press space to go change the piece you want to move) " + "\n" + "short castle is OO, long castle is OOO: ")
        
        while True:
            if move2 != " " and move2 != "OOO" and move2 != "OO":
                old = ""
                pos2 = move2[0].upper() + reverse[int(move2[1]) - 1]
                pos2 = pos2[::-1]
                #print(pos2)
                mate2 = False
                if pos2 in target.moveable:
                    temp = None
                    if cb.board[int(pos2[0])][row.index(pos2[1])] != ".":
                        temp = cb.board[int(pos2[0])][row.index(pos2[1])]
                        old = target.currentlocation
                        cb.board[int(pos2[0])][row.index(pos2[1])].currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = target
                    cb.board[int(current[0])][int(current[1])] = "."
                    target.currentlocation = pos2
                    for i in range(len(cb.board)):
                        for item in cb.board[i]:
                            if item != ".":
                                item.updatemove()
                    for i in range(len(cb.board)):
                        for item in cb.board[i]:
                            if item != ".":
                                if item.Icon.upper() == "K" and item.colour == target.colour:
                                    
                                    #print(target)
                                    if item.kingcheck2() == False:
                                        cb.board[int(current[0])][int(current[1])] = target
                                        if temp != None:
                                            cb.board[int(pos2[0])][row.index(pos2[1])] = temp
                                            cb.board[int(pos2[0])][row.index(pos2[1])].currentlocation = pos2
                                        else:
                                            cb.board[int(pos2[0])][row.index(pos2[1])] = "."
                                        cb.board[int(current[0])][int(current[1])].currentlocation = old
                                       
                                       
                                        break
                                    
                                    else:
                                        cb.board[int(current[0])][int(current[1])] = target
                                        if temp != None:
                                            cb.board[int(pos2[0])][row.index(pos2[1])] = temp
                                            cb.board[int(pos2[0])][row.index(pos2[1])].currentlocation = pos2
                                        else:
                                            cb.board[int(pos2[0])][row.index(pos2[1])] = "."
                                        cb.board[int(current[0])][int(current[1])].currentlocation == old
                                        for i in range(len(cb.board)):
                                            for item in cb.board[i]:
                                                if item != ".":
                                                    item.updatemove()
                                        
                                        mate2 = True
                                        break
                    if mate2 == True:
                        move2 = input("The move is not legal/invalid due to a check. Enter another move: ")
                    else:
                        break
                else:
                    move2 = input("The move is not legal/invalid. Enter another move: ")
            else:
                break
        
        if move2 != " " and move2 != "OO" and move2 != "OOO":       
            
            if cb.board[int(pos2[0])][row.index(pos2[1])] != ".":
                cb.board[int(pos2[0])][row.index(pos2[1])].currentlocation = None
            cb.board[int(pos2[0])][row.index(pos2[1])] = target
            cb.board[int(current[0])][int(current[1])] = "."
            
            if target.Icon == "P" and turn == "W":
                if cb.board[int(pos2[0]) + 1][row.index(pos2[1])] != ".":
                    if cb.board[int(pos2[0]) + 1][row.index(pos2[1])].Icon == "p" and cb.board[int(pos2[0]) + 1][row.index(pos2[1])].en == True:
                        cb.board[int(pos2[0]) + 1][row.index(pos2[1])].currentlocation = None
                        cb.board[int(pos2[0]) + 1][row.index(pos2[1])] = "."
            
            elif target.Icon == "p" and turn == "B":
                if cb.board[int(pos2[0]) - 1][row.index(pos2[1])] != ".":
                    if cb.board[int(pos2[0]) - 1][row.index(pos2[1])].Icon == "P" and cb.board[int(pos2[0]) - 1][row.index(pos2[1])].en == True:
                        cb.board[int(pos2[0]) - 1][row.index(pos2[1])].currentlocation = None
                        cb.board[int(pos2[0]) - 1][row.index(pos2[1])] = "."

            if turn == "B":
                for item in cb.board[3]:
                    if item != ".":
                        if item.Icon == "p":
                            item.en = False
            else:
                for item in cb.board[4]:
                    if item != ".":
                        if item.Icon == "P":
                                item.en = False   
            

            if turn == "B":
                for item in cb.board[3]:
                    if item == target:
                        if item.Icon == "p":
                            if item.FM == True:
                                item.en = True
            else:
                for item in cb.board[4]:
                    if item == target:
                        if item.Icon == "P":
                            if item.FM == True:
                                item.en = True
                    
            
            moveflag = False
            
            target.currentlocation = pos2
            #print(target.currentlocation)
           
            if target.Icon.upper() == "P" and target.FM == True:
                target.FM = False
            if target.Icon.upper() == "K" or target.Icon.upper() == "R":
                target.castle = False

            if turn == "W" and target.Icon.upper() == "P" and int(target.currentlocation[0]) == 0:
                convert = input("What do you want to promote your pawn to? \n (use the abbreviation of the piece(R H B Q): ")
                conversion = "RHBQ"
                while True:
                    if len(convert) == 1 and convert.upper() in conversion:
                        break
                    else:
                        convert = input("invalid input, enter a valid input \n (use the abbreviation of the piece(R H B Q): ")

                if convert.upper() == "R":
                    new = rook("R",target.currentlocation,"white")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "H":
                    new = knight("H",target.currentlocation,"white")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "B":
                    new = bishop("B",target.currentlocation,"white")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "Q":
                    new = queen("Q",target.currentlocation,"white")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new

            if turn == "B" and target.Icon.upper() == "P" and int(target.currentlocation[0]) == 7:
                convert = input("What do you want to promote your pawn to? \n (use the abbreviation of the piece(R H B Q): ")
                conversion = "RHBQ"
                while True:
                    if len(convert) == 1 and convert.upper() in conversion:
                        break
                    else:
                        convert = input("invalid input, enter a valid input \n (use the abbreviation of the piece(R H B Q): ")

                if convert.upper() == "R":
                    new = rook("r",target.currentlocation,"black")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "H":
                    new = knight("h",target.currentlocation,"black")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "B":
                    new = bishop("b",target.currentlocation,"black")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                elif convert.upper() == "Q":
                    new = queen("q",target.currentlocation,"black")
                    target.currentlocation = None
                    cb.board[int(pos2[0])][row.index(pos2[1])] = new
                    
                    

                
                        
            if turn == "W":
                turn = "B"
            else:
                turn = "W"

        elif move2 == "OOO":
            target2 = cb.board[int(target.currentlocation[0])][0]
            cb.board[int(target.currentlocation[0])][2] = target
            cb.board[int(target.currentlocation[0])][3] = target2
            cb.board[int(target.currentlocation[0])][0] = "."
            cb.board[int(target.currentlocation[0])][4] = "."
            target.currentlocation = target.currentlocation[0] + colom[2]
            target2.currentlocation = target2.currentlocation[0] + colom[3]
            target.castle = False
            target2.castle = False

            if turn == "B":
                for item in cb.board[3]:
                    if item != ".":
                        if item.Icon == "p":
                            item.en = False
            else:
                for item in cb.board[4]:
                    if item != ".":
                        if item.Icon == "P":
                                item.en = False

            moveflag = False

            if turn == "W":
                turn = "B"
            else:
                turn = "W"

        elif move2 == "OO":
            target2 = cb.board[int(target.currentlocation[0])][7]
            cb.board[int(target.currentlocation[0])][6] = target
            cb.board[int(target.currentlocation[0])][5] = target2
            cb.board[int(target.currentlocation[0])][7] = "."
            cb.board[int(target.currentlocation[0])][4] = "."
            target.currentlocation = target.currentlocation[0] + colom[6]
            target2.currentlocation = target2.currentlocation[0] + colom[5]
            target.castle = False
            target2.castle = False

            if turn == "B":
                for item in cb.board[3]:
                    if item != ".":
                        if item.Icon == "p":
                            item.en = False
            else:
                for item in cb.board[4]:
                    if item != ".":
                        if item.Icon == "P":
                                item.en = False

            moveflag = False

            if turn == "W":
                turn = "B"
            else:
                turn = "W"

                
                        
    
    

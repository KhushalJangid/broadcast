import random

class User:
    def __init__(self):
        return

class File:
    def __init__(self,path,user:User):
        self.path = path
        self.user = user


class Room:
    
    members = []
    files = []
    limit = 0
    creator = None
    
    def __init__(self,creator,limit):
        id = random.randint(1,899999)+100000
        self.id = id
        self.creator = creator
        self.limit = limit
        
        return id
    
    def addFile(self,file:File):
        self.files.append(file)
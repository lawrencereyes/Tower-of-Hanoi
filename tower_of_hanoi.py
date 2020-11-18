import json
from resource.errors import errors, StateGetError, StateUpdateError, NewGameStartError, FromRodEmptyError, SameRodsError, LargerDiskOnTopError, WrongRodInputError, LogsUpdateError

class TowerOfHanoi():

    #Constructor
    def __init__(self):
        #Start a new game
        self.newGame()

    #Get the current state of the game
    def getState(self):
        try:
            f = open('resource/current_state.json', 'r')
            state_data = json.loads(f.read())

            return state_data
        except:
            print(errors['StateGetError'])
        finally:
            f.close()

    #Update the current state of the game
    def updateState(self, new_state):
        try:
            f = open('resource/current_state.json', 'w+')
            f.write(json.dumps(new_state))
        except:
            print(errors['StateUpdateError'])
        finally:
            f.close()

    # expected 'a' or 'b' or 'c' for both parameters
    def moveDisk(self, from_rod, to_rod):
        try:
            state = self.getState()

            #Check if the from_rod input is wrong
            if from_rod != "a" and from_rod != "b" and from_rod != "c":
                raise WrongRodInputError

            #Check if the to_rod input is wrong
            if to_rod != 'a' and to_rod != 'b' and to_rod != 'c':
                raise WrongRodInputError

            #List of all the disks in the from_rod
            from_rod_disks = state[from_rod]

            #List of all the disks in the to_rod
            to_rod_disks = state[to_rod]

            #Check if from_rod is empty, meaning we are not able to get a disk to move
            if not from_rod_disks:
                raise FromRodEmptyError 
            
            #Check if from_rod and to_rod are the same
            if from_rod == to_rod:
                raise SameRodsError
            
            #The top disk in the from_rod
            disk_to_move = state[from_rod][0]

            #Check that the to_rod is empty, if it is then just move the disk over without checking
            if not to_rod_disks:
                #Insert the top disk of the from_rod into the to_rod
                to_rod_disks.insert(0, disk_to_move)
                #Remove the top disk in the from_rod from the list
                from_rod_disks.pop(0)
                #Update the current state with the new state after the disk move
                self.updateState(state)

                self.log(message = "Disk #" + str(disk_to_move) + " has moved from rod '" + from_rod + "' to rod '" + to_rod + "'.\n")

            #If the to_rod is not empty, check that the disk_to_move is smaller than the top disk in to_rod
            elif to_rod_disks[0] < disk_to_move:
                raise LargerDiskOnTopError
            
            else:
                #Insert the top disk of the from_rod into the to_rod
                to_rod_disks.insert(0, disk_to_move)
                #Remove the top disk in the from_rod from the list
                from_rod_disks.pop(0)
                #Update the current state with the new state after the disk move
                self.updateState(state)

                self.log(message = "Disk #" + str(disk_to_move) + " is moving from rod '" + from_rod + "' to rod '" + to_rod + "'.\n")
        except FromRodEmptyError:
            #If from_rod is empty, meaning we are not able to get a disk to move
            return errors['FromRodEmptyError']
        except SameRodsError:
            #If from_rod and to_rod are the same
            return errors['SameRodsError']
        except WrongRodInputError:
            #If the from_rod or to_rod input is wrong
            return errors['WrongRodInputError']
        except LargerDiskOnTopError:
            #If the to_rod is not empty, check that the disk_to_move is smaller than the top disk in to_rod
            return errors['LargerDiskOnTopError']

    #Set the state of the game back to a new state
    def newGame(self):
        try:
            ns = open('resource/new_state.json', 'r')
            new_state_data = json.loads(ns.read())

            f = open('resource/current_state.json', 'w+')
            f.write(json.dumps(new_state_data))

            log = open('resource/game_logs.txt', 'w+')
            log.write('')
        except:
            print(errors['NewGameStartError'])
        finally:
            ns.close()
            f.close()
            log.close()

    def restart(self):
        self.newGame()

    def log(self, message):
        try:
            f = open('resource/game_logs.txt', 'a+')
            f.write(message)
        except:
            print(errors['LogsUpdateError'])
        finally:
            f.close()

#Manual Test
# g = TowerOfHanoi()

# g.newGame()
# print(g.getState())
# g.moveDisk('a','b')
# print(g.getState())
# g.moveDisk('a','c')
# print(g.getState())
# g.moveDisk('b','c')
# print(g.getState())
# g.moveDisk('a','b')
# print(g.getState())
# g.moveDisk('c','a')
# print(g.getState())
# g.moveDisk('c','b')
# print(g.getState())
# g.moveDisk('a','b')
# print(g.getState())
# g.moveDisk('a','c')
# print(g.getState())
# g.moveDisk('b','c')
# print(g.getState())
# g.moveDisk('b','a')
# print(g.getState())
# g.moveDisk('c','a')
# print(g.getState())
# g.moveDisk('b','c')
# print(g.getState())
# g.moveDisk('a','b')
# print(g.getState())
# g.moveDisk('a','c')
# print(g.getState())
# g.moveDisk('b','c')
# print(g.getState())
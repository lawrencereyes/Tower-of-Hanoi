class StateGetError(Exception):
    pass

class StateUpdateError(Exception):
    pass

class NewGameStartError(Exception):
    pass

class FromRodEmptyError(Exception):
    pass

class SameRodsError(Exception):
    pass

class LargerDiskOnTopError(Exception):
    pass

class WrongRodInputError(Exception):
    pass

class LogsUpdateError(Exception):
    pass

errors = {
    "StateGetError": {
        "message": "Not able to get the state of the game",
        "status": 500
    },
     "StateUpdateError": {
         "message": "Not able to update the state of the game",
         "status": 500
     },
     "NewGameStartError": {
         "message": "Not able to get the start a new game",
         "status": 500
     },
     "FromRodEmptyError": {
         "message": "The from_rod you is empty",
         "status": 400
     },
     "SameRodsError": {
         "message": "The from_rod and to_rod cannot be the same",
         "status": 400
     },
    "LargerDiskOnTopError": {
         "message": "You are only allowed to put a smaller disk on top of another disk",
         "status": 400
     },
     "WrongRodInputError": {
         "message": "The rod input is wrong. The only available options are 'a', 'b' or 'c'",
         "status": 400
     },
     "LogsUpdateError": {
         "message": "The logs were not updated",
         "status": 500
     },
}
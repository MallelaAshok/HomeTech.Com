from enum import Enum
import json


class ResultType(Enum):
    SUCCESS="SUCCESS"
    WORNING="WORNING"
    ERROR="ERROR"
    NONE="NONE"
    
def CreateAPIResult(ResultType,ErrorCode,ErrorDescription,ResultData): 
    ResultDict={"ResultType":ResultType,
                "ErrorCode":ErrorCode,
                "ErrorDescription":ErrorDescription,
                "ResultData":ResultData
                } 
    return json.dumps(ResultDict)
            
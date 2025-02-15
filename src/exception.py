import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logger import logging


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # its store all info about the exception like where and why occur this exception.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    
## up function is required when my exception is occurred then call this function to print error details.

## now create custom exception class

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys, *args):
        super().__init__(error_message, *args)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    


if __name__=="__main__":
    try:
        a=1/0
    except Exception as ex:
        logging.info("DIvided by zero error")
        raise CustomException(ex, sys)
        
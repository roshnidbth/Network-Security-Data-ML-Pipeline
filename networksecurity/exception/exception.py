
# Custom Exception = normal error ko capture karke
# uska message + exact file + exact line number provide karna.

import sys                              # system / exception details
from networksecurity.logging import logger  # project logger

class NetworkSecurityException(Exception):  # custom exception
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message          # store error message
        _,_,exc_tb = error_details.exc_info()       # get traceback

        self.lineno=exc_tb.tb_lineno                # error line number
        self.file_name=exc_tb.tb_frame.f_code.co_filename  # error file name

    def __str__(self):                              # custom error display
        return "Error occured in python script name [{0}] line number [{1}] error message [{2]}".format(
            self.file_name,                         # file
            self.lineno,                            # line
            str(self.error_message)                 # error
        )

if __name__=='__main__':                            # run directly
    try:                                            # try risky code
        logger.logging.info("Enter the try block")  # log execution
        a=1/0                                       # error occurs
        print("This will not be printed",a)

    except Exception as e:                          # catch error
        raise NetworkSecurityException(e,sys)       # raise custom error

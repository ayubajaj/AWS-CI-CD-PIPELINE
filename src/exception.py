import sys
from src.logger import logging
def err_message_detail(error, detail: sys):
    _, _, exc_tb = detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred in script: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = err_message_detail(error_message, detail=error_detail)

    def __str__(self):
        return self.error_message


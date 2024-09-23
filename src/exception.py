import sys

def error_message_detail(error,error_message:sys):
    pass_,_,exc_tab=error_message.exc_info()

    error_message="Error occured in [{0}] line number [{1}] error_message [{2}] ".formta(
        exc_tab.tb_frame.f_code.co_filename,exc_tab.tb_lineno,str(error)
    )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
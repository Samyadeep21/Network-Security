import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class for Network Security project
        
        Args:
            error_message: Error message string
            error_detail: sys module to extract traceback info
        """
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys) -> str:
        """
        Extract detailed error information including file name and line number
        
        Returns:
            Formatted error message with file and line details
        """
        _, _, exc_tb = error_detail.exc_info()
        
        # Get the frame where exception occurred
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        
        error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return NetworkSecurityException.__name__.__str__()

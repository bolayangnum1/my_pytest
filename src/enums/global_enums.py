from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'RECEIVED STATUS CODE IS NOT equal TO EXPECTED.'
    WRONG_ELEMENT_COUNT = 'NUMBER OF ITEMS IS NOT equal TO EXPECTED.'

"""
Determines a question and outputs the answer
"""

# pylint: disable= too-few-public-methods
#This is only used by main. It doesn't need a public method
class QA(object):
    """Performs anyalysis on question"""
    def __init__(self, question, answer):
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer

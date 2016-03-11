"""
This holds a list of question and many interactions involving those questions
"""
import time
from datetime import datetime
import difflib
import getpass
from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answers import fibonacci_sequence, pi_func, convert, check_dictionary,\
    shape_checker_2, alphabet_checker, polynomial_checker, sin_calculator
from source.git_utils import is_file_in_repo, get_git_file_info,\
    get_file_info, get_repo_branch, get_repo_url

# pylint: disable= bare-except
# Because if it reaches the except, it will do something
# pylint: disable= useless-else-on-loop
# I can't fix this without breaking the program
# pylint: disable= too-many-return-statements
# Because it needs this many return statements
# pylint: disable= too-many-branches
# Because it needs this many branches
# pylint: disable= too-many-statements
# Because it needs this many statements


NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    """Class used for entire project with main"""

    def __init__(self, filename='Log_file.txt'):
        self.fileout = open(filename, 'w')
        self.fileout.close()
        self.fileout = open(filename, 'a')

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Please", "Open", "Do", "Is"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ':
                QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it': QA('What time is it',
                                  'The current time is :' +
                                  datetime.utcnow().strftime("%m-%d-%Y %H:%M")),
            'What is the digit of fibonacci':
                QA('What is the digit of fibonacci', fibonacci_sequence),
            'What is the digit of pi':
                QA('What is the digit of pi', pi_func),
            'Please clear memory':
                QA('Please clear memory', self.clear),
            'Open the door hal':
                QA('Open the door hal',
                   'I\'m afraid I can\'t do that ' + getpass.getuser()),
            'What is the meaning of life':
                QA('What is the meaning of life', '42'),
            'Please make me a grilled cheese':
                QA('Please make me a grilled cheese', 'I can\'t make sandwiches'),
            'Do you have a facebook':
                QA('Do you have a facebook', 'No I have a life'),
            'What is myspace':
                QA('What is myspace', 'I\'m sorry. I have no information on trash'),
            'Do you eat':
                QA('Do you eat', 'No I am a computer'),
            'What polygon has sides':
                QA('What polygon has sides', shape_checker_2),
            'What is the letter of the alphabet':
                QA('What is the letter of the alphabet', alphabet_checker),
            'What degree of polynomial is x^ ':
                QA('What degree of polynomial is x^ ', polynomial_checker),
            'What is the sine of ':
                QA('What is the sine of ', sin_calculator),
            'Is the in the repo':
                QA('Is the in the repo', is_file_in_repo),
            'What is the status of':
                QA('What is the status of', get_git_file_info),
            'What is the deal with ':
                QA('What is the deal with ', get_file_info),
            'What branch is ':
                QA('What branch is ', get_repo_branch),
            'Where did come from':
                QA('Where did come from', get_repo_url)

        }
        self.last_question = None

    def ask(self, question=""):
        """Ask method for Interface object"""
        start = time.clock()
        self.fileout.write(str(question) + ': ')
        if not isinstance(question, str):
            self.fileout.write('Exception: Not a string' + '\n')
            self.last_question = None
            self.fileout.write(str(time.clock() - start) + '\n\n')
            raise Exception('Not A String!')
        if question[:8] == 'Convert ':
            token = question.split(' ')
            try:
                float(token[1])
            except:
                self.fileout.write('Cannot convert to float' + '\n')
                self.fileout.write(str(time.clock() - start) + '\n\n')
                return 'Cannot convert to float'
            convert_variable = convert(float(token[1]), token[2], token[4])
            self.fileout.write(str(convert_variable) + '\n')
            self.fileout.write(str(time.clock() - start) + '\n\n')
            return convert_variable
        if question[:7] == 'Define ':
            token2 = question.split(' ')
            check_dict_variable = check_dictionary(token2[1])
            self.fileout.write(check_dict_variable + '\n')
            self.fileout.write(str(time.clock() - start) + '\n\n')
            return check_dict_variable
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            self.fileout.write('No Answer' + '\n')
            self.fileout.write(str(time.clock() - start) + '\n\n')
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    if keyword[0] == '<' and keyword[-1] == '>':
                        file_name = keyword[1:len(keyword)-1]
                        args.append(file_name)
                    else:
                        args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        self.fileout.write(str(answer.value) + '\n')
                        self.fileout.write(str(time.clock() - start) + '\n\n')
                        return answer.value
                    else:
                        try:
                            arguments_variable = answer.function(*args)
                            self.fileout.write(str(arguments_variable) + '\n')
                            self.fileout.write(str(time.clock() - start) + '\n\n')
                            return arguments_variable
                        except Exception as ex:
                            self.fileout.write('Exception: ' + str(ex) + '\n')
                            self.fileout.write(str(time.clock() - start) + '\n\n')
                            print ex
                            raise ex

            else:
                self.fileout.write(UNKNOWN_QUESTION + '\n')
                self.fileout.write(str(time.clock() - start) + '\n\n')
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        """Teach method for Interface object"""
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        """Correct method for Interface object"""
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        """Add_answer method for Interface object"""
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def clear(self):
        """Clear method for Interface object"""
        self.question_answers = 0
        self.__init__()

"""
This is the functionality for job stories and requirements
"""
from nose2.events import Plugin

# pylint: disable= no-init
# Because the class doesn't need an init
# pylint: disable= no-self-use
# Because the program calls it and i don't
# pylint: disable= too-few-public-methods
# Because the user cannot directly access this
# pylint: disable= invalid-name
# Because i can't not use the global variable names for my dictionaries


class ReqTracer(Plugin):
    """This class is the functionality for requirements"""
    configSection = "req-tracer"

    def after_summary_report(self, dummy):
        """This adds data to the dictionary"""
        output_file = open("Project_Traces.txt", "w")
        output_file.write('\nRequirements\n************\n\n')
        for key, item in sorted(Requirements.items()):
            output_file.write(key + ' ')
            output_file.write(item.req_text)
            for func in item.func_name:
                output_file.write('\t' + func)
                output_file.write('\n')

        output_file.write('\nJob Stories\n***********\n\n')
        for job in Stories:
            output_file.write(job.JStext + '\n')
            for func in job.func_name:
                output_file.write('\t' + func)
                output_file.write('\n')




class RequirementTrace(object):
    """This adds data to the dictionary"""
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}


def requirements(req_list):
    """This adds data to the dictionary"""
    def wrapper(func):
        """This adds data to the dictionary"""
        def add_req_and_call(*args, **kwargs):
            """This adds data to the dictionary"""
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def job_story(job_stories):
    """This adds data to the dictionary"""
    def wrapper(func):
        """This adds data to the dictionary"""
        def add_story_and_call(*args, **kwargs):
            """This adds data to the dictionary"""
            for job in Stories:
                if job.JStext == job_stories:
                    job.func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_story_and_call

    return wrapper

Stories = []


class JSTrace(object):
    """This adds data to the dictionary"""
    JS_text = ""

    def __init__(self, text):
        self.JStext = text
        self.func_name = []

with open('Project_Requirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)

        elif line[0] == '*':
            job_id = line[1:].strip()
            Stories.append(JSTrace(job_id))

# -*- coding: UTF-8 -*-

class TaskFlowDelayed(Exception):

    def __init__(self, task, message=""):
        super(TaskFlowDelayed, self).__init__(message)
        self.task = task

class TaskFlowRefused(Exception):
    pass

class TaskFlowProcessing(Exception):
    pass

class TaskAlreadyApproved(Exception):
    pass

class TaskUnsubmitted(Exception):
    pass

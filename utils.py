import time


def get_str_set(job_status_dict, xx):
    union_set = job_status_dict.get('SUCCEEDED', set()).union(job_status_dict.get('SKIPPED', set()))
    return "[\"" + "\",\"".join(union_set) + "\"]"


def get_current_timekey():
    return time.strftime("%Y%m%d%H%M%S")

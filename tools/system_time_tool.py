import datetime
from langchain.agents import tool

@tool
def check_system_time(format:str="%Y-%m-%d %H:%M:%S"):
    """return the current time in your time zone a certain format"""
    current_time = datetime.datetime.now()
    return current_time.strftime(format) 
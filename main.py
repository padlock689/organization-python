box1 = ["Tool1", "Tool2", "Tool3", "Tool4", "Tool5"]

box2 = ["Tool6", "Tool7", "Tool8", "Tool9", "Tool10"]

box3 = ["Tool11", "Tool12", "Tool13", "Tool14", "Tool15"]

all_tools = box1 + box2 + box3

def find(tool_wanted):
    if tool_wanted in box1:
        return print("The tool wanted is in Box 1")
    elif tool_wanted in box2:
        return print("The tool wanted is in Box 2")
    elif tool_wanted in box3:
        return print("The tool wanted is in Box 3")
    else:
        return print("The tool you are looking for does not exist")

find("Tool")

box1 = ["Tool1", "Tool2", "Tool3", "Tool4", "Tool5"]

box2 = ["Tool6", "Tool7", "Tool8", "Tool9", "Tool10"]

box3 = ["Tool11", "Tool12", "Tool13", "Tool14", "Tool15"]

box4 = ["Tool420"]

box5 = ["Tool69"]

all_tools = box1 + box2 + box3

def find(tool_wanted):
    if tool_wanted in box1:
        return print("The tool wanted is in Box 1")
    elif tool_wanted in box2:
        return print("The tool wanted is in Box 2")
    elif tool_wanted in box3:
        return print("The tool wanted is in Box 3")
    elif tool_wanted in box4:
        return print("Ah ha Ah ha Ah ha, that tool don't exist braaa")
    elif tool_wanted in box5:
        return print("Niceeeeeeeee, but that tool doesn't exist")
    else:
        return print("The tool you are looking for does not exist")


# find("Tool1")

# find("Tool6")

# find("Tool11")

# find("Tool420")

# find("Tool69")

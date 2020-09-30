bl_info = {
    "name" : "Test Add-on",
    "blender" : (2, 80, 0),
    "category" : "Object"
}

def register():
    print("Registered")

def unregister():
    print("Unregistered")
# Blender Add-Ons

This folder will house all the Blender add-ons I make. Below is some documentation for writing basic add-ons.

## Example

```python
bl_info = {
    "name" : "Test Addon",
    "blender" : (2, 80, 0),
    "category" : "Object"

}

def register():
    # Execute something

def unregister():
    # Execute something
```

The above snippet is the simplest example of a Blender add-on.

* `bl_info`: A dictionary that has necessary metadeta
    - `name`: The name of the add-on (as shown in the Blender menu)
    - `blender`: The version of Blender it's meant for as a tuple
    - `category`: The category of Blender this add-on is for
* `register()`: The function that gets run when the add-on is enabled. Think of it as an `init` for the add-on
* `unregister()`: The function that gets run when the add-on is disabled
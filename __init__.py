"""
ANNOTATED EXAMPLE: __init__.py - How ComfyUI Discovers Your Nodes

This file is the entry point for your custom node package.
ComfyUI looks for this file in every subfolder of custom_nodes/
"""

# Import your node classes
from .example_node_annotated import ExampleTextNode


# ============================================================================
# REQUIRED: Node Class Mappings
# ============================================================================
# This dictionary tells ComfyUI:
# - What nodes you're providing
# - What they're called in the UI

NODE_CLASS_MAPPINGS = {
    # Key: The name that appears in the UI "Add Node" menu
    # Value: The actual Python class
    "Example Text Node": ExampleTextNode,

    # You can add more nodes here:
    # "Another Node": AnotherNodeClass,
}


# ============================================================================
# OPTIONAL: Display Name Mappings
# ============================================================================
# This provides user-friendly names for nodes
# If not provided, ComfyUI uses the keys from NODE_CLASS_MAPPINGS

NODE_DISPLAY_NAME_MAPPINGS = {
    # Key: Must match a key from NODE_CLASS_MAPPINGS
    # Value: Friendly name shown in UI
    "Example Text Node": "Example: Add Prefix",
}


# ============================================================================
# How ComfyUI Uses This File:
# ============================================================================
"""
1. ComfyUI scans custom_nodes/ for directories
2. For each directory, it tries to import __init__.py
3. It looks for NODE_CLASS_MAPPINGS in the module
4. Each class in the mapping gets registered
5. The nodes appear in the UI under their CATEGORY

If this file has errors, your entire node package won't load!
Check the console/logs if your nodes don't appear.
"""


# ============================================================================
# Optional: Package Initialization Code
# ============================================================================
# You can run code when the package loads:

print("***********************************************************************")
print("***********************************************************************")
print("***********************************************************************")
print("****                                                               ****")
print("****                                                               ****")
print("****       LOADING THE MOST IMPORTANT NODE IN THE WORLD!!!         ****")
print("****                                                               ****")
print("****                                                               ****")
print("***********************************************************************")
print("***********************************************************************")
print("***********************************************************************")



# Check dependencies, set up resources, etc.
# But keep it minimal - this runs every time ComfyUI starts!

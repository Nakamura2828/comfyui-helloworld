"""
ANNOTATED EXAMPLE: A Simple ComfyUI Node

This is a minimal example showing all required components.
We'll use this as a reference for building your hello world node.
"""


class ExampleTextNode:
    """
    A simple node that takes text input and adds a prefix to it.

    This demonstrates the minimum required structure for any ComfyUI node.
    """

    # ========================================================================
    # REQUIRED CLASS METHOD: Defines what appears in the UI
    # ========================================================================
    @classmethod
    def INPUT_TYPES(cls):
        """
        Tells ComfyUI what inputs this node accepts.

        Returns a dictionary with "required" and optionally "optional" keys.
        Each input needs:
        - A name (the key in the dict)
        - A type specification (tuple describing the input widget)
        """
        return {
            "required": {
                # First parameter: input name (shows in UI)
                # Second parameter: tuple of (widget_type, options_dict)
                "text": ("STRING", {
                    "default": "Hello",      # Default value
                    "multiline": False       # Single line input
                }),
                "prefix": ("STRING", {
                    "default": "Output: ",
                    "multiline": False
                }),
                "make_uppercase": ("BOOLEAN", {
                    "default": False  # Checkbox, unchecked by default
                }),
                "style": (["normal", "excited", "formal"],),
            },
            # Optional inputs go here (we don't have any for this example)
            # "optional": { ... }
        }

    # ========================================================================
    # REQUIRED CLASS ATTRIBUTES: Tell ComfyUI about outputs and behavior
    # ========================================================================

    # What type(s) does this node output? Must be a tuple, even for single output
    RETURN_TYPES = ("STRING",)

    # Optional: Names for the outputs (shows in UI when connecting)
    RETURN_NAMES = ("prefixed_text",)

    # The name of the method to call when node executes
    FUNCTION = "add_prefix"

    # Where this node appears in the "Add Node" menu
    CATEGORY = "tutorial/text"

    # ========================================================================
    # THE ACTUAL FUNCTION: This is where your logic goes
    # ========================================================================

    def add_prefix(self, text, prefix, make_uppercase=False):
        """
        This method is called when the node executes.

        IMPORTANT RULES:
        1. Parameter names MUST match the keys in INPUT_TYPES
        2. Must return a tuple (even for single value)
        3. Tuple length must match RETURN_TYPES length

        Args:
            text: The input text (from "text" input)
            prefix: The prefix to add (from "prefix" input)
            make_uppercase: Whether to uppercase the prefix (from "make_uppercase" input)

        Returns:
            tuple: A single-element tuple containing the result
        """
        # Apply uppercase if requested
        if make_uppercase:
            prefix = prefix.upper()

        # Apply style
        if style == "excited":
            text = text + "!!!"
        elif style == "formal":
            text = text + "."

        result = prefix + text

        # CRITICAL: Always return a tuple!
        return (result,)  # Note the comma - this makes it a tuple


# =============================================================================
# Additional Examples of Common Input Types
# =============================================================================

class InputTypesReference:
    """
    This class isn't meant to run - it's just showing common input types.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Text input
                "text": ("STRING", {"default": ""}),

                # Multiline text
                "long_text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),

                # Integer with range
                "number": ("INT", {
                    "default": 10,
                    "min": 0,
                    "max": 100,
                    "step": 1
                }),

                # Float
                "decimal": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.1
                }),

                # Boolean (checkbox)
                "enabled": ("BOOLEAN", {"default": True}),

                # Dropdown selection
                "mode": (["fast", "quality", "balanced"],),  # Note: tuple of list

                # Image input (from another node's output)
                "image": ("IMAGE",),  # No default - must be connected
            }
        }


# ============================================================================
# Key Takeaways:
# ============================================================================
"""
1. INPUT_TYPES is a class method that returns a dict
2. The function name matches the FUNCTION attribute
3. Function parameters match INPUT_TYPES keys exactly
4. Always return a tuple, even for single values
5. RETURN_TYPES must match your return tuple length
6. CATEGORY determines menu location (use "/" for submenus)
"""

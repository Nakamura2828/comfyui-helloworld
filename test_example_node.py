"""
Unit tests for ExampleTextNode

This demonstrates proper testing with assertions.
Run with: python test_example_node.py
"""
import inspect
from example_node_annotated import ExampleTextNode


def test_basic_prefix():
    """Test basic prefix functionality"""
    node = ExampleTextNode()

    # Test 1: Simple prefix
    result = node.add_prefix("World", "Hello ")
    assert result == ("Hello World",), f"Expected ('Hello World',) but got {result}"

    # Test 2: Your example
    result = node.add_prefix("cd", "ab")
    assert result == ("abcd",), f"Expected ('abcd',) but got {result}"

    print("✓ test_basic_prefix passed")


def test_uppercase_prefix():
    """Test uppercase prefix functionality"""
    node = ExampleTextNode()

    # Test 1: Prefix with uppercase enabled
    result = node.add_prefix("World", "Hello ", make_uppercase=True)
    assert result == ("HELLO World",), f"Expected ('HELLO World',) but got {result}"

    # Test 2: Prefix with uppercase explicitly disabled
    result = node.add_prefix("World", "Hello ", make_uppercase=False)
    assert result == ("Hello World",), f"Expected ('Hello World',) but got {result}"

    # Test 3: Default (should be False)
    result = node.add_prefix("World", "Hello ")
    assert result == ("Hello World",), f"Expected ('Hello World',) but got {result}"

    print("✓ test_uppercase_prefix passed")


def test_return_type():
    """Test that return value is always a tuple"""
    node = ExampleTextNode()

    result = node.add_prefix("test", "prefix")

    # Check it's a tuple
    assert isinstance(result, tuple), f"Return value should be tuple, got {type(result)}"

    # Check tuple has exactly one element
    assert len(result) == 1, f"Tuple should have 1 element, got {len(result)}"

    # Check the element is a string
    assert isinstance(result[0], str), f"First element should be string, got {type(result[0])}"

    print("✓ test_return_type passed")


def test_empty_strings():
    """Test edge case: empty strings"""
    node = ExampleTextNode()

    # Empty text
    result = node.add_prefix("", "Prefix: ")
    assert result == ("Prefix: ",), f"Expected ('Prefix: ',) but got {result}"

    # Empty prefix
    result = node.add_prefix("text", "")
    assert result == ("text",), f"Expected ('text',) but got {result}"

    # Both empty
    result = node.add_prefix("", "")
    assert result == ("",), f"Expected ('',) but got {result}"

    print("✓ test_empty_strings passed")


def test_special_characters():
    """Test that special characters work correctly"""
    node = ExampleTextNode()

    # Test with newlines
    result = node.add_prefix("World", "Hello\n")
    assert result == ("Hello\nWorld",), f"Newline handling failed: {result}"

    # Test with unicode
    result = node.add_prefix("🌍", "Hello ")
    assert result == ("Hello 🌍",), f"Unicode handling failed: {result}"

    # Test with special chars
    result = node.add_prefix("test", ">>>")
    assert result == (">>>test",), f"Special chars failed: {result}"

    print("✓ test_special_characters passed")


def test_input_types_structure():
    """Verify INPUT_TYPES returns correct structure"""
    input_types = ExampleTextNode.INPUT_TYPES()

    # Check it's a dict
    assert isinstance(input_types, dict), "INPUT_TYPES should return dict"

    # Check required key exists
    assert "required" in input_types, "INPUT_TYPES must have 'required' key"

    # Check our inputs are defined
    required = input_types["required"]
    assert "text" in required, "Missing 'text' input"
    assert "prefix" in required, "Missing 'prefix' input"
    assert "make_uppercase" in required, "Missing 'make_uppercase' input"

    print("✓ test_input_types_structure passed")

###############################################################################

def test_input_types_matches_function_signature():
    """
    Automatically verify that INPUT_TYPES keys match the actual function parameters.

    This catches the exact bug you had - adding a parameter without updating INPUT_TYPES!
    """
    node = ExampleTextNode()

    # Get the INPUT_TYPES configuration
    input_types = ExampleTextNode.INPUT_TYPES()
    all_inputs = set()

    # Collect all input names from INPUT_TYPES
    if "required" in input_types:
        all_inputs.update(input_types["required"].keys())
    if "optional" in input_types:
        all_inputs.update(input_types["optional"].keys())

    # Get the function that will be called
    function_name = ExampleTextNode.FUNCTION
    function = getattr(node, function_name)

    # Use inspect to get the function's parameters
    sig = inspect.signature(function)
    # Remove 'self' from parameters (it's implicit)
    function_params = set(sig.parameters.keys()) - {'self'}

    # Check they match
    missing_in_inputs = function_params - all_inputs
    extra_in_inputs = all_inputs - function_params

    assert not missing_in_inputs, \
        f"Function has parameters not in INPUT_TYPES: {missing_in_inputs}"
    assert not extra_in_inputs, \
        f"INPUT_TYPES has entries not in function parameters: {extra_in_inputs}"

    print(f"✓ INPUT_TYPES matches function signature")
    print(f"  Verified parameters: {sorted(function_params)}")


def test_function_defaults_match_input_types():
    """
    Check that function default values match INPUT_TYPES defaults.

    This is extra thorough - making sure defaults are consistent!
    """
    node = ExampleTextNode()
    input_types = ExampleTextNode.INPUT_TYPES()

    # Get function signature
    function = getattr(node, ExampleTextNode.FUNCTION)
    sig = inspect.signature(function)

    # Check each parameter
    for param_name, param in sig.parameters.items():
        if param_name == 'self':
            continue

        # Find this parameter in INPUT_TYPES
        found_in = None
        param_config = None

        if "required" in input_types and param_name in input_types["required"]:
            found_in = "required"
            param_config = input_types["required"][param_name]
        elif "optional" in input_types and param_name in input_types["optional"]:
            found_in = "optional"
            param_config = input_types["optional"][param_name]

        if found_in:
            # If it's required in INPUT_TYPES, function shouldn't have a default
            if found_in == "required":
                # Unless INPUT_TYPES provides a default
                if isinstance(param_config, tuple) and len(param_config) > 1:
                    if isinstance(param_config[1], dict) and "default" in param_config[1]:
                        # INPUT_TYPES has a default, function should too
                        input_default = param_config[1]["default"]
                        if param.default != inspect.Parameter.empty:
                            # Both have defaults - they should match types at least
                            assert type(param.default) == type(input_default), \
                                f"Parameter '{param_name}' has mismatched default types"

    print("✓ Function defaults are consistent with INPUT_TYPES")

###############################################################################

def run_all_tests():
    """Run all test functions"""
    print("Running tests for ExampleTextNode...\n")

    try:
        test_basic_prefix()
        test_uppercase_prefix()
        test_return_type()
        test_empty_strings()
        test_special_characters()
        test_input_types_structure()

        # more meta structural tests
        test_input_types_matches_function_signature()
        test_function_defaults_match_input_types()

        print("\n" + "="*50)
        print("✅ ALL TESTS PASSED!")
        print("="*50)
        return True

    except AssertionError as e:
        print("\n" + "="*50)
        print(f"❌ TEST FAILED: {e}")
        print("="*50)
        return False
    except Exception as e:
        print("\n" + "="*50)
        print(f"❌ UNEXPECTED ERROR: {e}")
        print("="*50)
        return False


if __name__ == "__main__":
    run_all_tests()

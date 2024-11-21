"""
A Python script demonstrating solutions to the "'charmap' codec can't encode character" error, commonly encountered in
Windows environments where the default encoding (e.g., charmap or cp1252) lacks full Unicode support.

This script provides examples for handling encoding issues with explanations and best practices.
"""

import sys

# Example input string containing a character that might not be supported by some encodings
text_with_unicode = "The price is 100₺."


def example_utf8_encoding():
    """
    Approach 1: Use UTF-8 encoding explicitly to handle Unicode characters.
    """
    print("\n--- Example 1: UTF-8 Encoding ---")
    try:
        with open("output_utf8.txt", "w", encoding="utf-8") as file:
            file.write(text_with_unicode)
        print("Successfully wrote the text using UTF-8 encoding to 'output_utf8.txt'.")
    except Exception as e:
        print(f"Error in UTF-8 encoding example: {e}")


def example_replace_unsupported_characters():
    """
    Approach 2: Replace unsupported characters with a placeholder (e.g., '?').
    """
    print("\n--- Example 2: Replace Unsupported Characters ---")
    try:
        encoded_text = text_with_unicode.encode("charmap", errors="replace").decode("charmap")
        print(f"Original text: {text_with_unicode}")
        print(f"Encoded text with unsupported characters replaced: {encoded_text}")
    except Exception as e:
        print(f"Error in replace unsupported characters example: {e}")


def example_check_default_encoding():
    """
    Approach 3: Check the default encoding in Python.
    """
    print("\n--- Example 3: Check and Change Default Encoding ---")
    try:
        print(f"Default system encoding: {sys.getdefaultencoding()}")
        print(f"Current console encoding: {sys.stdout.encoding}")
    except Exception as e:
        print(f"Error in check default encoding example: {e}")


if __name__ == "__main__":
    print("Running encoding examples...")
    example_utf8_encoding()
    example_replace_unsupported_characters()
    example_check_default_encoding()

    print("\nAll examples completed. Check 'output_utf8.txt' for results from Example 1.")

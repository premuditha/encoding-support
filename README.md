# Encoding Error Handling Examples

This project demonstrates various approaches to handle the common Python error:

```
'charmap' codec can't encode character '\u20ba' in position X
```

This error occurs when trying to encode Unicode characters that are not supported by the specified encoding. The script includes solutions for common scenarios, such as writing files, replacing unsupported characters, and configuring encoding settings.

**Note:** This error commonly encountered in Windows environments where the default encoding (e.g., charmap or cp1252) lacks full Unicode support.

## Features

- **UTF-8 Encoding**: Explicitly encode text using `utf-8` to support all Unicode characters.
- **Custom Character Replacement**: Replace unsupported characters with a specified character.
- **Check the Default Encoding**: Inspect and the Python default encoding.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/premuditha/encoding-support.git
   cd encoding_support
   ```

2. **Run the Script**:
   Execute the script with Python:
   ```bash
   python encoding_support.py
   ```

3. **Output**:
   - Example 1: Writes the text to a file (`output_utf8.txt`) using `utf-8` encoding.
   - Example 2: Replaces unsupported characters in the text.
   - Example 3: Shows how to inspect Python's default encoding.

## Prerequisites

- Python 3.7 or later.
## Contributing

Feel free to open issues or submit pull requests to enhance this project.

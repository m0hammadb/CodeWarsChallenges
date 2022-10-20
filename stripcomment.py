def strip_comments(inp,commentChars):
    lines = inp.split("\n")
    final = ""
    for i in range(len(lines)):
        currentLine = lines[i]
        for c in commentChars:
            codeIndex = currentLine.find(c)
            if(codeIndex != -1):
                currentLine = currentLine[:codeIndex]
        lines[i] = currentLine
        final += currentLine.rstrip()
        if(i < len(lines) - 1):
            final += "\n"
    return lines

strip_comments("a #b\nc\nd $e f g",["#","$"])
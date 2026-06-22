def isValidParenthesis(s: str) -> bool:
    # Write your code here
    pass
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

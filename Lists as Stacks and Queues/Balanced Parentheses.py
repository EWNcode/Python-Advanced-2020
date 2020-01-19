"""
Given a sequence consisting of parentheses, determine whether the expression is balanced. A sequence of parentheses is
balanced if every open parenthesis can be paired uniquely with a closed parenthesis that occurs after the former. Also,
the interval between them must be balanced. You will be given three types of parentheses: (, {, and [.
{[()]} - This is a balanced parenthesis.
{[(])} - This is not a balanced parenthesis.

"""

def balanced_parentheses(text):
    brackets = []
    opening_brackets = '[({'

    for ch in text:
        if ch in opening_brackets:
            brackets.append(ch)
        elif brackets:
            if ch == ')' and brackets[-1] == '(':
                brackets.pop()
            elif ch == ']' and brackets[-1] == '[':
                brackets.pop()
            elif ch == '}' and brackets[-1] == '{':
                brackets.pop()
            else:
                break
        else:
            return 'NO'
    if not brackets:
        return 'YES'
    return 'NO'

#tests = [
#        '{[()]}',
#        '{[(])}',
#        '{{[[(())]]}}',
#]
#
#[print(balanced_parentheses(text)) for text in tests]

print(balanced_parentheses(input()))
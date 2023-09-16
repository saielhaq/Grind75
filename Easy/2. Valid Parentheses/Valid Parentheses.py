class Solution:
    def isValid(self, s: str) -> bool:
        anca = []
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for bracket in s:
            if bracket in brackets:
                anca.append(bracket)
            elif len(anca) == 0 or bracket != brackets[anca.pop()]:
                return False

        return len(anca) == 0

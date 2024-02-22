class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split("/")
        stack = []
        for file in files:
            if file == "/":
                pass
            elif file == "..":
                if stack:
                    stack.pop()
            elif file == "":
                pass
            elif file == ".":
                pass
            else:
                stack.append(file)
        
        return "/"+"/".join(stack)
        
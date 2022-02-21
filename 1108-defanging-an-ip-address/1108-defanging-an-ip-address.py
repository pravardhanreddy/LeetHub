class Solution:
    def defangIPaddr(self, address: str) -> str:
        a,b,c,d = address.split(".")
        return a + "[.]" + b + "[.]" + c + "[.]" + d
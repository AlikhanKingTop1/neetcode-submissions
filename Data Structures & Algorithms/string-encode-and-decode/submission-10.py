class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            res = "~".join(strs)
            print(res)
            return str(res)
        else:
            return "pidaras"
    def decode(self, s: str) -> List[str]:
        if s != "pidaras":
            ult = s.split("~") 
            return ult
        else:
            return []
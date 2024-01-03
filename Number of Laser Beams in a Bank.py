class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
      res=0
      pc=0
      for i in bank:
          c=i.count("1")
          if(c==0):
              continue
          res=res+c*pc
          pc=c
      return res

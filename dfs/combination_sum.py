class Solution:  # https://leetcode-cn.com/problems/combination-sum/
    """
给定一个无重复candidates列表 一个目标int, 返回能够sum to target的无重复组合 (可以以任何顺序返回)
同一个数可以被重复选中无限次,
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []
        self.dfs(candidates=sorted(list(set(candidates))), start_idx=0, target=target, comb=[], result=result)
        return result

    # 组合的dfs一般是index based, 排列一般需要visited set
    def dfs(self, candidates, start_idx, target, comb, result):  # 找到以comb位前缀 sum to target的无重复组合
        if target == 0:
            result.append(list(comb))
            return
        for i in range(start_idx, len(candidates)):
            if candidates[i] > target:
                return
            comb.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], comb, result)
            comb.pop()

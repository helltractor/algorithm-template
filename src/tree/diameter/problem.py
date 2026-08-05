#!/usr/bin/env python3

from typing import List

from tree.diameter.template import TreeDiameter


class Solution:

    @staticmethod
    def lc1245_tree_diameter(edges: List[List[int]]) -> int:
        """
        link: https://leetcode.cn/problems/tree-diameter/
        """
        return TreeDiameter.treeDiameterDFS(edges)

    @staticmethod
    def lc543_diameter_of_binary_tree() -> int:
        """
        link: https://leetcode.cn/problems/diameter-of-binary-tree/
        """
        # 示例二叉树：1-2, 2-3, 2-4
        edges = [[1, 2], [2, 3], [2, 4]]
        return TreeDiameter.treeDiameterDFS(edges)

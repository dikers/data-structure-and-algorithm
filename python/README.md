



----------------------------
# 数组


|  难度   | 题目 |   完成情况 |
|  ----  | ----  | ----     |
| 简单  | [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) |     已完成  |


----------------------------
# 链表


|  难度   | 题目 |   完成情况 |
|  ----  | ----  | ----     |
| 简单  | [2. 两数之和](https://leetcode-cn.com/problems/add-two-numbers/) |     已完成  |
| 简单  | [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | -    |
| 简单  | [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)| -    |
| 简单  | [160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) | -    |
| 简单  | [725. 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts/)| -    |
| 中等  | [1669. 合并两个链表](https://leetcode-cn.com/problems/merge-in-between-linked-lists/)| -    |


| 困难  | [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | 已经完成    |


    
    
----------------------------
# 贪心算法


|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 中等  | [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/) |     已完成  |  二维数组排序 |
| 中等  | [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/) |     已完成  | 记录当前能到达的最远位置 [视频讲解](https://www.bilibili.com/video/BV1Sk4y1C7cD?from=search&seid=12972546831710779530) |

           

----------------------------
# 动态规划


|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 中等  | [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) | 已完成      | if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j]+1)  |
| 中等  | [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/submissions/) | 已完成      | dp[i] = max(nums[i], nums[i] + dp[i-1])  |
| 中等  | [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/) | 已完成      |   |
| 简单  | [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) |     已完成  |   |
| 中等  | [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/) |     已完成  |   |
| 中等  | [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/) |     已完成  |   |
| 中等  | [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) |     已完成  |   |
| 中等  | [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) |     已完成  |   |
| 中等  | [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/) |     已完成  |   |
| 中等  | [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/) |       |   |
| 中等  | [279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/submissions/) |     已完成  |   |
| 中等  | [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/) |     | dp[i]= max(dp[i-1], dp[i-2] + nums[i])  |
| 中等  | [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/) |     |   |
| 中等  | [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/) |     |   |
| 中等  | [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |     |   |
| 简单  | [674. 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/) |     已完成  |   |
| 困难  | [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/) |        |   |
| 中等  | [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/) |     已完成  |   |
| 中等  | [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/) |       |   |
| 中等  | [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/) |   已经完成    | dp[i] = min(dp[i], 1+dp[i-coin])  |
| 中等  | [377. 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv/) |       |   |
| 中等  | [474. 一和零](https://leetcode-cn.com/problems/ones-and-zeroes/) |       |   |
| 中等  | [139. 单词拆分](https://leetcode-cn.com/problems/word-break/) |       |   |
| 中等  | [376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/) | 已完成      |   |
| 困难  | [354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/) | 已完成      | 先排序，然后 最长递增子序列  |


### 双序列问题
|  难度   | 题目 |     |    要点    |
|  ----  | ----  | ----     |    ------    |
| 中等  | [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) | 已完成      |   |
| 困难  | [97. 交错字符串](https://leetcode-cn.com/problems/interleaving-string/) |        |   |
| 困难  | [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/) |        |   |
| 困难  | [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/) |        |   |




----------------------------
# 树

|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 中等  | [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) |    |  递归和栈两种实现 |
| 中等  | [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) |    |  递归和栈两种实现 |
| 中等  | [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) |    |  递归和栈两种实现 |
| 中等  | [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) |    |  队列实现 |
| 中等  | [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum) |    |   后续遍历、递归 |
| 中等  | [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) |    |   递归 |



| 中等  | [894. 所有可能的满二叉树](https://leetcode-cn.com/problems/all-possible-full-binary-trees/) |    |  [视频讲解](https://www.bilibili.com/video/BV1rW411Z7Sb)     |
| 困难  | [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/submissions/) |    |  [视频讲解](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/)     |
| 中等  | [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |    |       |
| 中等  | [894. 所有可能的满二叉树](https://leetcode-cn.com/problems/all-possible-full-binary-trees/) |    |  [视频讲解](https://www.bilibili.com/video/BV1rW411Z7Sb)     |


    
 

144
94
145
102
107
103
314


297
428
449
1008

106
889
426
    
    
----------------------------
# 回溯算法


|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 简单  | [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) |     已完成  |   |
| 简单  | [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) |     已完成  |   |
| 中等  | [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/) |     已完成  |  [视频讲解](https://leetcode-cn.com/problems/combination-sum/solution/gua-he-xin-shou-peng-you-de-shi-pin-jiang-jie-ru-h/) |
| 中等  | [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/) |     已完成  |   |
| 中等  | [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/) |     已完成  |   |
| 中等  | [46. 全排列](https://leetcode-cn.com/problems/permutations/) |     已完成  |   |
| 中等  | [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/) |     已完成  | 先排序   |
| 中等  | [77. 组合](https://leetcode-cn.com/problems/combinations/) |     已完成  |   注意结束条件   |
| 中等  | [78. 子集](https://leetcode-cn.com/problems/subsets/) |      |      |
| 中等  | [79. 单词搜索](https://leetcode-cn.com/problems/word-search/) |     已完成 |      |
| 中等  | [89. 格雷编码](https://leetcode-cn.com/problems/gray-code/) |       |   |
| 中等  | [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/) |      |      |
| 中等  | [93. 复原 IP 地址](https://leetcode-cn.com/problems/restore-ip-addresses/) |       |   |
| 中等  | [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/) |     已完成  |   |
| 中等  | [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/) |       |   |
| 简单  | [401. 二进制手表](https://leetcode-cn.com/problems/binary-watch/) |       |   |
| 难   | [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/) |    |   |
| 难   | [51. N 皇后](https://leetcode-cn.com/problems/n-queens/) |    |  [视频讲解](https://www.bilibili.com/video/BV1ZK411K7A8/?spm_id_from=autoNext)     |

           
 

        

----------------------------
# 排序      

|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 简单  | [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) |     已完成  |   |
| 简单  | [148. 排序链表](https://leetcode-cn.com/problems/sort-list/) |     已完成  |   |
| 简单  | [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) |     已完成  |   |


----------------------------
# 栈 队列
|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 简单  | [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) |     已完成  |  栈 |
| 简单  | [155. 最小栈](https://leetcode-cn.com/problems/min-stack/) |     已完成  |  用两个栈来实现 |

1381
1441
622



----------------------------
# BFS

102
111
127
207
210
490
505


----------------------------
# DFS

78
90
46
47
77
37
51
144





----------------------------
# 二分搜索


|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 简单  | [704. 二分查找](https://leetcode-cn.com/problems/binary-search/) |     已完成  |   |

4
278
410




----------------------------
# 滑动窗口

3
159
340
395
424

209
76
992
1248



----------------------------
# 设计类

LRU





----------------------------
# 二叉搜索树

230
236
235




----------------------------
# 单调栈 

|  难度   | 题目 |   完成情况 |    要点    |
|  ----  | ----  | ----     |    ------    |
| 简单  | [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/) |     已完成  |   |
| 中等  | [503. 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/) |      |   nums[i %n] |
| 中等  | [1019. 链表中的下一个更大节点](https://leetcode-cn.com/problems/next-greater-node-in-linked-list/) |      |   |
| 中等  | [739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/) |      | 保存index  |
| 中等  | [316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/) |      |    |
| 中等  | [1081. 不同字符的最小子序列](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/) |      |  same 316  |
| 中等  | [402. 移掉K位数字](https://leetcode-cn.com/problems/remove-k-digits/) |      |   |
| 困难  | [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) |      |   |
| 中等  | [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) |      |    |



----------------------------
# 单调队列

239
862
1425
1438
1696

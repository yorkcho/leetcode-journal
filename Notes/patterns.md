### H-Index
- array
- 釐清H Index的判斷方式，在list裡面操作，對於比大小的操作還要加強
- 因為忘記寫 for loop 整趟結束後要 return，這部分也是 h index 的重要環節

### 380. Insert Delete GetRandom O(1)
- hash table
- 讓新增、刪除的時間複雜度在 O(1)
- 可以用set來寫，不過為了處理第三個getRandom()，要用random必須要有list，所以解決方式是用一個dict+一個list同時紀錄元素

### roman to integer
- dict, string, math
- 釐清羅馬字母前後/左右影響”I”符號屬於加減，前者比後者如“IV”即要做減法，相對”VI”則是加法
- for a,b in zip(s, s[1:]) 來同時迭代兩個前後符號，最後者會被忽略，return 前要加上
- 或者，使用 for idx in range(0,len(s)-1) 比較id 與 idx+1，但要處理list out of range error

### 14. Longest Common Prefix
- string
- 使用sort讓第一個string與最後一個string，為相差最大兩者，找出兩者的共同prefix即為答案

### 167. Two Sum II - Input Array Is Sorted
- array, two pointers
- non-decreasing order, 唯一一組解，回傳的index為1-based indexing
- 因為有排序，往左代表減，往右代表加，設兩端指標朝中間搜尋

### 3sum
- two pointer, O(N^2)
- sort過後由小到大。主要的for loop中固定i，總和小於0就透過j往右，大於就靠j往左，
- 避免重複，在迴圈中檢查 i 的重複，j(或k)的重複，

### max depth of binary tree
- dfs？recursive
- 也可用數學公式解出，使用len(tree)開根號+1

### 100. Same Tree
- recursive解法最直接
- queue的用法要注意

### 290. Word Pattern
- 2 hash maps , 或 數學驗證方式（bijection）
- 檢查兩組字串長短是否一致

### 134. Gas Station
- Mid
- divide and conquer
- 專注在constraints，只有一個解，很重要。判斷是否通過false，回傳stop

### 49. Group Anagrams
- Mid, Hash map
- str 可以被sort，但是會回傳list
- 需要認知到 用sorted過的字串 作為 key ，來將str 分堆

### 238. Product of Array Except Self
- Mid, array
- 暴力破解、減法方式、不靠減法 prefix product + suffix product
- prefix product = array中在自己之前所有的相乘，suffix product相反，兩個相乘即是except self

### 209. Minimum Size Subarray Sum
- Mid, sliding window
- 注意無解時的回傳解答

### 11. Container With Most Water
- Mid, sliding windows
- min max函數使用
- 思考到，選左右兩端比較矮的來移動，不太容易

### 36. Valid Sudoku
- Mid, matrix
- 紀錄每個row, column ,box(一個3X3區塊)，上的1~9，出現與否
- box index的計算需要想一下

### 135. Candy
- array, greedy
- greedy，先順向搜索滿足條件，再反著搜索
- 注意python for迴圈的細節，如果 i=0，list[i-1]會相當於list[-1]（最後一個值）

### Happy Number
- 數學的cycle，整除法
- 重點1.計算數字每一位數的square加總, 2.認定/驗證無解的話一定都有cycle → 計算並檢查有無cycle
- 因為這種計算都有cycle，可採用快慢2 pointers方式，slow正常跑，fast每次都計算多一次，會追上slow的時候，檢查是否是happy number

### 1. Two sum
- hash table , 經典題
- 進行迴圈同時找減去後餘數是否有對應key

### 42. Trapping Rain Water
- hard, array, twopointer
- 要trap到水的條件就是兩邊要高。兩邊不斷比較大小。故要用two pointer

### 228. Summary Ranges
- range, easy
- 也是用two pointer好做

### 20. Valid Parentheses
- stack, easy
- bracket的palindrome，stack用法，遇上closed bracket就檢查一次

### 71. Simplify Path
- stack, medium
- ‘/’ 斜線不管幾條都視作一條，要想到用split來做

### 12. Integer to Roman
- hash map, medium,有一題roman to integer 延伸
- 建立一個map 數字從大到小的羅馬對應
- 從數字進行迴圈，讓數字去對應map。或從map進行迴圈，讓數字減去

### 151. Reverse Words in a String
- mid
- O(n)空間可以改善O(1)?

### 155. Min Stack
- stack
- stack中的每一個元素同時儲存當時最小值（stack會由上往下pop不會動到舊的值）

### 6. Zigzag Conversion
- list of list , medium
- 判定當下是row的頭還是尾來決定方向

### 2. Add Two Numbers
- linked list
- 反著加反著return，所以不用做reverse

### 21. Merge Two Sorted Lists
- linked list, easy

### 56. Merge Intervals
- List, Medium
- 三項：sort解決intervals忽大忽小、判定有無需合併interval、interval合併
- interval之間有交集的情況不好判定，可判定無交集情況，有交集則為else

### 138. Copy List with Random Pointer
- Hash table
- 做出old-new對應的hash table
- 第一次主要是將old-new對應，第二次迭代才更新next,random

### 3. Longest Substring Without Repeating Characters
- sliding windows/hash table
- 不重複的話適合用 set / hash table 來實作

### 28. Find the Index of the First Occurrence in a String
- easy
- string 內建函數 find() 就直接完成
- 其他方式如 KMP（Knuth–Morris–Prat）

# [Unrated] Doublets - 4412 

[문제 링크](https://www.acmicpc.net/problem/4412) 

### 성능 요약

메모리: 174076 KB, 시간: 1388 ms

### 분류

Empty

### 문제 설명

<p>A <em>Doublet</em> is a pair of words that differ in exactly one letter; for example, "booster" and "rooster" or "rooster" and "roaster" or "roaster" and "roasted".</p>

<p>You are given a dictionary of up to 25143 lower case words, not exceeding 16 letters each. You are then given a number of pairs of words. For each pair of words, find the shortest sequence of words that begins with the first word and ends with the second, such that each pair of adjacent words is a doublet. For example, if you were given the input pair "booster" and "roasted", a possible solution would be: ("booster", "rooster", "roaster", "roasted") provided that these words are all in the dictionary.</p>

### 입력 

 <p>Input consists of the dictionary followed by a number of word pairs. The dictionary consists of a number of words, one per line, and is terminated by an empty line. The pairs of input words follow; the words of each pair occur on a line separated by a space.</p>

### 출력 

 <p>For each input pair, print a set of lines starting with the first word and ending with the last. Each pair of adjacent lines must be a doublet. If there are several minimal solutions, any one will do. If there is no solution, print a line: "No solution." Leave a blank line between cases.</p>


"""
유효한 팰린드롬
- 주어진 문자열이 팰린드롬인지 확인하라. 대소묹를 구분하지 않으면, 영문자와 숫자만을 대상으로 한다.
"""

'''
첫번째 풀이
- 리스트로 변환
'''
# def isPalindrome(self, s : str) -> bool:
#     strs = []
#     for char in s:
#         if char.alnum():
#             strs.append(char.lower())
#
#     # 펠린드롬 여부 판별
#     while len(strs) > 1:
#         if strs.pop() != strs.pop(0):
#             return False
#
#     return True

'''
두번째 풀이
- 데크로 풀기
'''
# import collections, mypy
# def isPalindrome(self, s : str) -> bool:
#     # 자료형 데크로 선언
#     strs : Deque = collections.deque()
#
#     for char in s:
#         if char.alnum():
#             strs.append(char.lower())
#
#     # 펠린드롬 여부 판별
#     while len(strs) > 1:
#         if strs.pop() != strs.popleft():
#             return False
#     return True
'''
세번쨰 풀이
- 슬라이싱 사용
'''
import re
def isPalindrome(self, s : str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


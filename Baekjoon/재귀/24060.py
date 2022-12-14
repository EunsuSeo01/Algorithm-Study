# 알고리즘 수업 - 병합 정렬 1 : 실버 4
import sys

answer = []

A, K = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))


def merge_sort(unsorted_list):
    # 크기가 1이하면 반환
    if len(unsorted_list) == 1:
        return unsorted_list

    # 리스트를 2분할해서 각각을 재귀적으로 병합 정렬 실행
    mid = (len(unsorted_list) + 1) // 2
    left = merge_sort(unsorted_list[:mid])
    right = merge_sort(unsorted_list[mid:])

    i, j = 0, 0
    sorted_list = []

    # 경우에 따라 두 개의 리스트를 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            answer.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        answer.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        answer.append(right[j])
        j += 1
    return sorted_list


merge_sort(numbers)
if len(answer) >= K:
    print(answer[K - 1])
else:
    print(-1)

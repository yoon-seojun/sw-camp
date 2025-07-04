import numpy as np

arr1 = np.loadtxt('mars_base_main_parts-001.csv', delimiter=',')
arr2 = np.loadtxt('mars_base_main_parts-002.csv', delimiter=',')
arr3 = np.loadtxt('mars_base_main_parts-003.csv', delimiter=',')

parts = np.concatenate([arr1, arr2, arr3], axis=0)

means = np.mean(parts, axis=0)
print("각 항목의 평균값:", means)

# 평균값이 50보다 작은 열의 인덱스 추출
target_indices = np.where(means < 50)[0]
# 해당 열만 parts에서 추출
parts_to_work_on = parts[:, target_indices]
# 파일로 저장
np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',')
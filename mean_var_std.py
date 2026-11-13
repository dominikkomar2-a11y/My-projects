import numpy as np
def calculate(_list):
    array = np.array(_list)
    array = array.reshape(3, 3)
    mean_axis0 = np.mean(array, axis=0)
    mean_axis1 = np.mean(array, axis=1)
    mean = np.mean(array)
    variance_axis0 = np.var(array, axis=0)
    variance_axis1 = np.var(array, axis=1)
    variance = np.var(array)
    std_dev_axis0 = np.std(array, axis=0)
    std_dev_axis1 = np.std(array, axis=1)
    std_dev = np.std(array)
    max_axis0 = np.max(array, axis=0)
    max_axis1 = np.max(array, axis=1)
    max_value = np.max(array)
    min_axis0 = np.min(array, axis=0)
    min_axis1 = np.min(array, axis=1)
    min_value = np.min(array)
    sum_axis0 = np.sum(array, axis=0)
    sum_axis1 = np.sum(array, axis=1)
    sum_value = np.sum(array)
    dictionary = {
        'mean': [mean_axis0.tolist(), mean_axis1.tolist(), float(mean)],
        'variance': [variance_axis0.tolist(), variance_axis1.tolist(), float(variance)],
        'standard deviation': [std_dev_axis0.tolist(), std_dev_axis1.tolist(), float(std_dev)],
        'max': [max_axis0.tolist(), max_axis1.tolist(), float(max_value)],
        'min': [min_axis0.tolist(), min_axis1.tolist(), float(min_value)],
        'sum': [sum_axis0.tolist(), sum_axis1.tolist(), float(sum_value)]
    }
    return dictionary
print(calculate([0,1,2,3,4,5,6,7,8]))

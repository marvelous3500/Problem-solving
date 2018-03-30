find the absolute dffent of two sensor value in the giving example 
sensor_A = [8, 5, 8, 18, 20] sensor_B = [5, 3, 2, 16, 15] example  8 - 5 = 3 

def get_sum_of_sensor_values(sensor_a, sensor_b, length):
    total_deferent_sensor_value = 0

    if length < 0:
        return total_deferent_sensor_value

    total_deferent_sensor_value += sensor_a[length] - sensor_b[length]
    total_deferent_sensor_value += get_sum_of_sensor_values(sensor_A, sensor_B, length - 1)

    return total_deferent_sensor_value

sensor_A = [8, 5, 8, 18, 20]
sensor_B = [5, 3, 2, 16, 15]
size_of_array = len(sensor_A)

print(get_sum_of_sensor_values(sensor_A, sensor_B, size_of_array - 1))
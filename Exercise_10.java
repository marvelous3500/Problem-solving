public class SumOfSensorValues {

    public static int getSumOfSensorValues(int sensorA[], int sensorB[]) {
        return getSumOfSensorValues(sensorA, sensorB, sensorA.length - 1);
    }

    private static int getSumOfSensorValues(int sensorA[], int sensorB[], int length) {
        int sumOfValues = 0;
        
        if (length < 0) return sumOfValues;

        sumOfValues += sensorA[length] - sensorB[length];
        sumOfValues += getSumOfSensorValues(sensorA, sensorB, --length);

        return sumOfValues;
    }


    public static void main(String... args) {
        int[] array = {8, 5, 8, 18, 20};
        int[] array2 = {5, 3, 2, 16, 15};

        System.out.print(getSumOfSensorValues(array, array2));
    }
}
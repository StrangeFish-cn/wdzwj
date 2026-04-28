package com.example.practice.ex04;

public class MaxArrayExercise {
    public static void main(String[] args) {
        int[] numbers = {3, 8, 2, 15, 6};
        int max = numbers[0];

        for (int number : numbers) {
            if (number > max) {
                max = number;
            }
        }

        System.out.println("Task: find max in array");
        System.out.println("max = " + max);
    }
}

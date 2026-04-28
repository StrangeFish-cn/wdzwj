package com.example.practice.ex09;

public class MethodExercise {
    public static void main(String[] args) {
        int result = square(6);

        System.out.println("Task: simple method extraction");
        System.out.println("square = " + result);
    }

    public static int square(int number) {
        return number * number;
    }
}

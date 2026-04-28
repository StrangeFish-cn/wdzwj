package com.example.practice.ex07;

import java.util.List;

public class AverageScoreExercise {
    public static void main(String[] args) {
        List<Integer> scores = List.of(88, 92, 79, 95);
        int total = 0;

        for (int score : scores) {
            total += score;
        }

        double average = (double) total / scores.size();
        System.out.println("Task: average scores with List");
        System.out.println("average = " + average);
    }
}

package com.example.practice.ex08;

import java.util.HashMap;
import java.util.Map;

public class WordCountExercise {
    public static void main(String[] args) {
        String[] words = {"java", "sql", "java", "python", "java", "sql"};
        Map<String, Integer> counts = new HashMap<>();

        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0) + 1);
        }

        System.out.println("Task: count words with Map");
        System.out.println(counts);
    }
}

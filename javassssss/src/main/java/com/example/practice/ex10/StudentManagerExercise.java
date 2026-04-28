package com.example.practice.ex10;

import java.util.ArrayList;
import java.util.List;

public class StudentManagerExercise {
    public static void main(String[] args) {
        List<String> students = new ArrayList<>();
        students.add("Alice");
        students.add("Bob");
        students.add("Cindy");

        System.out.println("Task: mini student manager");
        for (String student : students) {
            System.out.println(student);
        }
    }
}

package com.example.practice.ex06;

public class StudentRecordExercise {
    public static void main(String[] args) {
        Student student = new Student("Alice", 95);

        System.out.println("Task: build a student object");
        System.out.println(student.name() + " -> " + student.score());
    }

    record Student(String name, int score) {
    }
}

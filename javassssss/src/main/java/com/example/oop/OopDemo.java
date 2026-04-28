package com.example.oop;

public class OopDemo {
    public static void run() {
        Student student = new Student("Alice", 20);
        student.study("Java");
        System.out.println("[oop] student name = " + student.getName());
        System.out.println("[oop] student age = " + student.getAge());
    }
}

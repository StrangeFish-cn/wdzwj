package com.example.oop;

public class Student {
    private final String name;
    private final int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void study(String subject) {
        System.out.println("[oop] " + name + " is studying " + subject);
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

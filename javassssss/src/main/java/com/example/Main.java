package com.example;

import com.example.basic.BasicDemo;
import com.example.collections.CollectionsDemo;
import com.example.oop.OopDemo;
import com.example.practice.PracticeDemo;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Java Learning Starter ===");
        BasicDemo.run();
        System.out.println();
        OopDemo.run();
        System.out.println();
        CollectionsDemo.run();
        System.out.println();
        PracticeDemo.show();
    }
}

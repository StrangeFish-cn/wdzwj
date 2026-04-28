package com.example.basic;

public class BasicDemo {
    public static void run() {
        int age = 18;
        double score = 95.5;
        boolean passed = score >= 60;

        System.out.println("[basic] age = " + age);
        System.out.println("[basic] score = " + score);
        System.out.println("[basic] passed = " + passed);

        for (int i = 1; i <= 3; i++) {
            System.out.println("[basic] loop i = " + i);
        }
    }
}

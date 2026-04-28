package com.example.collections;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CollectionsDemo {
    public static void run() {
        List<String> topics = new ArrayList<>();
        topics.add("Variables and types");
        topics.add("Conditions and loops");
        topics.add("Object-oriented programming");

        System.out.println("[collections] topics:");
        for (String topic : topics) {
            System.out.println("  - " + topic);
        }

        Map<String, Integer> scores = new HashMap<>();
        scores.put("Java", 90);
        scores.put("SQL", 80);
        System.out.println("[collections] Java score = " + scores.get("Java"));
    }
}

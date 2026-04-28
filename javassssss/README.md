# Java Learning Starter

## Structure

```
javassssss/
  src/main/java/com/example/
    Main.java
    basic/BasicDemo.java
    oop/OopDemo.java
    oop/Student.java
    collections/CollectionsDemo.java
    practice/PracticeDemo.java
    practice/ex01/... to ex10/...
```

## Learning Path

1. `basic`: variables, operators, if/for
2. `oop`: class, object, encapsulation, method
3. `collections`: List, Map, foreach
4. `practice`: 10 small exercises from easy to medium

## Java 21 Notes

- Current project target: Java 21
- Example modern syntax included: `record`, `List.of()`

## Run (PowerShell)

Compile all Java files:

```powershell
javac -d out (Get-ChildItem -Recurse -Path "src/main/java" -Filter "*.java" | ForEach-Object { $_.FullName })
```

Run:

```powershell
java -cp out com.example.Main
```

Run a single exercise:

```powershell
java -cp out com.example.practice.ex06.StudentRecordExercise
```

## Suggested Order

1. Finish `basic`
2. Understand `oop`
3. Practice `collections`
4. Solve `practice/ex01` to `practice/ex10`

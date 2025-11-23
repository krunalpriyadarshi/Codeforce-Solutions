# 📘 Learn Gradle

## My findings

- Gradle Build = Gradle Project
- gradle build file -> the instruction manual to build application
- .java files -> actual application
- `gradle` V/S `gradlew`
  - `gradle` is for System-wide command.
  - `gradlew` AKA `gradle wrapper`. Each project can have its own gradle version. Used in collaborative project, to avoid issues or version mismatch.

> **⚠️ NOTE:** Always use the Gradle wrapper!

## build.gradle file

It is BUILD SCRIPT.
When you run `gradle` command. Output is visible in Configure project section inside the terminal.

### Gradle tasks

Tasks are individual jobs that Gradle can run.

- **Built-in** tasks come with plugins. Run them by `gradle taskName`

  - ```gradle
    plugins {
        id 'java'
    }

    // Now you automatically have these tasks available:
    // - compileJava
    // - test  
    // - clean
    // - jar
    // - build
    ```

- **Custom tasks**

  - ```gradle
    task sayHello {
        doLast {
            println "Hello from Gradle!"
        }
    }
    ```

### Plugins

Plugins are additional resource. It adds extra functionality and capabilities.

```gradle
plugins{
    id 'base'   // core-Gradle plugins; clean, build, zip task etc,.
    id 'java'   // compileJava, test tasks
    id 'org.springframework.boot'  // BootRun, dependency management task
    id 'jacoco' // code coverage plugin; test report
    id 'application'    // Core-gradle plugin; for CLI and server apps.
}

// Run `gradle tasks` to check new tasks.
```

## Gradle

`gradle init` will automatically install gradle wrapper.
If project uses different version than `.gradlew build` will use right version.

`./gradlew -v` To check Gradle version

### Project layout

#### (Auto-generated)
- `.gradle` Gradle's private workspace and cache directory
- `gradle` Gradle system files
- `gradlew` Gradle runner (Mac/ Linux)
- `gradlew.bat` Gradle runner (Windows)
- `build` Generated files from `.gradlew build` command

#### (Configuration files)
- `build.gradle` Main build configuration
- `gradle.properties` Project specific properties
- `settings.gradle` Project setting

`./gradlew tasks` - Shows only tasks who are part of atleast one Group
`./gradlew tasks --all` - Shows all tasks


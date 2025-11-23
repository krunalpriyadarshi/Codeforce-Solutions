# 📘 Learn Gradle

## My findings

- Gradle Build = Gradle Project
- gradle build file -> the instruction manual to build application
- .java files -> actual application

:::
*`gradle` command is for whole device
`gradlew` command is for specific project since different versions of gradle can be used my machine but project must be worked on by same version.*
:::

## build.gradle file

It is BUILD SCRIPT.
When you run `gradle` command. Output is visible in Configure project section inside the terminal.

### Gradle tasks

Tasks are individual jobs that Gradle can run.

- Built-in tasks come with plugins. Run them by `gradle taskName`

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

- Custom tasks.

  - ```gradle
    task sayHello {
        doLast {
            println "Hello from Gradle!"
        }
    }
    ```


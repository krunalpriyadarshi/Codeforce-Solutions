# 📘 Learn Gradle

## Project layout

- `.gradle` Gradle's private workspace and cache directory
- `gradle` Gradle system files
- `gradlew` Gradle runner (Mac/ Linux)
- `gradlew.bat` Gradle runner (Windows)
- `build` Generated files from `.gradlew build` command
- `build.gradle` Main build configuration
- `gradle.properties` Project specific properties
- `settings.gradle` Project setting

> Always use the Gradle wrapper!

- `gradle` v/s `gradlew`
  - `gradle` is for System-wide command.
  - `gradlew` AKA `gradle wrapper`. Each project can have its own gradle version. Used in collaborative project, to avoid issues or version mismatch.

> Gradle supports `Groovey` and `Kotlin` DSL (Domain Specific Language).

NOTE: In Gradle, the order matters inside `build.gradle` file. `plugin {}` must come first, before any other statements like `description`, `version`, `group`, or custom code.

### Groovey V/S Kotlin

### Groovey

- Groovey is JVM language hence all java-library can be used.
- It is loosely type language where brackets and pre-defined variable is optional.
- Less boilerplate code.

#### Closure in Groovy

A closure is similar as lambda function. You can also call it by using call() method.

- def lambda = { println("...processing...) }
  - lambda()
  - lambda.call()
- def lambda = { int num -> return num * 2 }
  - lambda(10)
  - lambda.call(10)
- def lambda = { a, b -> return a + b }
  - lambda(2, 4)
  - lambda.call(2, 4)

⚠️ ⚠️ TODO: Learn variables, strings, collections in groovy!!

### Kotlin

- Kotlin is also JVM labguage.
- It is statically typed language. And more IDE support.
- Kotlin uses lambda functions instead of closures.

## Build Lifecycle phases

1. **Initialization** - What projects take part in build.
2. **Configuration** - Executes Build-script and Maps model for project.
3. **Execution** - Execute project based on command.

### Commands

- `gradle init` will automatically install gradle wrapper.
- `./gradlew -v` To check Gradle version
- `./gradlew tasks` - Shows only tasks who are part of atleast one Group
- `./gradlew tasks --all` - Shows all tasks
- `./gradlew --help`

> ⚠️ NOTE: Abbreviated task names : Use first letter of each word Instead of whole task-name. `./gradlew gD` -> `./gradlew generateDescriptions`

> ⚠️ NOTE: "UP-TO-DATE" means Gradlew skipped task since last compile, nothing has changed.

### Execution Order
  > `doFirst` is Stack-like (LIFO) while `doLast` is Queue-like (FIFO).

- During configuration, Gradle evalutes all build scripts and prints logs from:

  - Top-level code in `build.gradle`
  - All logs (Except logs from doFirst and doLast) from `Eagerly` initialized tasks
  - If commands runs `Lazy` initialized task then their logs (But not from doFirst and doLast closure)

- During Execution

  - logs from doFirst() closure but in LIFO format.
  - logs from doLast{} closure but in FIFO format.
  - NOTE: If a task is skipped, its execution will not take place, so any logs inside doFirst {} and doLast {} will not be printed. However, configuration-phase logs are always executed and displayed, even for skipped tasks.

- ```gradle
  plugins {
      id 'java'
  }

  description = 'Learn Execution Phases'
  println '[Configuration] Phase A'

  task ("taskA") {
      println "[Configuration] Phase B"
      doFirst {
          println "[Execution] Phase C" // doFirst uses stack for all doFirst log from same task hence it is printed below Phase F log.
      }
      doLast {
          println "[Execution] Phase D"
      }
  }

  tasks.named("taskA"){
      println "[Configuration] Phase E"
      doFirst {
          println "[Execution] Phase F"
      }

      doLast {
          println "[Execution] Phase G"
      }
  }

  tasks.register('taskB'){  // This create new section on CLI
      dependsOn('taskA')
      println "[Configuration] Phase H" // Since this is LAZY initialized task, logs from printed once whole script is configured.
      doFirst {
          println "[Execution] Phase I"
      }

      doLast {
          println "[Execution] Phase J"
      }
  }

  println '[configuration] Phase K'
  
  /** OUTPUT: 
  
  ./gradlew taskB

  > Configure project :
  [Configuration] Phase A
  [Configuration] Phase B
  [Configuration] Phase E
  [configuration] Phase K
  [Configuration] Phase H

  > Task :taskA
  [Execution] Phase F
  [Execution] Phase C
  [Execution] Phase D
  [Execution] Phase G

  > Task :taskB
  [Execution] Phase I
  [Execution] Phase J

  BUILD SUCCESSFUL
  */
  ```

## Gradle Daemon

Daemon is long-running background process after initial build. It helps to execute application faster.

`./gradlew --status` Shows which daemons are running. (IDLE = Ready and waiting for command; BUSY = Currently running a build; STOPPED = Daemon has stopped.)

`./gradlew --stopped` All Daemons will stop running.

```bash
# Cold start (first build of the day)
$ ./gradlew clean build
BUILD SUCCESSFUL in 45s

# Hot builds (daemon running)
$ ./gradlew build 
BUILD SUCCESSFUL in 3s    # 15x faster!
```

- It is adviced, not to disable darmon but it can be disable from properties file `org.gradle.daemon = false` or from command line `./gradlew build --no-daemon`.

- If project is big, you can increase memory usage for deamon by providing this property: `org.gradle.jvmargs=-Xmx8g -XX:+UseG1GC` - Adds more memory for daemon usage

## build.gradle file

It is BUILD SCRIPT.
When you run `gradle` command. Output is visible in Configure project section inside the terminal.

## Gradle tasks

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

  - Ad-hoc Tasks (Simple custom tasks)

    - ```gradle
       task sayHello {
        doLast {
            println "Hello from Gradle!"
        }
      }
      ```

  - Class-based Tasks (Typed tasks)

    - Class-based tasks are Plugin tasks which need developer configuration prior using it.
    - ex., `copy` task has it's implementation but it doesn't know what to copy and where. Hence Class-based task is defined which provides these configuration. 

    - ```gradle
        // uses `Copy` class:
        task copyConfigs(type: copy){
          from 'config
          into 'build/config'
        }
      ```

  - Ad-hoc V/S Class-based Tasks:

    - Ad-hoc tasks are written from scratch hence it requires `more code` while Class-based tasks require `less code`.
    - Error handling requires for Ad-hoc task while Class-based tasks have built-in error handling.
    - Incremental build is tough to implement by Ad-hocs but it is already done for Class-based.

    *(NOTE) Incremental build - Where all files don't need to recompile but only those changed need to compile. Which is harder to implement in Ad-hocs.*

- **Task configuration properties**:

  - group:

    - Create separate group for task and it is visible when you run `./gradlew tasks --all` command or on gradle task list on IDE.

  - description:

    - Defines definition of task for better readibility when you run `./gradlew tasks --all`.

  - doFirst and dolast:

    - Closures which run either prior or post execution of the task. Self-explaining.

  - eabled:

    - By default it is `True` but you can set it to false by `enabled: False`.

    - ```gradle
      tasks.register('sayHello'){
        enabled: false  // Task will be Skipped.
        
        doLast{
          println 'This won't run...'
        }
      }
      ```

  - onlyIf - conditional clouser:

    - Same as `enabled` but you can define logic here.

    - ```gradle
      tasks.register('sayHello'){
        onlyIf{
          1 == 2 - 2
        }

        doLast{
          println '... runs only when expression is true else Skipped'
        }
      }
      ```

- **Lazy V/s Eager Initialization**

  - `Eager tasks` are created during Configuration time While `Lazy Tasks` are only created when needed. Large build slow down the system commands hence Lazy tasks are usually preferred over Eager tasks.

  - ```gradle
    // Eager Initialization (Slower)
    task sayHello{
      doLast{
        println("Hello!")
      }
    }
    ```

  - ```gradle
    // Lazy Initialization (Faster)
    tasks.register("sayHello"){
      doLast{
        println("Hello!")
      }
    }
    ```
  
- **Locating tasks**

  - tasks.named(): Adjust or extend the behavior of an existing task. Note: tasks.named() can't be used for non-existing task.

    - Modify behaviour of ad-hoc task:

      - ```gradle
        tasks.register("sayHello") {
          println "Hello world!"
          doLast {
              println "end of sayHello task!"
          }
        }

        tasks.named("sayHello"){
          println "modification of sayHello task!"
        }

        /** OUTPUT:

        ./gradlew sayHello

        > Configure project :
        Hello world!
        modification of sayHello task!

        > Task :sayHello
        end of sayHello task!
        */
        ```

    - Modify behaviour of tasks from plugins:

      - ```gradle
        tasks.named("build") {
            dependsOn("integrationTest")  // ensures `integrationTest` runs whenever `build` runs
        }
        ```

      - To change behaviour of task from plugin, we can use `tasks.named()` and it adds extra functionality to built in tasks.

- dependsOn()
  - `taskA.dependsOn(taskB)` : Before Task A runs, you must finish Task B.

  - For better readability, Always define such tasks which are not depends on others. Later define such task which depends on others.

  - ```gradle
    // Here Integration task will execute prior to Build task.
    tasks.register('integrationTest'){
      println 'performing integration test'
    }

    tasks.register('build'){
      dependsOn('integrationTest')
      println 'performing build task'
    }
    ```

## Plugins

Plugins are additional resource. It adds extra functionality and capabilities.

```gradle
plugins{
    id 'base'   // core-Gradle plugins; clean, build, zip task etc,.
    id 'java'   // compileJava, test tasks
    id 'org.springframework.boot'  // BootRun, dependency management task
    id 'jacoco' // code coverage plugin; test report
    id 'application'    // Core-gradle plugin; for CLI and server apps.
}

// Run `gradle tasks` to check new tasks imported by Plugins
```

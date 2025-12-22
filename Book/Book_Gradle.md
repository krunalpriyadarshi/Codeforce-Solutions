# 📘 Learn Gradle

Gradle is incremental means if a task is not modified, it will not execute it.

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

⚠️ ⚠️ TODO: testing.suits from gradle. Also, Learn variables, strings, collections in groovy!!

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

> NOTE: "UP-TO-DATE" means Gradlew skipped task since last compile, nothing has changed.

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

  - tasks.getByName(): Same as tasks.named() but this initializes task as EAGER TASK.

    - ```gradle
      tasks.getByName('clean'){
        doLast{
          println 'Eager initilizes clean task by tasks.getByName() method.'
        }
      }
      ```

    > NOTE: Shorthand syntex: tasks.TaskName{...}

    - ```gradle
      tasks.clean{
        doLast{
          println 'Eager initilizes clean task by short-hand method.'
        }
      }
      ```
  
  - Groovey shorthand method: Define by directly using name of task. And initialization will be EAGER type as well.

    - ```gradle
      description = 'Learn Execution Phases'
      println '[Configuration] Phase A'

      tasks.register("taskA") {
          println "[Configuration] Phase B"
          doFirst {
              println "[Execution] Phase C"
          }
          doLast {
              println "[Execution] Phase D"
          }
      }

      taskA{
          println "[Configuration] Phase E"
      }

      println '[configuration] Phase O'

      // OUTPUT
      /**
      ./gradlew clean

      > Configure project :
      [Configuration] Phase A
      [Configuration] Phase B
      [Configuration] Phase E
      [configuration] Phase O
      */
      ```
  
- **Task dependencies & ordering**

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

  - mustRunAfter()
    - It defines order of execution if multiple tasks are inside dependsOn() block.

    - ```gradle
      tasks.register('task1'){
        mustRunAfter(task2) // Overwrites default execution order. Task2 will run first then task1.
        println 'configuration: task1'
      }

      tasks.register('task2'){
        println 'configuration: task2'
      }

      tasks.register('mainTask'){
        dependsOn(task1, task2) // Default order of execution is task1 then task2
        println 'configuration main task'
      }

      /** OUTPUT

      configuration: task2
      configuration: task1
      configuration main task
      > Task :task2 UP-TO-DATE
      > Task :task1 UP-TO-DATE
      > Task :mainTask UP-TO-DATE
      */
      ```

  - finalizedBy()
    - Finalized blocks always run during execution phase even if task fails or exception occurs. NOTE: If exception thrown during configuration phase, Finalized block will not execute.

    - ```gradle
      tasks.register('cleanUp'){
        println 'Configuration: clean up'
        doLast{
          println 'Execution: clean up done.'
        }
      }

      tasks.register('mainTask'){
        println 'configuration: main task'
        finalizedBy 'cleanUp'
        doLast{
          throw new Exception('custom error')   // Since Exception occurs during Execution phase, it will execute finalized block.
          println 'Execution: main task done.'
        }
      }

      tasks.register('failTask'){
        println 'configuration: fail task'
        throw new execption('custom error') // Since execption occues during configuration phase, it won/'t execute finalized block.
        doLast{
          println 'execution: fail task'
        }
      }
      ```

- **Inputs & Outputs**
  - Inputs + Outputs tell Gradle when a task needs to run; without them, Gradle always runs it. If Input is changed or Output is missing, Gradle will execute the task else task will be skipped. - This logic is used for Incremental Build.

  - Task A (producer)

  - ```gradle
    tasks.register("generateData") {
      outputs.file("$buildDir/data.txt")
      doLast {
          file("$buildDir/data.txt").text = "Generated"
      }
    }
    ```
  
  - Task B (consumer)

  - ```gradle
    tasks.register("readData") {
      inputs.file("$buildDir/data.txt")
      doLast {
          println file("$buildDir/data.txt").text
      }
    }
    ```

  - Another example of Producer-consumer linking:
  
  - ```gradle
    tasks.register('copyTask', Copy){ 
      from 'temp.txt'
      into "$buildDir/workspace"
    }

    tasks.register('zipTask', Zip){ 
      from copyTask
      archiveFileName = 'workspace.zip'
      destinationDirectory = file("$buildDir")
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

## Java Project

- `soureceCompatibility` tells Which java version used to write codebase.

  - ```gradle
    sourceCompatibility = 11
    // Java 11 -> ✅
    // Java 17 -> ❌ (compiler error if 17 features were used.)
    ```

- `targetCompatibility` tells which java version is expected to run during execution.

  - ```gradle
    targetCompatibility = 11
    // Java 11 JVM → ✅ 
    // Java 17 JVM → ✅ (JVM backward compatibility)
    // Java 8 JVM → ❌ fails
    ```

Since `soureceCompatibility` and `targetCompatibility` assume that correct java version is setup for machine and it creats issue during build or run phase; `toolChain` was introduced.

⚠️ `Java toolChain` forces gradle to use specific java version to avoid mismatch of java version. ✅ Gradle will download the JDK automatically if missing.

- ```gradle
  java{
      toolchain {
          languageVersion = JavaLanguageVersion.of(11)  // Java 11 will be used by JVM.
      }
  }
  ```

- Individual Gradle tasks can override and use a different Java version if needed.

  - ```gradle
    tasks.withType(JavaExec).configureEach{
      javaLauncher = javaToolchains.auncherFor{
        languageVersion = JavaLanguageVersion.of(11)    // Application will run on java 11.
      }
    }
    ```

### Dependency

- Group:Name:version of dependency is required before implementation.

- ```groovey
  // Make sure to define repository from where dependencies can be downloaded.
  repository{
    mavenCentral()
  }

  dependencies{
    implementation 'org.apache.commons:commons-lang3:3.12.0'
  }
  ```

### Phases & ClassPath

- **ClassPath**: Classpath are locations of Jar files, modules or directories.

- There're different phases:
  - *Compile time phase*: It type checks and generate byte codes.
  - *Runtime phase*: Execute byte codes.
  - *Test compile phase*: Compile test code.
  - *Test runtime phase*: Execute tests.

- Each phases need different dependencies.

  - ```groovey
    dependencies {
      implementation 'org.springframework:spring-core'          // Avaliable for all phases (availbale for test phases)
      compileOnly 'org.projectlombok:lombok'                    // Available only for compile time phase
      runtimeOnly 'ch.qos.logback:logback-classic'              // Available only for runtime phase

      testImplementation 'org.junit.jupiter:junit-jupiter-api'  // Available only for test compile and runtime phase
      testCompileOnly 'com.example.library:library:0.0.0'       // Available only for test-compile time phase
      testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine'  // Available only for test runtime phase
    }
    ```

- **Why different phases exist?**: To fails early. (Means find issues in early stage rather than finding issue later on and debugging it.)

  - **Why can't put everything in one classpath**

    - Because:

      - One classpath feels simpler, but it hides bugs, breaks encapsulation, slows builds, and causes production failures.
      - Bigger, slower and messier builds: Compiler will scan every JARs and build time will be high. Also, Runtime will take longer to startup and large memory footprint.
      - Bloated artifact (Fat JARs)
      - Version conflicts

  - Can be easily understand by TestCompileTime and TestRunTime example:

    - Test compile classpath: junit-jupiter-api
    - Test runtime classpath: junit-jupiter-engine
    - Here, Needs:
      - `@Test` annotation -> compile time
      - Test engine -> runtime
    - Hence,
      - testImplementation junit-jupiter-api
      - testRuntimeOnly junit-jupiter-engine

  - Usage example:

    - `compileOnly`: A library needed only during compilation, not at runtime.
      - Lombock library (@Data, @Getter, @Setter...) needed during compile time. Once it is compiled we don't need it during runtime since getter-setter were created by Lombok and included in byte code.
    - `implementation`: A library needed both at compile time and at runtime.
      - Spring library: Compiler needs the classes and method signatures. While JVM needs the same library to execute logic at runtime.
    - `runtimeOnly`: A library needed only at runtime, not during compilation.
      - Database drivers `runtimeOnly 'org.postgresql:postgresql:42.6.0'`; Driver classes are loaded via reflection at runtime. Compiler doesn’t need the driver classes.
      - Junit engine is another exampel where engine only needed during runtime to execute annotations while for compilation junit-jupiter lib is used to define annotation and it is being checked during compilation.

### Extra Properties

- A block where you can define custom properties for project like springVersion or junitJupiterVersion.

  - Extra veriable can be used by "${propertyName}".

  - ```gradle
    ext{
      junitJupiterVersion = '5.7.2'
    }

    dependencies {
      testImplementation "org.junit.jupiter:junit-jupiter-api:${junitJupiterVersion}"
      testImplementation "org.junit.jupiter:junit-jupiter-params:${junitJupiterVersion}"
      testRuntimeOnly "org.junit.jupiter:junit-jupiter-engine:${junitJupiterVersion}"
    }
    ```

### run application

- One way is to create JAR file by `./gradlew jar` and run application from CLI by `java -jar fileLocation/fileName.jar`. 

- Or setup application plugin and define main class:

  - ```gradle
    plugin{
      id 'application'  // Application plugin automatically imports Java plugin.
    }

    application{
      mainClass = 'com.krunal.themepark.RideStatusService'  // format: "Package name + entry point class name"
    }
    ```

### Debug application

- Via IDE: In gradle task list (on right side), right-click on any task and choose `debug` option.

### Testing application

- Implement test class using Junit4, Junit5 or TestNG library.

#### How to run test classes

- **Via IDE**:
  - Manually running `check` or `test` task to execute all test classes from application.
  - Go to any testClass and right click on it which opens menu with `run testClass` or `debug testClass` option.

- **Via CLI**:
  - `./gradlew test` or `./gradle check` runs all test classes.
  - `./gradlew test --console=verbose`: Detailed log in command line.
  - `./gradlew test --tests SomeTestClass` Runs specific test file
  - `./gradlew test --tests SomeTestClass.someMethod` Runs specific method of a class
  - `./gradlew cleanTest` Deletes only test outputs.
  - `./gradlew cleanTest test --console=verbose` Force delete test outputs then re-runs tests.

#### Testing Types

- Manual Testing:

  - Known as Human testing or Exploratory testing.
  - A testing performed by human without automated scripts to validate UI/UX behaviour or making sure business flows make sense from a user's perspective.
  - verifing logs, error handling, data consistency, and calling APIs.

- Unit Testing:

  - Used to verify the smallest units of code like methods or classes work as expected.
  - Used to check business logic or validation rule after the change.
  - It is quick to runFast and provides feedback during development.

- Integration Testing:

  - To verify Integration of DB, REST Apis, file systems and configuration or external resources which makes `Integration testing` slower than `Unit testing`.
  - To check if components work together as expected after change.
  - ex., @SpringBootTest file can be used to check Controller, Service, Repository and Database integration.

#### Integration Testing

- Step 1: Create integration test classes on src/integrationTest/java/.. directory
- Step 2: Use testing.suites{} block to define testing setup.

  - ```gradle
    testing {
      suites {
          integrationTest(JvmTestSuite) {
              useJUnitJupiter()   // Import dependencies for testing phase
              dependencies {
                  implementation project  // Additional testing dependencies
              }
          }
      }
    }
    ```

- Step 3: (optional) Modify to run Integration testing for `Check` or `test` task.

  - ```gradle
    tasks.named('check'){
      dependsOn testing.suites.integrationTest  // Before `check` task runs, `IntegrationTest` will always run.
    }
    ```

#### Testing Plugins

- JVM Test Suite plugin (Gradle 7.3+)
- TestSets plugin (Custum plugin for less than Gradle 7.3)

### Publichsing to Maven



## TIPS

- `./gradlew assemble` task is same as `build` task but it doesn't run `check` task. Usecase of this task is to save time when you just want to build jar but not want to test your application. s

- ⚠️ NOTE: Abbreviated task names : Use first letter of each word Instead of whole task-name. `./gradlew gD` -> `./gradlew generateDescriptions`

- Run application by JAR files:

  - JAR is bundle of class files, resources, and metadata which can be shared, deployed or run across systems.
  - Thin Jar has only code while Fat Jar has code + dependencies.

  - ```command
    // run application by
    java -jar location_of_jar_file/JarName.jar
    ```

# 📘 Learn Gradle

Gradle is incremental means if a task is not modified, it will not execute it.

## Project layout

- `.gradle` Gradle's private workspace and cache directory
- `gradle` Gradle system files
- `gradlew` Gradle runner (Mac/ Linux)
- `gradlew.bat` Gradle runner (Windows)
- `build` Generated files from `.gradlew build` command
- `build.gradle` Main build configuration
- `gradle.properties` Project specific properties (Gradle properties like `org.gradle.daemon = true` or Global variable like `javaVersion = 17`)
- `settings.gradle` Project setting (rootProject name,  `include subProject`, and `includeBuild buildSrc`) 

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

  - In gradle, An abstract class can be created as a Custom task class and can be used to register a task.

    - ```gradle
      abstract class CompareNumbersTask extends DefaultTask {
        @Input int a  // Get values from Task
        @Input int b  // Get values from Task

        @TaskAction // Custom task logic
        void compare() { 
            print (a == b)? "same" : (( > b)? "A is big" : "B is big")
        }
      }
      tasks.register('compareNumbers', CompareNumbersTask) {
          a = 1000
          b = 200
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

> When running `./gradlew help`, during the configuration phase, eager tasks are fully created (task objects are created), while lazy tasks are only registered as metadata. However, configuration code for both eager and lazy tasks is executed during the configuration phase.

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
    - It defines order of execution. It controls the order if both are call same time.
    - For ex., dependsOn(task1, task2) -> here both tasks are called -> now mustRunAfter() defines the order (Which needs to run first) -> as per below code task2 will execute first -> then task1.
    - (we usually run `./gradle clean build` - here 2 commands are called)
    - We can force ordering like `./gradle task1 task2` but as per build script it will run task2 first. 

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
  - This is used for Incremental Build. -> input-output tells if something is modified or not. Based of metadata it tell gradle to run particular task or not.

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

### Publising Maven

- Step 1: Import plugin `id 'maven-publish'`.

  - ```gradle
    plugins{
      id 'maven-publish'
    }
    ```

  - `publish` task publishes all publications according to defined configuration.
  - While `publishToMavenLocal` task, publishes to local directory: `~/.m2/repository`.

- Step 2: Publishing configuration

  - ```gradle
    publishing {
      publications {
          mavenJava(MavenPublication) {
              from components.java

              // Co-ordinates:
              groupId = 'com.example'
              artifactId = 'my-library' 
              version = '1.0.0'
          }
      }

      repositories {
          mavenLocal()    // Stores locally on `~/.m2/repository` directory.
          // can be stored in remote location like mavenRepository and AWS Repository.
      }
    }
    ```
  
### SpringBoot project

```gradle
plugins{
  id 'org.springframework.boot' version '2.5.4'     // Can't fetch version value dynamic way from ext{..} because plugin initilized before ext{..} block.
}
```

- Plugin automatically finds entry point of application which is decalred in `@SpringBootApplication` annotation in `src/main/..` directory.

- All `boot*` related tasks are being brought by springBoot plugin.

- `bootJar` task creates JAR file. To run, `java -jar filePath/fileName.jar` use command.

- `id 'io.spring.dependency-management' version '1.0.11.RELEASE'` plugin used to manage dependencies.

#### ABI (Application Binary Interface)

- ABI = the rules that define how programs and libraries communicate at the compiled/binary level.

- Benefits:
  - cleaner classpaths
  - faster compilation

- `api` dependencies are being added during compile & runtime classpaths. While `implementation` dependencies are only for runtime classpath.

#### Example of ABI impact

- Library A:

  - ```gradle
    dependencies {
        api 'com.google.guava:guava:31.1-jre'           // exposed to consumers
        implementation 'org.slf4j:slf4j-api:1.7.36'     // internal only
        compileOnly 'org.projectlombok:lombok:1.18.26'  // compile-time only
        runtimeOnly 'mysql:mysql-connector-java:8.1.0'  // runtime only
    }
    ```
  
  - When published, a Slim JAR is created, only `api` dependencies are added to JAR.
  - Slim JAR hides implementation & compileOnly deps from consumer (Application which import or implement `library A`)
  - Consumer does not need to redeclare compileOnly or implementation deps if they never call those libraries directly.
  - Runtime-only dependencies must be present on consumer’s runtime classpath → otherwise runtime fails.

  - Result will be:
    - Consumer compileClasspath → LibraryA.class (SLF4J hidden, Lombok code already there)
    - Consumer runtimeClasspath → LibraryA.class + runtimeOnly deps (MySQL) must be present

### Deploy application

- `.war` file can be used for deployment to run on Tomcat server.
- How to create WAR files:

  - Add plugin `war` which import `java` plugin as default.
  - main class must extend `SpringBootServletInitializer`

    - ```spring
      @SpringBootApplication
      public class ThemeParkAplication extends SpringBootServletInitializer{
        ...
      }
      ```

  - Use `bootWar` task to create WAR file.
  - Run `.war` file same way we run JAR files.

    - ```command
      java -jar fileLocation/fileName.war
      ```

#### Deployment using Docker

- A WAR file can't be run itself. It needs JAVA environment + Tomcat server.

  - Http request -> TomcatServer -> WAR application -> output

- Dockerfile replaces a physical server by packaging Java, Tomcat, and your WAR into one reproducible runtime.

  - ```DockerFile
    FROM tomcat:9.0-jdk17

    # Remove default apps (Best practise) for clean directory. Easy for tomcat to locate WAR and no url conflicts after deployment.
    RUN rm -rf /usr/local/tomcat/webapps/*

    # Copy your WAR to TOMCAT folder so that tomcat knows which webapps exist.
    COPY build/libs/theme-park-api.war /usr/local/tomcat/webapps/theme-park-api.war

    # TOMCAT listens on 8080 port
    EXPOSE 8080

    # Boot up TOMCAT server and make sure it listens for HTTP request
    CMD ["catalina.sh", "run"]
    ```
  
- Create docker image by `docker build -t theme-park-api .`

- Check image created succesfully by `docker images`

- Create docker container and run it: `docker run -p 8080:8080 theme-park-api`.
  
  - ```chart
      Docker container starts
              ↓
      CMD executes: `catalina.sh` run so that TOMCAT starts and listen on predefined port.
              ↓
      Tomcat server boots (JVM initializes)
              ↓
      Tomcat scans /usr/local/tomcat/webapps
              ↓
      theme-park-api.war is detected
              ↓
      WAR is unpacked (exploded) into a directory
              ↓
      Servlets / Controllers are initialized
              ↓
      Application becomes available
              ↓
      Access via: http://localhost:8080/theme-park-api
    ```

- ⚠️ Remember, Application is available on `localhost:defined-port-number/webApp-name/endpoint`. Here, it will be `http://localhost:8080/theme-park-api`

### Advance Dependencies Management

- Types of Dependencies

  - Direct dependency
    - Your application use it directly
  - Transitive dependency
    - A dependency using another dependencies are Transitive dependency.

- Version Conflict Resolution in gradle will automatically use highest version dependency if there're multiple versions are being fetched.

- Manage Dependency

  - Exclude transitive dependency

    - ```gradle
      implementation('org.springframework.boot:spring-boot-starter-web'){
        // Exclude single dependency.
        exclude(group: 'com.fasterxml.jackson.core', module:'jackson-core')

        // Exclude by group only - All modules in the group will be excluded.
        exclude(group: 'org.springframework')
      }
      ```

    - ⚠️ Exclude Rule is avoided if another library pulls same library as transitive dependency. But `configuration.all` or `configuration.implemnetation` is used if particular library you wish not to use at all.

    - ```gradle
      // Brings `logging` library as Transitive dependency.
      implementation('org.springframework.boot:spring-boot-starter-web')

      // `logging` library will be excluded for all `implementation` block. And `logging` will not be visible on dependencyTree.
      configurations.implementation {
          exclude(group: 'org.springframework.boot', module:'spring-boot-starter-logging')
      }
      ```

    - Configuration Exclude is useful when developer is confident that particular library isn't needed at all.

  - Replace transitive dependency

    - ```gradle
      implementation('org.springframework.boot:spring-boot-starter-web')

      modules {
          module('org.springframework.boot:spring-boot-starter-logging'){
            // Raplces `logging` lib with `log4j2` lib:
              replacedBy 'org.springframework.boot:spring-boot-starter-log4j2'
          }
      }
      ```

  - Constraint transitive dependency

    - Constraint doesn't pull library. It replaces a library if some other library tries to pull same constraint library will defined version.

    - ```gradle
      implementation('org.springframework.boot:spring-boot-starter-web')

        constraints {
            // Fetch 1.5.3 logback library only if some other library pulls logback else it will not be pull.
            implementation('ch.qos.logback:logback-classic:1.5.3') {
                because('Security vulnerability fix')
            }
        }
      ```

## Multi-project builds (Modulization)

- Monolithic Gradle project takes more time to execute each tasks while sub-project takes less time as specific codebase is target for execution.

### Create multi-project

- Execute `gradle init`
- Add subproject inside `settings.gradle` file.

  - ```gradle
    rootProject.name = 'multi-project-example'
    include('subProject1')
    include('subProject2')
    ```

  - Remeber, `./gradlew taskName` command from main directory executes same name task from main project and executes same task from all subProjects if exists.

    - ```gradle
      // Execute command for from Main directory
      ./gradlew sayHello

      /** OUTPUT
      > Task :sayHello
      Hi from Main project!

      > Task :subProject1:sayHello
      Hi but from 1

      > Task :subProject2:sayHello
      Hi but from 2
      */
      ```

  - To run specific task from a subproject: `./gradle :subProject:taskName`

    - `./gradlew :subProject1:hello`

### Use method of another subProject

- Make sure `setings.gradle` file includes new subProjects.

  - ```gradle
    rootProject.name = 'theme-park-manager'
    include('api')
    include('service')
    ```

- Declare subproject as java-library whose gonna provide methods to other subProject.

  - ```gradle
    plugins{
      id 'java-library'
    }
    ```

- Now add subProject as dependency to use methods of it. Add it to `build.gradle` file of subProject who wants to use methods.

  - ```gradle
    dependencies {
      implementation project(':service')
    }
    ```

### Conventional Plugin

- Gradle way to centralize and consistent build logic so you don't have to repeat configuration across multiple projects or subProjects.

- Example: For 3 subProjects, we've common dependencies, plugins and a custom task which can be centralized.

  - Create directory `buildSrc` and add `'groovy-gradle-plugin'` plugin to build.gradle file.
  - Add this `buildSrc` folder to setting.gradle file at root directory to tell gradle that there's a centraizlied build folder.

    - ```gradle
      includeBuild('buildLogic')
      ```

  - At buildSrc/src/main/groovy/conventional.gradle file and write script:

    - ```gradle (buildSrc/src/main/groovy/conventional.gradle)
      plugins{
        id 'java'
      }

      repositories {
        mavenCentral()
      }

      java{
          toolchain{
              languageVersion.set(JavaLanguageVersion.of(17))
          }
      }

      // Task modifier - make sure `clean` task run prior to `build` task.
      tasks.named('build'){
          dependsOn tasks.named('clean')
      }
      ```

  - At subproject, add newly created plugin by fileName. In this case, file name is `conventional`.

    - ```gradle (subproject/build.gradle)
      plugins{
        id 'conventional'
      }
      ```

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

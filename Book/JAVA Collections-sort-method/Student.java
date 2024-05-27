public class Student {
    private String name;
    private int age;
    private String grade;

    public Student(String name, int age, String grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    public String getName(){
        return this.name;
    }

    public int getAge(){
        return this.age;
    }

    public String getGrade(){
        return this.grade;
    }

    public void display(){
        System.out.println(this.name+ " "+ this.age+ " "+ this.grade);
    }
}

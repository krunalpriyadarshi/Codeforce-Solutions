import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        ArrayList<Student> students= new ArrayList<>();

        Student s= new Student("Krunal", 25, "A+");
        students.add(s);

        s= new Student("Ankit", 22, "A+");
        students.add(s);

        s= new Student("Mohit", 33, "A+");
        students.add(s);

        s= new Student("Mohit", 28, "A+");
        students.add(s);

        s= new Student("Mohit", 27, "A+");
        students.add(s);

        for(Student su: students){
            su.display();
        }

        Collections.sort(students, new StudentComparator());
        // using Lambda expression:
        /*
            Collections.sort(students, (s1, s2)->{
                int gradeComparison= s1.getGrade().compareTo(s2.getGrade());
                if(gradeComparison!= 0)
                    return gradeComparison;

                int nameComparison= s1.getName().compareTo(s2.getName());
                if(nameComparison!= 0)
                    return nameComparison;

                return Integer.compare(s1.getAge(), s2.getAge());
            });
        */

        System.out.println("After sorting: ");
        for(Student su: students){
            su.display();
        }
    }
}
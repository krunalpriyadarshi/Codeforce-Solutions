// Create a class Student with fields name, grade, and age. 
// Write a comparator to sort a list of Student objects first by grade (descending), then by name (alphabetically), 
// and finally by age (ascending).

import java.util.Comparator;

public class StudentComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2){
        int gradeComparison= s2.getGrade().compareTo(s1.getGrade());
        if(gradeComparison!= 0){
            return gradeComparison;
        }

        int nameComparison= s1.getName().compareTo(s2.getName());
        if(nameComparison!= 0)
            return nameComparison;

        return Integer.compare(s1.getAge(), s2.getAge());
    }
}
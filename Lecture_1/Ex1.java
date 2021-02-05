public class Ex1 {
    public static void main(String[] args){
        Employee c = new Employee();
        c.name = "Chan Tai Man";
        c.setSalary(20000);
        c.setSalary(-1);
        c.print();
    }
}

class Employee {
    String name;
    int salary;
    Employee () {

    }

    Employee (String TEMP) {
        name = TEMP;
    }

    Employee (int s) {
        salary = s;
    }

    void setSalary(int s){
        if (s<0) return;
        salary = s;
    }

    void print() {
        System.out.println("Name is " + name);
        System.out.println("Salary is " + salary);
    }
}

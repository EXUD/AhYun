public class Ex2 {
    public static void main(String[] args){
        Employee c = new Employee("Chan Tai Man", 20000);
        c.print();
        Employee s = new Employee("", -1);
        s.print();
    }
}

class Employee {
    String name;
    int salary;
    Employee () {

    }

    Employee(String n, int s){
        if (s<0) salary = 1;
        else salary = s;
        if (n=="") name = "unknown";
        else name = n;
    }

    void print() {
        System.out.println("Name is " + name);
        System.out.println("Salary is " + salary);
    }
}

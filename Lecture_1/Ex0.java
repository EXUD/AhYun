public class Ex0 {
    public static void main (String[] args){
        Employee c = new Employee();
        c.name = "Chan Tai Man";
        c.salary = 20000;
        c.print();
    }
}

class Employee {

    String name;
    int salary;
    
    Employee () {
        name = "";
        salary = 0;
    }

    Employee (String TEMP) {
        name = TEMP;
    }

    Employee (int temp) {
        salary = temp;
    }

    void print() {
        System.out.println("Name is " + name);
        System.out.println("Salary is " + salary);
    }
}

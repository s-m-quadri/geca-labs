#include <stdio.h>

// Define structure
struct Student {
    char name[50];
    int age;
    float grade;
};

int main() {
    // Declare structure variable
    struct Student student1;

    // Declare a pointer to structure
    struct Student *ptr;

    // Assign the address of student1 to the pointer
    ptr = &student1;

    // Accessing members using the pointer
    printf("Enter student's name: ");
    scanf("%s", ptr->name);

    printf("Enter student's age: ");
    scanf("%d", &ptr->age);

    printf("Enter student's grade: ");
    scanf("%f", &ptr->grade);

    // Display data using pointer
    printf("\nStudent Information:\n");
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Grade: %.2f\n", ptr->grade);

    return 0;
}
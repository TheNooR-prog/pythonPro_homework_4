import client
import custom_extantions
import group
import item
import order
import studentclass

if __name__ == '__main__':

    try:
        item_1 = item.Item("Book", 150, 20, 10, 5)
        item_2 = item.Item("Notebook", 50, 15, 8, 2)
        item_3 = item.Item("Album", 30, 30, 20, 3)
    except ValueError as err:
        print("Wrong price value")
    except custom_extantions.NegativeValue as err:
        print(err)

    client_1 = client.Client("Ivanov", "Petro", "Semenovych", "+380991231212")
    client_2 = client.Client("Petrov", "Ivan", "Semenovych", "+380991231313")
    client_3 = client.Client("Semenov", "Semen", "Petrovych", "+380991231414")

    order_1 = order.Order("Order 1", client_2)
    order_1.add_items(item_1)
    order_1.add_items(item_2)
    order_1.add_items("Hello")
    order_1.add_items(item_2)
    order_1.add_items(item_3)

    print(order_1)
    print(order_1.total())
    print("\n")

    students = [studentclass.Student('Ivanov1', 'Ivan'),
                studentclass.Student('Ivanov2', 'Ivan'),
                studentclass.Student('Ivanov3', 'Ivan'),
                studentclass.Student('Ivanov4', 'Ivan'),
                studentclass.Student('Ivanov5', 'Ivan'),
                ]

    group_1 = group.Group("PythonPro", students_limit=4)

    try:
        for student in students:
            group_1.add_student(student)
    except Exception:
        pass

    print(group_1)
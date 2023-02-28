#include <Python.h>

void print_python_list(PyObject *p) {
	printf("[*] Python list info\n");
    if (p == NULL || !PyList_Check(p)) {
        fprintf(stderr, "[Error] Invalid List Object\n");
        return;
    }
    PyListObject *list = (PyListObject *) p;
    Py_ssize_t size = PySequence_Size(p);
    if (size < 0) {
        PyErr_Print();
        return;
    }
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *elem = list->ob_item[i];
        if (PyBytes_Check(elem)) {
            printf("Element %ld: bytes\n", i);
	    printf("[.] bytes object info\n");
	    printf("  size: %ld\n", PyBytes_Size(elem));
            printf("  trying string: ");
	    PyObject_Print(elem, stdout, 0);
	    printf("first %ld bytes: ", PyBytes_Size(elem) + 1);
            for (Py_ssize_t j = 0; j < PyBytes_Size(elem); j++) {
                printf("%02x ", (unsigned char) PyBytes_AsString(elem)[j]);
            }
            printf("\n");
        } else if (PyLong_Check(elem)) {
            printf("Element %ld: int", i);
        } else if (PyFloat_Check(elem)) {
            printf("Element %ld: float", i);
	    printf("[.] float object info\n");
	    printf("  value: %f\n", PyFloat_AsDouble(elem));
        } else if (PyList_Check(elem)) {
            printf("Element %ld: list\n", i);
            print_python_list(elem);
    }
}

#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;
	
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes;
	
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", size + 1);
	bytes = (PyBytesObject *)p;
	for (i = 0; i <= size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i < size)
			printf(" ");
	}
	printf("\n");
}


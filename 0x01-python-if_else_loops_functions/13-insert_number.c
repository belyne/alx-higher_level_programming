#include "lists.h"

/**
 * insert_node - function that inserts a number into
 * a sorted singly-linked list.
 * @head: a pointer the head of the linked list.
 * @number: the number to insert.
 * Return: returns NULL if the function fails.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;
	current = *head;
	
	prev = NULL;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	
	new->n = number;
	
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = current;
		prev->next = new;
	}
	return (new);
}

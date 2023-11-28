#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the linked list's head
 * @number: the value to insert
 *
 * Return: a pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *prev = NULL;
	listint_t *node = malloc(sizeof(listint_t));

	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	while(tmp)
	{
		if (number < tmp->n)
		{

			if (prev == NULL)
			{
				*head = node;
				node->next = tmp;
			}
			else
			{
				node->next = tmp;
				prev->next = node;
			}
			return (node);
		}

		prev = tmp;
		tmp = tmp->next;
	}
	prev->next = node;
	return (node);

}

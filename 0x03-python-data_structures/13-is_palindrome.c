#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: the head of the list
 *
 * Return: 1 if true, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{

	listint_t *list = *head;
	size_t length = 0, count = 0;
	int *visited;

	while (list)
	{
		length++;
		list = list->next;
	}
	list = *head;
	while (list)
	{
		count++;
		if (count <= length / 2)
		{
			visited = realloc(visited, count * sizeof(int));
			visited[count - 1] = list->n;
		}
		else if (length % 2 && count == length / 2 + 1)
			;
		else if (list->n != visited[length - count])
		{
			free(visited);
			return (0);
		}
		list = list->next;
	}
	free(visited);
	return (1);
}

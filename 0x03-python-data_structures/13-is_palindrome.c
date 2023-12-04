#include "lists.h"

/**
 * reverse_list - reverses a list
 * @list: a pointer to the list
 *
 * Return: pointer to the reversed list.
*/
listint_t *reverse_list(listint_t *list)
{
	listint_t *prev = NULL, *current = list, *next = NULL;

	while(current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: the head of the list
 *
 * Return: 1 if true, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{

	listint_t *list = *head, *slow, *fast, *second;

	slow = list;
	fast = list;
	while(fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second = reverse_list(slow);
	while(second != NULL)
	{
		if (list->n != second->n)
			return (0);
		list = list->next;
		second = second->next;
	}

	slow = reverse_list(slow);

	return (1);
}

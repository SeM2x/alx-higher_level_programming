#include "lists.h"

/**
 *reverse_list - reverses a list
 *@list: a pointer to the list
 *
 *Return: pointer to the reversed list.
 */
listint_t* reverse_list(listint_t *list)
{
	listint_t *prev = NULL, *current = list, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 *is_palindrome -  checks if a singly linked list is a palindrome.
 *@head: the head of the list
 *
 *Return: 1 if true, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *list = *head, *prev_slow, *slow, *fast, *second, *head_second;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	prev_slow = NULL;
	slow = list;
	fast = list;
	while (fast && fast->next)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	head_second = reverse_list(slow);
	second = head_second;
	while (second != NULL)
	{
		if (list->n != second->n)
		{
			is_palindrome = 0;
			break;
		}
		list = list->next;
		second = second->next;
	}
	
	prev_slow->next = reverse_list(head_second);

	return (is_palindrome);
}

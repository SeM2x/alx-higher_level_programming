#include "lists.h"

int is_visited(listint_t *list, listint_t **visited)
{
    listint_t **tmp = visited;

    while (*tmp)
    {
        if (*tmp == list)
            return (1);
        tmp++;
    }

    return (0);
}

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the linked list
 *
 * Return: 0 or 1.
 */
int check_cycle(listint_t *list)
{
    listint_t *tmp = list;
    size_t size = 0;
    listint_t **visited = malloc(1000 * sizeof(listint_t *));

    while (tmp)
    {
        if (is_visited(tmp, visited))
        {
            free(visited);
            return (1);
        }

        visited[size++] = tmp;
        tmp = tmp->next;
    }

    free(visited);
    return (0);
}

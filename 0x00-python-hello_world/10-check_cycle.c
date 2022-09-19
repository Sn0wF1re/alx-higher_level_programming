#include "lists.h"
/**
 *check_cycle - checks if a singly-linked list has a cycle in it
 *@list: singly-linked list
 *
 *Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *new;

	if (!list)
		return (0);
	new = list->next;
	while (new)
	{
		if (new == list)
			return (1);
		new = new->next;
	}

	return (0);
}

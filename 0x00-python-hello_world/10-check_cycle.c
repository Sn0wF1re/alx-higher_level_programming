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
	listint_t *prev;

	if (!list)
		return (0);
	prev = list;
	new = list;
	while (new && prev && new->next)
	{
		prev = prev->next;
		new = new->next->next;
		if (prev == new)
			return (1);
	}

	return (0);
}

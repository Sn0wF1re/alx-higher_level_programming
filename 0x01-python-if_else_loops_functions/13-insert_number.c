#include "lists.h"

/**
 *insert_node - insert numberinto sorted singly-linked list
 *
 *@head: singly-linked list
 *@number: number to be inserted in singly-linked list
 *Return: singly-linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL)
	{
		if ((current->next)->n >= number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	new_node->next = NULL;
	current->next = new_node;
	return (new_node);
}

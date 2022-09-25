#include "lists.h"
/**
 *reverse_list - reverse a linked list
 *@head: pointer to first node in list
 *
 *Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}

/**
 *is_palindrome - checks if a singly-linked list is a palindrome
 *@head: double pointer to linked list
 *
 *Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *temp = *head;
	listint_t *half = NULL;

	if (*head != NULL || (*head)->next != NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			half = slow_ptr->next;
		}
		if (!fast_ptr->next)
		{
			half = slow_ptr->next->next;
		}
		slow_ptr = slow_ptr->next;
	}
	reverse_list(&half);

	while (half && temp)
	{
		if (temp->n == half->n)
		{
			temp = temp->next;
			half = half->next;
		}
		else
			return (0);
	}
	if (!half)
		return (1);

	return (0);
}

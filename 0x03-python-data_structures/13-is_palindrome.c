#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint - func reverses singly-linked listint_t list
 * @head: head node pointer of list
 * Return: list head pointer
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - func checks if singly linked list is a palindrome
 * @head: head linked list pointer
 * Return: if linked list is not a palindrome (0),
 * if linked list is a palindrome (1)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		tmp = tmp->next;
	}

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
	{
		return (0);
	}

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
		{
			return (0);
		}
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

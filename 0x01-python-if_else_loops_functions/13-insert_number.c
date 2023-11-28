#include "lists.h"

/**
 * insert_node - Fucn inserts node into sorted linked list
 * @head: list start pointer
 * @number: number to add
 * Return: Sorted linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux;
	int flag = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}
	new->n = number;
	aux = *head;
	if (!*head || !head)
	{
		new->next = NULL;
		(*head) = new;
		return (*head);
	}
	while (aux->next != NULL)
	{
		if (number < (*head)->n)
		{
			flag = 1;
			break;
		}
		else if (number < aux->next->n)
			break;
		aux = aux->next;
	}
	new->next = aux->next;
	if (flag == 1)
	{
		(*head) = new;
		new->next = aux;
	}
	else
		aux->next = new;
	return (*head);
}

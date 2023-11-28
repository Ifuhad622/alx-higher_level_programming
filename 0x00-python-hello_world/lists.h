#ifndef LISTS_H
#define LISTS_H

/* Std Lib */
#include <stdlib.h>

/* Struct */

/**
 * struct listint_s - struct for singly linked list
 * @n: integer
 * @next: points to next node
 *
 * Description: node structure for singly liked list
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Prototypes */
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);

#endif /* end of LIST_H file */

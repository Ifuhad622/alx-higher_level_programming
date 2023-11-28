#include "lists.h"

/**
 * check_cycle - func verifies linked list for cycle
 * @list: linked list to verify
 * Return: no cycle (0), there is a cycle (1)
 */
int check_cycle(listint_t *list)
{
	listint_t *list_slow, *list_fast;

	if (!list)
	{
		return (0);
	}

	list_fast = list_slow = list;
	while (list_fast)
	{
		if (list_fast->next == NULL || (list_fast->next)->next == NULL)
		{
			return (0);
		}
		list_fast = (list_fast->next)->next;
		if (list_slow == list_fast)
		{
			return (1);
		}
		list_slow = list_slow->next;
	}
	return (0);
}

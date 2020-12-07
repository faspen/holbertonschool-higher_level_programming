#include "lists.h"

/**
* check_cycle - check if there is a loop
* @list: list to be checked
* Return: 0 if no loop, 1 if loop exists
*/

int check_cycle(listint_t *list)
{
	listint_t *test1 = list;
	listint_t *test2 = list;

	if (list == NULL)
		return (0);

	while (test1 && test1->next)
	{
		test1 = test1->next->next; /* iterate by 2 */
		test2 = test2->next; /* by 1 */

		if (test1 == test2) /* if they are the same, return 1 */
			return (1);
	}
	return (0);
}

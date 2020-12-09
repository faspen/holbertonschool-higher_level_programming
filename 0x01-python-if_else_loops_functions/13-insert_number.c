#include "lists.h"

/**
* insert_node - insert a number into sorted list
* @head: pointer pointer to first node
* @number: number to be added
* Return: address of new node, NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *copy = *head;

	new = malloc(sizeof(listint_t)); /* set up new */
	if (!new)
		return (NULL);
	new->n = number;

	if (!copy) /* check if copy is null */
		return (NULL);
	if (!*head) /* check if head is null */
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	
	if (number <= 0) /* what if it is 0 or less? */
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (copy)

	return (NULL);
}

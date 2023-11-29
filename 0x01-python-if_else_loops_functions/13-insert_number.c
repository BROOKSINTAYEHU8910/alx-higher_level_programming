#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails to allocate memory - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    /* Create a new node */
    listint_t *current = *head;
    listint_t *newNode = malloc(sizeof(listint_t));

    /* Check if memory allocation for the new node failed */
    if (!newNode)
        return NULL;

    /* Initialize the new node with the given number */
    newNode->n = number;
    newNode->next = NULL;

    /* If the list is empty or the new node should be inserted at the beginning */
    if (current == NULL || current->n >= number)
    {
        newNode->next = current;
        *head = newNode;
        return newNode;
    }

    /* Traverse the list to find the correct position to insert the new node */
    while (current->next && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node into the list */
    newNode->next = current->next;
    current->next = newNode;

    return newNode;
}

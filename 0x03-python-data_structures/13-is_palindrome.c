#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Identify if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *reversed = NULL, *temp = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    // Move slow and fast pointers to find the middle
    while (fast != NULL && fast->next != NULL)
    {
        // Update reversed list
        temp = reversed;
        reversed = malloc(sizeof(listint_t));
        if (reversed == NULL)
        {
            // Handle memory allocation failure
            free_listint(reversed);
            return (0);
        }
        reversed->n = slow->n;
        reversed->next = temp;

        slow = slow->next;
        fast = fast->next->next;
    }

    // If the length is odd, move slow one step forward
    if (fast != NULL)
        slow = slow->next;

    // Compare the first half and the reversed second half
    while (slow != NULL)
    {
        if ((*head)->n != reversed->n)
        {
            // Clean up and return 0 if not a palindrome
            free_listint(reversed);
            return (0);
        }

        *head = (*head)->next;
        temp = reversed;
        reversed = reversed->next;
        free(temp);

        slow = slow->next;
    }

    // Clean up reversed list
    free_listint(reversed);

    // It is a palindrome
    return (1);
}

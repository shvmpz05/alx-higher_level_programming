#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if the list is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp, *front, *back;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    front = *head;
    back = *head;

    while (front->next != NULL)
    {
        front = front->next;
        if (front->next != NULL)
            front = front->next;
        else
            break;
        back = back->next;
    }

    temp = back->next;
    back->next = NULL;
    back = temp;

    while (back != NULL)
    {
        if (front->n != back->n)
            return (0);
        front = front->next;
        back = back->next;
    }

    return (1);
}


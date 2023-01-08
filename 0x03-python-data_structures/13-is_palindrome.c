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
    int values[1024];
    int i, j;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    front = *head;
    back = *head;
    i = 0;

    while (front->next != NULL)
    {
        values[i] = front->n;
        i++;
        front = front->next;
        if (front->next != NULL)
            front = front->next;
        else
            break;
        back = back->next;
    }

    if (front->next == NULL && i % 2 == 0)
    {
        values[i] = front->n;
        i++;
    }

    temp = back->next;
    back->next = NULL;
    back = temp;

    j = i - 1;
    for (i = 0; i < j; i++, j--)
    {
        if (values[i] > 0 && values[j] < 0)
            return (0);
        if (values[i] < 0 && values[j] > 0)
            return (0);
        if (values[i] != values[j])
            return (0);
    }

    return (1);
}


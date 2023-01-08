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
    listint_t *temp;
    int values[1024];
    int i, j;

    temp = *head;
    i = 0;
    while (temp != NULL)
    {
        values[i] = temp->n;
        temp = temp->next;
        i++;
    }

    j = i - 1;
    for (i = 0; i < j; i++, j--)
    {
        if (values[i] != values[j])
            return (0);
    }

    return (1);
}


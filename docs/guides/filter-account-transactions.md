# Filter account transactions


In the Account view, you can easily filter and search for transactions.

## Using the period drop down

The period drop down allows you to filter transactions made within a specified time range.  
The default values are:  

* All transactions
* Last 3 months
* Last 30 days

!!! note ""

    More options will be available later. Keep Finko updated.

## Using search bar

The search bar is located at the top right of the transactions list.  
When you enter text to search, the search will be performed on the transaction's Label field.  
The search is not case sensitive and matchs when the values contain the specified text.  
You can however search in the third party name or in the category name using the patterns bellow:

| Pattern    | Description                                                                         |
|------------|-------------------------------------------------------------------------------------|
| `tp:TEXT`  | Will search transactions with when the third party name contains the specified text |
| `cat:TEXT` | Will search transactions with when the category name contains the specified text    |

### Examples

* Type `tp:Amazon` in the search box to search for transactions made with Amazon.  
You can also just type `tp:ama`.

* Type `cat:food` in the search box to search for transactions with the "Food" category.

## Using context menu


* Right click on a transaction in the list of the **Account view** then click **Transactions with the same category** to filter only the transactions with the category of the selected transaction.
* Right click on a transaction in the list of the **Account view** then click **Transactions with the same third party** to filter only the transactions with the third party of the selected transaction.

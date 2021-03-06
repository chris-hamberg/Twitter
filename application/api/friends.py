try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.subprocess.subroutines import filter
finally:
    from requests import get

class ids(AbstractBase): 
    '''Returns a cursored collection of user IDs for every user the specified 
user is following (otherwise known as their “friends”). 

At this time, results are ordered with the most recent following first — 
however, this ordering is subject to unannounced change and eventual consistency 
issues. Results are given in groups of 5,000 user IDs and multiple “pages” of 
results can be navigated through using the next_cursor value in subsequent 
requests. See Using cursors to navigate collections for more information. 

This method is especially powerful when used in conjunction with GET users / 
lookup, a method that allows you to convert user IDs into full user objects in 
bulk. 

	- user_id
	The ID of the user for whom to return results for. 

	- screen_name
	The screen name of the user for whom to return results for. 

	- cursor
	Causes the list of connections to be broken into pages of no more than 5000 
    IDs at a time. The number of IDs returned is not guaranteed to be 5000 as 
    suspended users are filtered out after connections are queried. If no cursor 
    is provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See Using cursors to navigate collections for 
    more information. 

	- stringify_ids
	Many programming environments will not consume our Tweet ids due to their 
    size. Provide this option to have ids returned as strings instead. More 
    about Twitter IDs. 

	- count
	Specifies the number of IDs attempt retrieval of, up to a maximum of 5,000 
    per distinct request. The value of count is best thought of as a limit to 
    the number of results to return. When using the count parameter with this 
    method, it is wise to use a consistent count value across all requests to 
    the same user’s collection. Usage of this parameter is encouraged in 
    environments where all 5,000 IDs constitutes too large of a response.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, cursor=None, 
            stringify_ids=False, count=5000):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id       -> int
 screen_name   -> string
 cursor        -> string
 stringify_ids -> bool
 count         -> int'''
        
class List(AbstractBase): 
    '''Returns a cursored collection of user objects for every user the 
specified user is following (otherwise known as their “friends”). 

At this time, results are ordered with the most recent following first — 
however, this ordering is subject to unannounced change and eventual consistency 
issues. Results are given in groups of 20 users and multiple “pages” of results 
can be navigated through using the next_cursor value in subsequent requests. See 
Using cursors to navigate collections for more information. 

	- user_id
	The ID of the user for whom to return results for. 

	- screen_name
	The screen name of the user for whom to return results for. 

	- cursor
	Causes the results to be broken into pages. If no cursor is provided, a 
    value of -1 will be assumed, which is the first “page.” The response from 
    the API will include a previous_cursor and next_cursor to allow paging back 
    and forth. See [node:10362, title=”Using cursors to navigate collections”] 
    for more information. 

	- count
	The number of users to return per page, up to a maximum of 200. Defaults to 
    20. 

	- skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects. 

	- include_user_entities
	The user object entities node will be disincluded when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, cursor=None, count=20, 
		    skip_status=False, include_user_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id               -> int
 screen_name           -> string
 cursor                -> string
 count                 -> int
 skip_status           -> bool
 include_user_entities -> bool'''

# encapsulate namespace
friends = AbstractModule(globals())

# enforce singleton
del (ids, List,
     AbstractBase, AbstractModule, get)

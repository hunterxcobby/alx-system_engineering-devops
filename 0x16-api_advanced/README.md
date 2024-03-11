# Project: 0x16. API advanced

![api_guide](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png)

## Background Context

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Resources

### Read or watch:-

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives

### General

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Tasks

0. [How many subs?](./0-subs.py) :

Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```sh
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$ python3 0-main.py programming
5909053
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$ python3 0-main.py this_is_a_fake_subreddit
0
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$
```

1. [Top Ten](./1-top_ten.py) :

Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

First submission:

```py
url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Ensure a custom User-Agent to prevent errors.
    headers = {'User-Agent': 'My User Agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        data = response.json()

        posts = data['data']['children']
        if len(posts) == 0:
            print(None)
        else:
            for post in posts:
                print(post['data']['title'])
    except requests.RequestException:
        print(None)
```

```sh
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$ python3 1-main.py programming
[META] The future of r/programming
It's not microservice or monolith; it's cognitive load you need to understand first
The (short) story of how the SSH port became 22
New record for fastest FizzBuzz implementation (283 GB/s)
The High-Risk Refactoring
Adding AddressSanitizer support to the Cheerp WebAssembly compiler
Coq theorem prover will be renamed into Rocq
Database Fundamentals
Beyond RBAC: When standard models just aren’t enough | Permit
(Almost) Every infrastructure decision I endorse or regret after 4 years running infrastructure at a startup
Git Tips and Tricks
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$
```

2. [Recurse it!](./2-recurse.py) :

Write a recursive function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])

- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
- If not a valid subreddit, return None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)

```sh
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$ python3 2-main.py programming
925
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x16-api_advanced$
```

3. [Count it!](./100-count.py) :

Write a recursive function that queries the [Reddit API](https://www.reddit.com/dev/api/), parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. `Javascript` should count as `javascript`, but `java` should not).

Requirements:

- Prototype: `def count_words(subreddit, word_list)`
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
- If `word_list` contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with `java`)
- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in. `java java java` counts as 3 separate occurrences of java.
- To make life easier, `java`. or `java!` or `java_` should not count as `java`
- If no posts match or the subreddit is invalid, print nothing.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)

Disclaimer: number presented in this example cannot be accurate now - Reddit is hot articles are always changing.

---

### Environment

- Language: Python 3.4.3
  - OS: Ubuntu 20.04 LTS
  - Compiler: Python3
  - Style guidelines:
    - [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)

---
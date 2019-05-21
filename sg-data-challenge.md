# Tag Recommendation

### Context
Given a list of events, including pageview and search events, recommend tags to add to each page based on search terms. In addition, take 30-minute session into consideration.


### Challenge
Set up a small project to take inputs and output the recommendations. Besides, set up tests to make sure it works correctly.


### Example
Given events as below,

id | user_id | event_type | timestamp | url | content
--- | --- | --- | --- | --- | ---
a5d14ae3-eed8-4787-a41d-67a435e57f62 | 2 | pageview | 1558357800 | https://example.sg.nl |
8595ee0a-7bc6-11e9-8f9e-2a86e4085a59 | 2 | search | 1558359000 | https://example.sg.nl | biscuit
541fe921-9ebb-4da9-bf3e-46468152bc6e | 1 | pageview | 1558437815 | https://example.sg.nl |
496f805a-3225-4e0b-a2ec-3b9434dad2f5 | 2 | pageview | 1558437817 | https://example.sg.nl/health |
496f805a-3225-4e0b-a2ec-3b9434dad2f5 | 2 | pageview | 1558437845 | https://example.sg.nl |
b8e58a3c-a6c5-40e1-a43a-60a58b471fa6 | 1 | search | 1558437956 | https://example.sg.nl | m
9929d4d1-1188-4579-97fe-f2cea4b982a5 | 1 | search | 1558437960 | https://example.sg.nl | mo
eb44e44a-0488-4f10-9ec4-033589b67d46 | 1 | search | 1558437975 | https://example.sg.nl | mov
b9cfd806-ff26-4d28-8b4c-6289d5c6d77a | 1 | search | 1558437980 | https://example.sg.nl | mo
4da560cd-533e-4c0c-95df-c93e80f7282f | 1 | search | 1558437984 | https://example.sg.nl | mob
b0f1b42f-2914-479b-ad52-cc6eb9e55e50 | 1 | search | 1558437990 | https://example.sg.nl | mobi
4133206d-62b9-4d27-8aed-f5875a9d132f | 1 | search | 1558437992 | https://example.sg.nl | mobil
7392c9a9-7028-4827-8f8b-622bcbaa281b | 2 | search | 1558437992 | https://example.sg.nl | android
000dac0e-1b22-487c-84c5-a5d511346b0d | 1 | search | 1558438000 | https://example.sg.nl | mobilr
7e9a79ae-d965-4647-921a-ca76825dea2f | 2 | pageview | 1558438001 | https://example.sg.nl/pixel-3a |
bed1b23e-ea8c-461d-9824-854d4e6fe9c1 | 1 | search | 1558438010 | https://example.sg.nl | mobil
2429b8d2-ff69-4bd5-9e37-d745225a35e7 | 1 | search | 1558438013 | https://example.sg.nl | mobile
5d48231c-62ec-4120-a2bf-4c122b44c4c8 | 1 | search | 1558438100 | https://example.sg.nl | google phone
e0b54454-d624-4211-bcb1-266fe7660c01 | 1 | search | 1558438200 | https://example.sg.nl | 
8a21e01a-1211-4910-99a2-0f4b46b6d91c | 1 | pageview | 1558438400 | https://example.sg.nl/pixel-3a |

the recommended extra tags for `https://example.sg.nl/pixel-3a` are `mobile` and `google phone`.


### Languages
Feel free to use either or combination of the languages below:
- SQL
- Javascript
- Python


### Input
Start with one of the context:
1. data in a database with format as example
2. data as a list/an array as below
```
events = [
  {
    id: "541fe921-9ebb-4da9-bf3e-46468152bc6e",
    user_id: "1",
    event_type: "pageview",
    timestamp: 1558437815,
    url: "https://example.sg.nl",
    content: null
  }, {
    ...
  },
  ...
]
```

### Output
Print the result with `console.log` or `print`.


### A Plus
What else would you take into consideration in the real world, with the above data but not limited to it, and how?


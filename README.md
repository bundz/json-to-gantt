# json-to-gantt
From json to gantt char. (Python)

## How it works
- Simple write your json file like this:

```javascript
{
    "title": "I love Beatles!",
    "label": "Some number",
    "legend": [
        {"color": "yellow", "text": "Yellow!"},
        {"color": "blue", "text": "Blue!"},
        {"color": "green", "text": "Green!"},
        {"color": "purple", "text": "Purple!"},
        {"color": "red", "text": "Red!"}
    ],
    "rows": ["John", "Paul", "George", "Ringo"],
    "columns": [0,1,2,3,4,5,6,7,8],
    "bars": [
        {"row": "John", "from": 0, "to": 4, "color": "yellow"},
        {"row": "John", "from": 4, "to": 8, "color": "purple"},
        {"row": "Paul", "from": 0, "to": 8, "color": "blue"},
        {"row": "George", "from": 0, "to": 8, "color": "green"},
        {"row": "Ringo", "from": 0, "to": 8, "color": "red"}
    ],
    "bar_height": 0.5
}
```
- execute this command:

> ganttify [your json path]

- and get this gantt chart:
![alt tag](https://s21.postimg.org/4s3lqec6v/figure_1.png)

YAAAAY!

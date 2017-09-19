# On-Belay

## storage of mood tracking within csv


This initial file is to fulfill requirement for [issue tracker 30](https://github.com/OperationCode/on-belay/issues/30), an initial attempt at [issue tracker 28](https://github.com/OperationCode/on-belay/issues/28).



Uses a base comma separated file in the format:
```
date,time,rating
06/11/2017,0617,1
06/11/2017,1016,3
06/11/2017,1412,4
06/11/2017,1701,1
06/11/2017,2219,3
```


The MoodManager class can be called in either with the implied default file name or by using a custom file name.

```
mood_default = MoodManager()
mood_custom = MoodManger('custom_mood_values.csv')
```


In order to process the stored files into the tuple class use the `construct_mood_event_objects` method. 

```
mood_default.construct_mood_event_objects()
```

This method processes the stored csv line by line into a list of namedtuple objects:
```
MoodEvent(date='06/12/2017', time='2114', rating='2')
```

The benefit to this is the elements retain their identity. Individual elements can be referenced by accessing the single attribute for the desired tuple.

```
>>> value = mood_default.currently_held_moods[0]
>>> print(value)
MoodEvent(date='06/11/2017', time='0617', rating='1')
>>> value.date
'06/11/2017'
>>> value.time
'0617'
>>> value.rating
'1'
```

Lastly, because we all hate dates and times there are simple method calls to conver the string instances and datetimes to remove this frustrating laborous event from the user:

```
for item in mm.currently_held_moods[:10]:
        print(item)
        print( mm.string_pair_to_date(item.date, item.time))
        print( mm.date_to_string_list(mm.string_pair_to_date(item.date, item.time)))
```

```
MoodEvent(date='06/12/2017', time='2114', rating='2')
2017-06-12 21:14:00
['06/12/2017', '2114']
```

Lastly, since we all love adding new data points. In the chance we get actual users, we need to add actual data. We can call the `log_new_mood` data point after the user enters their mood. This takes the current datetime, builds the tuple, and adds it to the current list. It also updates the `events.csv` data file. 

```
mm.log_new_mood(4)
```

How can you help? As any IO process has to deal with IO issues, we could definitely use implementation for these great functions:

#### FileHandler methods

`def delete_single_entry`

`def delete_all_values`

`def file_exception_handler`

`def partial_loading`

#### MoodManager methods

`def get_n_recent_tuples`

#### MoodEvent ideas

* Pass in the header values, to create a namedtuple that doesn't have hardcoding for it's attributes. 




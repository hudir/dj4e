overwritting the method of gviwe list class
- get_queryset()
- get_context_data()

```python
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['crazy_thing'] = "CRAZY THING"
    return context
```